print("Welcome to @cryofloe 's project.\n This is a basic and beginner calculator project. \n This project writen BY @gainacula. \n Thanks for your using.")
print("This is my second project in python. \n ------------------------------------")

#Right now my english language is little but i'm learning all time. 03/03/2026 :))

#Get the number

first_number_str = 0
second_number_str = 0
secondnum = 0
firstnum = 0
process = 0
conclusion = 0

while True:
    first_number_str = input("First num: ").strip()

#Checking input have a wrong or something like that.

    if first_number_str.isdigit():
        firstnum = int(first_number_str)
        break
    else:
        print("Invalid")
        continue

while True:
    second_number_str = input("Second num: ").strip()

#Checking input have a wrong or something.

    if second_number_str.isdigit():
        secondnum = int(second_number_str)
        break
    else:
        print("Invalid")
        continue

process = input("Input operator (*,/,+,-): ")
while True:
    if process == "*":
        conclusion = firstnum * secondnum

    if process == "/":
        conclusion = firstnum / secondnum

    if process == "+":
        conclusion = firstnum  + secondnum

    if process == "+":
        conclusion = firstnum - secondnum

    print(f"{firstnum} {process} {secondnum} = {conclusion}")
    break
