#Basic python programs
#Positive or Negative or Zero
num = int(input("Enter the number:"))
if num < 0:
  print("Negative number")
elif num > 0:
  print("positive number")
else:
  print("Zero")

#Even or Odd 1
num = int(input("Enter a number: "))
if num % 2 == 0:
  print("Even")
else:
  print("Odd")  

#Even or Odd 2
num = 37
print("Even number") if num % 2 == 0 else print("Odd number")

#Arithmetic operations
num1 = 10
num2 = 5
add = num1 + num2
print(f"Addition: {num1} + {num2} = {add}")
sub = num1 - num2
print(f"Subtraction: {num1} - {num2} = {sub}")
mul = num1 * num2
print(f"Multiplication: {num1} * {num2} = {mul}")
div = num1 / num2
print(f"Division: {num1} / {num2} = {div}")
mod = num1 % num2
print(f"Modulus: {num1} % {num2} = {mod}")
exp = num1 ** num2
print(f"Exponentiation: {num1} ** {num2} = {exp}")
floordiv= num1 // num2
print(f"Floor Division: {num1} // {num2} = {floordiv}")

# Palindrome num 1
num = 7337
rev = int(str(num)[::-1])
if num == rev:
  print('Palindrome')
else:
  print("Not Palindrome")

# Palindrome num 2
num = 1234
temp = num
rev = 0
while temp > 0:
    remainder = temp % 10
    rev = (rev * 10) + remainder
    temp = temp // 10
if num == rev:
  print('Palindrome')
else:
  print("Not Palindrome")

#Palindrome str 
str = "python"
rev = reversed(str)
if str == rev:
  print('Palindrome')
else:
  print("Not Palindrome")

#Factorial 1
num = 7
fact = 1
for i in range(1,num+1):
  fact *= i
print("Factorial of",num,"is",fact)

# Factorial 2
def fact(n):
  return 1 if(n==0 or n==1) else n * fact(n-1)
num=3
print("The factorial of",num,"is",fact(num))

# Fibonacci series 1
terms = int(input("Enter the terms "))
num1, num2 = 0, 1
count = 0
if terms <= 0:
   print("Invalid input")
elif terms == 1:
   print("Fibonacci sequence upto",terms,":")
   print(num1)
else:
   print("Fibonacci sequence:")
   while count < terms:
       print(num1)
       nth = num1 + num2
       num1 = num2
       num2 = nth
       count += 1

# Fibonacci series 2
def fib(num):
    if num < 0:
        print("Incorrect input")
    elif num == 0:
        return 0
    elif num == 1 or num == 2:
        return 1
    else:
        return fib(num-1) + fib(num-2)
print(fib(5))

#Temperature converter
def convert_temperature():
    print("Temperature Converter")
    print("1. Convert Celsius to Fahrenheit")
    print("2. Convert Fahrenheit to Celsius")
    choice = input("Choose an option (1 or 2): ")
    print()
    
    if choice == "1":
        celsius = float(input("Enter temperature in Celsius: "))
        fahrenheit = (celsius * 9/5) + 32
        print(f"{celsius:.2f}°C is equal to {fahrenheit:.2f}°F.")
    elif choice == "2":        
        fahrenheit = float(input("Enter temperature in Fahrenheit: "))
        celsius = (fahrenheit - 32) * 5/9
        print(f"{fahrenheit:.2f}°F is equal to {celsius:.2f}°C.")
    else:
        print("Invalid choice! Please enter 1 or 2.")
convert_temperature()

#Swap a number 1
a,b = 3,7
a,b = b,a
print(f"The value of a  is {a} and b is {b}")

#Swap a number 2
num1 = int(input("Enter the first number:"))
num2 = int(input("Enter the second number:"))
num1 = num1+num2
num2 = num1-num2
num1 = num1-num2
print(f"The value of num1 is {num1} and num2 is {num2}")

#Length of a string
str = input("Enter a string: ")
length = len(str)
print(f"The length of the string is: {length}")

#Min, max and second largest of a number
nums = [7,3,37,1,50,0,73]
nums.sort()
print(f"The maximum number is {max(nums)}  \nThe minimum number is {min(nums)} \nThe second largest number is {nums[-2]}")

# Armstrong number
num = int(input("Enter a number: "))
sum = 0
temp = num
while temp > 0:
   digit = temp % 10
   sum += digit ** 3
   temp //= 10
if num == sum:
   print(num,"is an Armstrong number")
else:
   print(num,"is not an Armstrong number")
   
# Prime number
def prime(num):
  if num <= 1:
    return False
  for i in range(2, int(num**0.5) + 1):
    if num % i == 0:
      return False
  return True
num = int(input("Enter a number: "))
if prime(num):
  print("Prime")
else:
  print("Not prime")  

#Sum of all numbers from 1 to given number
num = int(input("Enter a number: "))
res = sum(range(1, num + 1))
print("Sum:", res)    

#Power of a number
base = int(input("Enter the base: "))
exponent = int(input("Enter the exponent: "))
res = base ** exponent
print("Result:", res)  

#Square root of a number
num = float(input("Enter a number: "))
square_root = num ** 0.5
print("The square root of",num,"is", square_root)

#Leap year or not
year = int(input("Enter a year: "))
if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print("leap year")
else:
    print("Not a leap year")

