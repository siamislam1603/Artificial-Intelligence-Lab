tupleList1=[('parent', 'Hasib', 'Rakib'),('parent', 'Rakib', 'Sohel'),
            ('parent', 'Rakib', 'Rahim'),('parent', 'Rakib', 'Rebeka'),
            ('parent', 'Sohel', 'Salam'),('parent', 'Rashid', 'Hasib'),
            ('parent','Rebeka','Urmi'),('parent','Urmi','Mousumi')]

male=['Hasib','Rakib','Sohel','Rahim','Salam','Rashid']
female=['Rebeka','Urmi','Mousumi']

X=str(input("Sister:"))
output=''

for i in range(len(tupleList1)):
    if (tupleList1[i][0] == 'parent'):
        if(tupleList1[i][2] == X):
            for j in range(len(tupleList1)):
                if ((tupleList1[j][0] == 'parent') &(tupleList1[i][1] == tupleList1[j][1]) & (i!=j) & (tupleList1[i][2] in female)):
                    output+=tupleList1[j][2]+' '
if(len(output)>0):
    print('Siblings:',output)
else:
    print('Siblings:','Not Found')