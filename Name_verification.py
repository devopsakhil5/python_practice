name=input("please give me your name \n").split(" ")
print("Hi  " + name[0] + "," + " i think your surname is " + name[1])

decision =input("If it is correct, enter 'Y' or else enter 'N' \n")
if decision == 'Y':
    print("Thank you " + name[0] + " " + name[1])
elif decision == 'N':
    print("Ok " + name[0])
else:
    print("Enter only 'Y' or 'N' only \n")

