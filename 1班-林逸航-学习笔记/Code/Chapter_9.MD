#  第九章  
##  9.1  
```
class Restaurant:
    def __init__(self,name,type):
        self.name = name
        self.type = type
    def describe_res(self):
        print(self.name+" "+self.type)
    def open(self):
        print("Open")

if __name__ == '__main__':
    res = Restaurant("a","b")
    res.describe_res()
    res.open()
```
a b    
Open    
##    9.4
```
class Restaurant:
    def __init__(self,name,type):
        self.name = name
        self.type = type
        self.number = 0
    def set_num(self,num):
        self.number = num
        print(self.number)
    def incre_num(self):
        self.number+=1
        print(self.number)
    def describe_res(self):
        print(self.name+" "+self.type)
    def open(self):
        print("Open")
```
##    9.6
```
class Restaurant:
    def __init__(self,name,type):
        self.name = name
        self.type = type
        self.number = 0
    def set_num(self,num):
        self.number = num
        print(self.number)
    def incre_num(self):
        self.number+=1
        print(self.number)
    def describe_res(self):
        print(self.name+" "+self.type)
    def open(self):
        print("Open")

class IceCream(Restaurant):
    def __init__(self,name,type,falvors):
        super().__init__(name,type)
        self.falovrs = falvors
    def show(self):
        print(self.name+" "+self.type+" "+self.falovrs)
```
##    9.13    
```
class Die:
    def __init__(self,sides = 6):
        self.sides = sides
    def roll(self):
        print(random.randint(1,self.sides))


if __name__ == '__main__':
    die = Die(10)
    for num in range(0,10):
        die.roll()
```
6    
3    
10    
2    
10    
5    
9    
8    
3    
7    

进程已结束，退出代码 0

