from UserData import UserData

passwords = {}

with open("passwords.txt") as file:
    lines = file.readlines()
    for line in lines:
        line = line.strip()
        username, password = line.split(":",1)
        passwords[username] = password

userdata = {}

with open("userdata.txt","r") as file:
    lines = file.readlines()
    for line in lines:
        line = line.strip()
        username, datastring = line.split(",",1)
        data = UserData(*datastring.split(","))
        userdata[username] = data

un = input("enter username: ")
print(passwords[un])
print(userdata[un])

# TODO: create menu
# TODO: login function
# TODO: change password function
# TODO: create account function