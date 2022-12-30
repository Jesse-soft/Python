# control flow is the order in which instructions are executed in a python program
# CONDITIONAL STATEMENT: if-else-elif(else if)
# put any number from 50 to test the match statement
age = input('Enter your current Age ')
age = int(age)
if age >= 18 and age < 50:
    print('Your not a Juvenile!')
    print("Answer y/n !")
    answer = input("let's calculate your Date of Birth? ")
    if answer == "y":
        currentYear = input("What year is this? ")
        currentYear = int(currentYear)
        input = input("Where you born in "+str(currentYear-age)+" ")
        if input == "y": #ENTER NO("n") TO TEST FOR LOOPING!!
            print("Great, that proves python is the best!!")
        else:
            print("Try Again!!")
    else:
        print("Okay!!")
        print("Have a great time learning Python!!")
elif age < 18 and age > 0:
    print('Nice to meet you early python learner')
    print("Answer y/n !")
    answer = input("let's calculate your Date of Birth? ")
    if answer == "y":
        currentYear = input("What year is this? ")
        currentYear = int(currentYear)
        input = input("Where you born in "+str(currentYear-age)+" ")
        if input == "y":
            print("Great, that proves python is the best!!")
        else:
            print("Try Again!!")
    else:
        print("Okay!!")
        print("Have a great time learning Python!!")
else:
    print("Hmmm looks like you are either above 50 or you put a wrong number!!")

    # this example reviews some of what we have learnt
    # SWITCH STATEMENT: match-case
    http_status = input("Enter any status code ")
    http_status = int(http_status)
    match http_status:
        case 200 | 201:
            print("Success")
        case 300|301:
            print("Site moved")
        case 400:
            print("Bad Request")   
        case 500 | 501:
            print("Server Error")   
        case _:
            print("Unknown")          
# LOOPS: for-while

name= input("Enter your Name: ")
count=0
for item in name:
    print(item)
    while count<len(name):
        print("Testing your name with while", name[count])
        count+=1

    # 