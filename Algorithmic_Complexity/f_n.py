#ley de la suma
def f(n):
    for i in range(n):
        print(i)
    for i in range(n):
        print(i)
# Crecimiento lineal
  
#ley de la multiplicación
def f(n):
    for i in range(n):
        for j in range(n):
            print(i, j)

#0(n) * 0(n) = crecimiento cuadrático 0(n^2)

def fibonacci(n):
    if n ==0 or n ==1:
        return 1
    return fibonacci (n-1) + fibonacci(n-1)
    # 0 (2**n)
#crecimiento exponencial, llamadas recursivas