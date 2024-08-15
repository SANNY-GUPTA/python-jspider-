import keyword
print(keyword.kwlist)

20-01-2024––––––––––––––––––

-python is an interpreted languages, its excute line by line when control get any error the excution ofprogram are terminated 
-python supportes cross platform -window,linux if we write a program in one operating sysytem and the same program in another operating system we will get same o/p
-variable can take one value at on  time.
-its scripting lang if any lang is interpreted lang then that lang is scripting lang
-we use python for scripting purpose
-  .py to .pyc use import thatfile name in second file and then run the first file.
- python is High level progarming langu(standard by human as well as pc)
- Open source language(free to use) 


                         PMM (PYTHON MEMORY MANAGEMENT) 

variable is the name that is given for one memory allocation
id() fun are  useing to give to address of variable
a=6
print(id(a))
140703416072792--o/p


- if  two variable are diff but value are same then Memory allocation are also Same.
if any value is not  having any reference  then the value is elegible for python Garbage locator.
a=30
b=5
print(a,b)
30 5 -- o/p
a=20
print(a+b)
25  -- o/p



  21-01-2023 ------------------------------
                                                identifires
  

- identifireis is use for identify make its name func name and class name.
     Rules of Identifires
  * identifres should not start with digit
  *  special character are not allow as an indetifires except _ (underscore)
  *  keyword are not allow in as an identify
        if =90                                                                                    
        SyntaxError: invalid syntax                                                                         
        True=2
        SyntaxError: cannot assign to True

  *  all variable are identifires

write down the program to print all keyword
 

          modules(keyword)
  import keyword
  print(keyword.kwlist)
                
   

o/p--========== RESTART: C:/Users/sanny/Desktop/J_SPIDER/PYTHON/keyword.py ==========
['False', 'None', 'True', 'and', 'as', 'assert', 'async', 'await', 'break', 'class', 'continue', 'def', 'del', 'elif', 'else', 'except', 'finally', 'for', 'from', 'global', 'if', 'import', 'in', 'is', 'lambda', 'nonlocal', 'not', 'or', 'pass', 'raise', 'return', 'try', 'while', 'with', 'yield']

Here only False ,True And None are start from first word captial letter.



       
                         DATA TYPES----


SINGLE  DT -------- Integer , Float, Boolean , Complex
COLLECTION DT  ----------  Stirng , tuple , Set , Dict , List                  
 
*   INTEGER  - Value without any deciaml point are called interger and it's either + or - 
    Float   -  Value with  deciaml point are called Float  and it's either + or -  type(10.0)   ---  <class 'float'>
    Boolean -  Boolean has teo value that are True or False , True and False are keywords in python
   
     print(True)
         True
     print(True + True)
         2
     print(False)
        False
     print(False + False)
        0
 

    COMPLEX  - This data types contains two part one is real and second are imagemery part 
                  Representation of complex are :- a+ bj
             
                    5+7J
                          (5+7j)
                   type(6+7J)
                           <class 'complex'>
      

     STRING --  * [ ' ' ]  , [" " ] , ['''  '''] 
                -string are declared while using single,double and triple quotes
                -we use single and double for single line of strings , for multiplr line string use triple 
                -string are ordered data type 
                - string allows dupliccates 
                - String suppots indexing and its two type one is Positive( +) and negative (-) 								+ index start with  0 sfrom left side 
                         - index start from -1 from right side
                - sting are Homegenous data types
                - Sting is Immutable data type[which can't modify]
                
                   s='asdjka;s' 
                   print(s[6])
                                       ;   -- o/p
                   print(s[5]) 
                                       a   -- o/p

 

22-01-2023 ----------
                                                  LIST

* List is declared while using square bracket []
* List is ordered type
* List is hetrogenoues nature 
* List is mutable datatype , which means modify data
* List is support indexing
* List allows duplicates
* List store mutable and immutable data types
*  var=[['abcd' , 'Hello'] ,'python','java',[['mear', 'sql']],200]
len(var) = 
len(var[3]) = 
var[0][0] =
var[-2][-1][-2][2] = 
 
                                                Tuple

* ordered datatype , support indexing 
* tuple is declare using Round bracket where as single value in tuble is declare using a comma(,)
* Tuple is imutable data types it can't be modify
* Tuple is Hetrogeneous data types
* Duplicate allow 
* when we use (9) single value in bracket then also use (,) then it's tuple otherwise it's int data types.
other form to declare tuple----- 
 a=10,20,30
        a
           (10, 20, 30)
  n=10,
  type(n)
           <class 'tuple'>

t=('abcd',(10,20),[14,15,16,17])
t[-1][-1]=95
print(t)
                 ('abcd', (10, 20), [14, 15, 16, 95])

* if is store mutable data type in tuple then its not 100% immutable

                                                       SET

* we can't performing indexing in set
* Duplicate not allow 
* it's unorderd data types , Hetrogenous data types
* Mutable data types ,its can store only immutable data types
* set() declare empty set 
* {} declare using set



23-01-2023  --------------------------------



* In set { int, float, bool ,complex, str, tuple }
* str and tuple support hashable 
* a={'abc',(10,[20])}
Traceback (most recent call last):
  File "<pyshell#17>", line 1, in <module>
    a={'abc',(10,[20])}
TypeError: unhashable type: 'list'
                                                                                                          
example----

s={True,-10,10,1.0,1,0,False,'abc'}
print(s)
{0, True, 'abc', -10, 10}  --- o/p
                                              Dict
  

* Dict doesn't support imdexing
* if key are not there then show KeyError
* Mutable data type ,it can be modify  
* ordered data types 
* ver-3 ordered data and var-2 data are unordered data types
* Duplicate key not allow , only replece previous key 
* Dic id declare with {} element of key:value pairs
* suppot hashng data types
* In Dic keys are unique and values can duplicates 
* Key are immutable and  value are both mutable or immutable 



example ---

s={'s1':{'sem1':{'m1':45,'phy':25,'c':18}, 'sem2':{'m2':32,'che':33,'c++':44},'sem3':{'ds':41,'dbms':35,'ai':22}} , 's2':{'sem1':{'m1':40,'phy':33,'c':17}, 'sem2':{'m2':31,'che':22,'c++':25},'sem3':{'ds':42,'dbms':36,'ai':23}} , 's3':{'sem1':{'m1':23,'phy':36,'c':16}, 'sem2':{'m2':35,'che':44,'c++':40},'sem3':{'ds':43,'dbms':37,'ai':24}}}


24-01-2024 ---------------------------



s=10      
print(type(type(s)))      
<class 'type'>


print(print(20+10*5))
               70
                None

* sep data type only  use in string data types

*  Seperated by commma then use 
 
   print(10,20, sep=' , ')                                       
                 10 , 20   ---o/p
    
   print(10,20, sep='1')
                     10120130 ---- o/p
   

* \n use for change line 
* \t use for escape tab the words

                                                                   PRINT                                     
         

 * print metheod is used to display output of given expresssion
 * By using print method print multiple value
 * if we display multiple value , they are seprated by spacce( ) because of attribute sep(sepereter)
  
print mrthod attribute
            sep= ' ' , its use for remove the comma and the add sep value and its string data type
            end =    use for print in same line ,also its srting data types


print(10,20,30, sep='@')
                         10@20@30   ----- o/p
print(10,20,30, sep='1')
                         10120130   ----- o/p
print(10,20,30, sep='$')
                         10$20$30    ----- o/p
print(10,20,30, sep='-')
                         10-20-30    ----- o/p
print(10,20,30, sep=',')
                          10,20,30    ----- o/p
print(10,20,30)
                          10 20 30    ----- o/p

print(10,sep=',')
                           10       ----- o/p  in one value no use , 

print(10,20,30, end=',')
                           10 20 30,   ------ o/p
print(10,20,30, sep='@')
                           10@20@30   ------- o/p

print(10,end='z')
print(20,end='@')
print(30,end='.')
                           10z20@30.    ------- o/p

print(10,20,30, sep=',' ,  end ='@')
                                         10,20,30@    ----- o/p

print('we','python',sep='love', end='in begining')

                                          welovepythonin begining   ----- o/p

print('we','python',sep='lo\nve', end='in begining')     welo 
                                                            vepyhon in 



print('we','weekend',sep='lov\ne', end='after\njob')

welov
eweekendafter
job

print('we','no wishkey',sep='sa\ny', end='to\neverone')

wesa
yno wishkeyto
everone







25-01-2024  ------------


                                                                 OPERATORS



Arthmetic operator -
Relational Operator / comparision Operator -
Logical Operator -
Bitwise operator- 
Assigment operator -
identity  operator -
membership operator -
Ternany operator -


Arthmetic operator -

   Add - + using for adding the number and char
   sub - -using for sub the number
   Mul - *using for Multiply the number and char
   Div ---- a) true (/)  Return float data type  10/2 -- 5.0 , 24/5 -- 4.8
            b) floor ( // )  Retunrn int data types , Round off to lowest Value   10//2 - 5 , 24//5 - 4  , -24//2 -- -3 ,
            c) modula ( %)   Return Remainder , if we divide x by 2 then also get remainder are: 0,1 and when x divided by 3 then we get    the in range 0,1,2  example - 2 % 4 -- 2 , 42%2 - 0   ,    -127%10 - 3 (after divide find Remainder then add the divisior and find the answer for - ve number) 

   exp(pow)- ** Return the Square , 8**2 - 64 , 5**3 - 125 , 2**3**2 then its are 2**(3**2) = 2**9 = 512 are o/p Means that we traversal right to left then get o/p

 (2+2j) * (3+4j) --- -2+14j

