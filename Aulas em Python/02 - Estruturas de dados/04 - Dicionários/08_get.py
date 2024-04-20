contatos = {"flaviabelar@gmail.com": {"nome": "Flavia", "telefone": "1234-1234"}}

# contatos["chave"]   # KeyError

resultado = contatos.get("chave")
print(resultado)

resultado = contatos.get("chave", {})
print(resultado)

resultado = contatos.get(
    "flaviabelar@gmail.com", {}
)
print(resultado)