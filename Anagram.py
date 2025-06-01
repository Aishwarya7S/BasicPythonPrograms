def anagram(str1, str2):
  return sorted(str1) == sorted(str2)

string1 = input("Enter the first string: ")
string2 = input("Enter the second string: ")
if anagram(string1, string2):
  print("Anagrams")
else:
  print("Not anagrams")  