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

