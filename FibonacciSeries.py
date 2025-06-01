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

# Another Way
# def fib(num):
#     if num < 0:
#         print("Incorrect input")
#     elif num == 0:
#         return 0
#     elif num == 1 or num == 2:
#         return 1
#     else:
#         return fib(num-1) + fib(num-2)
# print(fib(5))


