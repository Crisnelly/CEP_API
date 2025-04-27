import requests

def buscar_cep(cep):

    response=requests.get(f"https://viacep.com.br/ws/{cep}/json/")
    api= response.json()
    return f"seu uf é: {api['uf']}, seu logradouro é: {api['logradouro']}, seu bairro é: {api['bairro']}, sua localidade é: {api['localidade']} "


cep1 = input("digite um cep:")

cep = buscar_cep(cep1)

print(cep)