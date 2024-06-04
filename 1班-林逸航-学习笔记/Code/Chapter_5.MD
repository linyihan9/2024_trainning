#  第五章  
##  5.1
```
car = 'subaru' 
print("Is car == 'subaru'? I predict True.") 
print(car == 'subaru') 
print("\nIs car == 'audi'? I predict False.") 
print(car == 'audi')
```
Is car == 'subaru'? I predict True.  
True  

Is car == 'audi'? I predict False.  
False  
##  5.2  
```
str1 = "Aaa"
str2 = "bbb"
str3 = 'aaa'
if(str1 == str3):
    print("str1 = str3")
if(str1.lower()==str3):
    print("str1.lower()=str3")
```
##  5.3  
```
alien_color = "green"
if alien_color == "green":
    print("get 5")
```
##  5.4  
```
alien_color = "green"
if alien_color == "green":
    print("get 5")
else:
    print("get 10")
```
##  5.5  
```
alien_color = "green"
if alien_color == "green":
    print("get 5")
elif alien_color == "yellow":
    print("get 10")
elif alien_color == "red":
    print("get 15")
```
##  5.6  
```
if age < 2:
    print("littleBaby")
elif age >= 2 and age <4:
    print("baby")
elif age >= 4 and age < 13:
    print("chile")
elif age>=13 and age < 18:
    print("student")
elif age >=18 and age <65:
    print("people")
elif age>=65:
    print("older")
```
##  5.7  
```
favourite_fruit = ["apple","banana","strawberry"]
fruit = "banana"
if fruit in favourite_fruit:
    print("You really like bananas!")
```
##  5.8  
```
names = ["admin","a","b"]
if user == "admin":
    print("Hello admin, would you like to see a status report?")
else:
    print("Hello Jaden, thank you for logging in again.")
```
##  5.9  
```
names = ["admin","a","b"]
if user == "admin":
    print("Hello admin, would you like to see a status report?")
elif user == None:
    print("We need to find some users")
else:
    print("Hello Jaden, thank you for logging in again.")
```
##  5.10  
```
current_users = ["a","b","c","d","e"]
new_users = ["a","b","f","g","h"]
current_users_small = []
for current_user in current_users:
    current_users_small.append(current_user.lower())
for newUser in new_users:
    if newUser.lower() in current_users:
        print(f"change userName:{newUser}")
    else:
        print(f"{newUser} not be used")
```
change userName:a    
change userName:b    
f not be used  
g not be used  
h not be used  
##  5.11  
```
for num in range(1,10):
    if num ==1:
        print(f"{num}st")
    elif num ==2:
        print(f"{num}nd")
    elif num ==3:
        print(f"{num}rd")
    else:
        print(f"{num}th")
```
