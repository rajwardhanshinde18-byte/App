# F(n)= F(n-1)+F(n-2)
#F(0)=0 ,F(1)=1
# n=1+1
# 0,1,1,2,3,5,8,13,21

def fibonacci(n):
    if n<=1:
        return n

    return fibonacci(n-1)+fibonacci(n-2)

# print fibonacci no.

def fibonacci_memo(n, memo):
    if n<=1:
        return n
    if n in memo:
        return memo[n]

    memo[n]=(fibonacci_memo(n-1,memo) +fibonacci_memo(n-2, memo))

    return memo[n]

memo = {}
print(fibonacci_memo(40,memo))
print("Memo:",memo)
    