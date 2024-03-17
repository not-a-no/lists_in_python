#[]indicate a list
bicycles = ['trek','cannondale', 'redline', 'specialized']
print(bicycles)

#index
print(bicycles[0])
print(bicycles[0].title())

#special syntax for accessing the last elements in a list, index -1
print(bicycles[-1])

message = f"My first bicycle was a {bicycles[0].title()}"
print(message)

#modifying elements
motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)
motorcycles[0] = 'ducati'
print(motorcycles)

#adding elements
motorcycles.append('honda')
print(motorcycles)

#you can start with an empty list then add items

motorcycles = []
motorcycles.append('honda')
motorcycles.append('yamaha')
motorcycles.append('suzuki')
print(motorcycles)

#insert elements
motorcycles = ['honda', 'yamaha', 'suzuki']
motorcycles.insert(0, 'ducati')
print(motorcycles)

#removing elements
#if you know the position of the item
motorcycles = ['honda', 'yamaha', 'suzuki']
del motorcycles[0]
print(motorcycles)
#removing an item with the pop() method
#the pop() method removes the last item in a list
#but it lets you work with that item after removing

motorcycles = ['honda', 'yamaha', 'suzuki']
popped_motorcycle = motorcycles.pop()
print(motorcycles)
print(popped_motorcycle)
