""" /*
 * Crea una única función (importante que sólo sea una) que sea capaz
 * de calcular y retornar el área de un polígono.
 * - La función recibirá por parámetro sólo UN polígono a la vez.
 * - Los polígonos soportados serán Triángulo, Cuadrado y Rectángulo.
 * - Imprime el cálculo del área de un polígono de cada tipo.
 */ """


def get_area(shape, width, height = 0):
    match shape:
        case 'square':
            return get_square_area(width)
        case 'rectangle':
            return get_rectangle_area(width, height)
        case 'triangle':
            return get_triangle_area(width, height)
        case _:
            return "invalid shape"


def get_square_area(side):
    return side * side

def get_rectangle_area(width, height):
    return width * height

def get_triangle_area(width, height):
    return (width * height) / 2


print(f"Square area 2x2 is {get_area("square", 2)}")
print(f"Rectangle area 4x10 is {get_area("rectangle", 4, 10)}")
print(f"Triangle area 3x5 is {get_area("triangle", 3, 5)}")
print(f"Circle area radius 10 is {get_area("circle", 10)}")