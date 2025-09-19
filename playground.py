class Pet:
    def __init__(self,name,category,age):
        self.name = name
        self.category = category
        self.age = 0
        def __str__(self):
            mystatus = ('Name:',name,'Category',category,'Age:',str(age))
            return mystatus

p1 = Pet('Ohio','Cat',12)

print(p1)
