parent('Hasib' , 'Rakib'). parent('Rakib' , 'Sohel').
parent('Rakib' , 'Rahim'). parent('Rakib','Rebeka').
parent('Sohel','Salam'). parent('Rebeka','Urmi').
parent('Urmi','Mousumi'). parent('Rashid' , 'Hasib').

male('Rakib'). male('Sohel'). male('Rahim'). male('Hasib').
male('Rahim'). male('Salam'). male('Rashid').

female('Rebeka'). female('Urmi'). female('Mousumi').

brother(X,Y):-parent(Z,X), parent(Z,Y), male(X), not(X=Y).