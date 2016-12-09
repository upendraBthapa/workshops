__author__ = 'jc449735'
in_file=open("stock.txt","r")
for line in in_file:
    line=line.strip()
    #print(line)
    split_line=line.split(",")
    print("Name:",split_line[0],)
    print("Year:",split_line[1])
    print("Price:${:.2f}".format(float(split_line[2])))
in_file.close()
"""
Basic Kivy test code
If this works, it will produce a GUI window with "hello world" in the middle
and you know you have set everything up correctly.
It also prints the Python version in the run output (may be mixed in with Kivy output)
The Python version should be 3.x (not 2.x).
"""
