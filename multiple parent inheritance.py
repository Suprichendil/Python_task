##multiple parent n single child class-
class flower():
    def flowertype(self,name,color):
        print("flower name",name)
        print("flower color",color)
class flower2():
    def flowertype2(self,name,color):
        print("flower name",name)
        print("flower color",color)
class flowerchild(flower,flower2):
    def flowertype(self,name,color):
        print("child1flower name",name)
        print("child1flower color",color)

x=flowerchild()
x.flowertype("rose","red")
x.flowertype2("jasmine","white")
x.flowertype("lily","yellow")
