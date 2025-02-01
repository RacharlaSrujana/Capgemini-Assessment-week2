'''Create a `Product` class with attributes `name`, `price`, and `stock`. Write a method `check_availability(quantity)` that returns whether 
    the requested quantity is available'''

class Product:
    products_list=[
        {"Name":"Air pods","Price":1000,"Stock":10},
        {"Name":"Watch","Price":2000,"Stock":13},
        {"Name":"Laptop","Price":90000,"Stock":5}
    ]
    def check_availability(self,item,quantity):
        for p in Product.products_list:
            if p["Name"].lower()==item.lower():
                if p["Stock"]>=quantity:
                    return "The requested product is available in the store"
                else:
                    return "The requested product is available but not in sufficient quantity"
        return "The requested product is not available"
item=input("Enter item name : ")
quantity=int(input("Enter quantity : "))
product=Product()
result=product.check_availability(item,quantity)
print(result)