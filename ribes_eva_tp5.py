from math import atan2, sqrt





class Point:
    def __init__(self, *args):
        if len(args) == 0:
            self.x = 0
            self.y = 0
        elif len(args) == 1:
            self.x = args[0].x
            self.y = args[0].y
        elif len(args) == 2:
            self.x = args[0]
            self.y = args[1]


        

    
    def __getitem__(self, i):
        if i == 0:
           return self.x
        elif i == 1:
            return self.y
        else:
            return IndexError
        
    

    def __str__(self):
        return '(' + str(self.x) + ', ' + str(self.y) +')'



    def egaux(self, p):
        return (self.x == p.x) and (self.y == p.y)



    def angle(self, p):
        return atan2(p.y - self.y, p.x - self.x)
        


    def distance_point(self, p):
        return sqrt((self.x - p.x)**2 + (self.y - p.y)**2)
    
    
    def determinant(self, p, d):
        ls_1 = [p.x - self.x, p.y -self.y]
        ls_2 = [d.x - self.x, d.y -self.y]
        return ls_1[0]*ls_2[1] - ls_1[1]*ls_2[0]



 
p = Point(1, 2)
Point(p)

d = Point(2, 3)

b = Point(4, 4)

#print(p.__getitem__(10))  #<class 'IndexError'>
#print(p.__getitem__(1))   #2

#print(p.__str__())   #(1, 2)

#print(p.egaux(p))   #True
#print(p.egaux(d))   #False


#print(p.angle(d))   #0.7853981633974483
#print(p.angle(p))    #0.0

#print(p.distance_point(d))  #1.4142135623730951
#print(p.distance_point(p))  #0.0

#print(p.determinant(d, b))  #-1
#print(d.determinant(p, b))  #1







