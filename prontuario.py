class Segurado:
    def __init__(self, nome, idade, sexo, peso, altura):
        self.nome = nome
        self.idade = idade
        self.sexo = sexo
        self.peso = peso
        self.altura = altura
        self.historico_doenca_familiar = None
        self.habitos_prejudiciais = None
        self.medication = None
        self.pratica_esportes = None
        self.periodicidade_checkup = None
        self.suplementacao = None
        self.batimentos_cardiacos = None
        self.pressao_arterial = None
        self.alergia_medicacao = None
        self.exames = []

    def atualizar_informacoes_saude(self):
        self.historico_doenca_familiar = input("Informe se há histórico de doença familiar, caso sim, qual?: ")
        self.habitos_prejudiciais = input("Informe se há hábitos prejudiciais (fumar, excesso de álcool, etc): ")
        self.medication = input("Informe caso haja o uso de medicação contínua: ")
        self.pratica_esportes = int(input("Quantas vezes você pratica esporte na semana? : "))
        self.periodicidade_checkup = input("Informe a periodicidade na qual realiza exames de check-up: ")
        self.suplementacao = input("Utiliza alguma suplementação? Se sim, qual? : ")
        self.batimentos_cardiacos = input("Informe os batimentos cardíacos (opcional): ")
        self.pressao_arterial = input("Informe a pressão arterial (opcional): ")
        self.alergia_medicacao = input("Você tem alguma alergia à medicação? Se sim, qual? : ")

    def adicionar_exame(self, nome_exame, resultado):
        self.exames.append({"nome_exame": nome_exame, "resultado": resultado})

    def exibir_informacoes_saude(self):
        print(f"Informações de Saúde para {self.nome} (Idade: {self.idade} - Sexo: {self.sexo}):")
        print(f"Peso: {self.peso} kg")
        print(f"Altura: {self.altura} m")
        print(f"Histórico de doença familiar: {self.historico_doenca_familiar}")
        print(f"Hábitos prejudiciais: {self.habitos_prejudiciais}")
        print(f"Medicação contínua: {self.medication}")
        print(f"Prática de esportes: {self.pratica_esportes}")
        print(f"Periodicidade de check-up: {self.periodicidade_checkup}")
        print(f"Utiliza suplementação: {self.suplementacao}")
        print(f"Batimentos Cardíacos: {self.batimentos_cardiacos}")
        print(f"Pressão Arterial: {self.pressao_arterial}")
        print(f"Alergia a medicação: {self.alergia_medicacao}")
        print("\nExames Anteriores:")
        for exame in self.exames:
            print(f"{exame['nome_exame']}: {exame['resultado']}")

