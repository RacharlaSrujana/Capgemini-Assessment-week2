'''12. Pattern Generator'''

# rows=int(input("Enter number of rows : "))
# print("Actual pattern")
# for i in range(rows):
#     print('*'*(i+1))
# print("Reverse pattern")
# for j in range(rows,-1,-1):
#     print("*"*(j))

rows=int(input("Enter number of rows : "))
print("Actual Pattern")
for i in range(rows):
    for j in range(i+1):
        if j<=i:
            print("*",end='')
    print()
print("Reverse pattern")
for i in range(rows):
    for j in range(rows,-1,-1):
        if j>i:
            print("*",end='')
    print()