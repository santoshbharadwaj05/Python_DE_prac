#  ++  and  --  operators  demo  program
a = 25
print(++a)  #  +(+a) = +a  =  25
#print(a++) #  (a+)+  =  a+ =  25+  throws   error
#print(a++1)  #  a + (+1)  =  a +  1 = 25 + 1  = 26
print(--a) #25
#print(a--) #error
#print(a--1)#error
print(-a) #-25
print(+-a)#-25
print(-+a)#-25

#  Semicolon  demo  program
print('One');#One
print('Two');#Two
print('Three');#Three
print('Hyd')  ;   #Hyd 
print('Sec')  ;#Sec  
print('Cyb')#Cyb

#  floor()  and  ceil()  functions  demo  program
import  math
print(math . floor(10.8))  #10
print(math . ceil(10.8)) #  11
print(math . floor(25.0)) #25
print(math . ceil(25.0)) #25
print(math . floor(-3.5)) #-4
print(math . ceil(-3.5)) #-3
print(math . floor(-9.0)) #-9
print(math . ceil(-9.0)) #-9
print(math . floor(25.1)) #25
print(math . ceil(25.1)) #26
#print(floor(3.5)) #Error 
#print(ceil(3.5)) #error
'''
1) What  does  floor(x)  do ?  --->  Returns  nearest  previous  integer  of  'x'

2) What  does  ceil(x)  do ?  --->  Returns  nearest  next  integer  of  'x'
'''

# gcd()  function  demo  program
import  math
print(math . gcd(12 , 15)) #    3
print(math . gcd(12 , 18))  #  6
print(math . gcd(4 , 7)) #   1
print(math . gcd(7 , 7)) # 7
print(math . gcd(-18 , -27)) #-3
print(math . gcd(-4 , 6)) #2
print(math . gcd(0 , 7))#7
print(math . gcd(3 , 0)) #3
print(math . gcd(0 , 0)) #0
#print(gcd(5 , 15)) #error

#  abs()  function  demo  program
from  builtins  import  abs
print(abs(-35.8))#35.8
print(abs(-27))#27
print(abs(29.5))#29.5
print(abs(32))#32
import  builtins
print(builtins . abs(-25))#25

#  max()  and  min()   functions  demo  program
from  builtins  import   max , min
print(max(10.8 , 20.6)) #20.6
print(min(10.8 , 20.6 , 5.9 , 12.3))#5.9
print(max(25 , 10.8))#25
import  builtins
print(builtins . max(10 , 20 , 30))#30
print(builtins . min(10 , 20 , 15 , 5 , 12))#20

# pow()  function  demo  program
from  builtins  import  pow
print(pow(10 , -2))#0.01
print(pow(4 , pow(3 , 2)))#4^9
import  builtins
print(builtins . pow(2 , 3))#8
print(builtins . pow(-2 , -3))#-2^-3


'''
# Find  outputs
How  to  import   kw  list #import keyword
How  to  print  kwlist #print(keyword.kwlist)
How  to  print  number  of  keywords #print(len(keyword.kwlist)) 
How  to  print  type  of kwlist #print(type(keyword.kwlist))
print(keyword . kwlist) #keyword list printed  

#  Find  outputs  (Home  work)
How  to  import   keyword  module #import keyword
How  to  print  kwlist  #print(keyword.kwlist)
How  to  print  number  of  keywords #print(len(keyword.kwlist))                                                                                                                          How  to  print  type  of kwlist #print(type(keyword.kwlist))
print(kwlist) #keyword list printed
'''