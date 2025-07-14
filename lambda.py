squared=lambda num: num * num

print (squared(2))

addTwo=lambda num : num + 2

print (addTwo(7))

sumt=lambda a,b:a+b

print(sumt(4,2))


##################
def funbulder(x):
   return lambda num : num +x

addTen=funbulder(10)

addTweny=funbulder(20)

print(addTen(7))
print(addTweny(7))



####################



numbers=[2,4,53,6,7,8,2,33,5]

squarednums=map(lambda num : num * num, numbers)

print(list(squarednums))


############

lambda num : num % 2 !=0

odd_nums=filter(lambda num : num % 2 !=0, numbers)

print(list(odd_nums))


#############

from functools import reduce


numbers=[1,2,3,6,8,1]

total=reduce(lambda acc,curr:acc+curr,numbers)

print(total)

print(sum(numbers))




names=['Dave gray ', 'lhayyal aba ', 'ahmed ali ', 'haydy alh']

char_count=reduce(lambda acc, curr: acc+ len(curr),names,0)

print(char_count)