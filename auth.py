# auth.py
import time
import hashlib
import os
from utils import log_write


login_creds = {
    "admin": "admin123",
    "user": "user123",
    "arjun": "arjun123"
}

users=f"users\\user.txt"
def login():
    try:
        counter = 0
        while counter < 3:
            counter += 1
            time_stamp = time.strftime('%Y-%m-%d-%H:%M:%S')
            uname = input("\n Enter username:").strip()
            pwd = input("\n Enter password:")

            user_not_found = f"{uname} | user not found | Attempt {counter} | {time_stamp}"
            invalid_password = f"{uname} | Invalid password | Attempt {counter} | {time_stamp}"

            if uname in login_creds:
                if pwd == login_creds[uname]:
                    print("\n Login Successful")
                    break
                else:
                    log_write(invalid_password)
                    if counter == 3:
                        print("\nLogin failed")
                    else:
                        print("\n Enter correct username and password ")
            else:
                log_write(user_not_found)
                if counter == 3:
                    print("\nLogin failed")
                else:
                    print("\n Enter correct username and password ")
    except Exception as e:
        print(f"Exception: {e}")

def register():
    try:
        user_name=input("\n Enter username:")
        password=input("\n Enter password:")
        with open(users,"a")as f2:
            f2.write("")

        password=hashlib.sha256(password.encode()).hexdigest()
        with open(users,"r") as f:
            print("Entering reader")
            creds=f.readlines()
            print(creds)
            if len(creds)>0:
                for items in creds:
                    print("Enter for loop")
                    if items.split(":")[0].strip()==user_name:
                        print("Entering if cndition")
                        # Writing the username and password in users file
                        print("Username already exists")
                        return
                with open(users, "a") as f1:
                    print("Username being written")
                    f1.writelines(f"\n{user_name}:{password}")


            else:
                with open(users, "a") as f1:
                    print("Username being written")
                    f1.writelines(f"\n{user_name}:{password}")





    except Exception as e:
        print(f"Exception:{e}")





