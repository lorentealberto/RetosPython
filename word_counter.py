import string

""" /*
 * Crea un programa que cuente cuantas veces se repite cada palabra
 * y que muestre el recuento final de todas ellas.
 * - Los signos de puntuación no forman parte de la palabra.
 * - Una palabra es la misma aunque aparezca en mayúsculas y minúsculas.
 * - No se pueden utilizar funciones propias del lenguaje que
 *   lo resuelvan automáticamente.
 */ """

def remove_puntuation(text):
    translator = str.maketrans('', '', string.punctuation)
    return text.translate(translator)


phrase = "Mi nombre es Alberto Escribano Lorente y tengo 28 años de edad. Es cierto que me gusta, como decir, lo que me gusta y me gusta mucho."

phrase = remove_puntuation(phrase.lower())

tuple = phrase.split(' ')

words = {}

for word in tuple:
    if word in words:
        words[word] += 1
    else:
        words[word] = 1


#Sort dictionary
words = dict(sorted(words.items(), key = lambda item: item[1], reverse = True))


#Show values
for key, value in words.items():
    print(f'La palabra "{key}" se repite {value} veces')