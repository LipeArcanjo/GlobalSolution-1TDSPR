from prontuario import Segurado  # Importando a classe Segurado do arquivo segurado.py


# Função para inclusão dos dados do segurado
def prontuario_segurado():
    nome = input("Informe o nome: ")
    idade = int(input("Informe a idade: "))
    sexo = input("Informe seu sexo: ")
    peso = float(input("Informe o peso (em kg): "))
    altura = float(input("Informe a altura (em cm): "))
    segurado = Segurado(nome, idade, sexo, peso, altura)

    # Inputação dos dados cadastrais
    segurado.atualizar_informacoes_saude()

    # Cadastrar exames anteriores
    opc = input("Existe algum exame anterior que você queira anexar (SIM/NÃO): ")
    while (opc.lower() == 'sim'):
        nome_exame = input("Informe o nome do exame: ")
        resultado = input("Informe o resultado do exame: ")
        segurado.adicionar_exame(nome_exame, resultado)
        opc = input("Você gostaria de adicionar outro exame? (1-SIM/2-NÃO) ")

    # Print da lista:
    segurado.exibir_informacoes_saude()

    calculo_imc = float(calcular_imc(peso, altura))
    global calculo_tmb
    calculo_tmb = int(calcula_tmb(sexo, peso, altura, idade))
    calculo_protein = int(calcula_protein(peso))
    calculo_agua = int(calcula_agua(peso))
    calculo_calcio = int(calcula_calcio(idade, sexo))
    global calculo_caloria
    calculo_caloria = float(calcula_caloria())
    calculo_carb = float(calc_carboidrato())
    calculo_gord = float(calc_gordura())

    # Definifindo as váriaveis como globais

    global imc_calculado
    imc_calculado = float(calculo_imc)

    global tmb_calculado
    tmb_calculado = int(calculo_tmb)

    global protein_calculada
    protein_calculada = int(calculo_protein)

    global agua_calculada
    agua_calculada = int(calculo_agua)

    global calcio_calculado
    calcio_calculado = int(calculo_calcio)

    global caloria_calculado
    caloria_calculado = float(calculo_caloria)

    global carb_calculado
    carb_calculado = float(calculo_carb)

    global gord_calculado
    gord_calculado = float(calculo_gord)


def opcao_nutricionais(opcao):
    match opcao:
        case 1:
            return "\nInformações pessoais de saúde:\n"
        case 2:
            return ("\nInformações nutricionais relevantes:\n"
                    "\n1) Horários de refeições:"
                    "\n2) Gorduras saturadas e trans:"
                    "\n3) Alimentos ricos em ferro:"
                    "\n4) Gorduras saudáveis:"
                    "\n5) Influência do sono na dieta:"
                    "\n6) Refeições pré e pós-treino:"
                    "\n0) Voltar")
        case 3:
            return ("\nDieta equilibrada para vegetarianos/veganos:\n"
                    "Para uma dieta saudável e que todos os nutrientes, veganos/vegetarianos devem focar em incluir uma variedade de frutas, legumes e verduras, alimentos que são ricos em vitaminas e minerais essenciais para suprir todas as necessidades nutricionais do corpo, além disso pode-se considerar a inclusão de um suplemento de aminoácidos isolado em proporções ideias.")
        case 4:
            return ("\nNecessidades calóricas durante a gravidez/amamentação:\n"
                    "No primeiro trimestre o gasto energético não se altera, sendo assim não é recomendado consumo adicional de energia. A partir do segundo trimestre é essencial o consumo aumentado de energia, visto que o consumo do corpo aumenta em cerca de 340 a 450kcal por dia. A recomendação proteica para gestantes é de 60g/dia sendo pelo menos 50% de proteinas de alto valor biológico.")
        case _:
            return "Opção inválida. Por favor, escolha novamente."


