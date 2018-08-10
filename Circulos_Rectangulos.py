from math import pi
class circulo:
    def __init__(self, radio, coordenada_x, coordenada_y):
        self.coordenada_x=coordenada_x
        self.coordenada_y=coordenada_y
        self.radio = radio
    def obtener_area(self):
        return((self.radio**2)*pi)
    def obtener_perimetro(self):
        return(2*pi*self.radio)
    def __str__(self):
        return("Es un circulo de radio {}, con perimetro {} y área {} ubicado en la posición {},{}".format(self.radio,self.obtener_perimetro(),self.obtener_area(),self.coordenada_x,self.coordenada_y))
#class rectangulo (coordenada_x_inferior_izquierda,coordenada_y_inferior_izquierda,angulo_sobre_la_horizontal,largo_inferior,largo_superior)

print(circulo(3,1,2))
