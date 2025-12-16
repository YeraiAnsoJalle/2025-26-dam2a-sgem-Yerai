class Rectangle:
    def __init__(self, x, y , width, height):
        self.x = x
        self.y = y 
        self.width = width
        self.height = height
    
    def intersecting(self, rectangle):
        self_ancho= self.x + self.width
        self_alto = self.y + self.height
        rectangulo_ancho = rectangle.x + rectangle.width
        rectangulo_alto = rectangle.y + rectangle.height
        
        no_colisionan = (self_ancho < rectangle.x or self.x > rectangulo_ancho or self_alto < rectangle.y or self.y > rectangulo_alto)          
        
        return not no_colisionan

if __name__ == "__main__":
    a = Rectangle(10, 20, 100, 20)
    b = Rectangle(10, 40, 15, 20)
    c = Rectangle(50, 50, 20, 30)
    
    print("a intersecta con b:", a.intersecting(b))
    print("a intersecta con c:", a.intersecting(c))
    print("b intersecta con a:", b.intersecting(a))
    print("b intersecta con c:", b.intersecting(c))
    print("c intersecta con a:", c.intersecting(a))
    print("c intersecta con b:", c.intersecting(b))