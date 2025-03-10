import streamlit as st




morse = {
    # Letters
    'a': '.-',    'b': '-...',  'c': '-.-.',  'd': '-..',   'e': '.',     'f': '..-.',
    'g': '--.',   'h': '....',  'i': '..',    'j': '.---',  'k': '-.-',   'l': '.-..',
    'm': '--',    'n': '-.',    'ñ': '--.--', 'o': '---',   'p': '.--.',  'q': '--.-',
    'r': '.-.',   's': '...',   't': '-',     'u': '..-',   'v': '...-',  'w': '.--',
    'x': '-..-',  'y': '-.--',  'z': '--..',

    # Numbers
    '0': '-----', '1': '.----', '2': '..---', '3': '...--', '4': '....-', '5': '.....',
    '6': '-....', '7': '--...', '8': '---..', '9': '----.',

    # Space
    ' ': '/'
}
reverse_morse = { v: k for k, v in morse.items() }




def is_plain(txt):
    for l in txt:
        if l not in morse:
            return False
    return True


def translate(txt):
    if is_plain(txt):
        return encode(txt)
    else:
        return decode(txt)


def encode(txt):
    msg = ''

    for l in txt:
        msg += morse[l] + ' '
    
    return msg

def decode(txt):
    msg = ''
    tmp = txt.split()

    for l in tmp:
        msg += reverse_morse[l]
    
    return msg


text = 'Hola Mundo'
text_morse = '.... --- .-.. .- / -- ..- -. -.. ---'



# App
st.title('Morsecode Translator')

txt = st.text_area('Introduce el texto que quieras traducir')

if st.button('Traducir'):
    st.write(f'Aquí está la traducción de su texto: "{translate(txt.lower())}"')