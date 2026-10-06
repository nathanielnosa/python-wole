#::::: FUNCTION :::::
# def greet():
#     block of codes

# greet()

# def greet():
#     print(f"Hello wole how have you been ?")
# greet()
    
# function with parameters.
# def greet(name):
#     print(f'Hello how are you doing {name} ?')
# greet("WoleSoyinka")

# def greet(pin="1234"):
#     print(f'Hello your default pin is {pin}, change it at the ATM')
# greet("9012")

# RETURN 

# def greet():
#     return(f"Hello wole how have you been ?")
# print(greet())
    
# function with parameters.
# def greet(name):
#     return(f'Hello how are you doing {name} ?')
# print(greet("WoleSoyinka"))

# def greet(pin="1234"):
#     return(f'Hello your default pin is {pin}, change it at the ATM')
# print(greet("9012"))

# def sum_numbers(x,y):
#     return x+y


# def calculator():
#     a= 8
#     b=9
#     return sum_numbers(a,b)
# print(calculator())

# def names(first_name, last_name):
#     return sum_numbers(first_name,last_name)
# print(names("nathaniel", "soyinka"))

# ARGS & KWARGS
# # *args

# def add_numbers(*args):
#     total = 0
#     for _num in args:
#         total += _num
#     return total
# print(add_numbers(2, 3, 5))
# print(add_numbers(1,2, 3,4, 5))

# **kwargs
# students = {
#     "names":"wole soyinka",
#     "class": "level-3",
#     "age": 26,
#     "grade": "A"
# }
# def students_info(**kwargs):
#     for key,value in students.items():
#         print(f"{key}: {value}")

# students_info()

# def allfunc(name,*args,**kwargs):
#     print(f"Hello my name is {name}")
#     total_score = 0
#     for _score in args:
#         print(_score)
#         total_score += _score
#         print(f"my total score is {total_score}")

#     for key,value in kwargs.items():
#         print(f"{key}:{value}")

# allfunc("Wole", 90, 80, 70, 60, class_level="degree", grade="A", location="Lagos")
