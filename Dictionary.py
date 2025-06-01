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

