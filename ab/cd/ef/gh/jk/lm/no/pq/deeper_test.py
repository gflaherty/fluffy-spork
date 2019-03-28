
print("Hello, world!")

if __name__ == "foo":
    print("This")
    print("Is not")
    print("Covered. :(")

print("But this")
print("Is.")

def test_dummy():
    assert(True)
    if __name__ == "bar":
        assert(False)
        print("Not covered")
