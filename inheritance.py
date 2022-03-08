##single parent multiple child inheritence-
class flower():
    def flowertype(self,name,color):
        print("flower name",name)
        print("flower color",color)
class flowerchild2(flower):
    def flowertype2(self,name,color):
        print("child1flower name",name)
        print("child1flower color",color)
class flowerchild3(flower):
    def flowertype3(self,name,color):
        print("child2flower name",name)
        print("child2flower color",color)


x=flowerchild2()
x.flowertype("jasmine","white")
x.flowertype2("rose","red")

y=flowerchild3()
y.flowertype("rose","red")
y.flowertype3("jasmine","white")
