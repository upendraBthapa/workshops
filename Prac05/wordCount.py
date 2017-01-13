__author__ = 'jc437345'

string = input("Text: ")
list_string = string.split()
repeat = {}
for i in list_string:
    repeat[i]=list_string.count(i)

for count in repeat:
    print("{}: {}".format(count,repeat[count]))
print("number of words:",list_string.__len__())

