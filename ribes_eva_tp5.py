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



 
p = Point(1, 2)
Point(p)

d = Point(2, 3)

#print(p.__getitem__(10))  #<class 'IndexError'>
#print(p.__getitem__(1))   #2

#print(p.__str__())   #(1, 2)

#print(p.egaux(p))   #True
#print(p.egaux(d))   #False



