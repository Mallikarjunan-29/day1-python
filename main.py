# main.py
from utils import  log_read
from auth import register, login


import time


# def login():
#     try:
#         counter = 0
#         while counter < 3:
#             counter += 1
#             time_stamp = time.strftime('%Y-%m-%d-%H:%M:%S')
#             uname = input("\n Enter username: ").strip()
#             pwd = input("\n Enter password: ").strip()
#             user_not_found = f"{uname} | user not found | Attempt {counter} | {time_stamp}"
#             invalid_password = f"{uname} | Invalid password | Attempt {counter} | {time_stamp}"
#
#             if uname in login_creds:
#                 if pwd == login_creds[uname]:
#                     print("\n Login Successful")
#                     break
#                 else:
#                     log_write(invalid_password)
#                     if counter == 3:
#                         print("\nLogin failed")
#                     else:
#                         print("\n Enter correct username and password ")
#             else:
#                 log_write(user_not_found)
#                 if counter == 3:
#                     print("\nLogin failed")
#                 else:
#                     print("\n Enter correct username and password ")
#     except Exception as e:
#         print(f"Exception: {e}")

if __name__ == "__main__":
     register()
     # login()
    # log_read()
