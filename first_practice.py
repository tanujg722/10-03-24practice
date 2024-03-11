#How to creatye a list and tuple with comma separated number in python

values = input("input some numbers: ")
list = values.split(",")
tuple = tuple(list)

print("list: " , list)
print("tuple: " , tuple)