**  2+2j * 3+4j = 2+2j*3+4j = 2+6j+4j = 2+ 10j


(2+4j) *(3+2j) = 6+4j+12j-8 =-2+16j
(3-2j) *(3+2j) = 9+4= 13




26-01-2024 ------------------------  Test 

29-01-2024   -----------------------




30-01-2024    -----------------------


Logical Operator - 

 logical operator-- logical and , logical or in [ java  (&& , ||) ]  and in  [ python (and , or) ]
 In or operator first is true or ____ ( Result is always True ) when true are first in or then no need to check second expression
 In or operator first is False  or ____ ( Result is may be True/False ) when False are first in or then need to check second expression
 
 True or 'a' +4
           True  ---- o/p
 
 False or 'a'+4
                   typeerror 
 

 True and 'a'+4
                   typeError
 False and 'a'+4
                  False
 
logical and - in logical and  all condition are True then we get o/p are True otherwise o/p is False
             . when first condition is true then control checks the second condition .

logical or - in logical or all condition are false then we get o/p are False otherwise  o/p is True
           . when first condition is False then control  checks the second conditions .

 ex- 1 and 1 then 1---o/p second 1 are showing in result
       1 and 1.0
                   1.0   -----o/p
       1 or 1.0
                   1    -------o/p

  0.0000001 or 45 ( in int (0) and float (0.0) are False  and in complex (0+0j) ) otherwise true 
                    1e-07 ---------- o/p

  0.0 or 44 ( in int (0) and float (0.0) are False ) otherwise true
                    44   --------- o/p
  
  -5 or 5
               -5  -------- o/p (only in int datatype are [0] is false otherwise like -5,10,-55 are true )
 
 
 False value are  --- in String - '' 
                      in list  - []
                      in tuple - ()
                      in set  -  set()
                      in Dictnonary - {} 
                      None

***  
  1 and 1 -- 1
  0 and 1  -- 0
  0 and 0 --- 0
  1 and 0.0  --- 0.0
  1 and 1.0 -- 1.0
  1 or 1.0  ---- 1
  12 and 14  --- 14 
  0.0 or 54  ----- 54





31-01-2024 -------------------------

Assigment operator -  Assigement operaator is used to store values in variable
   * to initialize multiple varibles in single line we use below syntax
 Syntax ----  var1 ,var2, var3 -----varn = value1, value2 , value3 ------ value n              
   *  to assign same value for multiple varibles  
         var1 =var2 =var3 =------=varn =value

a=b=c=d=23
print(a)
23
print(b)
23
print(c)
23
print(d)
23


a=10
a+=25  --- a=a+25 =10+25=35
a-=30  ---- a=a-30 = 35-30=5
a%=3   ----- a=a%3 = 5%3=2
a**3 ---- a=a**3= 2**3=8

 
**     To update a variable we use 
                                     -= , += , /= , //= , %= , *= , **=



01-02-2024 ------------------------
 write on copy



02-02-20204 ---------------------


05-02-2024 ------------



