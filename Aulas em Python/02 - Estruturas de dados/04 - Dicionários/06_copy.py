contatos = {"flaviabelar@gmail.com": {"nome": "Flavia", "telefone": "1234-1234"}}

copia = contatos.copy()
copia["flaviabelar@gmail.com"] = {"nome": "Belar"}

print(contatos["flaviabelar@gmail.com"])
print(copia["flaviabelar@gmail.com"])