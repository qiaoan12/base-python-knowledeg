*********************************************************************************异常
try :
    answer = int('ui')
except ZeroDivisionError:
    print("您的结果异常")
else:
    print(answer)

**************************************************************************文件的读取和写入
​#读取文件
with open('./123/123.txt') as file_object:
    content = file_object.read()
print(content)
​
​
#逐行读取
filename = 'pi.txt'
--------------------------------------------
with open(filename) as file_object:
    for line in file_object:
        print(line.rstrip())
​
-------------------------------------------
with open(filename) as file_object:
    lines = file_object.readlines()
​
for line in lines:
    print(line.rstrip())
​
​
​
*******************************************************************"""写入文件"""
filename = 'programing.txt'
​
with open(filename,'w') as file_object:
    file_object.write(" i love python")
    
--------------------------------------------
添加内容而不是覆盖内容
filename = "123.txt"
​
with open(filename,'a') as file_object:
    file_object.write("111111111111111111")

***********************************************************************************类以及类的继承
​class Dog:  #Dog 实例
    def __init__(self,name,age):  #__init__调用Dog实例时自动执行，self是python自动传递，name和age是我们传递给函数
        self.name = name  #以self为前缀的变量可供类中的所有方法使用（接下来定义的所有函数都可以使用）
        self.age = age
        #name和age被称为属性
​
    def sit(self):
        print('sit')
​
    def roll_over(self):
        print('roll_over')
​
    #sit和roll_over被称为方法
​
#创建my_dog实例
my_dog = Dog('WILLIN',8)
​
#访问name属性
my_dog.name
​
​
"""继承"""
class Car:
    def __init__(self,make,model,year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0
​
    def get_descriptive_name(self):
        long_name = f"{self.year}{self.model}{self.make}"
​
​
class ElectricCar(Car):
    def __init__(self,make,model,year):
        super().__init__(make,model,year)
        self.battery_size = 75
​
    def describe_battery(self):
        print(f"这辆车的电池尺寸是：{self.battery_size}")
        
​
my_tesla = ElectricCar('tesla','model s',2019)
​

***********************************************************************************嵌套问题（遍历）
​#字典的嵌套问题
​
1,列表嵌套字典
aliens=[]
​
for alien_number in range(30):
    new_alien = {'color':'green','point':5,'speed':'slow'}
    aliens.append(new_alien)
​
for alien in aliens[:3]:
    if alien['color'] =='green':
        alien['color'] == 'yellow'
​
​
​
​
2,字典嵌套列表
pizza = {
    'crust':'thick',
    'toppings':['mushroom','extra cheese'],
}
print(f"you ordered a {pizza['crust']}")
​
for topping in pizza['toppings']:
    print('\t'+ topping)
​
eg2:
favorite_languages = {
    'jen': ['python','ruby']
    'sarah': ['c']
    'edward': ['ruby','go']
    'phil': ['python','hasd']
}
for name,languages in favorite_languages.items():
    print(f"\n{name.title()}'s favorite language are :")
    for language in languages:
        print(f"\t{language.title()}")
​
​
​
3,字典包字典
users = {
    'aeintein':{
        'first':'albert',
        'last':'einf',
        'location':'print',
    },
    'musid':{
        'first':'dsjijh',
        'last':'crui',
        'location':'parish',
    },
}
for username,user_info in users.items():
    print(f"username:{username}")
    full_name = f"{user_info[first]}{user_info['last']}"
    location = user_info['location']

字典的操作
​"""字典的操作"""
alien = {'color':'green','point':5}
#访问字典 print(alien['color'])
# 访问字典时，访问的键可能不存在，使用get
alien_color = alien.get('point','no such key')  #如果不存在返回no such key
​
# 添加字典中的元素   alien['x_position'] = 0
# 修改字典中的值  alien['color'] = 'yellow'
# 删除键值对  del alien['color']
#遍历字典
user_0 {
    'username':'efermi',
    'first':'enrico',
    'last':'fermi',
}
for key,value in user_0.items():
    print(f"\nKey:{key}")
    print(f"\nvalue{value}")
    
    
#遍历字典中的所有键
 for name in favorite_language.keys():
     

********************************************************************************列表的操作
​#几个容器(列表)
​
​
"""列表"""
bicycles = ['trek','cannon','redline','specile']
#访问列表
print(bicycles[0])
"""列表的增删改查"""
# 改  bicycles[0] = 'dukati'
# 列表末尾增加元素  bicycles.append('dukati')
# 在指定位置前加入  bicycles.insert(0,'dukati') 在0前面添加一个元素
# 删   del bicycles[0] 删除第一个元素     ；弹出最后一个元素  bicycles.pop()；弹出指定位置元素  bicycles.pop(0)
#根据值删除  bicycles.remove('dukati')
​
​
​

