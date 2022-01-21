class Dog:
	''' A simple attempt to model a dog.'''
	def __init__(self,name,age):

		'''Initialize name and age attributes'''
#Attributes
		self.name = name
		self.age = age
#Methods
	def sit(self):
		'''Simulate a dog sitting in response to a command'''
		print(f"{self.name} is now sitting")
	def roll_over(self):
		'''simulate rolling over in response to a command.'''
		print(f"{self.name} rolled over!")


doge_1 = Dog("Max", 6)

doge_2 = Dog("Lucy", 3)

'''
When Python reads this line, it calls the __init__() method
in Dog with the arguments 'Willie' and 6
'''
#dog 1
print(f"My dog's name is {doge_1.name}")
print(f"My dog's age is {doge_1.age} years old")
doge_1.sit()
# dog 2
print(f"My dog's name is {doge_2.name}")
print(f"My dog's age is {doge_2.age} years old")
doge_1.sit() 
