
def calcular_sequencia_fibonacci(n):
    #FUNCAO RECURSIVA
    #F(n)=F(n−1)+F(n−2) formula matematica da sequencia de fibonacci
    numero = calcular_sequencia_fibonacci(n-1) + calcular_sequencia_fibonacci(n-2)
    return numero

result = calcular_sequencia_fibonacci(4)
print(result)