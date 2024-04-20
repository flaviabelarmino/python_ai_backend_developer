contatos = {
    "flaviabelar@gmail.com": {"nome": "Flavia", "telefone": "1234-1234"},
    "aerosmith@gmail.com": {"nome": "Aero", "telefone": "1111-1111"},
    "gunsandroses@gmail.com": {"nome": "Guns", "telefone": "2222-2222"},
    "queen@gmail.com": {"nome": "Queen", "telefone": "3333-3333"}
}

resultado = "flaviabelar@gmail.com" in contatos
print(resultado)

resultado = "pinkfloyd@gmail.com" in contatos
print(resultado)

resultado = "idade" in contatos["flaviabelar@gmail.com"]
print(resultado)

resultado = "telefone" in contatos["aerosmith@gmail.com"]
print(resultado)