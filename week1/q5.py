'''5. Shopping cart'''

def addCart(cart):
    items=input("Enter the item name and price (comma-separated) : ").split(",")
    cart.append(items)
def viewCart(cart):
    print(cart)
def bill(cart,total_bill,):
    for j in range(len(cart)):
        total_bill+=int(cart[j][1])
    print(f"Total bill = {total_bill}")
cart=[]
total_bill=0
while True:
    op=input("Select \n1.Add cart \n2.View Cart \n3.Bill \n4.exit\n")
    if op=='1':
        addCart(cart)
    elif op=='2':
        viewCart(cart)
    elif op=='3':
        bill(cart,total_bill)
    else:
        print("Thank you for visiting our site")
        break