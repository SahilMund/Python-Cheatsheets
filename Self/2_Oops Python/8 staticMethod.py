
#? static method

'''
1.It is just like a normal function .

2.It depends on method and object.

3.A decorator named @staticmethod is used for defining static method.

'''

#class methods
class person:
    count_instance=0
    def __init__(self,fname,lname,age):
        #instance variable
        person.count_instance += 1
        print("constructor ,method is called")
        self.first_name=fname
        self.last_name=lname
        self.age=age

    @classmethod
    def from_string(cls,string):
        first,last,age=string.split(',')
        return cls(first,last,age)

    @classmethod
    def count_instances(cls):
        return f"You have created {cls.count_instance} of person classes"
    
    def full_name(self):
        return f"{self.first_name} {self.last_name}"
    @staticmethod
    def hello():
        print('hyyyyy')
    
p1=person("sahil","mund",20)
p2=person("sammy","daniel",21)
p3=person.from_string('illeana,dcruz,30')
print(p3.full_name())
person.hello()
