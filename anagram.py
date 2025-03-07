""" /*
 * Escribe una función que reciba dos palabras (String) y retorne
 * verdadero o falso (Bool) según sean o no anagramas.
 * - Un Anagrama consiste en formar una palabra reordenando TODAS
 *   las letras de otra palabra inicial.
 * - NO hace falta comprobar que ambas palabras existan.
 * - Dos palabras exactamente iguales no son anagrama.
 */ """

def isAnagram(word_1, word_2):
    word_1 = word_1.lower()
    word_2 = word_2.lower()

    if word_1 == word_2:
        print("They must be different words")
        return
    
    for l in word_1:
        if not l in word_2:
            return False
    
    return True

word_1 = input("Enter a word: ")
word_2 = input("Enter another word: ")

if isAnagram(word_1, word_2):
    print("Both words are anagrams")
else:
    print("They aren't anagrams")
    