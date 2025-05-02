import os
file_path="C:\\Users\\ramya\\OneDrive\\Documents\\Logs\\"
file_full_path=file_path+"logstest.txt"
#
# with open(f"{file_path}logstest.txt", "a") as f:
#      f.write("\nfailed")
f = open(f"{file_path}logstest.txt", "r")
logs=f.readlines()
for line in logs:
    if "success" in line.lower():
        print(line)
# logs = list(f.read())

