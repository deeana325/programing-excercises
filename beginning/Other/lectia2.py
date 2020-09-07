In [3]: list(range(10))                                                                                                 
Out[3]: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

In [4]: l = [1, 53, 82]                                                                                                 

In [5]: l[:2]                                                                                                           
Out[5]: [1, 53]

In [6]: list(range(2))                                                                                                  
Out[6]: [0, 1]

In [7]: l = list(range(10))                                                                                             

In [8]: l[0:10:2]                                                                                                       
Out[8]: [0, 2, 4, 6, 8]

In [9]: list(range(0, 10, 2))                                                                                           
Out[9]: [0, 2, 4, 6, 8]

In [10]: range(10)                                                                                                      
Out[10]: range(0, 10)

In [11]: list(range(0, 10, 2))                                                                                          
Out[11]: [0, 2, 4, 6, 8]

In [12]: list(range(0, 10, 2))[:2]                                                                                      
Out[12]: [0, 2]

In [13]: range(0, 10, 2)[:2]                                                                                            
Out[13]: range(0, 4, 2)

In [14]: def count(l)                                                                                                   
  File "<ipython-input-14-c7696995c18d>", line 1
    def count(l)
                ^
SyntaxError: invalid syntax


In [15]: def count(l): 
    ...:     return  l.count(4) 
    ...:                                                                                                                

In [16]: count([1, 4, 44, 32780, 2, 3, 4])                                                                              
Out[16]: 2

In [17]: def count(l, n): 
    ...:     return  l.count(n) 
    ...:                                                                                                                

In [18]: count([1, 4, 44, 32780, 2, 3, 4])                                                                              
---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)
<ipython-input-18-8fe675cfe858> in <module>
----> 1 count([1, 4, 44, 32780, 2, 3, 4])

TypeError: count() missing 1 required positional argument: 'n'

In [19]: count([1, 4, 44, 32780, 2, 3, 4], 3)                                                                           
Out[19]: 1

In [20]: def count(l, n = 4): 
    ...:     return  l.count(n) 
    ...:                                                                                                                

In [21]:                                                                                                                

In [21]: count([1, 4, 44, 32780, 2, 3, 4])                                                                              
Out[21]: 2

In [22]: count([1, 4, 44, 32780, 2, 3, 4], n = 44)                                                                      
Out[22]: 1

In [23]: count([1, 4, 44, 32780, 2, 3, 4], 44)                                                                          
Out[23]: 1

In [24]: count(l = [1, 4, 44, 32780, 2, 3, 4], n = 44)                                                                  
Out[24]: 1

In [25]: def count(l, n = None): 
    ...:     return  l.count(n) 
    ...:                                                                                                                

In [26]:                                                                                                                

In [26]: count([1, 4, 44, 32780, 2, 3, 4])                                                                              
Out[26]: 0

In [27]: count([1, 4, 44, 32780, , 3, 4])                                                                               
  File "<ipython-input-27-64dc2589596e>", line 1
    count([1, 4, 44, 32780, , 3, 4])
                            ^
SyntaxError: invalid syntax


In [28]: count([1, 4, 44, 32780, None , 3, 4])                                                                          
Out[28]: 1

In [29]: type(4)                                                                                                        
Out[29]: int

In [30]: type([4])                                                                                                      
Out[30]: list

In [31]: type(None)                                                                                                     
Out[31]: NoneType

In [32]: def count(l, n = None): 
    ...:     l.count(n) 
    ...:                                                                                                                

In [33]: count([1, 4, 44, 32780, None , 3, 4], 4)                                                                       

In [34]: type(count([1, 4, 44, 32780, None , 3, 4], 4))                                                                 
Out[34]: NoneType

In [35]: type(a = 2)                                                                                                    
---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)
<ipython-input-35-c1727f10851b> in <module>
----> 1 type(a = 2)

TypeError: type() takes 1 or 3 arguments

In [36]: type(print('abc'))                                                                                             
abc
Out[36]: NoneType

