

arquivo = open(
    "c:/trilha-python-dio/05 - Manipulação de arquivos/teste2.txt", "w"
)
arquivo.write("Escrevendo dados em um novo arquivo.")
arquivo.writelines(["\n", "escrevendo", "\n", "um", "\n", "novo", "\n", "texto"])
arquivo.close()
