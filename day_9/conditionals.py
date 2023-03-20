age = int(input('Enter age: '))
if age > 18:
    print('tiene edad suficiente para conducir')
else: 
    print('necesitas', 18 - age  ,'más para conducir')

my_age = 17 

if age == my_age:
     print('tenemos la misma edad')
elif age > my_age: 
    print('tienes', age - my_age ,'años más que yo')
else:
     print('tienes', my_age - age ,'años menos que yo')

a = int(input('Enter number: '))
b = int(input('Enter number: '))

if a > b: 
    print(a, 'es mayor que' ,b)
elif a < b:
    print(a, 'es menor que' ,b)
else:
    print(a, 'es igual que' ,b)   


grade = int(input('Enter grade: '))
if grade < 101 and grade > 79:
    print('A')
elif grade < 80 and grade > 69: 
    print('B')
elif grade < 70 and grade > 59: 
    print('C')
elif grade < 60 and grade > 49:
    print('D')
else:
    print('F') 

month = input('Enter month: ')
if month in ['Septiembre','Octubre','Diciembre']:
    print('Otoño')
if month in ['Diciembre','Enero','Febrero']:
   print('Invierno')
if month in ['Marzo','Abril','Mayo']:
   print('Primavera')
elif month in ['Junio', 'Julio', 'Agosto']:
   print('Verano') 

fruits = ['banana', 'naranja', 'mango', 'limon']
fruit = input('Enter fruit: ')
if fruit in fruits:
    print('Esa fruta ya existe en la lista')
else: 
    fruits.append(fruit)
print(fruits)  