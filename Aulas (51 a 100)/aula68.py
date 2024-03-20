"""
Escopo de funções em Python
Escopo significa o local onde aquele código pode atingir.
*Existe o escopo global e local.
?O escopo global é o escopo onde todo o código é alcançavel.
!O escopo local é o escopo onde apenas nomes do mesmo local podem ser alcançados.
"""

# def escopo(): #!x faz parte do escopo local da função
#     x = 1    
#     print(x)
# escopo()

# x = 1   
# def escopo(): #!x faz parte do escopo local da função, ou seja é uma variável local
#     print(x)
# escopo()

# #*________________

# #!x não faz parte somente do escopo da função, ou seja é uma variável global
# x = 1 
# def escopo():             #!má prática de programação
#     print(x)
# print(x)    
# escopo()
#*________________

x = 1 

def escopo():             #!má prática de programação
    global x #!torna x = 10 como o valor global (x = 10 tanto dentro quanto fora da função)
    x = 10
    def outra_funcao():
        y = 2
        print(x , y)
    outra_funcao()
    print(x)

print(x)
escopo()