In [37]: def test(n = None): 
    ...:     if n == None: 
    ...:         print('nu am primit n') 
    ...:     else: 
    ...:         print('n este', n) 
    ...:                                                                                                                

In [38]: test()                                                                                                         
nu am primit n

In [39]: test(1)                                                                                                        
n este 1

In [40]: test(n=1)                                                                                                      
n este 1

In [41]: range?                                                                                                         
Init signature: range(self, /, *args, **kwargs)
Docstring:     
range(stop) -> range object
range(start, stop[, step]) -> range object

Return an object that produces a sequence of integers from start (inclusive)
to stop (exclusive) by step.  range(i, j) produces i, i+1, i+2, ..., j-1.
start defaults to 0, and stop is omitted!  range(4) produces 0, 1, 2, 3.
These are exactly the valid indices for a list of 4 elements.
When step is given, it specifies the increment (or decrement).
Type:           type
Subclasses:     

In [42]: s='abc'                                                                                                        

In [43]: s[:2]                                                                                                          
Out[43]: 'ab'

In [44]: s[:3]                                                                                                          
Out[44]: 'abc'

In [45]: s[:4]                                                                                                          
Out[45]: 'abc'

In [46]: s=''                                                                                                           

In [47]: s[:4]                                                                                                          
Out[47]: ''

In [48]: l = [1, 2, 3]                                                                                                  

In [49]: l[:4]                                                                                                          
Out[49]: [1, 2, 3]

In [50]: print('%3d' %10)                                                                                               
 10

In [51]: print('%-3d' %10)                                                                                              
10 

In [52]: print('%-3d' %10)                                                                                              
10 

In [53]: print('%3d %3d' %(10, 999))                                                                                    
 10 999

In [54]: print('a=%3d b=%3d' % (10, 999))                                                                               
a= 10 b=999

In [55]: print('%3x' %10)                                                                                               
  a

In [56]: print('%3f' %10)                                                                                               
10.000000

In [57]: print('%.3f' %10)                                                                                              
10.000

In [58]: l=['a', 'b', 'c']                                                                                              

In [59]: ''.join(l)                                                                                                     
Out[59]: 'abc'

In [60]: l=['a', 'b', 3]                                                                                                

In [61]: ''.join(l)                                                                                                     
---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)
<ipython-input-61-9e05f63092b3> in <module>
----> 1 ''.join(l)

TypeError: sequence item 2: expected str instance, int found

In [62]: [x for x in l]                                                                                                 
Out[62]: ['a', 'b', 3]

In [63]: [str(x) for x in l]                                                                                            
Out[63]: ['a', 'b', '3']

In [64]: ''.join[str(x) for x in l]                                                                                     
  File "<ipython-input-64-28be0c6c25f8>", line 1
    ''.join[str(x) for x in l]
                     ^
SyntaxError: invalid syntax


In [65]: ''.join([str(x) for x in l])                                                                                   
Out[65]: 'ab3'

In [66]: [str(x)*2 for x in l]                                                                                          
Out[66]: ['aa', 'bb', '33']

In [67]: [len(str(x)) for x in l]                                                                                       
Out[67]: [1, 1, 1]

In [68]: max([len(str(x)) for x in l])                                                                                  
Out[68]: 1

In [69]: l=[[1, 2, 3], [4, 5]]                                                                                          

In [70]: max([len(x) for x in l])                                                                                       
Out[70]: 3

In [71]: l=[[1, 2, 3], [4, 5], 5]                                                                                       

In [72]: max([len(x) for x in l])                                                                                       
---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)
<ipython-input-72-3bb1feea2b41> in <module>
----> 1 max([len(x) for x in l])

<ipython-input-72-3bb1feea2b41> in <listcomp>(.0)
----> 1 max([len(x) for x in l])

TypeError: object of type 'int' has no len()

In [73]: max([len(x) for x in l if type(x) == list])                                                                    
Out[73]: 3

In [74]: s = 'ana are mere'                                                                                             

In [75]: list(s)                                                                                                        
Out[75]: ['a', 'n', 'a', ' ', 'a', 'r', 'e', ' ', 'm', 'e', 'r', 'e']

