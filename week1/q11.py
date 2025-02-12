'''11. Password Strength Checker'''

password=input("Enter a password : ")
special_chars=['!','@','$','*','&','^','#']
upper_cnt=0
lower_cnt=0
digit_cnt=0
s_char=0
if len(password)>=8:
    for i in password:
        if i.isupper():
            upper_cnt+=1
        elif i.islower():
            lower_cnt+=1
        elif i.isdigit():
            digit_cnt+=1
        elif i in special_chars:
            s_char+=1
    if upper_cnt>=1 and lower_cnt>=1 and digit_cnt>=1 and s_char>=1:
        print("Your password is strong")
    else:
        print("Your password is not strong")
else:
    print("Password should contain atleast 8 characters")