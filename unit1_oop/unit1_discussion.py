"""
===========================================================
Unit 1 DISCUSSION: Python OOP, Namespaces, and Copying
===========================================================

INSTRUCTIONS:
In this assignment, you will build and explore object-oriented programming (OOP) concepts in Python.
You are provided with starter code containing TODO sections. Your task is to complete, modify, and
analyze the code to demonstrate understanding of inheritance, namespaces, and object copying.
"""


from copy import copy, deepcopy


# TODO 1:
# Create a parent class.
#
# Requirements:
# - Include at least one class variable.
# - Include at least two instance variables.
# - Include a constructor (__init__).
# - Include a method that returns or displays information about the object.
#
# Replace the pass statement with your implementation.

class ParentClass:
    category = "General Student" # Class variable

    def __init__(self, name, age):
        # Instance variables
        self.name = name
        self.age = age

    def display_info(self):
        return f"Name: {self.name}, Age: {self.age}, Category: {ParentClass.category}"


# TODO 2:
# Create a child class that inherits from the parent class.
#
# Requirements:
# - Use inheritance.
# - Add at least one new class variable.
# - Add at least two new instance variables.
# - Add at least one new method.
# - Override a method from the parent class.
#
# Replace the pass statement with your implementation.

class ChildClass(ParentClass):
    # New class variable
    category = "Advanced Student"

    def __init__(self, name, age, major, year):
        super().__init__(name, age) # Call the parent constructor

        # New instance variables
        self.major = major
        self.year = year

    def display_info(self):
        return f"Name: {self.name}, Age: {self.age}, Major: {self.major}, Year: {self.year}, Category: {ChildClass.category}"

# TODO 3:
# Create a function that demonstrates class namespaces and instance namespaces.
#
# Your function should:
# - Create at least two objects of the child class.
# - Access a class variable through the class itself.
# - Access the same class variable through an object.
# - Add a new attribute to only one object after it is created.
# - Display each object's namespace using __dict__.
# - Display information about the class namespace.

def demonstrate_namespaces():
    print("\n=== Namespace Demonstration ===")

    #Create two objects of the child class
    student1 = ChildClass("Alice", 20, "Computer Science", "Sophomore")
    student2 = ChildClass("Bob", 22, "Mathematics", "Senior")

    #Access class variable through the class itself
    print(f"Class variable accessed through class: {ChildClass.category}")

    #Access class variable through an object
    print(f"Class variable accessed through object: {student1.category}")

    #Add a new attribute to only one object after it is created
    student1.gpa = 3.8

    #Display each object's namespace using __dict__
    print(f"Student 1 namespace: {student1.__dict__}")
    print(f"Student 2 namespace: {student2.__dict__}")

    #Display information about the class namespace
    print(f"Class namespace: {ChildClass.__dict__}")


# TODO 4:
# Create a function that demonstrates shallow copying and deep copying.
#
# Requirements:
# - Create an object that contains nested mutable data.
# - Create a shallow copy.
# - Create a deep copy.
# - Modify the original object's nested data.
# - Display the original object, shallow copy, and deep copy.
# - Use comments to explain the difference between shallow and deep copying.

def demonstrate_copying():
    print("\n=== Copy Demonstration ===")

    #Original object with nested mutable data
    original = {
        "name": "Charlie",
        "grades": [90, 85, 92]
    }

    #Create a shallow copy
    shallow_copy = copy(original)

    #Create a deep copy
    deep_copy = deepcopy(original)

    print("\nBefore modifying the original object's nested data:")
    print(f"Original object: {original}")
    print(f"Shallow copy: {shallow_copy}")
    print(f"Deep copy: {deep_copy}")

    #Modify the original object's nested data
    original["grades"].append(95)

    print("\nAfter modifying the original object's nested data:")
    print(f"Original object: {original}")
    print(f"Shallow copy: {shallow_copy}")  # Shallow copy reflects the change because it shares the same reference to the nested list.
    print(f"Deep copy: {deep_copy}")  # Deep copy does not reflect the change because it has its own copy of the nested list.



# TODO 5:
# Complete the main function.
#
# Requirements:
# - Create at least one object from the parent class.
# - Create at least one object from the child class.
# - Demonstrate inheritance by calling methods.
# - Call your namespace demonstration function.
# - Call your copy demonstration function.

def main():
    print("=== Unit 1 OOP Assignment ===")

    print("\nCreating ParentClass object:")
    # Create an object from the parent class
    parent_obj = ParentClass("David", 30)
    print(parent_obj.display_info())

    #Create an object from the child class
    print("\nCreating ChildClass object:")
    child_obj = ChildClass("Eve", 21, "Physics", "Junior")
    print(child_obj.display_info())

    #Demonstrate inheritance by calling methods
    print("\nDemonstrating inheritance:")
    print(f"ParentClass method called from child object: {child_obj.display_info()}")
    
    demonstrate_namespaces()
    demonstrate_copying()


if __name__ == "__main__":
    main()