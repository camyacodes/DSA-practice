class Cookie:
    def __init__(self, color):
        self.color = color

    def get_color(self):
        return self.color
    
    def set_color(self, color):
        self.color = color


cookie1 = Cookie('blue')
cookie2=Cookie('green')

cookie2.set_color("pink")
cookie1.set_color("yellow")

print("cookie 1 is ", cookie1.get_color(), "\ncookie 2 is ", cookie2.get_color())