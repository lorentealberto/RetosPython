from PIL import Image
import requests

""" /*
 * Crea un programa que se encargue de calcular el aspect ratio de una
 * imagen a partir de una url.
 * - Url de ejemplo:
 *   https://raw.githubusercontent.com/mouredevmouredev/master/mouredev_github_profile.png
 * - Por ratio hacemos referencia por ejemplo a los "16:9" de una
 *   imagen de 1920*1080px.
 */ """

url = 'https://static.vecteezy.com/system/resources/previews/015/132/103/non_2x/light-cyan-background-images-hd-pictures-and-wallpaper-for-free-download-free-photo.jpg'

img = Image.open(requests.get(url, stream = True).raw)


n_1, n_2 = img.size

def get_gcd(a, b):
    if a == 0:
        return b
    return get_gcd(b % a, a)


def calc_aspect_ratio(n_1, n_2):
    gcd = get_gcd(n_1, n_2)

    w = n_1 // gcd
    h = n_2 // gcd

    return [str(w), str(h)]


ratio = calc_aspect_ratio(n_1, n_2)

print(f'El aspect ratio de una imagen de {n_1}x{n_2}px es {':'.join(ratio)}')
