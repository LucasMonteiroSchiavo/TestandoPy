nome = "Lucas"
idade = 27
faculdade = "Análise e Desenvolvimento de Sistemas"
nota1 = 7.2
nota2 = 7.1
nota3 = 7.5
nota4 = 8.0
aluno_passou = input(' O Aluno Passou ? (sim/nao): ')


print(f'Nome do Aluno: {nome}')
print(f'Idade do aluno: {idade}')
print(f'Nota da Máteria 1: {nota1}')
print(f'Nota da Matéria 2: {nota2}')
print(f'Nota da Matéria 3: {nota3}')
print(f'Nota da máteria 4: {nota4}')g

# Verificar resposta e imprimir
if aluno_passou.lower() == 'sim':
    print(f'{nome} Passou!')
elif aluno_passou.lower() == 'nao':
    print(f'{nome} infelizmente não passou!')
else:
    print('Resposta inválida, digite "sim" ou "nao"')


print('O vasco é o melhor time do mundo')