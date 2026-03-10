def fibonacci(n):
    a = 0
    b = 1
    for i in range(n):
        a, b = b, a + b
    return a

def cetakFibo(n):
    a = 0
    b = 1
    for i in range(n):
        print(a, end=" ")
        a, b = b, a + b

n = int(input())
print(fibonacci(n))
cetakFibo(n)
