__author__ = 'jc449735'
num=0
temp_file=open("convert number in","w")
while num >= 0:
    num=int(input("NUMBER :"))
    if num >= 0:
        print(str(num),file=temp_file)
    else:
            print("input only positive integer value")
temp_file.close()