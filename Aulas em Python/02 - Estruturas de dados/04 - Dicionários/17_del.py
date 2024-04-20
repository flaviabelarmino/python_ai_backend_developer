contatos = {
    "flaviabelar@gmail.com": {"nome": "Flavia", "telefone": "1234-1234"},
    "aerosmith@gmail.com": {"nome": "Aero", "telefone": "1111-1111"},
    "gunsandroses@gmail.com": {"nome": "Guns", "telefone": "2222-2222"},
    "queen@gmail.com": {"nome": "Queen", "telefone": "3333-3333"}
}

del contatos["flaviabelar@gmail.com"]["telefone"]
del contatos["queen@gmail.com"]

print(contatos)