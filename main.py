
#• Compreender os fundamentos do Processamento de Linguagem Natural (NLP).
#• Construir um diálogo homem-máquina em Python.
#• Explorar bibliotecas NLP em Python.
#• Aplicar conceitos de Linguística Aplicada em uma tarefa prática
# Analise do Sentimento

import nltk
from nltk.chat.util import Chat, reflections  # Importa o Chat e reflexões da NLTK
from nltk.tokenize import word_tokenize  # Importa o tokenizador de palavras da NLTK
from nltk.corpus import stopwords  # Importa stopwords da NLTK
from textblob import TextBlob  # Importa TextBlob para análise de sentimento
from nltk.probability import FreqDist  # Importa FreqDist para calcular a frequência das palavras

# Baixa as stopwords e o tokenizador de palavras da NLTK (se necessário)
nltk.download('stopwords')
nltk.download('punkt')

# Define uma função para analisar o sentimento de um texto usando TextBlob
def analisar_sentimento(texto):
    blob = TextBlob(texto)
    polaridade = blob.sentiment.polarity  # Calcula a polaridade do sentimento
    if polaridade > 0:
        return "Isso parece positivo!"
    elif polaridade < 0:
        return "Isso parece negativo."
    else:
        return "Não consigo determinar o sentimento com certeza."

# Define pares de entrada e saída para o chatbot
pares = [
   ['Oi', ['Olá!', 'Olá, como posso ajudar?']],
   ['Como você está?', ['Estou bem, obrigado. E você?', 'Tudo bem!']],
   ['Quem é você?', ['Sou seu professor virtual.', 'Me chame de Prof.']],
   ['Qual é o seu objetivo?', ['Meu objetivo é ajudar a responder suas perguntas.', 'Estou aqui para te ensinar.']],
   ['Qual é a sua comida favorita?', ['Eu sou um programa de computador, então não como.', 'Não tenho uma comida favorita, mas adoro ajudar você!']],
   ['Você gosta de música?', ['Como sou um programa de computador, não tenho preferências musicais.', 'Não posso ouvir música, mas posso te ajudar a encontrar recomendações!']],
   ['Qual é a sua cor favorita?', ['Não tenho uma cor favorita, mas posso mudar de cor se você quiser.', 'Sou neutro em cores, estou aqui para ajudar.']],
   ['Você pode me contar uma piada?', ['Claro! Por que o peixe é o animal mais difícil de ser enganado? Porque ele tem olho treinado!', 'Por que o programador comprou óculos? Porque ele achava que seu código estava embaçado!']],
   ['Você sabe alguma curiosidade interessante?', ['Claro! Você sabia que o cérebro humano tem a capacidade de armazenar mais informações do que todos os computadores do mundo juntos?', 'Uma curiosidade interessante é que as formigas podem carregar até 50 vezes o seu próprio peso!']],
   ['Qual é a capital do Brasil?', ['A capital do Brasil é Brasília.', 'Brasília é a capital do Brasil.']],
   ['Quanto é 2 + 2?', ['2 + 2 é igual a 4.', 'A resposta para 2 + 2 é 4.']],
]

# Cria um objeto Chat com os pares de diálogo e reflexões
chatbot = Chat(pares, reflections)

# Função principal que inicia o chat
def chat():
    print("#################---CHATBOT---##################")
    print("Olá! Digite 'sair' para encerrar o chat.")
    while True:
        mensagem = input("Você: ")  # Aceita entrada do usuário
        resultado_sentimento = analisar_sentimento(mensagem)  # Analisa o sentimento da entrada
        if mensagem.lower() == 'sair':  # Verifica se o usuário deseja sair
            print("Chat encerrado.")
            break
        resposta = chatbot.respond(mensagem)  # Obtem resposta do chatbot
        # Exibe análise de sentimento e resposta do chatbot
        print("Análise de Sentimento: ", resultado_sentimento)
        print("ChatGPT: ", resposta)
        print("###############################################")

# Chama a função chat para iniciar o chatbot

chat()

# Análise de Texto:


#• Apresentar a biblioteca Python NLTK.
#• Desenvolver um algoritmo simples de Processamento de Linguagem Natural (NLP) utilizando o NLTK.
#• Realizar uma aplicação prática do NLTK para análise de texto.
#• Utilizar o ambiente IDLE (Python) para escrever e executar código.

# Texto para análise
texto = "Textos são geralmente representados em computadores por meio de arquivos que contêem uma seqüência potencialmente longa de caracteres. Para a maioria dos tipos de processamento lingüístico é necessário identificar e categorizar as palavras de um texto. Esta se revela uma tarefa nada trivial. Neste capítulo iremos introduzir os toquens como sendo os blocos constituíntes dos textos e mostraremos de que forma estes últimos podem ser toquenizados. Em seguida, iremos considerar a categorização dos tokens de acordo com suas funções como parte-do-discurso, além de realizar uma exploração preliminar do Brown Corpus, uma conjunto de mais de um milhão de palavras em língua inglesa com tags (informações quanto à categorização das mesmas). Durante o capítulo serão apresentadas algumas aplicações interessantes: geração de textos aleatórios, classificação automática de palavras e análise dos verbos modais em textos de diferentes gêneros (sempre em língua inglesa)."

# Define as stopwords da língua portuguesa
stop_words = set(stopwords.words('portuguese'))

# Tokeniza o texto em palavras
tokens = word_tokenize(texto)

# Filtra as stopwords do texto
filtered_tokens = [word for word in tokens if word.lower() not in stop_words]

# Calcula a frequência das palavras no texto
freq_dist = FreqDist(filtered_tokens)

# Exibe os resultados da análise de texto
print("###################tokenizar###################")
print("Tokens: ", tokens)
print("###############################################")
print("Tokens Filtrados : ", filtered_tokens)
print("###############################################")
print("Palavras Frequentes : ", freq_dist.most_common(5))
print("###############################################")
