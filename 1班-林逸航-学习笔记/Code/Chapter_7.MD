#  第七章
##  7.1  
```
message = input("What car u need")
print(f"Let me see if I can find you a {message}.")
```
##  7.4  
```
while True:
    message = input("write down source")
    if message.strip() == "quit":
        break
    else:
        print(f"add {message}")
```
write down sourceaaa  
add aaa  
write down source bbb  
add  bbb  
write down source quit  

进程已结束，退出代码 0  
##  7.5
```
while True:
    message = input("write down age")
    if message.strip() == "quit":
        break
    elif int(message) <3:
        print("free")
    elif int(message) >=3 and int(message)<12:
        print("10")
    else:
        print("15")
```
write down age12  
15  
write down age15  
15  
write down age1  
free  
write down agequit  

进程已结束，退出代码 0
##  7.8
```
sandwich_orders = ["a","b","c"]
finished = []
while sandwich_orders:
    sanwich = sandwich_orders.pop()
    print(f"I made your {sanwich} sandwich.")
    finished.append(sanwich)
while finished:
    print(f"finished {finished.pop()}")
```
I made your c sandwich.  
I made your b sandwich.  
I made your a sandwich.  
finished a  
finished b  
finished c  
##  7.9
```
sandwich_orders = ["pastramia","pastramia","c"]
finished = "pastramia"
while finished in sandwich_orders:
    sandwich_orders.remove(finished)
    print(finished)
```