def informacoes_nutricionais(escolha):
    match escolha:
        case 1:
            return ("\nInformações nutricionais relevantes:\n"
                    "\nHorários de refeições: A importância de refeições regulares e intervalos apropriados.\n"
                    "De acordo com o estudo, se você acorda às sete da manhã e vai dormir às onze da noite, por exemplo, para que o metabolismo funcione de forma saudável o ideal é tomar o café da manhã às oito da manhã, almoçar ao meio dia, fazer um lanche por volta das 15 e 16 horas e jantar até as 20 horas, no máximo.\n")
        case 2:
            return ("\nGorduras saturadas e trans: Riscos associados ao consumo excessivo desses tipos de gorduras.\n"
                    "O consumo excessivo dessa gordura pode aumentar os níveis de colesterol LDL, contribuindo para problemas de saúde como obesidade, diabetes, infarto, derrame, aterosclerose e pressão alta. Além disso, o surgimento de doenças cardiovasculares não está apenas relacionado à gordura saturada, mas também ao consumo de alimentos industrializados, como bolachas recheadas, frituras, bolos, bebidas alcoólicas, refrigerantes, massas e sorvetes.\n")
        case 3:
            return ("\nAlimentos ricos em ferro: Boas fontes de ferro para prevenir deficiências.\n"
                    "Alimentos provenientes de animais:"
                    "1. Fígado de frango cozido = 12,9mg (Quantidade de ferro em 100gr desse alimento)."
                    "2. Coração de frango = 5,96mg (Quantidade de ferro em 100gr desse alimento)."
                    "3. Ostras cozidas = 4,9mg (Quantidade de ferro em 100gr desse alimento)."
                    "4. Fígado bovino grelhado = 5,8mg (Quantidade de ferro em 100gr desse alimento)."
                    "5. Carne moida cozida = 2,7mg (Quantidade de ferro em 100gr desse alimento)."
                    "6. Atum assado = 1,3mg (Quantidade de ferro em 100gr desse alimento)."
                    "7.  Gema de ovo cozida = 2,9mg (Quantidade de ferro em 100gr desse alimento)."
                    "8. Ovo de galinha inteiro cozido = 1,5mg (Quantidade de ferro em 100gr desse alimento)."
                    "9. Cordeiro cozido = 2,7mg (Quantidade de ferro em 100gr desse alimento)."
                    "10. Sardinha assada = 1,3mg (Quantidade de ferro em 100gr desse alimento)."
                    "\n\nAlimentos para vegetarianos e veganos:\n"
                    "1. Feijões = 5mg (Quantidade de ferro em 100gr desse alimento).\n2. Semente de gergelim = 5,4mg (Quantidade de ferro em 100gr desse alimento).\n3 Castanha de caju = 5,2mg (Quantidade de ferro em 100gr desse alimento).\n4 Taioba = 1,9mg (Quantidade de ferro em 100gr desse alimento).\n5 Espinafre = 0,6mg (Quantidade de ferro em 100gr desse alimento).\n6 Brócolis e couve = 0,5mg (Quantidade de ferro em 100gr desse alimento).\n7 Agrião = 3,1mg (Quantidade de ferro em 100gr desse alimento).\n8. Alface roxa = 2,5mg (Quantidade de ferro em 100gr desse alimento).\n9 Amendoim = 2,5mg (Quantidade de ferro em 100gr desse alimento).\n10 Grão de bico = 5,4mg (Quantidade de ferro em 100gr desse alimento).\n")
        case 4:
            return ("\nGorduras saudáveis:\n"
                    "A inclusão de gorduras insaturadas (saudáveis) na alimentação é importante. São fontes de gordura de origem vegetal encontradas nas castanhas, nozes, amêndoas, avelãs, abacate e alguns peixes, que elevam o nível de colesterol bom e diminuem o nível de colesterol ruim, além disso ajudam na produção de hormônios.\n")
        case 5:
            return ("\nInfluência do sono na dieta: Como a qualidade do sono pode afetar as escolhas alimentares."
                    "O sono e a alimentação estão diretamente ligados, visto que uma noite mal dormida pode impactar diretamente na alimentação do dia seguinte e o contrário também é verídico, uma alimentação ruim impacta na qualidade do sono. Dormir menos do que o habitual aumenta o apetite, tendo tendências a ingerir mais calorias, em especial alimentos gordurosos e açúcares. \n")
        case 6:
            return ("\nRefeições pré e pós-treino: Necessidades nutricionais antes e após a atividade física."
                    "As refeições pré e pós-treino desempenham papéis cruciais no desempenho atlético, na recuperação muscular e no alcance de objetivos de condicionamento físico."
                    "Refeições Pré e Pós-Treino:\n\nRefeição Pré-treino:\n\n1. *Fornecimento de Energia:*\nA refeição pré-treino fornece a energia necessária para sustentar o esforço durante o treino. Carboidratos complexos são especialmente importantes para uma liberação de energia gradual.\n\n2. *Melhora do Desempenho:*\nA ingestão adequada de carboidratos e proteínas antes do treino pode melhorar o desempenho físico, proporcionando combustível para os músculos.\n\n3. *Prevenção de Fadiga:*\nComer antes do treino ajuda a evitar a fadiga precoce, mantendo os níveis de glicose no sangue estáveis.\n\n4. *Hidratação:*\nA ingestão adequada de líquidos antes do treino ajuda na hidratação, crucial para o desempenho físico e para evitar a desidratação durante o exercício.\n\n Refeição Pós-treino:\n\n1. *Reposição de Reservas Energéticas:*\nApós o exercício, o corpo precisa repor as reservas de glicogênio esgotadas durante o treino. Consumir carboidratos pós-treino ajuda nessa reposição.\n\n2. *Recuperação Muscular:*\nA proteína é essencial para a reparação e crescimento muscular. Consumir proteínas após o treino ajuda na recuperação muscular, reparando os microdanos causados durante o exercício.\n\n3. *Diminuição do Catabolismo:*\nApós o treino, o corpo pode entrar em um estado catabólico, onde os músculos começam a quebrar. Consumir proteínas ajuda a diminuir esse processo.\n\n4. *Hidratação e Reposição de Eletrólitos:*\nO suor durante o exercício pode levar à perda de líquidos e eletrólitos. Consumir alimentos e bebidas pós-treino ajuda na reposição desses elementos essenciais.\n\n Dicas Gerais:\n\n- *Timing Importante:*\nConsumir refeições pré e pós-treino dentro de uma janela de tempo adequada otimiza os benefícios. Idealmente, a refeição pré-treino deve ser 2-3 horas antes do exercício, enquanto a pós-treino deve ser 30 minutos a 1 hora após.\n\n- *Individualidade:*\nAs necessidades nutricionais variam de pessoa para pessoa. O tipo de exercício, intensidade, duração e objetivos de condicionamento físico também influenciam as exigências nutricionais.\n\n- *Personalização:*\nA combinação específica de macronutrientes (proteínas, carboidratos, gorduras) pode variar com base nas preferências individuais e nas respostas do corpo.\n\nLembrando que é sempre aconselhável consultar um profissional de saúde ou nutricionista para obter orientações personalizadas, considerando as necessidades específicas de cada pessoa.\n")
        case _:
            return "Opção inválida. Por favor, escolha novamente."


