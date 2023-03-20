list = () 

fruits = ['naranja', 'banana', 'fresa', 'melon', 'manzana']
print(fruits)
print(len(fruits))

first_fruits = [0]
third_fruits = [2]
last_fruits = [4]
print(first_fruits)
print(third_fruits)
print(last_fruits)

mixed_data_types = ['Antonio', 17, 1.85, 'soltero', 'Jerez']

it_companies = ['Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon']
print(it_companies)

print(len(it_companies))

first_company = [0]
middle_company = [3]
last_company = [6]

it_companies[0] = 'Instagram'
print(it_companies)

it_companies.append('Nokia')

it_companies.insert(4, 'LG')

it_companies[0] = it_companies[0].upper()

it_companies = '#it_companies'

does_exist = 'Google' in it_companies
print(does_exist)

it_companies.sort()
print(it_companies) 

it_companies.sort(reverse=True)
print(it_companies)

INSTAGRAM, Google, Microsoft = it_companies[0:2]
Oracle, Amazon, Nokia = it_companies[6:8]
Apple, IBM, LG = it_companies[3:5]

it_companies.remove(INSTAGRAM)
it_companies.pop(3)
it_companies.pop(4)
it_companies.pop(5)
del it_companies
it_companies.clear()

front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
back_end = ['Node','Express', 'MongoDB']

final_list = front_end + back_end 
full_stack = final_list.copy()

full_stack.insert(5, 'Python')
full_stack.insert(6, 'SQL')
print(full_stack)

