contatos = {"flaviabelar@gmail.com": {"nome": "Flavia", "telefone": "1234-1234"}}

resultado = contatos.pop("flaviabelar@gmail.com")
print(resultado)

resultado = contatos.pop("flaviabelar@gmail.com", {})
print(resultado)