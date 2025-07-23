import os

# r = read 
# a = Append
# w = write 
# x = Create 


#Read - error if not exits 

f = open("names.txt")

#print(f.read())
#print(f.read(4))

# print(f.readline())
# print(f.readline())

for line in f :
    print(line)

f.close()      

try :
    f=open("names.txt")
    print(f.read())
except:
    print("The file you want to read dosen't exist")
finally:
    f.close()

# Append create a file if not exits
f=open("names.txt","a")
f.write("Neil\n")
f.close()

f=open("names.txt")
print(f.read())
f.close()

#write (overwrite)
f=open("context.txt","w")
f.write("I deleted all context")
f.close()

f=open("context.txt")
print(f.read())
f.close()

#Two ways to create a new file

#Opens a file for writing , create a file if it dose not exist
f=open("names_list.txt","w")
f.close()

# creates a specified file, but returens an error if the file exits 
if not os.path.exists("dave.txt"):
    f=open("dave.txt","x")
    f.close()

# Delete a file
# avoid an error if it dosen't exist

if os.path.exists("dave.txt"):
    os.remove("dave.txt")
else:
    print("The file you wish to delete  dosen't exist") 

with open("more_names.txt") as f:
    content=f.read()

with open("names.txt","w") as f :
    f.write(content)