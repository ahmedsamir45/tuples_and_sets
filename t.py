coordinates = (23,45)
list_of_tuples = [(2,3),(5,6),(2,6)]

# coordinates[0] = 77 ----> error doesnot support item assigment 
print(coordinates)
print(coordinates[0])
coordinates = list(coordinates)
coordinates.append(5)
coordinates = tuple(coordinates)
print(coordinates)
print(list_of_tuples)