In [76]: s.split('a')                                                                                                   
Out[76]: ['', 'n', ' ', 're mere']

In [77]: s.split('ar')                                                                                                  
Out[77]: ['ana ', 'e mere']

In [78]: s.split(' ', '')                                                                                               
---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)
<ipython-input-78-6d5fba156c1c> in <module>
----> 1 s.split(' ', '')

TypeError: 'str' object cannot be interpreted as an integer

In [79]: s.split(' ')                                                                                                   
Out[79]: ['ana', 'are', 'mere']

In [80]: s.replace(' ', '-')                                                                                            
Out[80]: 'ana-are-mere'

In [81]: s.replace(' ', '')                                                                                             
Out[81]: 'anaaremere'

In [82]: s.replace(' ', '').split('')                                                                                   
---------------------------------------------------------------------------
ValueError                                Traceback (most recent call last)
<ipython-input-82-ec2e706b6ef4> in <module>
----> 1 s.replace(' ', '').split('')

ValueError: empty separator

In [83]: list(s.replace(' ', ''))                                                                                       
Out[83]: ['a', 'n', 'a', 'a', 'r', 'e', 'm', 'e', 'r', 'e']

In [84]: s                                                                                                              
Out[84]: 'ana are mere'

In [85]: [x for x in s ]                                                                                                
Out[85]: ['a', 'n', 'a', ' ', 'a', 'r', 'e', ' ', 'm', 'e', 'r', 'e']

In [86]: [x for x in s if x in 'aeiouAEIOU']                                                                            
Out[86]: ['a', 'a', 'a', 'e', 'e', 'e']

In [87]: [x for x in s]                                                                                                 
Out[87]: ['a', 'n', 'a', ' ', 'a', 'r', 'e', ' ', 'm', 'e', 'r', 'e']

In [88]: x = 5                                                                                                          

In [89]: 'impar' if x%2 == 1 else 'par;                                                                                 
  File "<ipython-input-89-9054d72712d7>", line 1
    'impar' if x%2 == 1 else 'par;
                                  ^
SyntaxError: EOL while scanning string literal


In [90]: 'impar' if x%2 == 1 else 'par'                                                                                 
Out[90]: 'impar'

In [91]: [ x.upper() if x in 'aeiou' else x for x in s]                                                                 
Out[91]: ['A', 'n', 'A', ' ', 'A', 'r', 'E', ' ', 'm', 'E', 'r', 'E']

In [92]: str([x.upper() if x in 'aeiou' else x for x in s] 
    ...: )                                                                                                              
Out[92]: "['A', 'n', 'A', ' ', 'A', 'r', 'E', ' ', 'm', 'E', 'r', 'E']"

In [93]: ''.join([x.upper() if x in 'aeiou' else x for x in s] 
    ...: )                                                                                                              
Out[93]: 'AnA ArE mErE'

In [94]: a = 'impar' if x%2 == 1 else 'par'                                                                             

In [95]: l                                                                                                              
Out[95]: [[1, 2, 3], [4, 5], 5]

In [96]: l = [1, 2, 3]                                                                                                  

In [97]: type(l)                                                                                                        
Out[97]: list

In [98]: set(l)                                                                                                         
Out[98]: {1, 2, 3}

In [99]: l = [1, 2, 3, 1]                                                                                               

In [100]: set(l)                                                                                                        
Out[100]: {1, 2, 3}

In [101]: s = set(l)                                                                                                    

In [102]: s.add(4)                                                                                                      

In [103]: s                                                                                                             
Out[103]: {1, 2, 3, 4}

In [104]: s.add(4)                                                                                                      

In [105]: s                                                                                                             
Out[105]: {1, 2, 3, 4}

In [106]: s.intersection({2, 3})                                                                                        
Out[106]: {2, 3}

In [107]: s.intersection({2, 3, 5, 7})                                                                                  
Out[107]: {2, 3}

In [108]:                                                                                                               

In [108]: s.union({2, 7, 9, 6, 5})                                                                                      
Out[108]: {1, 2, 3, 4, 5, 6, 7, 9}

