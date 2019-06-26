
print("Hello, world!")

if __name__ == "foo":
    print("This")
    print("Is not")
    print("Covered. :(")


if __name__:
    print("Coverage here.")
    

print("But this")
print("Is.")

if False:
    print("Never gonna reach this.")

k = 3

if k > 2:
    print("Always gonna reach this")
elif k <= 2:
    print("Never this")
elif k > 2:
    print("Duplicate condition")
else:
    print("All other cases have been covered.")



