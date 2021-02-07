parent('Hasib' , 'Rakib'). parent('Rakib' , 'Sohel').
parent('Rakib' , 'Rahim'). parent('Rakib','Rebeka').
parent('Sohel','Salam'). parent('Rebeka','Urmi').
parent('Urmi','Mousumi'). parent('Rashid' , 'Hasib').

grandchildren(X, Y) :- parent(Y, Z),parent(Z, X).
