PasswordFile = open("PasswordFile.txt")
SecretePassword = PasswordFile.read()
print("Enter your password")

TypedPassword = input()
TypedPassword = int(TypedPassword)
SecretePassword = int(SecretePassword)
if TypedPassword == SecretePassword:
    print("Access granted")
elif TypedPassword == 123456:
    print("That's a password an idiot uses")
else:
    print("Wrong password")