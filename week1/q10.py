'''10. Bill Splitter'''

bill=int(input("Enter bill amount : "))
persons=int(input("Enter the number of persons : "))
tip_percent=int(input("Enter the tip percentage : "))
tip_amount=(tip_percent//bill)*100
total_amount=bill+tip_amount
print(f"Amount each person has to pay = {total_amount//persons}")

