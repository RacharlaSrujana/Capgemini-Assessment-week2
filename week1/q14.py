'''14. Factorial calculator'''

def isFact():
    num=int(input("Enter a number : "))
    fact=1
    for i in range(1,num+1):
        fact=fact*i
    print(f"Fcatorial of {num} is {fact}")
while True:
    op=input("Do you want to find factorial (y/n) : ")
    if op=='y':
        isFact()
    else:
        break