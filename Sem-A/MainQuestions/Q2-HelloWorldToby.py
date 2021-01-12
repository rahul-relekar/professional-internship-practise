"""
Singleton is a Design Pattern under the Creational Patterns
- which lets you can be considered as the global instance as 
  well as referred to the sam resource

Program will check take an input and save it as Singleton
Here, inputs will be Toby

Singleton()  ----- Exists?  ----> No  -----> Create Instance and store in Instance
                            ----> Yes -----> Return Instance            

"""

# Main Singleton class for accessing the same instance
class Singleton(object):

    # private variable
    _instance = None

    # Built-in method
    def __new__(self):

        # 
        if not self._instance:

            self._instance = super(Singleton, self).__new__(self)
            self.y="World"

        return self._instance


print("<------------------- First Check for Singleton -------------------->")
first = Singleton()
print("Hello"+first.y+"!")

second = Singleton()
print("Hello"+second.y+"!")
print("X------------------------------------------------------------------X\n")

print("<------------------- Final Change to Singleton -------------------->")
toby = Singleton()
toby.y = input()
print("Hello"+toby.y+"!")
print("<------ Change made to the instance --------->")

print("<------ New instance altered by previous assignment --------->")
last = Singleton()
print("Hello"+last.y+"!")
print("X------------------------------------------------------------------X")

