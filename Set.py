lang = {"c", "python", "java", "html", "css"}
lang.add("php")
print("After adding an item:", lang)\

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
