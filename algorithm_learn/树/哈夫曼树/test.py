class OB():
    def __init__(self,num):
        self.num = num
    def __lt__(self,other):
        return self.num<other.num

l = [OB(9),OB(4),OB(7),OB(1),OB(7)]
l.sort()
print([e.num for e in l])
