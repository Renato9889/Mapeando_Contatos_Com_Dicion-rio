contatos_lista = [('Yan', '1234-5678'), ('Pedro', '9999-9999'),
                    ('Ana', '8765-4321'), ('Marina', '8877-7788')]

contatos = dict(contatos_lista)
print(contatos)

print(contatos.get('Yan', 'Contato não encontrado'))
print(contatos.get('João', 'Contato não encontrado'))

print('Yan' in contatos)

print('9999-9999' in contatos)

print('9999-9999' in contatos.values())

contatos['João'] = '8887-7778'
print(contatos)

del contatos['Marina']
print(contatos)

contatos = {'Yan': '1234-5678', 'Pedro': '9999-9999', 'Ana': '8765-4321',
            'Marina': '8877-7788', 'João': '8887-7778'}

print(contatos.pop('Marina', 'Contato não encontrado'))
print(contatos.pop('Catarina', 'Contato não encontrado'))
print()
print(contatos)

meus_contatos = {'Yan': '1234-5678', 'Pedro': '9999-9999',
                    'Ana': '8765-4321', 'João': '8887-7778'}

contatos_do_pedro = {'Yan': '1234-5678', 'Fernando': '4345-5434',
                        'Luiza': '4567-7654'}

for nome in contatos_do_pedro:
    meus_contatos[nome] = contatos_do_pedro[nome]

print(meus_contatos)

meus_contatos_novo = {nome: '9' + meus_contatos[nome] for nome in meus_contatos}
print(meus_contatos_novo)