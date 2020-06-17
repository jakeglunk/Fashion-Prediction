import os

path = '/home/jake/Downloads/darknet-master/custom_data/images'

name = os.listdir(path)

newlist = name[0:436]
print(len(newlist))
print(len(name))

while len(name) > 3924:
    for i in name:
        if i in newlist:
            name.remove(i)


print(len(name))

write = open('train.txt','w')

for item in name:
    print(item)
    write.write('custom_data/images/'+item+'\n')

write.close()

write = open('test.txt','w')

for item in newlist:
    print(item)
    write.write('custom_data/images/'+item+'\n')

write.close()
