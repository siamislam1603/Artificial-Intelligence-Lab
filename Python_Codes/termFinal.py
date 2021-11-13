facts=['A','B','C','D']
rules=[('P','Q'),('C','L','P'),('D','M','P'),('B','L','M'),('A','P','L'),('A','B','L'),('A','D','G'),('G','B','C')]
print('KB:')
for fact in facts:
    print(fact)
for index in range(len(rules)):
    j=0
    for rule in rules[index][:-1]:
        if(j==0):
            print(f'{rule}',end=' ')
            j=1
        else:
            print(f'^ {rule}',end=' ')
    print(f'=> {rules[index][-1]}')

goal=input('enter your goal: ?')
stack=[]
visited=[]
def find_in_kb(item):
    flag=-1
    for i in range(len(rules)):
        if(rules[i][-1]==item):
            if(flag==-1):
                flag=i
            else:
                stack.append(i)
    return flag

def backward_chaining(index):
    j=0
    for rule in rules[index][:-1]:
        if(j==0):
            print(f'?{rule}',end=' ')
            j=1
        else:
            print(f'^ {rule}',end=' ')
    print(f'=> {rules[index][-1]}')

    if rules[index][-1] not in visited:
        visited.append(rules[index][-1])

    for rule in rules[index][:-1]:
        print(f'?{rule}')
        if rule in facts:
            print(f'{rule} found in KB')
        else:
            found=rule in visited
            if(found==False):
                index=find_in_kb(rule)
                if(index!=-1):
                    b=backward_chaining(index)
                else:
                    print(f'{rule} not found in KB')
                    return 0
            elif(found==True):
                if(len(stack)>0):
                    index=stack.pop()
                    b=backward_chaining(index)
                else:
                    print(f'Don\'t have any alternatives!')
                    return 0
            else:
                print(f'KB exhausted or goal {goal} not found')
                return 0
    return 1

if(goal in facts):
    print('Goal found in KB')
else:
    index=find_in_kb(goal)
    if(index!=-1):
        print('\nQuery:\n')
        found=backward_chaining(index)
        if(found==1):
            print(f'{goal} can be achieved from KB!')
        else:
            print(f'{goal} can\'t be achieved from KB')
    else:
        print(f'{goal} Not found in KB')