Ternany operator----

 >,<,>=,<= are not support in complex expression (8+8j) like.
 -- is operator and == are both are differnet ,is are define the address where the == are assigb the values.

Comparision operator is give boolen value as an output

example-

(5+8j) > (6+9j)
Traceback (most recent call last):
  File "<pyshell#15>", line 1, in <module>
    (5+8j) > (6+9j)
TypeError: '>' not supported between instances of 'complex' and 'complex'

Finding the ASCII value use - ord('a) - 97     , ord(A) - 65 ,ord('0') - 48

'abd' > 'abc'
           - True

 char('48')
      TypeError 
 char(48)
        '0' ------- o/p

integer start from ------ char(48) for '0' its output in [''] .
char start from -- ord('a') - 97     , ord('A') - 65

ord function is used for given char value
 char method -- char of given ASCII value

'abc' > 'ABC'  -- true [first are true then no need to check other]  a is 97 and A is 65 so {a} is larger than {A} 
'abc' < 'abc1' ------ True  ------- o/p
'a' > 1   TypeError  ---- o/p
'a' > True  TypeError    ---------- o/p
[1,4,5] > [2,4,5]         False ------- o/p
['a', 1,6] > [0,4,8]         False  ----------o/p , string and interger are never comparission .
['a',3] > ['a']               True -------------o/p
('a','b') > ('a', 4)           TypeError ---------------- string and interger are never comparission

set()==set()    True
{-1,2,1} > {5,3,'a'}        False-----------o/p its unpredict o/p value it's some time False , True, TypeError
{1,2,3} > {2,3}               True ----------- o/p

{'a':44} > {'a': 45} --- in dictonary < ,> <= ,>= are not support 
raceback (most recent call last):
  File "<pyshell#29>", line 1, in <module>
    {'a':44} > {'a': 45}
TypeError: '>' not supported between instances of 'dict' and 'dict'

{'a':44} == {'a': 44}    True ---------- o/p 
{'a':44} == {'a': 45}    False ----------------o/p
int(-9.4)   ------ -9   -----------------o/p




06-02-2024 ---------------------------


TypeCasting----------

converting one type of data to another type of data is called typecasting.

INT FUNCTION-

 default value of integer is--
print(int(0)) ---- 0 
******   IN int data type its change's only in [ float, bool , string(but it's only integer) ]
int('123')  -------- 123
int('123.4') ----------- in int only change int value(whose value are base 10) 
int([1,2,3])  ----- TypeError because data collection value never convert data Type
int('abcd') ----- Traceback (most recent call last):
  File "<pyshell#0>", line 1, in <module>
    int('abcd')
ValueError: invalid literal for int() with base 10: 'abcd'
int({1:3}} ----- TypeError


FLOAT FUNCTION--

float() --- 0.0
float(True) ------ 1.0
float(3)   ------ 3.0
float(9+8j) ----------- Traceback (most recent call last):
  File "<pyshell#19>", line 1, in <module>
    float(4+8j)
TypeError: float() argument must be a string or a real number, not 'complex'
IN Float data type are TypeError because data collection value never convert data Type
IN Float data type its change's only in [ int, bool , string(but it's only integer) ]


BOOL FUNCTION --

bool() -------- False
bool(8+8j) --------------- True
bool(0+0j)   --------- False
IN bool are value are change data type


COMPLEX FUNCTION ---


 complex()   ------oj
complex('3')   ------ 3+0j
complex('3','3') ----------- Traceback (most recent call last):
  File "<pyshell#20>", line 1, in <module>
    complex('3','3')
TypeError: complex() can't take second arg if first is a string

complex( 2+5j ,5+6j) ------------------- (-4+10j)
complex(8,9) ------------- 8+9J 


STRING FUNCTION


str()--- ''
str(4)   -------'4'
len(5678) ------ TypeError int has no len()
len(str(4.78)) ------------- 4
********** str(True)        ----------- 'True'
********** str(False) -----------------  'False'
str([5,8]) ----------- '[5,8]' -- 5
len(str({5,3,2}))  ---------- 9
len(str({5:90,3:None,3:'abc',4:45})) -------- 24


LIST FUNCTION ----\

list()           --- []
list(5) -------- int not iterable
list(True)     ------ error
list('True') ---------['T','r','u','e']
list(4+8j)        -  ------------- complex not iterable

