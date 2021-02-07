L=[6,1,5,7,4,3,8,1]
horizontal=[0 for x in range(8)]
diagonal_up=horizontal
diagonal_down=horizontal
attacking_pair=0
att={'hl':{},'dia_up':{},'dia_down':{}}
def evalState(I):
    if(I==8):
        return 0
    else:
        attacking_pair=hl(I)+dia_up(I)+dia_down(I)
        return evalState(I+1)+attacking_pair
def hl(I):
    count,element_I,index=0,L[I],I+1
    att['hl'][index]=[]
    for i in range(8):
        if((i!=I) & (L[i]==element_I) & (horizontal[i]==0)):
            count+=1
            att['hl'][index].append(i+1)
    if count>0:
        horizontal[I]=1
        print(f"hl({index}): {att['hl'][index]}")
    return count
def dia_up(I):
    count,diagonal_val,index=0,L[I]+1,I+1
    att['dia_up'][index]=[]
    for i in range(I+1,8,1):
        if((L[i]==diagonal_val) & (diagonal_up[i]==0)):
            count+=1
            att['dia_up'][index].append(i+1)
        diagonal_val+=1
    if count>0:
        diagonal_up[I]=1
        print(f"dia_up({index}): {att['dia_up'][index]}")
    return count
def dia_down(I):
    count,diagonal_val,index=0,L[I]-1,I+1
    att['dia_down'][index]=[]
    for i in range(I+1,8,1):
        if((L[i]==diagonal_val) & (diagonal_down[i]==0)):
            count+=1
            att['dia_down'][index].append(i+1)
        diagonal_val-=1
    if count>0:
        diagonal_down[I]=1
        print(f"dia_down({index}): {att['dia_down'][index]}")
    return count

print(f'Total no of attacking pairs: {evalState(0)}')