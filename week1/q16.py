'''16. Odd Even Separator'''

size=int(input("Enter size of list : "))
print("Enter elements of list:")
lst=[]
for i in range(size):
    ele=int(input())
    lst.append(ele)
even=[]
odd=[]
for i in lst:
    if i%2==0:
        even.append(i)
    else:
        odd.append(i)
print(f"Even list : {even}")
print(f"Odd list : {odd}")