 #? instance method VS class method
 
 '''
 In a class how many function we may create but we have to give the first argument as self always.
 '''
 
 
 '''
 A class method takes  "cls" as first argument but instance method takes "self" or "instance"
 as first argument .
 '''
 
class person:
    def __init__(self,fname,lname,age):		#instance method
        #instance variable
        print("constructor ,method is called")
        self.first_name=fname
        self.last_name=lname
        self.age=age

    def full_name(self,x):					#instance method
        return f"{self.first_name} {x} {self.last_name}"
		
p1=person("sahil","mund",20)
p2=person("sammy","daniel",21)
print(p1.full_name("ranjan"))



# To find the number of instances present in a class
class person:
    count_instance=0
    def __init__(self,fname,lname,age):
        #instance variable
        print("constructor ,method is called")
        person.count_instance+=1
        self.first_name=fname
        self.last_name=lname
        self.age=age

    def full_name(self,x):
        return f"{self.first_name} {x} {self.last_name}"
p1=person("sahil","mund",20)
p2=person("sammy","daniel",21)
print(p1.full_name("ranjan"))
print(person.count_instance)

