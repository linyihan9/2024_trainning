#  第二章  
##  2.1  
```
message = "Hello World"
print(message)  
```
Hello World  
##  2.2  
```
message = "Hello World"
print(message)
message = "World Hello"
print(message)
```
Hello World    
World Hello    
##  2.3  
```
name = "Eric"
message = f"Hello {name}, would you like to learn some Python today?"
print(message)
```
Hello Eric, would you like to learn some Python today?  
##  2.4  
```
name = "Eric"
message = f"Hello {name.upper()}, would you like to learn some Python today?"
print(message)
```
Hello ERIC, would you like to learn some Python today?
```
name = "Eric"
message = f"Hello {name.lower()}, would you like to learn some Python today?"
print(message)
```
Hello eric, would you like to learn some Python today?
```
name = "Eric"
message = f"Hello {name.title()}, would you like to learn some Python today?"
print(message)
```
Hello Eric, would you like to learn some Python today?  
##  2.5  
```
message = 'Albert Einstein once said, “A person who never made a mistake never tried anything new.”'
print(message)
```
Albert Einstein once said, “A person who never made a mistake never tried anything new.”
##  2.6  
```
name = "Albert Einstein"
message = f'{name} once said, “A person who never made a mistake never tried anything new.”'
print(message)
```
Albert Einstein once said, “A person who never made a mistake never tried anything new.”
##  2.7  
```
name = "    \tEric  \n"
print(name)
```
    	Eric  

```
name = "    \tEric  \n"
print(name.lstrip())
```
Eric    
##  2.8  
```
name = 'python_notes.txt'
print(name.removesuffix('.txt'))
```
python_notes  
##  2.9  
```
print(5+3)
print(9-1)
print(4*2)
print(16//2)
```
8    
8    
8    
8    
##  2.10  
```
num = 3
print(f"My favourite num is {num}")
```
My favourite num is 3    
##  2.11  
```
# 我最喜欢的数字
num = 3
print(f"My favourite num is {num}")
```
My favourite num is 3
