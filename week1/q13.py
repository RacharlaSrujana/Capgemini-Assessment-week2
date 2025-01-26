'''13. Palindrome checker'''

# def isPalindrome(op):
#     string=input("Enter a string : ")
#     rev_str=''
#     for i in string:
#         rev_str=i+rev_str
#     if string==rev_str:
#         print("It is a palindrome")
#     else:
#         print("It is not a palindrome")
# while True:
#     op=input("Do you want to enter a string (y/n) : ")
#     if op=='y':
#         isPalindrome(op)
#     else:
#         break

def isPalin():
    string=input("Enter a string : ")
    start=0
    end=len(string)-1
    flag=True
    while start<end:
        if string[start]!=string[end]:
            flag=False
        start+=1
        end-=1
    if flag:
        print("It is a palindrome")
    else:
        print("It is not a palindrome")
while True:
    op=input("Do you want to enter a string (y/n) : ")
    if op=='y':
        isPalin()
    else:
        break