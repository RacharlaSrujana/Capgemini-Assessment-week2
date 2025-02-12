'''7. Bank Loan Eligibility'''

salary=int(input("Enter your salary : "))
age=int(input("Enter your age : "))
credit_score=int(input("Enter your credit score : "))
if age<25:
    print("Loan is rejected as age is below 25")
elif salary<50000:
    print("Loan is rejected as salary is below 50000")
elif credit_score<600:
    print("Loan is rejected as your credit score is less")
elif age>=25 and salary>=50000 and credit_score>=600:
    print("Loan is approved")