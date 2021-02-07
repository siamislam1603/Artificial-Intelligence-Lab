tupleList1=[('parent', 'Hasib', 'Rakib'),('parent', 'Rakib', 'Sohel'),
            ('parent', 'Rakib', 'Rahim'),('parent', 'Rakib', 'Rebeka'),
            ('parent', 'Sohel', 'Salam'),('parent', 'Rashid', 'Hasib'),
            ('parent','Rebeka','Urmi'),('parent','Urmi','Mousumi')]

male=['Hasib','Rakib','Sohel','Rahim','Salam','Rashid']
female=['Rebeka','Urmi','Mousumi']

X=str(input("Aunt:"))
output=''

for i in range(len(tupleList1)):
    if (tupleList1[i][0] == 'parent'):
        if(tupleList1[i][2] == X):
            for j in range(len(tupleList1)):
                if ((tupleList1[j][0] == 'parent') &(tupleList1[i][1] == tupleList1[j][1]) & (i!=j) & (tupleList1[i][2] in female)):
                    for l in range(len(tupleList1)):
                        if(tupleList1[l][0]=='parent'):
                            if(tupleList1[l][1]==tupleList1[j][2]):
                                output+=tupleList1[l][2]+' '

if(len(output)>0):
    print('Niece/Nephews:',output)
else:
    print('Niece/Nephews:','Not Found')