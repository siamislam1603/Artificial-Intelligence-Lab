tupleList1=[('parent', 'Hasib', 'Rakib'),('parent', 'Rakib', 'Sohel'),
            ('parent', 'Rakib', 'Rahim'),('parent', 'Rakib', 'Rebeka'),
            ('parent', 'Sohel', 'Salam'),('parent', 'Rashid', 'Hasib'),
            ('parent','Rebeka','Urmi'),('parent','Urmi','Mousumi')]

X=str(input("Grandchildren:"))
output=''

for i in range(len(tupleList1)):
    if ((tupleList1[i][0] == 'parent')&( tupleList1[i][2] == X)):
        for j in range(len(tupleList1)):
            if ((tupleList1[j][0] == 'parent') & ( tupleList1[i][1] == tupleList1[j][2])):
                output+=tupleList1[j][1]+' '
                
if(len(output)>0):
    print('Grandparent:',output)
else:
    print('Grandparent:','Not Found')