# Adrian Luevanos Castillo A00827701
#07/05/2021
#https://github.com/adrianluev/memorama.git
#https://youtu.be/hpjKOheY2CU
# Fue muy interesante trabajar con listas anidadas y de como se puede crear un sistema de coordenadas con estos
# Tambien me gusto trabajar con los clicks en vez del teclado porque tiene diferentes usos y se tiene que hacer un interfaz
# diferente para que pueda ser usado de manera correcta.


from random import *
from turtle import *
from freegames import path

# car guarda el path a la memoria donde se encuentra car.gif
car = path('car.gif')

# se genera una lista de 64 items que van del 1-32 dos veces
tiles = list(range(32)) * 2
state = {'mark': None}
hide = [True] * 64

taps = 0
ancho = 50

writer = Turtle(visible=False)


def square(x, y):  # Esta funcion se usa para dibujar un cuadrado parte del memorama
    "Draw white square with black outline at (x, y)."
    up()
    goto(x, y)
    down()
    color('yellow', 'black')
    begin_fill()
    for count in range(4):  # dibuja el cuadrado
        forward(ancho)
        left(90)
    end_fill()


def index(x, y):  # convierte las coordenadas del turtle a coordenadas del tablero
    "Convert (x, y) coordinates to tiles index."
    return int((x + 200) // ancho + ((y + 200) // ancho) * 8)


def xy(count):  # convierte coordenadas del tablero a coordenadas del turtle
    "Convert tiles count to (x, y) coordinates."
    return (count % 8) * ancho - 200, (count // 8) * ancho - 200


def tap(x, y):  # cuenta los taps y ve los cuadros escondidos
    "Update mark and hidden tiles based on tap."
    global taps
    taps += 1
    spot = index(x, y)
    mark = state['mark']
    # Hace un update para ver que tile clickeo el usuario
    if mark is None or mark == spot or tiles[mark] != tiles[spot]:
        state['mark'] = spot
    else:
        hide[spot] = False
        hide[mark] = False
        state['mark'] = None


def draw():
    "Draw image and tiles."

    clear()

    global taps
    goto(0, 0)
    shape(car)
    stamp()  # Dibuja el carro

    for count in range(64):  # dibuja el tablero con las tiles escondidas
        if hide[count]:
            x, y = xy(count)
            square(x, y)

    mark = state['mark']  # Hace una carta esconderse

    if mark is not None and hide[mark]:
        x, y = xy(mark)
        up()
        goto(x + 2, y)
        color('white')
        write(tiles[mark], font=('Arial', 30, 'normal'))

    escondidas = hide.count(True)  # Cuenta las tiles escondidas

    if(escondidas == 0):
        up()
        goto(-200, 150)
        color('black')
        # pone el mensaje felicitatorio
        write('¡HAZ GANADO UN CARRO!', font=('Arial', 20, 'normal'))
        up()
        goto(-200, 130)
        color('black')
        # escribe el numero de taps que hace el usuario
        write(f'Hiciste {taps} taps', font=('Arial', 15, 'normal'))
        nombre()
        return  # acaba el programa

    update()
    ontimer(draw, 100)  # loop de draw cada 100 milisegundos


def nombre():  # escribe mi nombre en el centro
    up()
    goto(-50, 0)
    color('black')
    write('Adrian Luevanos Castillo', font=('Arial', 15, 'normal'))


setup(420, 420, 370, 0)

addshape(car)
hideturtle()
tracer(False)
onscreenclick(tap)
draw()
done()
