#Is Prime Number
#First Solution
def IsPrime_1(n):
    s = 0
    for i in range(1, n + 1):
        if n % i == 0:
            s += 1
    return s == 2

#Second Solution
def PrimeFactors(n):
    factors = []
    while n % 2 == 0:
        factors.append(2)
        n //= 2
    for i in range(3, n + 1, 2):
        while n % i == 0:
            factors.append(i)
            n //= i
    return factors

#n = int(input('enter number:'))
#while n % 2 == 0 :
 #   print('2')
  #  n //= 2
#for i in range(3,n+1,2):
 #   while n % i == 0 :
  #      print(i)
   #     n //= i
   
#Third Solution
def IsPrime_2(n):
    if n <= 1:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True
#Test
if __name__ == "__main__":
    num = int(input("Enter a number: "))
    
    if IsPrime_1(num):
        print(f"Method 1: {num} is prime")
    else:
        print(f"Method 1: {num} is not prime")
    
    print(f"Method 2 - Prime factors of {num}: {PrimeFactors(num)}")
    
    if IsPrime_2(num):
        print(f"Method 3: {num} is prime")
    else:
        print(f"Method 3: {num} is not prime")