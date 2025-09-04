value =1
while value<10:
    value+=1
    if value ==5:
        continue
    print(value)

while value<10:
    value+=1
    if value ==5:
        continue
    print(value)
else:
    print("value is now equal:"+str(value))

names=["khayyal","sara","ahmed"]

for x in names:
    print(x)
    
for x in names:
    if x=="sara":
        break
    print(x)
for x in names:
    if x=="sara":
        continue
    print(x)
for x in "hjdsg":
    print(x)

#ranges

for x in range(4):
    print(x)


for x in range(2,4):
    print(x)

for x in range(0,100,5):
    print(x)


for x in range(5,101,5):
    print(x)
else:
    print("thats over")

names=["khayyal","sara","ahmed"]
actions=["codes","eats","sleeps"]

for name in names:
    for action in actions:
        print (name + " "+ action+".")

    for action in actions:
        for name in names:
         print (name + " "+ action+".")