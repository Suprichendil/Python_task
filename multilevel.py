class flower():
    def __init__(self,name):
        self.name=name
    def flowerdetails(self):
        print("flower details",self.name)
class rose(flower):
    def __init__(self,name,color):
        self.color=color
        super().__init__(name)
        def rosedetails(self):
            print("rose red",self.color)

x=rose("redflower","redrose")
x.rosedetails()
x.rosedetails()
