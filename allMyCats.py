cat_names = []

while True:
    print(f"Enter the name of cat {len(cat_names) + 1} (Or enter nothing to stop.):")

    name = input()

    if name == "":
        break
    cat_names += [name]
print("The cats name are:")    
for index, name in enumerate(cat_names, start=1):
    print(f"{index}. {name}")
