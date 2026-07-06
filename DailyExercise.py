#Exercise
Text = input("Please Enter your text:")
Uper = 0
Lower =0
for i in Text:
    if i.isupper():
       Uper +=1
    elif i.islower():
        Lower+=1
        
print(f"Upper: {Uper} - Lower: {Lower}")

Text = input("Please Enter your text:")
print(Text[::-1])

def is_palindrome(Txt):
    return Txt == Txt[::-1]
print(is_palindrome(Text))

Text = input("Please Enter your text:")

# پاک‌سازی رشته
cleaned_text = Text.strip().lower()

# حذف فاصله‌ها
no_spaces = cleaned_text.replace(" ", "")

print(f"Original: {Text}")
print(f"Cleaned: {no_spaces}")

Text = input("Please Enter your text:")
counts = {}
for ch in Text:
       if ch != ',':
              counts[ch] = counts.get(ch, 0) + 1

for ch, count in counts.items():
       print(f"* {ch} : {count}")
            
Text = input("Please Enter your text:")
counts = {}

for ch in Text:
    if ch != ',':
        counts[ch] = counts.get(ch, 0) + 1

# پیدا کردن بیشترین تکرار
max_count = max(counts.values())

# پیدا کردن همه کاراکترهایی که بیشترین تکرار را دارند
most_frequent = [ch for ch, count in counts.items() if count == max_count]

print(f"Most frequent character(s): {most_frequent}")
print(f"Count: {max_count}")

NameList =["Nazanin","Nivan","Nicholas","Iran"]
ScoreList = [18,20,17,20]
StDict = dict(zip(NameList, ScoreList))
print(StDict)


#Exercise
Number = int(input("Please Enter a number: "))

def fibonacci_Sequence(n):
    if n == 1 or n == 2:
        return [1]
    
    a, b = 1, 1
    L = [1, 1]
    for _ in range(3, n + 1):
        a, b = b, a + b
        L.append(b)
    return L

fib_numbers = fibonacci_iterative(Number)

if Number in fib_numbers:
    print(f"✅ Number {Number} is in the Fibonacci Sequence")
else:
    print(f"❌ Number {Number} is NOT in the Fibonacci Sequence")


#Exercise

TestList = []
for i in range(1,21):
    TestList.append(i)
for j in TestList:
    if j%2==0 :
        print("The Number is Even")
    else:
        print("The Number is odd")
for k in TestList:
    if k%3==0:
        TestList.remove(k)


i =0
L =[]
while i<11:
    Number = int(input("Please Enter a Number:"))
    L.append(Number)
    i+=1
    repeated = {i: L.count(i) for i in L if L.count(i) > 1}
    
    if repeated:
        print(f"List: {L}")
        print("Duplicate elements:")
        for key in sorted(repeated):
            print(f"  {key} : {repeated[key]} times")
    else:
        print("No duplicates found")



def SumAll(*arg):
    sum = 0
    for item in arg:
        sum = sum + int(item)
    return sum
print(SumAll(2,5,6,7,4))
