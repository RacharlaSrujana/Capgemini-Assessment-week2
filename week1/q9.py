'''9. String analysis tool'''

string=input("Enter a string : ")
temp=string.lower()
vow=['a','e','i','o','u']
# dig=range(0,10)
vcnt,ccnt,dcnt,scnt=0,0,0,0
rev_str=''
for i in range(len(string)):
    rev_str=string[i]+rev_str
    if temp[i] in vow:
        vcnt+=1
    elif ord(temp[i])>=97 and ord(temp[i])<=122:
        ccnt+=1
    elif ord(temp[i])>=48 and ord(temp[i]) <=57:
        dcnt+=1
    else:
        scnt+=1
print(f"Vowel count = {vcnt}")
print(f"Consonant count = {ccnt}")
print(f"Digit count = {dcnt}")
print(f"Special character count = {scnt}")
print(f"Reverse string = {rev_str}")