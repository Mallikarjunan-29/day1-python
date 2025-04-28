import time
print("Welcome Greeting")
def greet_user():
    print("Welcome to Cyber Sec zone")
greet_user()

print("Function for adding 2 numbers")
def num_add(a,b):
    print(f"Sum of {a} and {b} is {a+b}")
num_add(1,2)

print("Checking for even numbers")
def is_even(a):
    if a%2==0:
        return True
    else:
        return False
print(is_even(2))

print("Detecting Failed logins")
def detect_failed_logins(logs):
    count=0
    for x in logs:
        if "failed" in x:
            count+=1
    print(f"Number of failed logins:{count}")

login_attempts=["Arjun-failed", "Ramyaa-Successful","Adhya-Successful", "Mallikarjunan-failed"]
detect_failed_logins(login_attempts)

def print_failed_logins(attempts):
    for x in attempts:
        if "failed" in x.lower():
            print(f"{time.strftime('%H:%M:%S')} - Failed logins:{x}")

print_failed_logins(login_attempts)
