print(".....This is a calculator program..... \n")
num1=input("please enter the first number \n")
num2=input("please enter the second number \n")
print("Please let us know what you want to do")
option=input("1. Addition \n 2. Subtraction \n 3. Multiplication \n 4. Division \n")
add = int(num1)+int(num2)
sub = int(num1)-int(num2)
mul = int(num1)*int(num2)
div = int(num1)/int(num2)
if(int(option) == 1):
  print(add)
if(int(option) == 2):
  print(sub)
if(int(option) == 3):
  print(mul)
if(int(option) == 4):
  print(div)
