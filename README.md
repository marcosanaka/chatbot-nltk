# chatbot-nltk

Este código é um exemplo de como construir um chatbot simples em Python utilizando a biblioteca NLTK (Natural Language Toolkit) para processamento de linguagem natural. Vou explicar as principais partes:

    Importações de bibliotecas: Começa importando as bibliotecas necessárias para o projeto, incluindo NLTK para processamento de linguagem natural, TextBlob para análise de sentimento e FreqDist para calcular a frequência das palavras.

    Função de Análise de Sentimento: Define uma função chamada analisar_sentimento(texto) que utiliza o TextBlob para calcular a polaridade do sentimento do texto de entrada.

    Pares de diálogo: Define uma lista de pares de entrada e saída para o chatbot. Cada par consiste em uma mensagem de entrada e uma lista de possíveis respostas.

    Inicialização do Chatbot: Cria uma instância do objeto Chat com os pares de diálogo e um conjunto de reflexões predefinidas.

    Função de Chat: Define a função chat() que inicia o loop de conversação, aceitando entrada do usuário, analisando o sentimento da entrada e respondendo usando o chatbot. O loop continua até que o usuário digite "sair".

    Análise de Texto: Após o chatbot, o código apresenta um exemplo de análise de texto. Ele tokeniza um texto em palavras, remove as stopwords (palavras comuns que geralmente não contribuem para o significado do texto) e calcula a frequência das palavras no texto.

O código é bem estruturado e comentado, facilitando a compreensão de cada parte. Ele mostra como construir um chatbot básico e também como realizar algumas operações simples de análise de texto utilizando o NLTK.
