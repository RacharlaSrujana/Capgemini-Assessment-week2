'''19. Find second largest number'''

import sys
size=int(input("Enter size of list : "))
print("Enter elements of list:")
lst=[]
for i in range(size):
    ele=int(input())
    lst.append(ele)
largest=-sys.maxsize-1
second_largest=-sys.maxsize-1
for i in range(size):
    if lst[i]>largest:
        second_largest=largest
        largest=lst[i]
    elif lst[i]>second_largest and lst[i]!=largest:
        second_largest=lst[i]
print(f"The second largest number is {second_largest}")