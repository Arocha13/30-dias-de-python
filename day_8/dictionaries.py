dog = {}
dog = {'name':'Max', 'color':'Blanco', 'breed':'Labrador retrieve', 'legs':'4', 'age':'3'}
student = {'first_name':'Antonio', 'last_name':'Arocha', 'gender':'hombre', 'age':'17', 'marital status':'soltero', 'skill': 'baloncesto', 'country':'España', 'city':'Jerez', 'address':'Ermita de la Oliva 28'}
print(len(student))
print(student['skill'])
print(type(student['skill']))
print(student['skill'].append('memorizar'))
keys = student.keys() 
values = student.values()
item = list(student.items())
student.pop('age')
del student