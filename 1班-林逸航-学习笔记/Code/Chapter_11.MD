#  第十一章
##  11.1
city.py
```
def getCityAndCountry(city,country):
    return f"{city},{country}"
```
test_city.py
```
from city import getCityAndCountry

def test_getCityAndCountry():
    assert getCityAndCountry("San","Chile") == "San,Chile"
```
##    11.3
emplo.py
```
class Employee:
    def __init__(self,firstName,lastName,salary):
        self.firstName = firstName
        self.lastName = lastName
        self.salary = salary
    def give_raise(self,add = 5000):
        self.salary+=add
        return self.salary
```
test_emplo.py    
**后面两个函数的参数名称需要与@pytest.fixture标注的函数名称相同**
```
import pytest
from emplo import Employee

@pytest.fixture()
def employeeFix():
    employee = Employee("a","b",1000)
    return employee

def test_give_default_raise(employeeFix):
    assert employeeFix.give_raise() == 6000

def test_give_custom_raise(employeeFix):
    assert employeeFix.give_raise(1000) == 2000
```
