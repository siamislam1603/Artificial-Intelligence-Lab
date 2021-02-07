gtp=[(1,1,1), (2,1,2), (3,1,3), (4,2,3), (5,3,3), (6,3,2), (7,3,1), (8,2,1)]
gblnk = (2,1)
tp=[(1,1,2), (2,1,3), (3,2,1), (4,2,3), (5,3,3), (6,2,2), (7,3,2), (8,1,1)]
blnk = (3,1)
h=0
manhattan_distance=[]
def calcH(T,manhattan_distance):
    if(T==8):
        return manhattan_distance
    else:
        D=dist(tp[T][0])
        manhattan_distance.append(D)
        return calcH(T+1,manhattan_distance)
def dist(T):
    V=0
    for i in range(8):
        if(tp[i][0]==T & gtp[i][0]==T):
            A,B,C,D=tp[i][1],tp[i][2],gtp[i][1],gtp[i][2]
            V=abs(A-C)+abs(B-D)
            break
    return V
def sumList(manhattan_distance):
    if(len(manhattan_distance)==0):
        return 0
    else:
        return manhattan_distance.pop(0)+sumList(manhattan_distance)
X=calcH(0,manhattan_distance)
print('Manhattan Distance:',X)
sum=sumList(manhattan_distance)
print('Heuristics:',sum)