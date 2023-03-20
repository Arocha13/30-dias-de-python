it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
len(it_companies)

it_companies.add('Twitter')
it_companies.update(['Instagram', 'Android', 'Samsung'])

it_companies.remove('Apple')

#si utilizas remove y el elemento no está presente te salta un error y con discard no te salta ningún error solo te imprime el conjunto original

A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}

C = A.union(B)
print(C)

print(A.intersection(B))
print(B.issubset(A))
print(A.difference(B))
print(A.union(B))
print(B.union(A))
print(A.symmetric_difference(B))

del A 
del B
del C