from http import client
from pydoc import cli


clientes = {
    'Cliente1': {
        'Nome': 'Antonio',
        'Sobrenome': 'Gabinio',
    },
    'Cliente2': {
        'Nome': 'Antonio',
        'Sobrenome': 'Filho',
    },
}

for clientes_k, clientes_v in clientes.items():
    print(f'Exibindo {clientes_k}')
    for dados_k, dados_v in clientes_v.items():
        print(f'\t {dados_k} = {dados_v} ')