print("Enter your weight....... \n")
weight = input('Weight = ')
val = input(" (K)gs or (L)bs: ")
m = 2.204* int(weight)
n = 0.45* int(weight)
if(val== 'K'or val == 'k'):
    print(m)
elif(val == 'L' or val == 'l'):
    print(n)
else:
    print('enter either K or L')
    
