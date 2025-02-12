'''6. Prime numbers in a range'''

def isPrime(num):
    if num==0 or num==1:
        return False
    else:
        for j in range(2,num):
            if num%j==0:
                return False
        return True

start=int(input("Enter the starting number : "))
end=int(input("Enter the ending number : "))
for i in range(start,end+1):
    if isPrime(i):
        print(f"{i} is a prime number")
