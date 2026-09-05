pets_db = {}

def adicionar_pet(id_pet, nome_pet, especie):
    pets_db[id_pet] = {
        'id': id_pet,
        'nome_pet': nome_pet,
        'especie': especie,
        'status': "Aguardando"
    }

def colocar_em_consulta(id_pet):
    pets_db[id_pet]['status'] = "Em Consulta"

def voltar_para_espera(id_pet):
    pets_db[id_pet]['status'] = "Aguardando"

def remover_pet(id_pet):
    del pets_db[id_pet]


print("1. Dicionário inicial (vazio):")
print(pets_db)
print("-" * 40)

print("2. Adicionando dois pets...")
adicionar_pet(101, "Rex", "Cachorro")
adicionar_pet(102, "Mimi", "Gato")
print(pets_db)
print("-" * 40)

print("3. Colocando o Rex (101) em consulta...")
colocar_em_consulta(101)
print(pets_db[101]) # Mostra só o Rex para ver o status mudado
print("-" * 40)

print("4. Voltando o Rex (101) para espera (simulando um erro de chamada)...")
voltar_para_espera(101)
print(pets_db[101]) # Mostra o Rex novamente
print("-" * 40)

print("5. Removendo a Mimi (102) (simulando um cadastro errado)...")
remover_pet(102)
print("Dicionário final:")
print(pets_db)