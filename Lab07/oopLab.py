
class Rectangle:
    def __init__(self, llPoint, urPoint):
        lx,ly = llPoint
        rx,ry = urPoint

        if (not (lx < rx)) or (not (ly < ry)):
            raise ValueError("LL point must be less than UR point!!")
        self.lowerLeft = llPoint
        self.upperRight = urPoint

    def isSquare(self):
        lx,ly = self.lowerLeft
        rx,ry = self.upperRight

        hor_side = rx - lx
        vert_side = ry - ly

        if(hor_side == vert_side):
            return True
        else:
            return False

    def isPointInside(self, point):

        px, py = point
        lx,ly = self.lowerLeft
        rx,ry = self.upperRight

        if (lx < px < rx) and (ly < py < ry):
            return True
        else:
            return False

    def intersectsWith(self, rect):
        rect_lx, rect_ly = rect.lowerLeft
        rect_rx, rect_ry = rect.upperRight

        if (self.isPointInside((rect_lx,rect_ry)) or self.isPointInside((rect_lx,rect_ly)) or self.isPointInside((rect_rx,rect_ly)) or self.isPointInside((rect_rx,rect_ry))):
            return True
        else:
            return False


if __name__ == "__main__":
    pass
    #rect1 = Rectangle((0,0),(4,6))
    #print(rect1.isSquare())
    #print(rect1.isPointInside((3,4)))
    #rect2 = Rectangle((1,1),(5,5))
    #print(rect1.intersectsWith(rect2))
