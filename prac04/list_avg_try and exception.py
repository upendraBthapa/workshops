__author__ = 'jc449735'
def list_avg(Le):
    try:
        avg=sum(Le)/len(Le)
    except TypeError:
        print("not all elements are numeric")
    except ZeroDivisionError:
        print("values must be anything else than zero")
    except:
        print("unknown error")
    return(avg)
print(list_avg([1,2,3,4]))