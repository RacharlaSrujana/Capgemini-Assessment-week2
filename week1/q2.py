'''2. Temperature Conversion Tool'''

def celToFahr(temp):
    return (temp*9/5)+32
def celToKel(temp):
    return temp+273.15
def fahrToKel(temp):
    return ((temp - 32) * 5/9) + 273.15

temp=int(input("Enter temperature: "))
print(f"Celsius to Fahrenheit : {celToFahr(temp)}F")
print(f"Celsius to Kelvin : {celToKel(temp)}K")
print(f"Fahrenheit to Kelvin : {fahrToKel(temp):.2f}K")