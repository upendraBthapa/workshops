__author__ = 'Cue'
def square_number(num):
    return(num * num)
print(square_number(5))

def is_prime(value):
    i = 2
    while i < value:
        remainder = value % i
        if remainder == 0:
            return False
        i += 1
    return True

is_prime(is_prime(5))



def inch_to_meter(inch):
    return(0.0254*inch)
print(inch_to_meter(5))