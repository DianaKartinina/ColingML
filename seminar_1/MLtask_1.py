import numpy as np
from nltk.tokenize import word_tokenize
from scipy.spatial import distance


with open ('sen.txt', 'r') as sent:
    low = sent.read().lower()
    number_sentences = sum(1 for _ in sent) # считаем количество предложений
    tok = word_tokenize(low)  #токенизация
    words = list(set(tok))
    dict_words = (dict(zip(range(len(words)), words))) #составление словаря

    matrix = np.zeros(shape=(number_sentences, len(dict_words))) #составление матрицы
    
    for i in range(number_sentences):  # пытаюсь выполнить пункт 5 из задания..Здесь все посыпалось.
        for j in range(len(dict_words)):
            matrix[i][j] = number_sentences[i].count(dict_words[j])
    print(matrix)
    
    cos_matrix = []
    for i in range(number_sentences):
        cos_matrix.append(distance.cosine(matrix[0], matrix[i]))
    cos_matrix = np.array(cos_matrix)
    print(cos_matrix)

