##from collections import 
##   
# With sequence of items 
##print(Counter(['B','B','A','B','C','A','B',
##               'B','A','C']))
   
# with dictionary
##print(Counter({'A':3, 'B':5, 'C':2}))
##   
### with keyword arguments
##print(Counter(A=3, B=5, C=2))

##ordered dict
##from collections import OrderedDict
##   
##print("This is a Dict:\n")
##d = {}
##d['a'] = 1
##d['b'] = 2
##d['c'] = 3
##d['d'] = 4
##print(d)
##   
##
##   
##print("\nThis is an Ordered Dict:\n")
##od = OrderedDict()
##od['a'] = 1
##od['b'] = 2
##od['c'] = 3
##from collections import defaultdict
    
    
### Defining the dict
##d = defaultdict(int)
##    
##L = [1, 2, 3, 4, 2, 4, 1, 2]
##    
### Iterate through the list
### for keeping the count
##for i in L:
##        
##    # The default value is 0
##    # so there is no need to 
##    # enter the key first
##    d[i] += 1
##        
##print(d)
####od['d'] = 4
####print(od)
##
##
##   
##
##from collections import ChainMap
##    
##    
##d1 = {'a': 1, 'b': 2}
##d2 = {'c': 3, 'd': 4}
##d3 = {'e': 5, 'f': 6}
## 
### Defining the chainmap
##c = ChainMap(d1, d2, d3)
##    
##print(c)



from collections import deque
   
# Declaring deque
queue = deque(['name','age','DOB'])
   
print(queue)
