edge(i,a,35). edge(i,b,45). edge(a,c,22).
edge(a,d,32). edge(b,d,28). edge(b,e,36).
edge(b,f,27). edge(c,d,31). edge(c,g,47).
edge(d,g,30). edge(e,g,26).

pathLength(X,Y,L):- edge(X,Y,L),!.
pathLength(X,Y,L):- edge(X,Z,L1), pathLength(Z,Y,L2), L is L1+L2.

findpl:- write('Source Vertice:'), read(X), write('Destination Verice:'),
	read(Y), pathLength(X,Y,L), write('Path Length:'), write(L), nl.