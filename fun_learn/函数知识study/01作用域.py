x = 3
def outer():
    x = 1
    def inner():
        x = 2
        print(f"inner:{x}")
    inner()
    print(f"outer:{x}")

    def change():
        global x
        x = 1122
    change()
outer()
print(f"global:{globals()['x']}")