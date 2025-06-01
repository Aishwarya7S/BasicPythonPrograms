num = 7337
rev = int(str(num)[::-1])

if num == rev:
  print('Palindrome')
else:
  print("Not Palindrome")

# Another Way
# num = 1234
# temp = num
# rev = 0
# while temp > 0:
#     remainder = temp % 10
#     rev = (rev * 10) + remainder
#     temp = temp // 10
# if num == rev:
#   print('Palindrome')
# else:
#   print("Not Palindrome")