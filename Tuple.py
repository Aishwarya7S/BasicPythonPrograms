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

