num = 7
fact = 1

for i in range(1,num+1):
  fact *= i
print("Factorial of",num,"is",fact)

# Another Way
# def fact(n):
#   return 1 if(n==0 or n==1) else n * fact(n-1)
# num=3
# print("The factorial of",num,"is",fact(num))
