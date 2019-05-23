# mylist = ["a", "b", "a", "c", "c"]
# mylist = list(dict.fromkeys(mylist))
# print(mylist)

def function(x):
    print("value inside",x)
    return list(dict.fromkeys(x))

mylist = function(["a", "b", "a", "c", "c"])
print(mylist)
