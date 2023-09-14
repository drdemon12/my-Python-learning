import datetime
x = datetime.datetime.now() 
print (x) 

print(x.strftime("%Y"))

import datetime
print(datetime.datetime.ctime(datetime.datetime.now()))

x = datetime.datetime.now()
print(x.strftime("%Y-%m-%d__%H:%M:%S"))