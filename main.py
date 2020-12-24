import tkinter as tk
from tkinter import ttk
from tkinter import *
import mysql.connector

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
    updateTab=ttk.Frame(tab_holder)
    deleteTab=ttk.Frame(tab_holder)
    tab_holder.add(createTab,text="Create")
    tab_holder.add(updateTab,text="Update")
    tab_holder.add(viewTab,text="View")
    tab_holder.add(deleteTab,text="Delete")
    tab_holder.pack(expand=1,fill='both')
    #Creating tabs end

    #Create tab
    Create(createTab)
    #View tab
    View(viewTab)
    #Update tab
    Update(updateTab)
    #Delete Tab
    Delete(deleteTab)

def Create(createTab):
    site=tk.StringVar()
    passwrd=tk.StringVar()
    Label(createTab, text="SiteName:").grid(row=0, column=0)
    Label(createTab, text="Password").grid(row=1, column=0)
    siteName = Entry(createTab,textvariable=site).grid(row=0, column=1)
    passWord = Entry(createTab,textvariable=passwrd).grid(row=1, column=1)
    submitbutton=Button(createTab,text="Create",command=lambda :CreateFunc(site.get(),passwrd.get())).grid(row=2,column=0)

def View(viewTab):
    site=tk.StringVar()
    Label(viewTab, text="SiteName:").grid(row=0, column=0)
    siteName = Entry(viewTab,textvariable=site).grid(row=0, column=1)
    viewbutton = Button(viewTab, text="View",command=lambda :ViewFunc(site.get())).grid(row=1, column=0)

def Update(updateTab):
    site = tk.StringVar()
    passwrd = tk.StringVar()
    Label(updateTab, text="SiteName:").grid(row=0, column=0)
    Label(updateTab, text="New Password").grid(row=1, column=0)
    siteName = Entry(updateTab, textvariable=site).grid(row=0, column=1)
    newpassWord = Entry(updateTab, textvariable=passwrd).grid(row=1, column=1)
    submitbutton = Button(updateTab, text="Update", command=lambda: UpdateFunc(site.get(), passwrd.get())).grid(row=2,
                                                                                                                column=0)

def Delete(deleteTab):
    site = tk.StringVar()
    Label(deleteTab, text="SiteName:").grid(row=0, column=0)
    siteName = Entry(deleteTab,textvariable=site).grid(row=0, column=1)

    deletebutton = Button(deleteTab, text="Delete",command=lambda :DeleteFunc(site.get())).grid(row=1, column=0)

def DeleteFunc(siteName):
    print(f"Deleted {siteName}")

def ViewFunc(siteName):
    print(f"viewing {siteName}")

def CreateFunc(siteName,passwrd):
    print(f"SiteName is: {siteName}")
    print(f"Password is: {passwrd}")

def UpdateFunc(siteName,passwrd):
    print(f"SiteName is: {siteName}")
    print(f"New Password is: {passwrd}")

if __name__=="__main__":

    window = tk.Tk()

    passWin()

    window.mainloop()

