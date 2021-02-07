findsum:- write('1st term:'), read(A), write('Interval:'), read(D),
	write('n-term:'), read(N), sum1(A, D, N, S),
	write('Sum of n terms:'), write(S).
sum1(_, _, 0, 0):-!.
sum1(A, D, N, S):-N1 is N-1, sum1(A, D, N1, S1), S is S1+A+(N-1)*D.