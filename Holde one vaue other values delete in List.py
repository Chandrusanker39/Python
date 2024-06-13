# This is a My won logical code By NS

print("""----------------------method ===> 1-----------------""")
                 
domains=["AI","data scientist","machine learning","devops engineer","cyber security"]
feature="AI" # type: ignore   #user selecting field 
data=len(domains) 

i=data
while i>1:
    domains.pop(-1)   #This method , selected your future(AI), is placeing on Index [0] (zero) from domain
    i=i-1
    if i==1:
        print("Your foeld : {} ".format(domains))
        
        
        
print("""-------------------Method ===>2-------------""" )

try:
    def fun(data):
        my="NS"
        if my in data :
            data.clear()
            data.append(my)
            for i in data: #for is get data in list and print str method 
                print(f"my field : {i}")
        else:
            print("Your selecting field con't exist in list")
except Exception:                           
       raise Exception
finally:
    fun(["data scientist","data analysis","cyber security","NS"])   



print("""-------------------------------Method ====>3 ---------------------------- """)    

class feature:
 def fun2(self,data): 
    try:
        for i in data: #for loop get the value in the list no't  ordered,  
            feature="NS"
            if i==feature:
                print("This is my Field : ",i)
                data.clear()  #once condiction is True print feature but other field con't remove  
            else:
                data.remove(i)
            continue       
    except Exception:
        raise 
    finally:
        data.append(feature)
        print("Final List value : ",(data))
    
obj_class=feature()
obj_class.fun2(["NS","data scientist","data analysis","cyber security"])

