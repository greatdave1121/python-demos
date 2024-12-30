while True:
    print("Who are you?")
    name = input().capitalize()
    if name != "Joe":
        continue
    print("Hello Joe, what is a password? (It is a fish)")
    password = input().capitalize()
    if password == "Swordfish":
        break
print("Access granted!")