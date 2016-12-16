__author__ = 'jc449735'
my_list = [5, -12, 45]

def get_low_high(values):
   return min(values), max(values)

low, high = get_low_high(my_list)
print(low, type(low)) # -12 <class 'int'>

z = get_low_high(my_list)
print(z, type(z)) # (-12, 45) <class 'tuple'>


s="   nale   "
print(s.strip())


i=0
for i in range(1,12,3):
	print(i , end=" ")
print(i)