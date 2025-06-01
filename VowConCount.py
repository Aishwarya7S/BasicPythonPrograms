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
