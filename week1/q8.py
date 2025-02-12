'''8. Multiplication Table Generator'''

number=int(input("Enter the number : "))
ran=int(input("Enter range to generate table : "))
for i in range(1,ran+1):
    print(f"{number} * {i} = {number*i}")