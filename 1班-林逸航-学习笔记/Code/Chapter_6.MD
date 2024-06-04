#  第六章  
##  6.1  
```
information = {"lastName":"a",
               "firstName":"b",
               "age":20,
               "city":"WuHan"}
print(information)
```
##  6.2
```
information = {"a":1,
               "b":2,
               "c":3,
               "d":4}
print(information)
```
##  6.3  
```
information = {"a":1,
               "b":2,
               "c":3,
               "d":4}
for key,value in information.items():
    print(f"{key}:{value}")
```
a:1  
b:2  
c:3  
d:4  
##  6.7
```
information_1 = {"lastName": "a",
               "firstName": "b",
               "age": 20,
               "city": "WuHan"}
information_2 = {"lastName": "c",
                 "firstName": "d",
                 "age": 20,
                 "city": "WuHan"}
information_3 = {"lastName": "e",
                 "firstName": "f",
                 "age": 20,
                 "city": "WuHan"}
peoples = [information_1,information_2,information_3]
for people in peoples:
    print(people)
```
##  6.10  
```
favoriteNum = {"a":[1,2],
               "b":[3,4],
               "c":[5,6]}
for name,nums in favoriteNum.items():
    print("\n")
    print(name+" ")
    for num in nums:
        print(num)
```
