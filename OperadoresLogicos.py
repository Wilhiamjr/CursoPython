#Operador de identidade
'Quando quero verificar se as variáveis usam o mesmo espaço de memoria utilizo o is.'

curso ='NomeCurso';
nome_curso = curso;

print(curso is nome_curso);


'Operador de associação utiliza-se o in OBS: Ele verifica se tem letra maiuscula ou não '

frutas = ['laranja','maça', 'limaão'];

print('maça' in frutas);  'TRUE'
print('Maça'in frutas);   'FALSE'
