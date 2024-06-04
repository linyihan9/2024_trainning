#  第十章  
##  10.1  
```
path = Path('test.txt')
contents = path.read_text()
c = path.read_bytes()
print(contents)
print(c)
lines = contents.splitlines()
print(lines)
```
##  10.4  
```
def write():
    path = Path('guest.txt')
    message = input("write down name")
    path.write_text(message)

if __name__ == '__main__':
    write()
```
##  10.5  
```
names = []
def write(message):
    names.append(message)

if __name__ == '__main__':
    while True:
        message = input("write down name")
        if message.strip() == "quit":
            break
        else:
            write(message)
    path = Path('guest.txt')
    text = ""
    for name in names:
        text+=name
        text+="\n"
    path.write_text(text)
```
##  10.7
```
def add(nums):
    ans = 0
    for num in nums:
        ans+=num
    return ans

if __name__ == '__main__':
    mark = 2
    nums = []
    while mark!=0:
        message = input("print")
        try:
            num = int(message)
            nums.append(num)
            mark-=1
        except:
            print("just print num")
    print(add(nums))
```
printa  
just print num  
printb  
just print num  
print1  
print2  
3  

进程已结束，退出代码 0  
##  10.13
```
path = Path("test.txt")

def write():
    path.write_text(json.dumps(data))

def read():
    contents = json.loads(path.read_text())
    print(contents["name"])

if __name__ == '__main__':
    write()
    read()
```

