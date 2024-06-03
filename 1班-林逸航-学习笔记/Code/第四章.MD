#  第四章  
##  4.1  
```
names = ['aaa', 'bbb','ccc']
message = "I like"
for name in names:
    print(message + " " + name)
print("I really like pizza")
```
I like aaa    
I like bbb  
I like ccc  
I really like pizza  
##  4.2  
```
names = ['aaa', 'bbb','ccc']
for name in names:
    message = f"A {name} would make a great pet."
    print(message)
print("Any of these animals would make a great pet!")
```
A aaa would make a great pet.  
A bbb would make a great pet.  
A ccc would make a great pet.  
Any of these animals would make a great pet!  
##  4.3  
```
for num in range(1,21):
    print(num)
```
##  4.4  
```
nums = list(range(1,1000001))
for num in nums:
    print(num)
```
##  4.5  
```
nums = list(range(1,1000001))
print(min(nums))
print(max(nums))
start_time = time.time()
sum(nums)
end_time = time.time()
elapsed_time = end_time-start_time
print(elapsed_time)
```
1  
1000000  
0.01994609832763672 
##  4.6  
```
nums = list(range(1,21,2))
for num in nums:
    print(num)
```
##  4.7  
```
nums = list(range(3,31))
for num in nums:
    if(num%3==0):
        print(num)
```
##  4.8  
```
nums = []
for num in range(1,11):
    nums.append(num**3)
for num in nums:
    print(num)
```
##  4.9  
```
nums = [num**3 for num in range(1,11)]
print(nums)
```
##  4.10  
```
nums = [num**3 for num in range(1,11)]
print(nums)
print(f"The first three items in the list are: {nums[:3]}")
print(f"Three items from the middle of the list are: {nums[3:6]}")
print(f"The last three items in the list are: {nums[-3:]}")
```
[1, 8, 27, 64, 125, 216, 343, 512, 729, 1000]    
The first three items in the list are: [1, 8, 27]    
Three items from the middle of the list are: [64, 125, 216]    
The last three items in the list are: [512, 729, 1000]    
##  4.11  
```
names = ['aaa', 'bbb', 'ccc']
friends = names[:]
names.append('ddd')
friends.append('eee')
print(f"My: {names}")
print(f"My friend: {friends}")
```
My: ['aaa', 'bbb', 'ccc', 'ddd']    
My friend: ['aaa', 'bbb', 'ccc', 'eee']    
##    4.13    
```
names = {'aaa', 'bbb', 'ccc'}
print(names)
names[0] = 'ddd'
names = {'ddd', 'eee', 'ccc'}
for name in names:
    print(name)
```
{'aaa', 'bbb', 'ccc'}    
Traceback (most recent call last):    
  File "D:/pythonProject/main.py", line 26, in <module>    
    myPrint()    
  File "D:/pythonProject/main.py", line 15, in myPrint    
    names[0] = 'ddd'    
TypeError: 'set' object does not support item assignment    
{'ccc', 'bbb', 'aaa'}    
ccc    
ddd    
eee    

