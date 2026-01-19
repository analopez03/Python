'''Crea una función distancia(p1, p2) que reciba dos tuplas representando
puntos en el plano (x, y) y devuelva la distancia entre ellos usando la fórmula: ((x2 - x1)^2 + (y2 - y1)^2))^1/2'''
def distancia(p1, p2):
    return ((p2[0] - p1[0]) ** 2 + (p2[1] - p1[1]) ** 2)**(1/2)

p1 = (7, 2)
p2 = (2, 9)
print(distancia(p1, p2))