In [109]: l                                                                                                             
Out[109]: [1, 2, 3, 1]

In [110]: list(set(l))                                                                                                  
Out[110]: [1, 2, 3]

In [111]: len(s)                                                                                                        
Out[111]: 4

In [112]: s.difference(set(l))                                                                                          
Out[112]: {4}

In [113]: {'ion':7, 'maricica':9, 'ana':4}                                                                              
Out[113]: {'ion': 7, 'maricica': 9, 'ana': 4}

In [114]: d={'ion':7, 'maricica':9, 'ana':4}                                                                            

In [115]: type(d)                                                                                                       
Out[115]: dict

In [116]: len(d)                                                                                                        
Out[116]: 3

In [117]: d.keys                                                                                                        
Out[117]: <function dict.keys>

In [118]: d.keys()                                                                                                      
Out[118]: dict_keys(['ion', 'maricica', 'ana'])

In [119]: d.values()                                                                                                    
Out[119]: dict_values([7, 9, 4])

In [120]: d.items()                                                                                                     
Out[120]: dict_items([('ion', 7), ('maricica', 9), ('ana', 4)])

In [121]: d[ion]                                                                                                        
---------------------------------------------------------------------------
NameError                                 Traceback (most recent call last)
<ipython-input-121-d5fd870ff1a7> in <module>
----> 1 d[ion]

NameError: name 'ion' is not defined

In [122]: d['ion']                                                                                                      
Out[122]: 7

In [123]: {ion:7, 'maricica':9, 'ana':4}                                                                                
---------------------------------------------------------------------------
NameError                                 Traceback (most recent call last)
<ipython-input-123-983aacf8a41b> in <module>
----> 1 {ion:7, 'maricica':9, 'ana':4}

NameError: name 'ion' is not defined

In [124]: ion=None                                                                                                      

In [125]: {ion:7, 'maricica':9, 'ana':4}                                                                                
Out[125]: {None: 7, 'maricica': 9, 'ana': 4}

In [126]: d2={ion:7, 'maricica':9, 'ana':4}                                                                             

In [127]: d2[NPN]                                                                                                       
---------------------------------------------------------------------------
NameError                                 Traceback (most recent call last)
<ipython-input-127-64504a6527f0> in <module>
----> 1 d2[NPN]

NameError: name 'NPN' is not defined

In [128]: d2[None]                                                                                                      
Out[128]: 7

In [129]: d2={ion:7, 'maricica':9, 'ana':{'mate':7, 'romana':5}}                                                        

In [130]: d2={ion:7, 'maricica':9, 'ana':{'mate':7, 'romana':5}}                                                        

In [131]: d2                                                                                                            
Out[131]: {None: 7, 'maricica': 9, 'ana': {'mate': 7, 'romana': 5}}

In [132]: d2['ana']                                                                                                     
Out[132]: {'mate': 7, 'romana': 5}

In [133]: d2['ana']['mate']                                                                                             
Out[133]: 7

In [134]: d2={ion:7, 'maricica':[1, 2, 3], 'ana':{'mate':7, 'romana':5}}                                                

In [135]: d2['maricica'][2]                                                                                             
Out[135]: 3

In [136]: [type(x) for x in d2]                                                                                         
Out[136]: [NoneType, str, str]

In [137]: [(type(x), type(d2[x])) for x in d2]                                                                          
Out[137]: [(NoneType, int), (str, list), (str, dict)]

In [138]: [(type(k), type(v)) for k, v in d2.items()]                                                                   
Out[138]: [(NoneType, int), (str, list), (str, dict)]

In [139]:                                                                                                               

In [139]:                                                                                                               

In [139]:                                                                                                               

In [139]:                                                                                                               

In [139]: 2, 3                                                                                                          
Out[139]: (2, 3)

In [140]:                                                                                                               

In [140]:                                                                                                               

In [140]:                                                                                                               

In [140]: a, b = 5, 6                                                                                                   

In [141]: a                                                                                                             
Out[141]: 5

In [142]: b                                                                                                             
Out[142]: 6
