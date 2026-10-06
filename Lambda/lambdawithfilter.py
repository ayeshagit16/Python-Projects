users = [
    {"name": "Alice", "age": 25, "active": True},
    {"name": "Bob", "age": 17, "active": True},
    {"name": "Charlie", "age": 30, "active": False}
]

active_users = list(filter(lambda u:u["active"] and u["age"] >= 18, users))
print(active_users)


words = ["apple", "avocado", "banana", "apricot", "pear"]

# Keep if it starts with 'a' and length > 5, otherwise drop it (False)
filtered_fruits = list(filter(lambda w:True if w.startswith("a") and len(w) > 5 else False, words))
print(filtered_fruits)

data = tuple(filter(lambda x: x%2 == 0, range(10)))
print(data)
