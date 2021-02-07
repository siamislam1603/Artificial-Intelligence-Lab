def sum1(A,D,N):
    if (N==0):
        return 0
    elif (N>0):
        return sum1(A,D,N-1)+A+(N-1)*D
t=int(input('No of test cases:'))
for i in range(1,t+1,1):
    print(f'\nCase-{i}:')
    A=int(input('1st element,A = '))
    D=int(input('Interval,D = '))
    N=int(input('n-terms = '))
    print('Sum of 1st n-terms:', sum1(A,D,N))
