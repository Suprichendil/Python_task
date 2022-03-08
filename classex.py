class car():
    def __init__(self,name,color):
        self.name=name
        self.color=color
    def baleno(self):
        print("car details",self.name,self.color)
    def i20(self):
        print("car details",self.name,self.color)
if __name__=="__main__":
    x=car('i20','red')
    x.baleno()
    x.i20()
    del x
    x.baleno()







    
    
        
