#Dictionaies
band={
    "voclas":"Planet",
    "guitar":"Page"
}
band2 =dict(vocals="Planet",guitar="Page")

print (band)
print(band2)
print(type(band))
print(type(band2))

#Access items
print(band["voclas"])
print(band.get("guitar"))

#list all key
print(band.keys())

#list all values
print(band.values())

#list of key /value pairs as tuples
print(band.items())

#verfy a key exist

print("guitar" in band)
print("triangel" in band)

#change values
band["voclas"]="choco"
band.update({"bass":"jpj"})

print(band)

print(band.pop("bass"))

print(band)

band["hi"]="hwll"
print(band)

print(band.popitem())
print(band)

#delete and clear
band["hi"]="hwll"
del band["hi"]
print(band)

band2.clear()
print(band2)
del band2

#copy 
# band2=band#create a refrence
# print("Bad copy")
# print(band)
# print(band2)

# band2["ggd"]="hdggd"
# print(band)

band2=band.copy()
band2["jsjc"]="jksabc" 
print(band)
print(band2)

#or use dict copy
band3=dict(band)
band3["jy"]="jhg" 
print(band)
print(band3)
#nested dict
m1={
    "name":"khaa",
    "jop":"tech"
}
m2={
    "name":"jd",
    "jop":"doc"
}
ban={
    "m1":m1,
    "m2":m2
}
print(ban)
print(ban["m1"]["name"])

#sets
nums={1,2,3,4,6}

nums2=set((1,2,4,6,4,2,))


print(nums)
print(nums2)
print(type(nums))
print(len(nums))
#no duplicates
nums={1,2,2,4,6}

print(nums)
nums={1,True,False,0,2,2,4,6}
print(nums)
#check if a value is there
print(2 in nums)


#adding element 

nums.add(8)
print(nums)

monums ={5,6,7}
nums.update(monums)
print(nums)

one={1,2,3}
tow={4,5,6}
mynewset=one.union(tow)
print(mynewset)

#keep only the dup
one={1,2,5}
tow={4,5,2}
one.intersection_update(tow)
print(one)
#keep all but the dup
one={1,2,5}
tow={4,5,2}
one.symmetric_difference_update(tow)
print(one)