import time
login_creds={
    "admin":"admin123",
    "user":"user123",
    "arjun":"arjun123"
}
counter =0
# def login_input(count=None):
#     if count<3:
#         count+=1
#         print(f"\ncounter is {count}")
#         if count==1:
#             username = input("\n Enter Username: ")
#             password = input("\n Enter Password: ")
#             login_check(username, password,count)
#         else:
#             print("\n enter correct username and password")
#             username = input("\n Enter Username: ")
#             password = input("\n Enter Password: ")
#             login_check(username, password, count)
#     else:
#         print("\n Login failed")
#         exit()
#
#
# def login_check(username,password,count):
#     for uname in login_creds.keys():
#         if uname == username:
#             if password == login_creds[uname]:
#                 print("Login Successful")
#                 break
#             else:
#                 login_input(count)
#
#
#         else:
#             login_input(count)
# login_input(counter)
failed_login_attempts=[]
def login():

    counter=0
    while counter<3:
        uname=input("\n Enter username:")
        pwd=input("\n Enter password:")
        if uname in login_creds:
            if pwd==login_creds[uname]:
                print("\n Login Successful")
                break
            else:
                counter+=1
                if counter ==3:
                    failed_login_attempts.append(uname+"-" + str(time.strftime("%Y-%m-%d-%H:%M:%S")))
                    print("\nLogin failed")
                else:
                    failed_login_attempts.append(uname+"-" + str(time.strftime("%Y-%m-%d-%H:%M:%S")))
                    print("\n Enter correct username and password ")
        else:
            counter+=1
            if counter == 3:
                failed_login_attempts.append(uname+"-" + str(time.strftime("%Y-%m-%d-%H:%M:%S")))
                print("\nLogin failed")
            else:
                failed_login_attempts.append(uname+"-" + str(time.strftime("%Y-%m-%d-%H:%M:%S")))
                print("\n Enter correct username and password ")

login()
print(f"\n{failed_login_attempts}")






