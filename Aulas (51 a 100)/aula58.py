from rich.traceback import install
install()

#!Interpretador do Python:
#*python mod.py (executa o mod):
#?um "módulo" é simplesmente um arquivo contendo código Python. Esse código pode conter definições de funções, classes, variáveis e outras instruções Python. 
#*python -u (unbuffered): 
#?se refere a um tipo de fluxo de dados onde a saída é exibida imediatamente, em vez de ser armazenada em um buffer antes de ser exibida.
#?Isso é relevante principalmente quando estamos lidando com a saída padrão (stdout), que é a forma pela qual o Python exibe informações no console.
#*python -m mod (lib mod como script): 
#?executa uma biblioteca do python como um script // executa a biblioteca do python como módulo.. ex:
#!pytohn -m venv 'nome do ambiente virtual' : comando p/ executar a biblioteca venv como um script (cria um ambiente virtual chamando 'ambiente')
#*python -c 'cmd' (comando):
#?pede para o python executar tal comando
#? -c 'print("Oi") ; print (1+1)' - ; deu a quebra de linha
#*python -i mod.py (interativo com mod):
#?carrega o arquivo python que for necessário 
#?python -i aula57.py (exemplo)


#todo python tem ; / ex:
#todo print (1 + 1) 
#todo print (2 + 2)

#todo poderia ser escrito da seguinte forma: print (1 + 1) ; print (2 + 2)
#todo o ; significa uma quebra de linha


#!The Zen of Python, por Tim Peters:

#*Bonito é melhor que feio.
#*Explícito é melhor que implícito.
#*Simples é melhor que complexo.
#*Complexo é melhor que complicado.
#*Plano é melhor que aglomerado.
#*Esparso é melhor que denso.
#*Legibilidade conta.
#*Casos especiais não são especiais o bastante para quebrar as regras.
#*Embora a praticidade vença a pureza.
#*Erros nunca devem passar silenciosamente.
#*A menos que sejam explicitamente silenciados.
#*Diante da ambiguidade, recuse a tentação de adivinhar.
#*Deve haver um -- e só um -- modo óbvio para fazer algo.
#*Embora esse modo possa não ser óbvio à primeira vista a menos que você seja holandês.
#*Agora é melhor que nunca.
#*Embora nunca frequentemente seja melhor que *exatamente* agora.
#*Se a implementação é difícil de explicar, é uma má ideia.
#*Se a implementação é fácil de explicar, pode ser uma boa ideia.
#*Namespaces são uma grande ideia -- vamos fazer mais dessas!



