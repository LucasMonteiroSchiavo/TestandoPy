nome = "Lucas"
idade = 27
faculdade = "Análise e Desenvolvimento de Sistemas"
nota1 = 7.2
nota2 = 7.1
nota3 = 7.5
nota4 = 8.0
aluno_passou = input(' O Aluno Passou ? (sim/nao): ')

#Verificar resposta e imprimir
if aluno_passou.lower() == 'sim':
    print (f'{nome} Passou!')
elif aluno_passou.lower() == 'nao':
    printf(f'{nome} infelizmente não passou!')
else:
    print('Resposta inválida, digite "sim" ou "nao"')

print(f'Nome do Aluno: {nome}')
print(f'Idade do aluno: {idade}')
print(f'Nota da Máteria 1: {nota1}')


