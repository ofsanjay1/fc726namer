import tkinter as tk
from tkinter import Canvas, Frame, filedialog, Text
import os
import tkinter
import pandas as pd 
from PIL import Image , ImageTk

root= tk.Tk()
root.title("Siemens FC726 Namer (*ofsanjay)")
root.iconbitmap('team.ico')


#Image for center(PILLOW)
image1= Image.open('siemensLOGO.png')
imagetk= ImageTk.PhotoImage(image1)

#Checking folder exsistance 
if (os.path.exists("PanelCsv")):
    print("Panel Folder Available")
else:
    os.mkdir("PanelCsv")

    
if(os.path.exists("LocationXL")):
    print("Location Folder Available")
else:
    os.mkdir("LocationXL")


    
#Output file name 
output_var=tk.StringVar()

#Creating list for containing folder location names
apps=[]

#Checking save.txt file & if present it reads the location
if os.path.isfile('save.txt'):
    with open('save.txt', 'r') as f:
        tempApps = f.read()
        tempApps= tempApps.split(',')
        print(tempApps)

#Collecting name from Input message box 
def submit():
    oFile= output_var.get()
    print("Your file name is :"+ oFile)
    apps.append(oFile)
    root.destroy()

#Selecting files from default folder
def addPanel():
     for widget in frame.winfo_children():
        widget.destroy()

     filename= filedialog.askopenfilename(initialdir="PanelCsv",title= "Panel file" ,filetypes=(("csv","*.csv"),("xlsx","*.xlsx")))
     apps.append(filename)
     print(filename)
     for app in apps:
         label= tk.Label(frame, text=app, bg= "blue")
         label.pack()

#Selecting files from default folder
def addNames():
     for widget in frame.winfo_children():
        widget.destroy()

     filename2= filedialog.askopenfilename(initialdir="LocationXL",title= "Location file" ,filetypes=(("xlsx","*.xlsx"),("csv","*.csv")))
     apps.append(filename2)
     print(filename2)
     for app in apps:
         label= tk.Label(frame, text=app, bg= "blue")
         label.pack()


# Body 
canvas=tk.Canvas(root,height=220, width=500, bg='#324544').pack()

frame= tk.Frame(root,bg="#f2efe4")
frame.place(relwidth=0.8, relheight=0.8, relx= 0.1, rely=0.1)

mainLabel=tk.Label(frame,text="Select Two files ").pack()

imLabel= tkinter.Label(image=imagetk)
imLabel.image=imagetk 
imLabel.place(x=100,y=110)

#Buttons Triggring Def
openfile= tk.Button(root, text="Select Panel File", padx=5, pady=5, fg ="white", bg= "#354235" , command=addPanel).pack(pady=5)

runApps= tk.Button(root, text="Add Location File", padx=10, pady=5, fg ="white", bg= "#354235" , command=addNames).pack(pady=5)

output_entry= tk.Entry(root, textvariable= output_var, font= ('calibre',10,'normal')).pack(pady=5)

out_btn= tk.Button(root, text="Submit", command= submit).pack(pady=20)

root.mainloop()

#writing location
with open ('save.txt','w') as f:
    for app in apps:
        f.write(app+',')


#reading location
with open ('save.txt','r')as fa:
     appnames=fa.read()
     appnames=appnames.split(',')

Panel= appnames[0]
locFile= appnames[1]
out_name=appnames[2]+'.csv'

df1= pd.read_csv(Panel, header=None)
df2= pd.read_excel(locFile, header=None)

df1 = df1[0].str.split(";", expand=True)
df1[4] = df1[4].apply(lambda x: v[-1] if (v := x.split()) else "")
df2[1] = df2[1].apply(lambda x: x.split("-")[0])

m = dict(zip(df2[1], df2[0]))

df1[4]= df1[4].replace(m)
#ofsanjay
print( 'Total Rows and Columns :' ,df1.shape[0],'x', len(df1.columns))
print(df1)
df1.to_csv (out_name, sep=';' , index_label=False, index= False, header= False)