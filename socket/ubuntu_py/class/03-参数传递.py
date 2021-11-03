def test(a,b,*args,**kwargc):
    print(a)
    print(b)
    print(args)
    print(kwargc)
    test1(*args,kwargc)

def test1(a,b,*args,**kwargc):
    print("------")
    print(a)
    print(b)
    print(args)
    print(kwargc)

test(33,44,55,66,77,88,99,name=10)

