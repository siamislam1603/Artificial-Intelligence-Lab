from queue import PriorityQueue
neighbor=[('i','a',35), ('a','i',35), ('i','b',45), ('b','i',45),
('a','c',22), ('c','a',22), ('a','d',32), ('d','a',32),
('b','d',28), ('d','b',28), ('b','e',36), ('e','b',36),
('b','f',27), ('f','b',27), ('c','d',31), ('d','c',31),
('c','g',47), ('g','c',47), ('d','g',30), ('g','d',30),
('e','g',26), ('g','e',26)]
h_fn={'i':80, 'a':55, 'b':42, 'c':34,
'd':25, 'e':20, 'f':17, 'g':0}
edge={}
pq=PriorityQueue()
pp={}
path_cost=0
def cal_gn(parent,node):
    if(parent==-1 or parent not in pp.keys()):
        return 0
    else:
        for v in edge[node]:
            if v[0]==pp[parent][0]:
                break
        return v[1]+cal_gn(pp[parent][1],pp[parent][0])
def a_star(src,dest):
    ind=0
    pq.put((h_fn[src],src,ind,-1))
    while not pq.empty():
        u = pq.get()
        pp[u[2]]=(u[1],u[3],u[0])
        if(u[1]==dest):
            return 1
        for v in edge[u[1]]:
            ind+=1
            fn=cal_gn(u[2],v[0])+h_fn[v[0]]
            pq.put((fn,v[0],ind,u[2]))
        if len(pp)>1:
            parent_list=list(pp.keys())
            while u[3]!=parent_list[-2] and len(parent_list)!=0:
                del pp[parent_list[-2]]
                parent_list.remove(parent_list[-2])
    return 0
        
for i in range(len(neighbor)):
    u=neighbor[i][0]
    v=neighbor[i][1]
    if u not in edge:
        edge[u]=list()
    edge[u].append((v,neighbor[i][2]))
find_path=a_star('i','g')
if(find_path==1):
    print(f'Possible path = {pp}')
    parent_list=list(pp.keys())
    for i in range(len(parent_list)-1,0,-1):
        u=pp[parent_list[i]][0]
        v=pp[parent_list[i-1]][0]
        for node in edge[u]:
            if(node[0]==v):
                path_cost+=node[1]
                break
    print(f'Path cost = {path_cost}')
else:
    print('Path not found')