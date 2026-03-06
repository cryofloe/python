print("This project is writen BY @cryofloe \nWelcome to +18 and captcha confirmation file. \nYou can use this project anywhere.")
print("_____________________________________")
#I can't explain everything, but i'll try.

#Import libraries
import random
import time

#Max wrong attempts rights
MAX_RIGHTS = 3 #Maximum wrong attempts rights.


#We are defining random numbers
secret_number = random.randint(1000,9999)
accesnumber = random.randint(1000,9999)

# Name input and rights
name_rights = 0

while name_rights < MAX_RIGHTS:
        name = input("Enter name: ").strip()

        if name.isdigit() or name == "":
            print("Invalid name. Try again.")
            name_rights += 1

            if name_rights >= MAX_RIGHTS:
                print("Too many wrong attempts. Wait 10 seconds...")
                time.sleep(10)
                name_rights = 0 #Reset rights

        else:
            break

#Defining age and age_rights for don't error :)
age_rights = 0
age = 0
while age_rights < MAX_RIGHTS:
    age_input = input("Enter your age: ").strip()
    if age_input.isdigit() and age_input != "":
        age = int(age_input)
        break
    else:
        print("Invalid age. Try again.")
        age_rights += 1

        if age_rights >= MAX_RIGHTS:
            print("Too many wrong attempts. Wait 10 seconds...")
            time.sleep(10)
            age_rights = 0
        continue

#code is explaining itself.
if age <= 18:
    print("Your age is under than 18. You can't have an acces the system.")

# Age checking
while age >= 18:
    print(f"You can see the secret number.")
    print(f"Secret number is = {secret_number}")
    enteringnumber_str = input("Please enter the secret number: ").strip() #Human confirmation
    enteringnumber = int(enteringnumber_str)
#I'm not definied max_rights here, because secret number is very important if user enter wrong number they must wait 10 seconds.
    if enteringnumber != secret_number:
        print("Wrong secret number. Wait 10 seconds...")
        time.sleep(10)
        continue

    if enteringnumber == secret_number:
        print(f"You have an acces the system, acces number is = {accesnumber} ")
        break
    else:
        print(f"Wrong")
#And finished also if you want use this code you can delete (#) words like this below, and you can use price is = just say thank you :)