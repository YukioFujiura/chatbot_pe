import csv
#Idea: todas as opcao comecam validas, com base em cada pergunta ler todas as validas e invalidar elas conforme a pergunta, validacao depende do ultimo valor da tabela criada "valida"
def criar_lista(): #cria um arquivo vazio com cabecalho
    # lista vazia para valores de cada linha
    cabecalho = [("id","date","price","bedrooms","bathrooms","sqft_living","sqft_lot","floors","waterfront","view","condition",
                "grade","sqft_above","sqft_basement","yr_built","yr_renovated","zipcode","lat","long","sqft_living15",
                "sqft_lot15","valido")]
    csvfile=open('valores.csv', 'w', newline='')   
    esc=csv.writer(csvfile)
    for linha in cabecalho:
        esc.writerow(linha)
    csvfile.close()
def monstrar_lista(): #deve precisar de algo assim no fim pra mostrar a selecao(mudar nome do arquivo)
    f = open('kc_house_data.csv','r', newline='')
    obj = csv.DictReader(f)
    texto = f.read()
    linhas = texto.splitlines()
    for i in range(1,len(linhas)): 
        info = linhas[i].split(",")
        print("ID: ",info[0])
        print("Data: ",info[1])
        print("Preco: ",info[2])
        print("Banheiros ",info[3])
        print("sqft_living",info[4])
        print("sqft_lot",info[5])
        print("floors",info[6])
        print("Waterfront",info[7])
        print("View",info[8])
        print("Condition",info[9])
        print("Grade",info[10])
        print("sqft_above",info[11])
        print("sqft_basement",info[12])
        print("yr_build",info[13])
        print("yr_renovated",info[14])
        print("zipcode",info[15])
        print("latitude",info[16])
        print("longitude",info[17])
        print("sqft_living15",info[18])
        print("sqft_lot5",info[19])
        print("")
    f.close()
def ler_lista():#le a nova lista criada
    with open('valores.csv', newline='') as f:
        reader = csv.reader(f, delimiter=';')
    for row in reader:
        print(row)

gravar_lista()