#  第三章
##  3.1  
```
names = ['aaa','bbb']
for name in names:
    print(name)
```
aaa    
bbb    
##  3.2  
```
names = ['aaa','bbb']
for name in names:
    print(name+" Hello")
```
aaa Hello    
bbb Hello    
##  3.3  
```
names = ['car','bicycle']
message = "I would like to own a"
for name in names:
    print(message+" "+name)
```
I would like to own a car    
I would like to own a bicycle    
##  3.4  
```
names = ['aaa','bbb']
message = "Come on"
for name in names:
    print(message+" "+name)
```
Come on aaa    
Come on bbb    
##  3.5  
```
names = ['aaa','bbb']
message = "Come on"
for name in names:
    print(message+" "+name)
print("aaa can not come")
names.remove('aaa')
names.append('ccc')
for name in names:
    print(message+" "+name)
```
Come on aaa    
Come on bbb    
aaa can not come    
Come on bbb    
Come on ccc      
##  3.6  
```
names = ['aaa','bbb']
message = "Come on"
names.insert(0,'ccc')
names.insert(2,'ddd')
names.append('eee')
for name in names:
    print(message+" "+name)
```
Come on ccc    
Come on aaa    
Come on ddd    
Come on bbb    
Come on eee    
##  3.7  
```
names = ['aaa','bbb']
message = "Come on"
names.insert(0,'ccc')
names.insert(2,'ddd')
names.append('eee')
for name in names:
    print(message+" "+name)
print("Sorry")
while(len(names)!=2):
    names.pop()
for name in names:
    print(message+" "+name)
del names
try:
    print(names)
except NameError:
    print("names is Null")
```
Come on ccc    
Come on aaa    
Come on ddd    
Come on bbb    
Come on eee    
Sorry    
Come on ccc    
Come on aaa    
names is Null    
##  3.8  
```
names = ['Tokyo','Paris','Beijing','Hubei','HongKong']
print(names)
print(sorted(names))
print(names)
names.reverse()
print(names)
names.sort()
print(names)
```
['Tokyo', 'Paris', 'Beijing', 'Hubei', 'HongKong']    
['Beijing', 'HongKong', 'Hubei', 'Paris', 'Tokyo']    
['Tokyo', 'Paris', 'Beijing', 'Hubei', 'HongKong']    
['HongKong', 'Hubei', 'Beijing', 'Paris', 'Tokyo']    
['Beijing', 'HongKong', 'Hubei', 'Paris', 'Tokyo']    
##  3.9
```
names = ['aaa', 'bbb']
message = "Come on"
names.insert(0, 'ccc')
names.insert(2, 'ddd')
names.append('eee')
for name in names:
    print(message + " " + name)
print(len(names))
```
Come on ccc    
Come on aaa    
Come on ddd    
Come on bbb    
Come on eee    
5
##  3.11  
```
names = ['aaa', 'bbb']
message = "Come on"
names.insert(0, 'ccc')
names.insert(2, 'ddd')
names.append('eee')
for name in names:
    print(message + " " + name)
print(names[-1])
```
Come on ccc    
Come on aaa    
Come on ddd    
Come on bbb    
Come on eee    
eee    
    
