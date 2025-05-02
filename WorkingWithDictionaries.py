import time
import os
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
# login_attempts=[]
def log_write(login_attempt):
    try:
        file_path="C:\\Users\\ramya\\OneDrive\\Documents\\Logs\\"
        file_full_path=file_path+"logs.txt"
        if os.path.exists(file_full_path):
            with open(f"{file_path}logs.txt", "a") as f:
                f.writelines("\n"+login_attempt)

        else:
            with open(f"{file_path}logs.txt", "x") as f:
                f.writelines("\n"+login_attempt)
    except FileExistsError:
        print("File already exists")
    except FileNotFoundError:
        print("File not found")
    finally:
        print("script executed")

def login():
    try:
        counter=0
        while counter<3:

            uname=input("\n Enter username:")
            pwd=input("\n Enter password:")
            if uname in login_creds:
                if pwd==login_creds[uname]:
                    # login_attempts.append(uname +"- Success-"+str(time.strftime('%Y-%m-%d-%H:%M:%S')))
                    log_write(uname +"- Success-"+str(time.strftime('%Y-%m-%d-%H:%M:%S')))
                    print("\n Login Successful")
                    break
                else:
                    counter+=1
                    if counter ==3:
                        # login_attempts.append(uname+"- failed -" + str(time.strftime("%Y-%m-%d-%H:%M:%S")))
                        log_write(uname + "- failed-" + str(time.strftime('%Y-%m-%d-%H:%M:%S')))
                        print("\nLogin failed")
                    else:
                        # login_attempts.append(uname+"- failed -" + str(time.strftime("%Y-%m-%d-%H:%M:%S")))
                        log_write(uname + "- failed-" + str(time.strftime('%Y-%m-%d-%H:%M:%S')))
                        print("\n Enter correct username and password ")
            else:
                counter+=1
                if counter == 3:
                    # login_attempts.append(uname+"- failed -" + str(time.strftime("%Y-%m-%d-%H:%M:%S")))
                    log_write(uname + "- failed-" + str(time.strftime('%Y-%m-%d-%H:%M:%S')))
                    print("\nLogin failed")
                else:
                    # login_attempts.append(uname+"- failed -" + str(time.strftime("%Y-%m-%d-%H:%M:%S")))
                    log_write(uname + "- failed-" + str(time.strftime('%Y-%m-%d-%H:%M:%S')))
                    print("\n Enter correct username and password ")
    except:
        print("Exception")

def log_read():
    try:
        file_path = "C:\\Users\\ramya\\OneDrive\\Documents\\Logs\\"
        file_full_path = file_path + "logs.txt"
        if os.path.exists(file_full_path):
            with open(f"{file_path}logs.txt", "r") as f:
                logs = f.readlines()
                for lines in logs:
                    if "failed" in lines.lower():
                        print(lines)
    except FileNotFoundError:
        print("File not found")
    except FileExistsError:
        print("File already exists")
login()
log_read()