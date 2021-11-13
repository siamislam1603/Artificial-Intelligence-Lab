dic = {}
with open('F:/4.1/AI/Lab/Python_Codes/dictionary.txt',mode='r') as f:
    for line in f:
        name, dept, cg = line.split()
        dic[name]=list((dept,cg))

print(dic)

for name in dic:
    if name=='rifat':
        dic[name][1]=3.0
    elif name =='hasib':
        dic[name][1]=3.5

print(dic)

with open('F:/4.1/AI/Lab/Python_Codes/file2.txt', mode='w') as f:
    for name in dic:
        f.write(name+'\t'+dic[name][0]+'\t'+str(dic[name][1])+'\n')