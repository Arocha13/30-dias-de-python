empty_tuple = ()

sisters = ('Tania', 'Itziar', 'Ariana')
brothers = ('Rodrigo', 'Alex')

siblings = sisters + brothers 

len(siblings)

siblings = list(siblings)
siblings[0] = 'Monica'
siblings[0] = 'Antonio'
siblings = tuple(siblings)

family_members = siblings + ('Antonio', 'Monica')
print(family_members)