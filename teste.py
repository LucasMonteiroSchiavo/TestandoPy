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
print(f'Nota da máteria 4: {nota4}')

# Verificar resposta e imprimir
if aluno_passou.lower() == 'sim':
    print(f'{nome} Passou! suas Notas foram: \n(nota 1: {nota1}) \n(nota 2: {nota2}) \n(nota 3: {nota3}) \n(nota 4: {nota4})\n Sua média foi de: {(nota1+nota2+nota3+nota4) /4}')
    print(f'Nome do Aluno: {nome} PARABÉNS')
elif aluno_passou.lower() == 'nao':
    print(f'{nome} infelizmente não passou!')
else:
    print('Resposta inválida, digite "sim" ou "nao"')

    print('Vasco')



