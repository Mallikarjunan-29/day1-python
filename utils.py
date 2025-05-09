import os
import time

# file_path = "C:\\Users\\ramya\\OneDrive\\Documents\\Logs\\"
file_path = f"logs\\failed_login_logs-{time.strftime("%Y-%m-%d")}.txt"



def log_write(login_attempt):
    with open(file_path, "a") as f:
        f.writelines("\n" + login_attempt)


def log_read():
    try:
        if os.path.exists(file_path):
            with open(file_path, "r") as f:
                lines = [line for line in f if line.strip()]
            unique_users = set()
            recent_timestamp = []
            for line in lines:
                parts = line.split("|")
                if len(parts) == 4:
                    unique_users.add(parts[0].strip())
                    recent_timestamp.append(parts[3].strip())
            recent_timestamp.sort(reverse=True)
            if lines:
                print(f"Total invalid attempts: {len(lines)}")
                print(f"Unique Users are: {unique_users}")
                print(f"Most Recent Timestamp: {recent_timestamp[0]}")
    except FileNotFoundError:
        print("File not found")
    except FileExistsError:
        print("File already exists")


