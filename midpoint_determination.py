class Coordinate:
    def __init__(self,x,y):
        self.x = x
        self.y = y
    def __str__(self):
        return f'Coordinate({self.x}, {self.y})'
    def translate(self,dx,dy):
        self.x += dx
        self.y += dy
    def __eq__(self, value):
        return (self.x == value.x) and (self.y == value.y)
startP = Coordinate(0,0)
endP = Coordinate(10,10)
class Line(Coordinate):
    def __init__(self,start, end):
        self.start = start
        self.end = end
    def __str__(self):
        return f"line starts {self.start} and ends {self.end}"
    def midpoint(self):
        midX = (self.start.x + self.end.x)/2 
        midY = (self.start.y + self.end.y)/2
        return Coordinate(midX,midY)
line = Line(startP,endP)
midpoint = line.midpoint()     
print(midpoint)
