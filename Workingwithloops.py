#importing time to work with time class
import time

# Print numbers from 1 to 10
print("\nPrinting numbers from 1 to 10")
for x in range(1,11):
    print(x)
#Print Even Numbers from 1 to 50
print("\nPrinting Even numbers from 1 to 50")
for x in range(2,51,2):
    print(x)

print("\nPrinting Sum of numbers from 1 to 100")
result=0
for x in range(1,101):
    result = int(result) +int(x)

print("\n Sum of first 100 numbers is ",result)

print("\n List of fruits")
fruits=["apple","banana","orange","strawberry"]
for x in fruits:
    print("\n",x)
i= int(1)
while i<6:
    print("\nStill working...")
    i=i+1

print("\n Fake failed attempts")
failed_attempts=["fail1","fail2","fail3","fail4","fail5"]
for x in failed_attempts:
    print("\n", str(time.strftime("%H:%M:%S", time.localtime())),"- Failed attempt -",x)
