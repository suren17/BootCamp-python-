'''
Hi there, today we are going to
review all the materials you
have learned more meticulously.
'''

# operators
'''
< : less than
> : bigger than
<= : less than or equal to 
>= : bigger than or equal to 
== : equal to
!= : not equal to
or : union
and : intersection 
in : checks for membership
not : contradiction
is : checks the type
// : floored quotient of x // y
% : returns the remainder
* : x * y will multiply x by y
/ : x / y will divide x by y
** : x**y is equivalent to x^y
'''

# Data Types
'''
String(str): a string representation usually in double quotation
Integers(int): an arbitrary integer
Float(float): an arbitrary number with decimals
Boolean(bool): A binary value mainly True or False
List(list): an array of objects in square brackets [] ---mutable
Tuple(tuple): an array of objects in parenthesis () --immutable
Dictionary(dict): {A:B} an array of object's where A(key) is mapped to B in brackets {} ---mutable
'''
# examples

# strings
a_str = "Hello_world"

# ints
b_int = 10

# Float
c_float = 10.01

# boolean
d_bool = True

# list
e_list = [a_str, b_int, c_float, d_bool]

# tuple
f_tuple = (a_str, b_int, c_float, d_bool, e_list)

# dictionary
g_dict = {a_str: b_int, c_float: d_bool, "list": e_list, "tuple": f_tuple, "dictionary": {1: 2}}


your_names = []

# for loop
for i in range(3):
    your_names.append(input("insert your name: "))

index = 0

# while loop
while index < len(your_names):
    print("Hello, {}".format(your_names[index]))
    index += 1
print("My name is Suren, welcome to introduction to intermediate Python\n" +
      "I will be your instructor starting from this week.")