list(('abc',4,2,True)) ----------- ['abc',4,1,True]
list({'abc',4,2,True}) --------------
list({''abc':[1,3,4],4:100,1:222,True:False}) ------------- ['abc', 4, 1]




TUPLE FUNCTION ---------


tuple() -------- ()
tuple(6) ------------------------- int not iterable
tuple('1234') --------- ('1','2','3','4')
tuple('1') ---------------- ('1',)


SET FUNCTION ----


 set(67) ---------- int not iterable
set('abdkdsl') --------------- {'a','b','d',k','d','s',1}
set([9,4,'a'.{'a' :45}] -------------------- TYpeError unhashaable Type 'dict'
set([9,3,'a']) ------------------- {9,'a',3}


DICT FUNCTION ------

dict() ------------------ {}
dict(10) ----------------- int not iterable
dict('ab') ---------------------- Traceback (most recent call last):
  File "<pyshell#39>", line 1, in <module>
    dict('ab')
ValueError: dictionary update sequence element #0 has length 1; 2 is required
dict(('ab','12')) ------------------------- {'a':'1' ,'b':'2'}
dict(['12']) -------------------- {'1':'2'}
dict({'12',[8,9]}) -------------  TypeError unhashable type
dict({'12',(8,9)}) ---------- 8:9 ,'1':'2'




07-02-2024---------------

dict([1,3]) ------------------- Traceback (most recent call last):
  File "<pyshell#0>", line 1, in <module>
    dict([1,3])
TypeError: cannot convert dictionary update sequence element #0 to a sequence




BUILT-IN FINCTION »»»»»»»»»»»»»»»»


Under the string input method --




UPPER--→→→→→→→

s='python' ------------    PYTHON--o/p, after print(b) --- python same of first one because str is immutable data type
- upper method converts all the char in to  upper cases
- return type of upper method is String

examples--

s='asalk akd;'
e=s.upper()
print(e)   ------------------------ ASALK AKD;
print(type(e))  ------------------------ <class 'str'>
print(s)   ---------------------------------------- asalk akd;

LOWER →→→→→→→→→→

Here it's convert upper cases to lower cases 

a='SANNY GUPTA'
print(a.lower()) ---------------------- sanny -- o/p



SWAPCASE →→→→→→→→→→

Swapcase are convert upper case to lower case and lower case to upper case.

a='skkAKSKKA'
print(a.swapcase())-------------------------- SKKakskka
print(a.swapcase(),type(a))  -----------------------  SKKakskka <class 'str'> 


TITILE →→→→→→→→→→

title method is converts first char of every words in to upper cases remaining are lower cases

print(a.title())  -------------------------- Sdfsd Sann Dkkd 
a='we Sanny GEt'    print(a.title()) ----------------------- We Sanny Get
print(a.title(),type(a))  -----------------------We Sanny Get <class 'str'>



CAPITALIZE →→→→→→→→→→ 

it's converts first char of entire string in upper otherwise in lower cases

s=s='Asss KADK SDJKJ SKDJJDF KASFJJL ASJF JSAKJLSJ '
print(s.capitalize()) --------------------- Asss kadk sdjkj skdjjdf kasfjjl asjf jsakjlsj 



 SPLIT →→→→→→→→→→ 
 
-  split is going to split the string according to the given deliminator
-  Given arrgument inside split function is not mandatory , 
-  if no arrugument  given space is consider as deliminator
-  split function return LIST

s='hell hel hello'  print(s.split())  --------------['hell', 'hel', 'hello']
  print(s.split('e',1)) -------------------['h', 'll hel hello']
  print(s.split('e',3)) --------------------- ['h', 'll h', 'l h', 'llo']
a='hello world'     print(a.split('l')) --------------------= ['he', '', 'o wor', 'd']
a='practice otherwise moye moye'    print(a.split()) ---------------------------------- ['practice', 'otherwise', 'moye', 'moye']
print(a.split('e')) ----------------------['practic', ' oth', 'rwis', ' moy', ' moy', '']
print(a.split('r')) -------------------------- ['p', 'actice othe', 'wise moye moye']
print(a.split('q')) -------------------------------- these word are not present so, same input are print as output form.




08-02-2024-----------------------


RELACE →→→→→→→→→→

Rpelace method , it replace the old sub string to new sub string
if the sub string is present then replaced happened otherwise not
Return type of replace is String
After replacing old string remains same

s='Thursday' 
s.replace(arg,arg2) --- (old, new)
a='we ae sks skd' ----- print(a.replace(' ','_',2))------------------------------we_ae_sks skd
print(a.replace('q','5')) ------------------- same the input value 



ISALPHA  →→→→→→→→→→

isalpha()- This is check is all char is my given string all alpha or not
If every char is an alpha then is alpha() method will give you a Boolean Value otherwise False


s='sdfals;'--------------print(s.isalpha())---------------------------False




ISDIGIT →→→→→→→→→→

isdigit() --  in isdigit() here the check in string total value  are int or not 
  if only integer is present then return True ,otherwise False.

-- a='dsd566' ---------print(a.isdigit())-----------------------False

print(a.isdigit('5'))
Traceback (most recent call last):
  File "<pyshell#37>", line 1, in <module>
    print(a.isdigit('5'))
TypeError: str.isdigit() takes no arguments (1 given)

-- s='3456' ----------print(s.digit()) ------------------------ True




ISALNUM →→→→→→→→→→

isalnum() --   is isalnum() checking , if in string present number and int then return True, otherwise False.

a='dsd566' ------print(a.isalnum())------------------True
a='5678as('------print(a.isalnum())-------------------False


INDEX →→→→→→→→→→

index() -- it gives the index value of the first accurance of sub-string 
 Return type of index method is Integer 


s='Hello world' 
 
print(s.index()) --------------------- TypeError [ atleast 1 argument gievn]
print(s.index('l')) ----------------   2
print(s.index('l',4)) --------------   9
print(s.index('l',0,3)) ---------------  2
print(s.index('l',3,3)) ------------------- starting index are also less than the ending index 
Traceback (most recent call last):
  File "<pyshell#46>", line 1, in <module>
    print(s.index('l',3,3))
ValueError: substring not found
print(s.index('o',-9,-1)) ---------------------- 4

s='Looking like a wow' ---- need to print 3rd occurance of 'o' --------------s.index('o',s.index('o',s.index('o')+1)+1)


 

09-02-2024 -----------




s='python is very good'  find 4 occurance of '0' ------------- s.index('o',s.index('o',s.index('o',s.index('o')+1)+1)+1)
                                                                                                       4

FIND  →→→→→→→→→→


  if the sub string is not present in string it's print [-1]
 It return type method is  integer 
in find method it works as index method but here we never get TypeError it's just print [-1] 


s.index(' ') ------------------------ 6 
s.find(' ') -------------------------  6
s.index('  ') --------------- Traceback (most recent call last):
  File "<pyshell#8>", line 1, in <module>
    s.index('  ')
ValueError: substring not found
s.find('  ') ---------------------------- -1



RINDEX ----------


s='we are developers' ------------ print all occurance 'e'
s.rindex('e') ----
s.rindex('e',0,s.rindex('e')) ------
s.rindex('e',0,s.rindex('e',0,s.rindex('e'))) ------------
 s.rindex('e',0,s.rindex('e',0,s.rindex('e',0,s.rindex('e',o,s.rindex('e'))))) --------------



RFIND  →→→→→→→→→→  

 rfind give last accurance of sub strig if present otherwise it -1

s.rfind('E') -------------- -1
s.rfind('e') ---------------- 14


FORMAT →→→→→→→→→→ 

using placeholders we can print a string in a meainingfull way 
string with placeholder . format with arguments     '{} {}'.format(arg,arg2)
name='sanny'
gender='boy'
print('{} is  very good {}'.format(name,gender))

name='rahul'
gender='boy'
print('{} is good {}'.format(name,gender))----------------- rahul is good boy
name1='harshit'
print('{} is good but {} are not good {}'.format(name,name1,gender))--------------rahul is good but harshit are not good boy



--- BY using index

print('{2} is s dk {0} akdj {1}'.format(name,gender,name1))-----------------harshit is s dk rahul akdj boy



---- By using any variable

print('{a} is good but {b} are not good {c}'.format(a=name,b=name1,c=gender))------------rahul is good but harshit are not good boy



USING FSTRING fstring()  →→→→→→→→→→ 


var1=3
var2=4
print(f'{var1} *{var2} ={var1*var2}') ---------------------------- 3*4=12
print(f'var1*var2 =var1*var2') --------------------- var1*var2=var1*var2

print(f'{name} is good but {name1} aare not{gender}')---------------------- rahul is good but harshit aare notboy



STRIP  strip() →→→→→→→→→→  

This method removes unwanted sub string given as an arguments
 Removes only at the starting and ending of the string
 it only one arguments are allow

s='amit is boy' --------- print(s.strip()) -------------  amit is boy
print(s.strip('y')) ------------ amit is bo
print(s.strip('t',2)) -------------- Error  one argument , got 2 argument


LSTRIP lstrip() --- in lstrip() just remove left side 
s='adklsdfjkaa'
print(s.lstrip('a')) -------------- dklsdgjkaa


RSTRIP lstrip() --- in rstrip() just remove right side 
s='adklsdfjkaa'
print(s.rstrip('a')) -------------- adklsdgjk



10-02-2024


COUNT →→→→→→→→→→  

Return the counts of sub string given as an argumants
if sub string is not present then conunt method gives 0(zero)

a='we are smart-students'
print(a.count('s'))
3
print(a.count())
Traceback (most recent call last):
  File "<pyshell#14>", line 1, in <module>
    print(a.count())
TypeError: count() takes at least 1 argument (0 given)
print(a.count('s','r'))
Traceback (most recent call last):
  File "<pyshell#15>", line 1, in <module>
    print(a.count('s','r'))
TypeError: slice indices must be integers or None or have an __index__ method



STARTSWITH ---  

check the sub stirng is present strating of string  or not 
if present  Return True , otherwise False.


ENDSWITH ----- 

check the sub stirng is present ending of string  or not 
if present  Return True , otherwise False.

a ---------------------- 'we are smart-students'
print(a.startswith('we'))---------------------True
print(a.endswith('st'))-------------------------------False



in-Build in LIST------

       TO ADD                             TO REMOVE  

       append                              remove
       insert                               pop
       extend                               clear

Append --- append add the element at the end of list
 Return type of append is None

a=[4,9,0]------------------- print(a.append(9))----------------   None ----o/p
print(a)------------- [4, 9, 0, 9]
a=[]------------------- print(a.append('av')) ------------------   None
print(a)-------------------['av']



INSERT ---------- It add the elements at given particular given index position 
 Declare by --- var.insert(index,val) 
Return type of insert is None


print(a.insert(0,5)) ---------------- None
print(a) ----------------------------- [5,'av']
a=[5,9,0,4]------------ print(a.insert(100,100))-------------------- None
a------------------[5, 9, 0, 4, 100]
print(a.insert(4,'abc'))---------------------- None
a---------------------- [5, 9, 0, 4, 'abc', 100]


EXTEND -------  This method can add multiple elements at end of the list
if extend method can only collection data type
var.extend(collection data type val)
 Retrun data type is None

name=[4]
print(name.extend(5))
Traceback (most recent call last):
  File "<pyshell#34>", line 1, in <module>
    print(name.extend(5))
TypeError: 'int' object is not iterable

print(name.extend('4'))-------------------- None
name-----------------[4, '4']
print(name.extend('56'))------------------ None
name----------------------- [4, '4', '5', '6']
print(name.extend({1,True,0,False,-1,0}))----------------------------- None
name--------------------------------------- [4, '4', '5', '6', 0, 1, -1]



REMOVE ------------ it remove the first occurance of the given value in remove() method
 if given value is not present then remove() method give ValueError
var.remove(val)

s=[8,9,2]----------------- print(s.remove(2))---------------------------- None
s------[8, 9]
print(s.remove(99))
Traceback (most recent call last):
  File "<pyshell#52>", line 1, in <module>
    print(s.remove(99))
ValueError: list.remove(x): x not in list

print(s.remove())
Traceback (most recent call last):
  File "<pyshell#53>", line 1, in <module>
    print(s.remove())
TypeError: list.remove() takes exactly one argument (0 given)



POP   pop() --------- it remove and returns the value given as an index in pop
 given arguments are not mandoatry if no argument is given it remove and returns last elememts
if index is not present it through index error
Return data type is Removed value

a=[4,7,8,'ad',[4,8]]-------------------------- print(a.pop())----------------------  [4, 8]
print(a.pop(1))------------------ 7
a--------------------- [4, 8, 'ad']
print(a.pop(2,1))
   
Traceback (most recent call last):
  File "<pyshell#60>", line 1, in <module>
    print(a.pop(2,1))
TypeError: pop expected at most 1 argument, got 2


CLEAR  clear() ----------- it remove all the element  in the list
var.clear()
Return type is None

a=[5,9,0,[9,7]] -----------------------  print(a.clear())  ------   None
a----------------- []



11-02-2024------------



COUNT    count() ------

l=[4,8,2,2,3]---------------- print(a.count(l))------------------------ 0
print(a.count(2))-------------------------- 0
print(l.count(2))---------------------------------- 2
print(l.count())
Traceback (most recent call last):
  File "<pyshell#27>", line 1, in <module>
    print(l.count())
TypeError: list.count() takes exactly one argument (0 given)


index   index() ---- 

l=[4,8,2,2,3]
print(l.index())
Traceback (most recent call last):
  File "<pyshell#29>", line 1, in <module>
    print(l.index())
TypeError: index expected at least 1 argument, got 0
print(l.index(2,2))-------------------------------- 2
print(l.index(100,2))
Traceback (most recent call last):
  File "<pyshell#31>", line 1, in <module>
    print(l.index(100,2))
ValueError: 100 is not in list



COPY   copy() -------- shallow copy ca be achieve by using copy method
 copy method creates the same data in a new memory location 
 But the address of elements incollection data type are same

a=[3,7,1,0]
b=a.copy()
print(a,b)----------------------------------- [3, 7.1, 0] [3, 7.1, 0]
print(id(a), id(b))--------------------------------------------1729311276736 1729311332160
print(id(a[0]) ,id(b[0]))-----------140737165277688 140737165277688 



JOIN  join() -------- This method connects the strings present in the list with a glue char
 glue.char.join(var)
  Return type of join is String

a=[3,7.1,0]--------------------------------- print(' '.join(a))
Traceback (most recent call last):
  File "<pyshell#38>", line 1, in <module>
    print(' '.join(a))
TypeError: sequence item 0: expected str instance, int found


a=['4','sa','5','99']-------------------------- print('_'.join(a))------------------------------------- 4_sa_5_99
print('res'.join(a))--------------------------------- 4ressares5res99




MAX  max() --------  It return height value  present in collection data type
a=[5,8,0]---------------------  print(max(a))------------------------------- 8
print(min(a))-------------- 0

MIN  min() ---------- It return lowest value  present in collection data type


SORT  sort() ---------- It arrange the elememts in ascending order by default ,another given argument are not neccessary 
 var.sort() ----  print ascendign order
 var.sort(reverse=True) ----- print descending order
 Return data type is None


a=[4,32,0,-5,-56,256]------------------------- print(a.sort())--------------------------- None
a----------------[-56, -5, 0, 4, 32, 256]
print(a.sort(reverse=True))---------------None
a------------------------------------------------ [256, 32, 4, 0, -5, -56]
a=['4','sa','5','99',9]
print(a.sort())
Traceback (most recent call last):
  File "<pyshell#56>", line 1, in <module>
    print(a.sort())
TypeError: '<' not supported between instances of 'int' and 'str



SORTED  sorted() ----------- It creates a new Memory with sorted elements 
    Return data type is List 
sorted(arg1) , By default it print ascending order 

a=['4','sa','5','99']------------------------------ print(sorted(a))------------------------- ['4', '5', '99', 'sa']
a--------------------['4', 'sa', '5', '99']
print(sorted(a,reverse=True))---------------------- ['sa', '99', '5', '4']



REVERSE   reverse() ----------- Return type of reverse is None 
 It changes the order of elements in exiting memory 

a=[7,0,6,'ak;']------------------------------- print(a.reverse())---------------------------------- None
a--------------------------- ['ak;', 6, 0, 7]



12-02-2024 -----------


IN-bulid method in tuple →→→→→→→→→→→



t=1,2,3,7,3------------------------------- print(type(t))-------------------------- <class 'tuple'>
sorted(t)----------------- [1, 2, 3, 3, 7]
sorted(t,reverse=True)----------------------- [7, 3, 3, 2, 1]
t ------------------- (1, 2, 3, 7, 3)
print(t.index(7))-------------------- 3
print(t.index(90))
Traceback (most recent call last):
  File "<pyshell#6>", line 1, in <module>
    print(t.index(90))
ValueError: tuple.index(x): x not in tuple

print(t.count(3))------------------------------------------------- 2
print(t.count(99))--------------------- 0
print(t.count())----------
Traceback (most recent call last):
  File "<pyshell#9>", line 1, in <module>
    print(t.count())
TypeError: tuple.count() takes exactly one argument (0 given)




ADD  add() ---------------
 None is return type of add method
 it adds the elements to the existing set 
 we can not predict the position of added elemet
 we can add only immutabble data value

s=set()----------------- s.add('12ab')------------------- print(s)--------------------------- {'12ab'}
print(s.add(5,2))
Traceback (most recent call last):
  File "<pyshell#14>", line 1, in <module>
    print(s.add(5,2))
TypeError: set.add() takes exactly one argument (2 given)
print(s.add(True))----------------- None ------------------ s---------------------- {'12ab', True}
s.add(4)-------------------------- s------------------------------- {'12ab', True, 4}
s.add([4,7])
Traceback (most recent call last):
  File "<pyshell#21>", line 1, in <module>
    s.add([4,7])
TypeError: unhashable type: 'list'
s.add(7+8j)----------------------- s---------------------- {'12ab', True, 4, (7+8j)}



UPDATA uptade() -------
 var.updaate(arg)  arg- CDT(immutale value, Single data type) 
 update method can add multiple data  type given as a CDT
 In the  case of Dict update method will add only keys of sets 
 order can not be predicted 

s={5}---------------------   s.update(6)
Traceback (most recent call last):
  File "<pyshell#25>", line 1, in <module>
s.update(6)
TypeError: 'int' object is not iterable
s.update([4,2,9,11])---------------- s--------------- {2, 4, 5, 9, 11}
print(s.update({'a':56,'b':10}))-------------- None---------------- s--------------------- {2, 4, 5, 9, 'a', 11, 'b'}
print(s.update(('akfjb')))----------------- None----------- s----------------{2, 'k', 4, 5, 9, 'a', 11, 'f', 'j', 'b'}
a={10,20}------------------- a.add('13')------------------- a----------------------{10, '13', 20}
a.update('453')----------------- a---------------------- {'4', 10, '13', '5', 20, '3'}
s.update([4,9,0])---------------------- s-------------------- {0, 9, 20, 4}
a.update([9,7,9])----------------- a------------------------------------------{'4', 7, 9, 10, '13', '5', 20, '3'}f



REMOVE  remove() --------

 It remove the element given as an argument 
 If element is present inside it remove the element , if element is not present in inside it throgh keyError
 Return type remove method is None.

s={'a',1,4,3,'b',True,False,0,450}---------------------- s.remove(3)---------------------- s----------{False, 1, 450, 4, 'b', 'a'}
s.remove('ab')
Traceback (most recent call last):
  File "<pyshell#48>", line 1, in <module>
    s.remove('ab')
KeyError: 'ab'


DISCARD   discard() --------
 if the element are not present inside the element it print same the previous o/p

s.discard(1)------------------- s------------------- {False, 450, 4, 'b', 'a'}
s.discard(99)--------------- s------------------- {False, 450, 4, 'b', 'a'}


POP pop()  ----------------
 it remove and return random elements from the set
 you should not give any argument
 It return the remove value

a={19,9,False,8,'34',0}---------------- a.pop()---------------------- False
a.pop()----------------- 19
a.pop()------------ 8
a-------------------------{9, '34'}
a.pop(50)
Traceback (most recent call last):
  File "<pyshell#58>", line 1, in <module>
    a.pop(50)
TypeError: set.pop() takes no arguments (1 given) 



INTERSECTION intersection()--------------

It gives the comman elements of two sets.
Return type 
it create one memory

a={10,9,8}
b={8}-------------------------- print(a.intersection(b))



UNIION  union() ---------

It combine both set and gives uniqe set(value)

print(a.union(b))------------{8, 9, 10}



13-02-2024 --------------------------------------- 

DIFFERENCE  difference() -----  Return type of difference method is Set



a={4,6,1}
b={5,3,1} ---------------- a-b------------------ {4, 6}
a.difference(b)--------- {4, 6}
a.difference(a)--------------------- set()
a.difference()---------- {1, 4, 6}
b.difference()--------------- {1, 3, 5}


SUBSET  subset()-----

a={1,5,6}
b={6}------------------- b.issubset(a)---------------------------- True
b.issubset(b)------------- True
a.issubset(b)--------------------------- False


CLAER clear()------ 

a={7,'asd',9,1,True}--------------- a.clear()  --------------------- a----------------------------- set()




IN-BUILD IN DICT →→→→→→→→→→→→→


- To add single key value pair
var[key]=value
s=dict()-------------- s------------------------- {}
s['d']='thursday'--------------------- s----------------------- {'d': 'thursday'}
s['next']='wednesday'--------------- s--------------- {'d': 'thursday', 'next': 'wednesday'}
s['d']='sunday'---------------- s----------------- {'d': 'sunday', 'next': 'wednesday'}


UPDATE update() ---------
 update method add mutiple key value pair in dict
 update method takes one mandatory arguments that is collection data type
 var.update(arg) -- arg ----- [list,tuple,set,dict] len of elements insisde is 2
 Return type of update is None



s---- {'d': 'sunday', 'next': 'wednesday'}
s.update('1234')----
Traceback (most recent call last):
  File "<pyshell#37>", line 1, in <module>
s.update('1234')
ValueError: dictionary update sequence element #0 has length 1; 2 is required

s.update('12')----
Traceback (most recent call last):
  File "<pyshell#38>", line 1, in <module>
s.update('12')
ValueError: dictionary update sequence element #0 has length 1; 2 is required

s.update(['12'])------------ s  ------------  {'d': 'sunday', 'next': 'wednesday', '1': '2'}

s.update(['ab',{'2':45,'3':19}])------------ s  ------------------ {'d': 'sunday', 'next': 'wednesday', '1': '2', 'a': 'b', '2': '3'}

s={}------------------- s.update(('76'))
 Traceback (most recent call last):
  File "<pyshell#44>", line 1, in <module>
s.update(('76'))
ValueError: dictionary update sequence element #0 has length 1; 2 is required

s.update(('56',{7,8}))---------------------- s------------------------ {'5': '6', 8: 7}

s.update(('56',([1,2],[3,4]))) ------  
   Traceback (most recent call last):
  File "<pyshell#49>", line 1, in <module>
    s.update(('56',([1,2],[3,4])))
TypeError: unhashable type: 'list'



GET get() ---------

Get method takes one mandatory key
it Return the value of particular key
if the key is present in dict then get() method gives value otherwise it gives default value
if default value is not given then get method gives None as a value 
var.get(arg)
var.get(arg,arg1) arg-key, arg1-default value

a={'name':'unknows','age':'secrete','salary':'unlimited'}   
print(a.get('name'))---------- unknows

print(a.get('gender','complicated'))--------------- complicated

print(a.get('month'))------------------ None



SETDEFAULT  setdefault() ------------

if the key is present in dict then setdefault() method gives value 
if not present then default value is give None 
After that it add the dic and print in same dic
 


print(a.setdefault('month'))----------- None
a----------   
{'name': 'unknows', 'age': 'secrete', 'salary': 'unlimited', 'month': None}

print(a.setdefault('staus','single'))---------------- single-------------- a
   == {'name': 'unknows', 'age': 'secrete', 'salary': 'unlimited', 'month': None, 'staus': 'single'}



KEYS  keys() ------
This method returns all the keys in form of list
var.keys()
Return type of keys is LIST

print(a.keys())------------------------------ dict_keys(['name', 'age', 'salary', 'month', 'staus'])



VALUES values() ---
This method returns all the value in form of list
var.values()
Return type of keys is LIST


a.values()----------------- dict_values(['unknows', 'secrete', 'unlimited', None, 'single'])


ITEMS items() ----
This method returns all the key and value in form of list
var.items()
Return type of keys is LIST


a.items()  ---------  dict_items([('name', 'unknows'), ('age', 'secrete'), ('salary', 'unlimited'), ('month', None), ('staus', 'single')])




14-02-2024 ----------------------------



POP pop () ------
 Pop method takes one arguments that is key
 it return  the respective value of the key and remove key value pair into dict
 var.pop(arg) -arg -key
 If the provided key not in dict pop method gives KeyError

a={'future':'builing','distraction':'might-be','future':'moye-moye'}---------------------------- a.pop()
Traceback (most recent call last):
  File "<pyshell#2>", line 1, in <module>
    a.pop()
TypeError: pop expected at least 1 argument, got 0

a.pop('distraction')----------------- 'might-be'

a-------------- {'future': 'moye-moye'}
a.pop('future')------------- 'moye-moye'
a.pop('present') -------------
Traceback (most recent call last):
  File "<pyshell#7>", line 1, in <module>
    a.pop('present')
KeyError: 'present'


POPITEAM popitem() -----------
 should not give any argu in popitem
 popitem return the last key:value pair in the form tuple and removes that key:value from dict 
 var.popitem()
Return type of popitem is tuple

a={'future':'builing','distraction':'might-be','life':'moye-moye'} ---------------- a.popitem() --------------('life', 'moye-moye')
a----------- {'future': 'builing', 'distraction': 'might-be'}
a.popitem()---------------- ('distraction', 'might-be')
a.popitem() -------------('future', 'builing')
a.popitem()-----------
 Traceback (most recent call last):
  File "<pyshell#17>", line 1, in <module>
    a.popitem()
KeyError: 'popitem(): dictionary is empty'


CLEAR  clear() ----
Return type is None 

a={'future':'builing','distraction':'might-be','life':'moye-moye'} ---------------- a.clear()
a ------------------- {}


 FROMKEYS  fromkeys() ----------
  fromkeys is used to give the comman value for all the keys 
  {}.fromkeys(arg) arg-- it should be CDT
  {} .format (arg ,arg1) arg - arg are CDT, arg1- can be single value
  If second argument is not given None will be considerd value of the key
  formkeys creates a New Memory with key:value pairs 
  
var='1234'
var1=399
var.fromkeys(var1)
Traceback (most recent call last):
  File "<pyshell#24>", line 1, in <module>
    var.fromkeys(var1)
AttributeError: 'str' object has no attribute 'fromkeys'

{}.fromkeys(var,var1)
{'1': 399, '2': 399, '3': 399, '4': 399}

var=1234
{}.fromkeys(var,var1)
Traceback (most recent call last):
  File "<pyshell#27>", line 1, in <module>
    {}.fromkeys(var,var1)
TypeError: 'int' object is not iterable

var=[5,7,8,9,0]
var1=420
{}.fromkeys(var,var1) ---------------- {5: 420, 7: 420, 8: 420, 9: 420, 0: 420}

var=[7,9,6,[5,6]]------------ {}.fromkeys(var,var1)
Traceback (most recent call last):
  File "<pyshell#32>", line 1, in <module>
    {}.fromkeys(var,var1)
TypeError: unhashable type: 'list'

{}.fromkeys((1,2,3,'a'))---------------------- {1: None, 2: None, 3: None, 'a': None}

{}.fromkeys({'a':56,'b':45},100)---------------- {'a': 100, 'b': 100}
a={} ---------- a.fromkeys('ab',[3,4,5]) ------------ {'a': [3, 4, 5], 'b': [3, 4, 5]}




ZIP zip() ----

Return type of zip() is zip object
zip() is used to make space to particular index positions for provided collection data type
zip is iteratorygffffffffffffffffffffffffffvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvv


k='abcd'
h='1234'
zip(k,h) ------------------ <zip object at 0x000001CE2BA36100>
tuple(zip(k,h)) ------------------ (('a', '1'), ('b', '2'), ('c', '3'), ('d', '4'))
a=[5,6,7,8]
zip(k,h,a) ------------------ <zip object at 0x000001CE2BA37040>
list(zip(k,h,a)) ----------------------- [('a', '1', 5), ('b', '2', 6), ('c', '3', 7), ('d', '4', 8)]
d='1234' ---------- zip(d) ------------ <zip object at 0x000001CE2BA372C0>
list(zip(d)) ------------ [('1',), ('2',), ('3',), ('4',)]
zip() ---------<zip object at 0x000001CE2BA376C0>
list(zip()) ------------------ [] 





15-02-2024 -------------------  Exam

16-02-2024 --------------- checking the copy


17-02-2024 -------------



COPY ----
  copy  can be achieve by using by assignment operator
  copy create a new object with the same address if we modify any value in a variable the other varible lso get affects 

var=[420,123,45]
print(var is copy)------ True
var[0]=840------------------- print(var,copy)---------------- [840, 123, 45] [840, 123, 45]


shallow copy -
 shallow copy can achieve by three way -

 using slicing
 in-built copy method
 copy method in copy module
 
shallow copy create a new memory but elements inside thr varibale address same
if we modify  any variable other varible will not affected

var=[10.20,30,40]------------- scopy=var[::]---------------- print(var is scopy)--------------False
var[2]=400--------- print(var,scopy)-------------[10.2, 30, 400] [10.2, 30, 40]
 

using in-built method---
 it create a new memory 
 if we modify  any variable other varible will not affected

var=[10,20,30,40]
 scopy=copy(var)
 print(var is scopy)
 var[3]=400
 print(var,scopy)
 
copy method in copy module --
 we have to import copy module in order to use copy method 
 import copy
 var=[10,20,30,40]
 scopy=copy.copy(var)
 print(var is scopy)  ----- false
 var[3]=400
 print(var,scopy)- [10,20,30,400] [10,20,30,40]


DEEP COPY   clone operator -----

deep copy achieved by using copy medule
deep copy create a new memory and further element present in the variable new memory has been created
 if modification is done on any variable other varibale not get affected

import copy
 var=[[4,5,6],[1,2,3]]
 dcopy=copy.deepcopy(var)
 print(var is dcopy)  ----- false
 var[0][1]=400
 print(var,scopy)- [[4,5,400],[1,2,3]] [[4,5,6],[1,2,3]]





19-02-2024 --------


CONDITINAL STATEMENTS -------(if,else,elif) 
mkdir -- cd -- code . --- py test.py

if (cond):     1 block for if
 → instruction

if(cond):   1 block for if-else 
  → instruction 
else:
  → instruction 


if(True):
→  print('hello')

print('program completed')

hello                             ----- o/p 
program completed


if(False):
    print('hello')
else:
    print('jeke')

print('program completed') 

jeke
program completed ----------- o/p 

write a program to check given no is Even or Odd ?

n=int(input('enter the number'))
if (n%2==0):
    print('Number is Even')
else:
    print('Number is Odd')


write a program to print height among two number ? 

a,b=4,7
if (a>b):
    print(' a is highest')
else:
    print('b is highest')


write a program to print height among three number ? 

a,b,c= 12,15,5
if (a>b):
    if(a>c):
        print('a is greter')
    else:
        print('c is greater')
else:
    if(b>c):
        print('b is greater')
    else:
        print('c is greater')


write a program to print height among four number ?

a,b,c,d =10,1,5,1
if(a>b):
    if(a>c):
        if(a>d):
            print('a is greater')
        else:
            print('d is greater')
    else:
        if(c>d):
            print('c is greater')
        else:
            print('d is greater')
       
else:
    if(b>c):
        if(b>d):
            print('b is grate')
        else:
            print('d is greateer')

    else:
        if(c>d):
            print('c is greate')
        else:
            pirnt('d is greater')


write a program to print height among three number ?
write a program to print height among four number ?
write a program to print height among five number ?

a,b,c=10,5,20
if a>b and a>c:
    print('a is large')
elif b>c:
    print('b is larger')
else:
    print('c is larger')

a,b,c,d =10,1,5,1
if a>b and a>c and a>d:
    print('a is greater')
elif  b>c and b>d:
    print('b is greater')
elif  c>d:
    print('c is greater')
else:
    print('d is greater')


a,b,c,d,e =10,1,5,1,15
if a>b and a>c and a>d and a>e:
    print('a is greater')
elif  b>c and b>d and b>e:
    print('b is greater')
elif  c>d and c>e:
    print('c is greater')
elif d>e:
    print('d is greater')
else:
    print('e is greater')


 20-02-2024 ----------


When given condition is True control enters in if block
When given condition is False control enters Else block
For using Else ,if is mondatary
we can use multiple elif 
To use elif , if is mondataory
For elif else is not mandatary






Ternary Operator ----


year=2300
print('leap' if((year%400==0) or (year%4==0 and year%100!=0)) else 'not leap year')




21-02-2024 -------------------- 

















 
