# 12 >= login >= 3
# 16 >= password >= 8,

login = input("login : ")
password = input("password : ")

if len(login) >= 3 and len(login) <= 12:
    print("login ok")
else:
    print("login start 3 to 12")

if len(password) >= 8 and len (password) <= 16 and not password.isdigit() and not password.isalpha():
    print("Password ok")
else:
    print("Retype password")

