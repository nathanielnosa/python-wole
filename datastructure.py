# ::: List :::
# fruits = ['apple','orange','mango','banana','cashew']

# get a fruit
# print(fruits[0])
# rename a fruit
# fruits[0] = 'grape'
# fruits.append('pineapple')
# fruits.remove('cashew')
# fruits.insert(1,'coconut')
# fruits.pop(3)
# fruits.sort()
# fruits.reverse()
# fruits.clear()
# print(fruits)

# ::: Tuple :::
# numbers = (1,2,3,4,5) 
# fruits = ('apple','orange','mango','banana','cashew')
# sizes = (
#     ('s','sm'),
#     ('m','mm'),
#     ('l','lg'),
# )

# menu = (
#     ('Rice',500),
#     ('Beans',200),
#     ('Yam',800),
# )

# print(numbers)
# print(type(numbers))
# get a number
# print(fruits[2])
# print(len(fruits))
# del fruits

# print(sizes)
# print(menu)

# ::: set :::
# fruits = {'apple', 'orange', 'mango', 'banana', 'cashew'}
# print(type(fruits))
# print(fruits)
# print('apple' in fruits)
# fruits.add('grape')
# fruits.remove('apple')
# fruits.update({'abcd','efghc'})
# fruits.update(['grape', 'coconut', 'melons'])
# fruits.clear()
# print(fruits)

# ::: Dictionary :::
# student = {
#     'name': 'Kendall',
#     'age': 20,
#     'courses': ['Math', 'CompSci'],
#     'is_alive': True
# }
# print(type(student))
# print(student)
# print(student.keys()) #list []
# print(student.values()) #list []
# print(student.items()) #[()]
# print(student['name'])
# print(student.get('name')) # safer than 
# student['name'] = 'Kendall Jenner'

# student_new = student.copy()
# print(student_new)
# print(len(student))
# student.update({'name': 'Kendall Jenner', 'age': 21, 'phone': '555-5555'})
# print(student)


# ::: List of Dictionary :::
todo_app = [
    {   'id' : 1,
        'task': 'Go to the gym',
        'status': 'pending'
    },
    {
       'id' : 2,
        'task': 'Buy groceries',
        'status': 'completed'
    },
    {
       'id' : 3,
        'task': 'Clean the house',
        'status': 'pending'
    }
]

# print(todo_app)
# print(todo_app[2])
# print(todo_app[1]['task'])