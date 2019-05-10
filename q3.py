def student(name, roll, age, address):
    print(name, roll, age,address)


student('pratima, name='pratima', 20, 20, 20)#output invalid syntax



student('pratima', 20, age=25,'kathmandu')#output positional argument follows keyword argument



student('pratima')#output TypeError: student() missing 3 required positional arguments: 'roll', 'age', and 'address'