n = int(input('Enter tickets quantity (min 1, max 100): '))
L = [int(input(f"Enter participant age for ticket {i}:")) for i in range(1,n+1)]
T = [990 for j in range(n) if 18 <= L[j] < 25]
T1 = [1390 for j in range(n) if 25 <= L[j]]
T2 = [*T, *T1]
if n > 3 and T2:
    print('Congratulation! You get 10% discount! Your price: ', 0.9 * sum(T2))
else:
    print('Your ticket(s) price: ', sum(T2))
print('Thank You')
