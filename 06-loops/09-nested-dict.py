nested_dict = {
    'a': {'name': 'Alice', 'age': 30},
    'b': {'name': 'Bob', 'age': 25},
    'c': {'name': 'Charlie', 'age': 35}
}

for key, value in nested_dict.items():
    print(f"Key: {key}")
    for subkey, subvalue in value.items():
        print(f"  {subkey}: {subvalue}")
