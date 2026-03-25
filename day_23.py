# print("Never Give up!!")
# l=[1,2,3,4,5,6]
# print(l)
# n=int(input(" Enter the n value : " ))
#------------------------------------------------------------------------------------------------------------------------------------------------------------
# class Human:
#     def  __init__(self, name):
#         self.name=name

#     def walk(self):
#        print(f"{self.name} is walking")
# Chandan=Human("ullas")
# darshan = Human("abc")
# Chandan.walk()
# darshan.walk()
#---------------------------------------------------------------------------------------------------------------------------------------------------------------
class mobile:
    def  __init__(self, name,brand,price):
        self.name=name
        self.brand=brand
        self.price=price

    def show(self):
       print(f"{self.name} is a {self.brand} mobile costing {self.price}")
Chandan=mobile("iphone 14","Apple",80000)
darshan = mobile("vivo-y28s","vivo",15000)
Chandan.show()
darshan.show()




