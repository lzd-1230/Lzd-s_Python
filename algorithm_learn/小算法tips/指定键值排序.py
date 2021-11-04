class User():
    def __init__(self,id):
        self.id = id

    def __repr__(self):
        return f"User({self.id})"

user_list = [User(1),User(3),User(2)]

res = sorted(user_list,key=lambda x: x.id)
print(res)
