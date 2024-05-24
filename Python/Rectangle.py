class Rectangle:
    def __init__(self):
        self.length = 0
        self.breadth = 0

    def setDim(self, length, breadth):
        self.length = length
        self.breadth = breadth

    def getArea(self):
        return self.length * self.breadth


rect1 = Rectangle()
rect2 = Rectangle()


length1 = float(input("Enter length of the first rectangle: "))
breadth1 = float(input("Enter breadth of the first rectangle: "))
rect1.setDim(length1, breadth1)


length2 = float(input("Enter length of the second rectangle: "))
breadth2 = float(input("Enter breadth of the second rectangle: "))
rect2.setDim(length2, breadth2)


area1 = rect1.getArea()
area2 = rect2.getArea()


if area1 > area2:
    print("The first rectangle has a greater area:", area1)
elif area2 > area1:
    print("The second rectangle has a greater area:", area2)
else:
    print("Both rectangles have the same area:", area1)
