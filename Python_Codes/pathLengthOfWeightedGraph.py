
list=[('i','a',35),('i','b',45),('a','c',22),('a','d',32),
    ('b','d',28),('b','e',36),('b','f',27),('c','d',31),
    ('c','g',47),('d','g',30),('e','g',26)]
edge={'i':[],'a':[],'b':[],'c':[],'d':[],'e':[],'f':[],'g':[]}
color={'i':0,'a':0,'b':0,'c':0,'d':0,'e':0,'f':0,'g':0}
path_length=0
path=[]
def pathLength(X,Y): 
    global path_length
    global path
    color[X]=1
    len_adj=len(edge[X])
    for i in range(len_adj):
        v=edge[X][i][0]
        w=edge[X][i][1]
        if((color[v]==0) & (v!=Y)):
            path_length+=w
            path.append((X,v,w))
            pathLength(v,Y)
        elif(color[v]==0):
            path.append((X,v,w))
            path_length+=w
            print('path:',path)
            print('path length:',path_length)
            path.pop()
            path_length-=w
            break
    if(len(path)!=0):
        w=path.pop()
        path_length-=w[2]

for i in range(len(list)):
    u=list[i][0]
    v=list[i][1]
    edge[u].append((v,list[i][2]))
X=str(input('Source Vertex,X = '))
Y=str(input('Destination Vertex,Y = '))
pathLength(X,Y)