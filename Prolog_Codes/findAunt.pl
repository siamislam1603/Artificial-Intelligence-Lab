parent('Hasib' , 'Rakib'). parent('Rakib' , 'Sohel').
parent('Rakib' , 'Rahim'). parent('Rakib','Rebeka').
parent('Sohel','Salam'). parent('Rebeka','Urmi').
parent('Urmi','Mousumi'). parent('Rashid' , 'Hasib').

male('Rakib'). male('Sohel'). male('Rahim'). male('Hasib').
male('Rahim'). male('Salam'). male('Rashid').

female('Rebeka'). female('Urmi'). female('Mousumi').

sister(X,Y):-parent(Z,X), parent(Z,Y), female(X), not(X=Y).

aunt(X,Y):-sister(X,Z), parent(Z,Y).
