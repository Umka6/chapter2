name = ['Gulya','Pesha','Ukulya','Altynay','Katya','Denis']
item = name.index(input('Which name you want to replace:'))
name[item] = input('enter a name to which you want to change:')
print('new contact list looks like this')
print(name)