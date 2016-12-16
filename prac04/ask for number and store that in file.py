__author__ = 'jc449735'
num=0
temp_file=open("convert number in","w")
while num >= 0:
    num=int(input("NUMBER :"))
    print(str(num),file=temp_file)
temp_file.close()