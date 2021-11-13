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
adj={}
visited={}
pq=PriorityQueue()
pp=[]
path_cost=0
def greedy_bfs(src,dest):
    pq.put((0,src))
    while not pq.empty():
        u = pq.get()[1]
        pp.append(u)
        visited[u]=1
        if(u==dest):
            return 1
        for v in edge[u]:
            if(visited[v]==0):
                pq.put((h_fn[v],v))
        if len(pp)>=2:
            while u not in edge[pp[-2]]:
                pp.remove(pp[-2])
    return 0
        
for i in range(len(neighbor)):
    u=neighbor[i][0]
    v=neighbor[i][1]
    if u not in edge:
        edge[u]=list()
        adj[u]=list()
        visited[u]=0
    edge[u].append(v)
    adj[u].append((v,neighbor[i][2]))
if(greedy_bfs('i','g')==1):
    print(f'Possible path: {pp}')
    for i in range(len(pp)-1):
        u=pp[i]
        v=pp[i+1]
        for node in adj[u]:
            if(v==node[0]):
                path_cost+=node[1]
                break
    print(f'Path Cost: {path_cost}')
else:
    print('Path not found')