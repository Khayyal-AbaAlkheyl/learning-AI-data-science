def add_one(num):
    if num >= 9:
        return num+1
    total=num+1
    print(total)
    return add_one(total)

print(add_one(0))
# loop to do the same 
def loop_add_one(num):
    for x in range(0,10):
     print(x)

loop_add_one(0)