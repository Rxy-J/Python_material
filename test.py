class Person():
    
    def __init__(self, name, gender, age):
        self.__name = name
        self.__gender = gender
        self.__age = age
    
    def getName(self):
        return self.__name
    
    def getGender(self):
        return self.__gender
    
    def getAge(self):
        return self.__age

class User(Person):

    def __init__(self, id, name, gender, age):
        #super().__init__(name, gender, age)
        self.__id = id

    def getId(self):
        return self.__id

a = User(123, "张三", "男", 18)
print(a.getId())
print(a.getName())
print(a.getGender())