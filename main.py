passwordsite=input("Enter the site for which you will save the password:\t")
password=input("Enter password:\t")
file=open("manager.pass","a")

file.write("site:\t"+passwordsite+"\n")
file.write("Password:\t"+password+"\n\n")
file.close()
