#  第八章  
##  8.2
```
def myPrint(title):
    print(f"One of my favorite books is {title}")

if __name__ == '__main__':
    myPrint("aaa")
```
##  8.3
```
def myPrint(size,word):
    print(str(size)+" "+word)

if __name__ == '__main__':
    myPrint(1,"a")
    myPrint(word="b",size=2)
```
##  8.4
```
def myPrint(size = 3,word = "I love Python"):
    print(str(size)+" "+word)

if __name__ == '__main__':
    myPrint()
    myPrint(2)
    myPrint(word="aaa")
```
3 I love Python  
2 I love Python  
3 aaa  
##  8.9    
```
def myPrint(message):
    print(message)

if __name__ == '__main__':
    myPrint("a")
    myPrint("b")
    myPrint("c")
```
##    8.12
```
def myPrint(*kwargs):
    print(kwargs)

if __name__ == '__main__':
    myPrint("a","b","c")
```
##    8.14
```
def myPrint(constructor,type,**kwargs):
    car = {}
    car.update({"constructor":constructor,
                "type":type,
                })
    car.update(kwargs)
    return car

if __name__ == '__main__':
    print(myPrint("a","b",color = "c",tow_package = "d"))
```
{'constructor': 'a', 'type': 'b', 'color': 'c', 'tow_package': 'd'}

