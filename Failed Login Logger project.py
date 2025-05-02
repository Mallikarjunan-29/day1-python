import time
import os
login_creds={
    "admin":"admin123",
    "user":"user123",
    "arjun":"arjun123"
}
counter =0
file_path="C:\\Users\\ramya\\OneDrive\\Documents\\Logs\\"
if not os.path.exists(file_path):
    os.mkdir(file_path)
file_name="failed_login_logs.txt"
file_full_path = os.path.join(file_path, file_name)

def log_write(login_attempt):
    try:
        with open(file_full_path, "a") as f:
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
            counter+=1
            time_stamp = time.strftime('%Y-%m-%d-%H:%M:%S')
            uname=input("\n Enter username:")
            pwd=input("\n Enter password:")
            user_not_found = f"{uname}  | user not found | Attempt {counter} | {time_stamp}"
            invalid_password= f"{uname} | Invalid password | Attempt {counter} | {time_stamp}"
            if uname in login_creds:
                if pwd==login_creds[uname]:
                    print("\n Login Successful")
                    break
                else:
                    if counter ==3:
                        log_write(invalid_password)
                        print("\nLogin failed")
                    else:
                        log_write(invalid_password)
                        print("\n Enter correct username and password ")
            else:
                if counter == 3:
                    log_write(user_not_found)
                    print("\nLogin failed")
                else:
                    log_write(user_not_found)
                    print("\n Enter correct username and password ")
    except Exception as e:
        print(f"Exception:{e}")

def log_read():
    try:
        if os.path.exists(file_full_path):
            with open(f"{file_full_path}", "r") as f:
               lines=[line for line in f if line.strip()]
            unique_users=set()
            recent_timestamp=[]
            for line in lines:
                parts=line.split("|")
                if len(parts)==4:
                    unique_users.add(parts[0])
                    recent_timestamp.append(parts[3])
            recent_timestamp.sort(reverse=True)
            if lines:
                print(f"Total invalid attemps: {len(lines)}")
                print(f"Unique Users are {unique_users}")
                print(f"Recent timestamp is {recent_timestamp[0]}")

                # for lines in logs:
                #     print(lines.strip())
    except FileNotFoundError:
        print("File not found")
    except FileExistsError:
        print("File already exists")

login()
log_read()