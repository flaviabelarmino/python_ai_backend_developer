contatos = {
    "flaviabelar@gmail.com": {"nome": "Flavia", "telefone": "1234-1234"},
    "aerosmith@gmail.com": {"nome": "Aero", "telefone": "1111-1111"},
    "gunsandroses@gmail.com": {"nome": "Guns", "telefone": "2222-2222"},
    "queen@gmail.com": {"nome": "Queen", "telefone": "3333-3333"}
}

for chave in contatos:
    print(chave, contatos[chave])

print("=" * 100)

for chave, valor in contatos.items():
    print(chave, valor)