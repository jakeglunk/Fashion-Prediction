import pandas as pd
import os

k=0

filename=''
labels =['Coat','Footwear','Glasses','Hat','Jacket','Jeans','Shirt','Suit','Sunglasses','Swimwear','Tie','Trousers']
path = '/home/jake/Downloads/OIDv4_ToolKit-master/OID/Dataset/test/'

while k < len(labels):
    print(k)
    i=0
    fullpath= path+labels[k]+'/'+'Label'
    folder = os.listdir(fullpath)

    while i < len(folder):
        filename = str(folder[i])

        with open(fullpath+'/'+filename, 'r') as myfile:
          data = myfile.readlines()

        for string in data:
            first = data[0].replace('\n','')
            data.remove(data[0])
            data.append(first)

        newlist =[]

        for string in data:
            new = string.split(' ')
            newlist.append(new)


        df = pd.DataFrame(newlist)
        column0 = df[0].copy()
        columnlist = column0.tolist()


        for string in columnlist:
            label = string.replace(labels[k],str(k))
            columnlist.remove(columnlist[0])
            columnlist.append(label)


        newcolumn = pd.DataFrame(columnlist)

        df = df.replace(df[0],newcolumn)

        finallist = df.to_numpy().tolist()

        write = open('/home/jake/Desktop/new_Test/'+'t_'+labels[k]+'/'+filename,'w')

        for list in finallist:
            george = ' '.join(list)
            print(george)
            write.write(george+'\n')

        write.close()
        i = i+1

    k = k+1