# Função para exibição dos dados nutricionais
def exibir_funcoes_nutricionais():
    print("\nBem-vindo ao programa de Saúde e Nutrição da SaúdeTotal!\n")
    opc = input("Você gostaria de ver informações nutricionais? (SIM/NÃO): ")

    if opc == ('não'):
        print("Saindo do programa. Até logo!")

    while (opc.lower() == 'sim'):
        print("\nEscolha uma opção:")
        print("1) Recomendações pessoais de saúde")
        print("2) Informações nutricionais relevantes")
        print("3) Dieta equilibrada para vegetarianos/veganos")
        print("4) Necessidades calóricas durante a gravidez/amamentação")
        print("0) Sair")

        # Case escolhido pelo segurado
        escolha = int(input("\nDigite o número da opção desejada: "))

        if (escolha == 0):
            print("Saindo do programa. Até logo!")
            break

        # Exibição das informações
        resultado = opcao_nutricionais(escolha)
        print(resultado)

        # Opção 1
        if (escolha == 1):
            print("\nSuas informações de saúde: \n")
            print(f"IMC: {imc_calculado:.2f}")
            print(f"TMB: {tmb_calculado:.2f}")
            print(
                f"Consumo médio de calorias díarias: {caloria_calculado:.2f}. Lembre-se de que é uma média, cada pessoa é única, por isso procure um especialista caso queira uma dieta adequada.")
            print(f"Consumo mínimo de água sugerido: {agua_calculada:.1f} ml de água por dia")
            print(f"Consumo mínimo de cálcio sugerido: {calcio_calculado:.0f} mg/dia")
            print(f"Distribuição de macronutrientes:\n"
                  f"Carboidrato: {carb_calculado:.2f} g\n"
                  f"Proteina: {protein_calculada:.2f} g\n"
                  f"Gordura:{gord_calculado:.2f} g\n"
                  f"Lembre-se de que essas são médias e as necessidades específicas podem variar. Algumas pessoas podem se sentir melhor com uma proporção ligeiramente diferente, dependendo de fatores como metabolismo, objetivos de condicionamento físico e preferências pessoais.\n\n")

        # Opção 2
        if (escolha == 2):
            escolha = int(input("\nQual tópico te interessa?: "))
            resultado = informacoes_nutricionais(escolha)
            print(resultado)

        # Perguntar se o segurado quer continuar verificando os temas:
        opc = input("Gostaria de ver sobre outro tema? (SIM/NÃO): ")

        # Despedida do programa!
        if opc == ('não'):
            print("Saindo do programa. Até logo!")


# Cálculos das funções
def calcular_imc(peso, altura):
    imc = peso / ((altura / 100) ** 2)
    return (imc)


def calcula_tmb(sexo, peso, altura, idade):
    if sexo.lower() == ('masculino') or sexo.lower() == ('homem'):
        tmb = 88.36 + (13.397 * peso) + (4.799 * altura) - (5.677 * idade)
        return (tmb)
    else:
        tmb = 447.593 + (9.247 * peso) + (3.098 * altura) - (4.330 * idade)
        return (tmb)


def calcula_protein(peso):
    proteina = peso * 0.8
    return (proteina)


def calcula_agua(peso):
    agua = peso * 30
    return (agua)


def calcula_calcio(idade, sexo):
    if (sexo.lower() == ('masculino') and idade >= 19) or (sexo.lower() == ('feminino') and idade >= 19):
        calcio = 1000
        return (calcio)
    elif (sexo.lower() == ('masculino') and idade > 70) or (sexo.lower() == ('feminino') and idade > 50):
        calcio = 1200
        return (calcio)


def calcula_caloria():
    caloria = calculo_tmb * 1.375
    return caloria


def calc_carboidrato():
    carboidrato = calculo_caloria * 0.45
    return carboidrato


def calc_gordura():
    gordura = calculo_caloria * 0.25
    return gordura
