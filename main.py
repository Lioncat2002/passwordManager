import tkinter as tk
from tkinter import ttk
from tkinter import *
import tkinter.messagebox
import json

def passWin():
    #Window init start

    window.title("LcPass")
    window.geometry("300x200")
    stylings()
    #Window init end

def stylings():
    #Creating tabs
    tab_holder=ttk.Notebook()
    createTab=ttk.Frame(tab_holder)
    viewTab=ttk.Frame(tab_holder)

    deleteTab=ttk.Frame(tab_holder)
    tab_holder.add(createTab,text="New/Update")

    tab_holder.add(viewTab,text="View")
    tab_holder.add(deleteTab,text="Delete")
    tab_holder.pack(expand=1,fill='both')
    #Creating tabs end

    #Create tab
    Create(createTab)
    #View tab
    View(viewTab)

    #Delete Tab
    Delete(deleteTab)

def Create(createTab):
    site=tk.StringVar()
    passwrd=tk.StringVar()
    Label(createTab, text="AccountName:").grid(row=0, column=0)
    Label(createTab, text="Password").grid(row=1, column=0)
    siteName = Entry(createTab,textvariable=site).grid(row=0, column=1)
    passWord = Entry(createTab,textvariable=passwrd).grid(row=1, column=1)
    submitbutton=Button(createTab,text="Create",command=lambda :CreateFunc(site.get(),passwrd.get())).grid(row=2,column=0)

def View(viewTab):
    site=tk.StringVar()
    Label(viewTab, text="AccountName:").grid(row=0, column=0)
    siteName = Entry(viewTab,textvariable=site).grid(row=0, column=1)
    viewbutton = Button(viewTab, text="View",command=lambda :ViewFunc(site.get())).grid(row=1, column=0)

def Delete(deleteTab):
    site = tk.StringVar()
    Label(deleteTab, text="AccountName:").grid(row=0, column=0)
    siteName = Entry(deleteTab,textvariable=site).grid(row=0, column=1)

    deletebutton = Button(deleteTab, text="Delete",command=lambda :DeleteFunc(site.get())).grid(row=1, column=0)

def DeleteFunc(siteName):

    for key in data.keys():
        if key==siteName:
            del data[siteName]
            txt="Deleted"
            break
        else:
            txt="Site not found"
    popUp(txt,"DeleteTab")

def ViewFunc(siteName):

    for key in data.keys():
        if key == siteName:
            txt = f"Password:{data[siteName]}"
            break
        else:
            txt = "Site not found"
    popUp(txt, "ViewTab")

def CreateFunc(siteName,passwrd):
    data[siteName]=passwrd
    popUp("Password saved","cerateTab")

def popUp(txt,windowname):
    tkinter.messagebox.showinfo(windowname,txt)

if __name__=="__main__":
    txt=""
    try:
        f=open("passwrd.json",'r')
        data=json.load(f)
        print(data)
        f.close()
    except(FileNotFoundError):
        data={}
        f = open("passwrd.json", 'w')
        f.close()
    except(json.decoder.JSONDecodeError):
        data={}
    f=open("passwrd.json",'w')
    window = tk.Tk()

    passWin()

    window.mainloop()
    json.dump(data,f)
    f.close()

