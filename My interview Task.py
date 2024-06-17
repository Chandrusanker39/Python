class storager:              #this class is used for stored value's ,Here's this is RE_USABLE_OF_CODE
    x=[1,2,3,4,10]    
    y=[1,2,3,4,5]
    arrays=numpy.array([6,5,10])
obj_storage=storager

"""--------------------------------# Task Type ===> 1----------------------------------------"""

def width_out(value):
    if True:
        # print("condiction")  >>>> this used for check the code is properly run 
        return value-1 
    else:
        return value 
     
res6=width_out(obj_storage.arrays) 
print("index value in widthout map function: {}".format(list(res6)))  

"""-----------------------------#Task Type ===> 2--------------------------------------------"""

ints=list(map(int,input("this is list value : ").strip().split()))  #get values for user's 

def index_val(c):
    if True:
        return c-1
res5=map(index_val,ints)
print("this index value : {}".format(list(res5)))    
