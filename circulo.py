import math

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Rectangle:
    def __init__(self, width, height, corner):
        self.width = width
        self.height = height
        self.corner = corner  # Assume-se que o canto é um objeto Point representando o canto superior esquerdo

class Circle:
    def __init__(self, center, radius):
        self.center = center  # Assume-se que center é um objeto Point
        self.radius = radius

def distancia_entre_pontos(ponto1, ponto2):
    return math.sqrt((ponto2.x - ponto1.x)**2 + (ponto2.y - ponto1.y)**2)

def ponto_no_circulo(circulo, ponto):
    distancia = distancia_entre_pontos(circulo.center, ponto)
    return distancia <= circulo.radius

def retangulo_no_circulo(circulo, retangulo):
    # Verifica se os quatro cantos do retângulo estão dentro ou no limite do círculo
    cantos = [(retangulo.corner.x, retangulo.corner.y),
              (retangulo.corner.x + retangulo.width, retangulo.corner.y),
              (retangulo.corner.x, retangulo.corner.y + retangulo.height),
              (retangulo.corner.x + retangulo.width, retangulo.corner.y + retangulo.height)]

    for canto in cantos:
        if not ponto_no_circulo(circulo, Point(canto[0], canto[1])):
            return False
    return True

def sobreposicao_retangulo_circulo(circulo, retangulo):
    # Verifica se algum dos cantos do retângulo está dentro do círculo
    cantos = [(retangulo.corner.x, retangulo.corner.y),
              (retangulo.corner.x + retangulo.width, retangulo.corner.y),
              (retangulo.corner.x, retangulo.corner.y + retangulo.height),
              (retangulo.corner.x + retangulo.width, retangulo.corner.y + retangulo.height)]

    for canto in cantos:
        if ponto_no_circulo(circulo, Point(canto[0], canto[1])):
            return True
    return False

# Instanciando um objeto Circle
circulo = Circle(Point(150, 100), 75)

# Testando as funções
ponto = Point(160, 90)
print("Ponto dentro do círculo:", ponto_no_circulo(circulo, ponto))

retangulo = Rectangle(50, 50, Point(100, 80))
print("Retângulo dentro do círculo:", retangulo_no_circulo(circulo, retangulo))

retangulo = Rectangle(50, 50, Point(180, 200))
print("Sobreposição retângulo-círculo:", sobreposicao_retangulo_circulo(circulo, retangulo))
