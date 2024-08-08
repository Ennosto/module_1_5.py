immutable_var = 1, 'Тупле', False
print(immutable_var)
print(type(immutable_var))
immutable_var = tuple[2] = True #Потому что кортеж - это неизменямый тип данных, как числа и строки.
mutable_list = [1234, 'White Rabbit', True]
print(mutable_list)
mutable_list[1] = 'Black Rabbit'
print(mutable_list)