#Counting vowels and consonanats
def count_vowels_and_consonants(text):
    vowels = "aeiouAEIOU"
    consonants = "bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ"
    vowel_count = sum(1 for char in text if char in vowels)
    consonant_count = sum(1 for char in text if char in consonants)
    return vowel_count, consonant_count
text = input("Enter a string: ")
vowels, consonants = count_vowels_and_consonants(text)
print("Vowels:", vowels)
print("Consonants:", consonants)

#Count character 
text = input("Enter a string: ")
char = input("Enter the character to count: ")
count = text.count(char)
print(f"The character '{char}' appears {count} times.")

#String 
str = "Python course"
length = len(str)
upper = str.upper()
lower = str.lower()
swapcase = str.swapcase()
capitalize = str.capitalize()
casefold = str.casefold()
title = str.title()
print("Original string is",str,"\n Some string method:\n",length,"\n",upper,"\n",lower,"\n",swapcase,"\n",capitalize,"\n",casefold,"\n",title)

#List 
fruits1 = ["apple", "banana", "orange", "strawberry"]
fruits1.append("papaya")
print("After append:", fruits1)
fruits2 = ["grape", "mango"]
fruits1.extend(fruits2)
print("After extend:", fruits1)
fruits1.insert(2, "blueberry")
print("After insert:", fruits1)
fruits1.remove("banana")
print("After remove:", fruits1)
removed_item = fruits1.pop(3)
print("After pop:", fruits1, "| Removed item:", removed_item)
index_of_orange = fruits1.index("orange")
print("Index of 'orange':", index_of_orange)
fruits1.append("apple")
apple_count = fruits1.count("apple")
print("Count of 'apple':", apple_count)
fruits1.reverse()
print("After reverse:", fruits1)
fruits1.sort()
print("After sort (ascending):", fruits1)
fruits1.sort(reverse=True)
print("After sort (descending):", fruits1)
fruits_copy = fruits1.copy()
print("Copy of the list:", fruits_copy)
fruits1.clear()
print("After clear:", fruits1)
print("Length of fruits_copy:", len(fruits_copy))

#Tuple 
veg1 = ("carrot", "cauliflower", "tomato", "onion")
veg1 = veg1 + ("cabbage",)
print("After adding an item:", veg1)
veg2 = ("radish", "potato")
veg1 = veg1 + veg2
print("After extending:", veg1)
veg1_list = list(veg1)
veg1_list.insert(2, "blueberry")
veg1 = tuple(veg1_list)
print("After inserting an item:", veg1)
veg1_list = list(veg1)
veg1_list.remove("onion")
veg1 = tuple(veg1_list)
print("After removing an item:", veg1)
veg1_list = list(veg1)
removed_item = veg1_list.pop(3)
veg1 = tuple(veg1_list)
print("After popping an item:", veg1, "| Removed item:", removed_item)
index_of_cauliflower= veg1.index("cauliflower")
print("Index of 'cauliflower':", index_of_cauliflower)
veg1 = veg1 + ("tomato",)
tomato_count = veg1.count("tomato")
print("Count of 'tomato':", tomato_count)
veg1_list = list(veg1)
veg1_list.reverse()
veg1 = tuple(veg1_list)
print("After reversing:", veg1)
veg1_list = list(veg1)
veg1_list.sort()
veg1 = tuple(veg1_list)
print("After sorting (ascending):", veg1)
veg1_list.sort(reverse=True)
veg1 = tuple(veg1_list)
print("After sorting (descending):", veg1)
veg1_copy = veg1
print("Copy of the tuple:", veg1_copy)
veg1 = ()
print("After clearing:", veg1)
print("Length of veg1_copy:", len(veg1_copy))

#Set 
lang = {"c", "python", "java", "html", "css"}
lang.add("php")
print("After adding an item:", lang)
more_fruits = {"sql", "ai"}
lang.update(more_fruits)
print("After extending:", lang)
lang.discard("css")
print("After removing an item:", lang)
removed_item = lang.pop()
print("After popping an item:", lang, "| Removed item:", removed_item)
apple_exists = "c" in lang
print("Does 'apple' exist in the set:", apple_exists)
lang.clear()
print("After clearing the set:", lang)

#Dictionary 
fruits = {"apple": 1, "banana": 2, "cherry": 3, "date": 4, "elderberry": 5}
fruits["fig"] = 6
print("After adding an item:", fruits)
fruits.update({"grape": 7, "honeydew": 8})
print("After extending:", fruits)
del fruits["banana"]
print("After removing an item:", fruits)
removed_item = fruits.pop("cherry")
print("After popping an item:", fruits, "| Removed item:", removed_item)
keys = list(fruits.keys())
print("Keys of the dictionary:", keys)
values = list(fruits.values())
print("Values of the dictionary:", values)
items = list(fruits.items())
print("Items of the dictionary:", items)
fig_exists = "fig" in fruits
print("Does 'fig' exist in the dictionary:", fig_exists)
fruits_copy = fruits.copy()
print("Copy of the dictionary:", fruits_copy)
fruits.clear()
print("After clearing the dictionary:", fruits)

#Anagram 
def anagram(str1, str2):
  return sorted(str1) == sorted(str2)
string1 = input("Enter the first string: ")
string2 = input("Enter the second string: ")
if anagram(string1, string2):
  print("Anagrams")
else:
  print("Not anagrams")  


 