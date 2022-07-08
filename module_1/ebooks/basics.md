# Introduction To Python Programming

## [1] Python Data Types

### Fundamental data types in Python
These are the data types that are core to the language - we can get most of our work done using these data types and represent almost anything with these.

The following are the fundamental data types in Python

#### `int`
This represents the integer data type. It is used to hold positive and negative numbers without any fractional part. For example **23**, **0**, **-100** etc.


#### `float`
This represents the floating point data type. A floating point data type is a number with fractional part. The fractional part can even be zero. For example **0.01**, **23.0**, **-0.5** etc.

#### `bool`
This represents the boolean data type. A boolean data type is one that can either be **True** or **False** and these are the only values allowed.


#### `str`
This represents the string data type. A string is just a sequence of characters. These characters can be alphabets, numbers, special characters or any combinations of them. For example **hello world**, **23** (note that here 23 is represented as a string, not an integer), **$&Gh!** etc.


#### `list`
A list represents a sequence of items stored one after the other. These items may or may not be of the same data type. For example **[10, 20, 30]** is a Python list. **[30.123, False, 10, "Hello"]** is also a Python list (in this case, the list holds items of different data types).


#### `tuple`
A tuple is a collection of objects which is ordered and immutable. Tuples are Python sequences just like lists. For example **(1, 2, 4, 10)** is a tuple. 


#### `set`
A set is a collection of unordered items. Each element in a set is unique, immutable and if duplicate elements are added, they automatically get removed. The set itself is however mutable. For example **{"Monday", "Tuesday", "Wednesday"}** is a set.

#### `dictionary`
A dictionary is used to store data in key:value pairs and is an *ordered* collection of items that are mutable but unique. Duplicates are not allowed. For example **{'name': 'anish', 'age': 23}** is a dictionary.

**NOTE**

As of Python **3.7** dictionaries are ordered. In Python **3.6** and earlier, they are unordered.

                                        PYTHON_DATA_TYPES
                                                |
                                                |
                                                |
                           ----------------------------------------------
                          |            |           |           |         |
                          |            |           |           |         |
                          |            |           |           |         |
                       NUMERIC    DICTIONARY    BOOLEAN       SET     SEQUENCE
                          |                                              |
                          |                                              |
                          |                                              |
                  ----------------                                ----------------
                 |        |       |                              |       |        | 
                 |        |       |                              |       |        | 
                 |        |       |                              |       |        |
              INTEGER   FLOAT  COMPLEX                        STRINGS   LIST    TUPLE

### Non Fundamental Data Types
These are the data types which are not core to the programming language but are very useful to solve certain problems/use cases. These data types are either built on top of the fundamental data types or mimic them with additional features.

#### `class`
Class is a custom data type - which means that we can use any combination of the fundamental data types to create the class data types. Note that two or more classes can also be combined to create a new data type. 

#### `None` 
This special data type in Python as it represents absence of data.

### Specialized Data Types
These are the data types that are derived externally from libraries, modules etc. These data types are not supported by Python natively so in order to use them we need to install the required module first. For example, the **dataframe** is a specialized data type that is provided from the **Pandas** library.

### Important Links

- [Data Types](https://realpython.com/python-data-types/)
- [Advanced Data Types](https://docs.python.org/3.8/library/datatypes.html)

## [1] Variables

Variables hold data that can be used in our program. At a deeper level, they contain the address of the memory location where the data is actually stored in memory.  

Consider the memory (RAM) snapshot below with memory locations of `10`, `20`, `30` and so on...  


                              10   20   30   40   50   60
                            |    |    |    |    |    |    |
                            |.   |.   |7.2 |.   |.   |.   |
                            

In the above example the data **7.2** is stored in the memory location `30` and assume there is a varible **a** that contains the data **7.2**.  
What it means is **a** actually contains the memory location `30` and when the program uses this variable it will know to look at the memory location `30` to access the data **7.2**  


A variable is created by specifying some characters followed by the *equals* symbol `=` followed by the data. The syntax is `a = 30`  
                        
In Python terms, this is also called as **defining a variable**. The proccess of assigning a value to a variable is called **binding**. In the above example, we can say that the number **30** is _bound_ to the variable `a`. Once the binding is complete, we say that the variable `a` has been **defined**


```python
# Python variables names with multiple words are separated by underscore character "_" 
# This style is called snake-case
# Variables which change values are denoted with small case characters
var = True
some_variable = 20
another_variable = "hello world"

print(var)
print(some_variable)
print(another_variable)
```

    True
    20
    hello world



```python
# Values inside variables can be updated anytime we want
var = False
some_variable = "New Value"
another_variable = 67.88

print(var)
print(some_variable)
print(another_variable)
```

    False
    New Value
    67.88



```python
# Variables which do not change their value during the course of execution are denoted with capital case characters
PI = 3.141
H = 6.626 * 10e-34

print(PI)
print(H)
```

    3.141
    6.626000000000001e-33



```python
# Variables denoted as constants can also be updated dynamically
PI = 5.6666
H = 2000

print(PI)
print(H)
```

    5.6666
    2000



```python
# Variable multi definition
# Define multiple variables simultaneously
a, b, c = 10, 20, 30

print(a)
print(b)
print(c)

# Binding more or less number of values to the variables leads to error
# a, b, c = 10, 20
# x, y, z = 100, 200, 300, 400
```

    10
    20
    30


### Keywords  

There are some reserved words which convey a special meaning to the Python compiler. These words are called as **keywords** and cannot be used for anything other than the purpose they are intended for. Examples of these words are:  

`print()`  `def()` `if` `elif` `list` etc..

It therefore goes without saying that these words cannot be used to define variables. For example `print = 23` or `def = "hello"` are not allowed.

### Type

We can check the data type of a variable with the keyword `type()`. It tells us what is the nature of the data that is stored in a variable. For example `type(23)` will give us `int` and `type("hello")` will give us `str`


```python
# Data of type 'str'
print(type("hello"))

# Data of type 'int'
print(type(23))

# Data of type 'float'
print(type(56.23))

# Data of type 'bool'
print(type(False))

# Data of type 'list'
print(type([]))

# Data of type 'dict'
print(type({}))
```

    <class 'str'>
    <class 'int'>
    <class 'float'>
    <class 'bool'>
    <class 'list'>
    <class 'dict'>


### Memory Address Of A Variable

As mentioned earlier, every variable we define gets stored in the memory under a particular location. This location is called the **address** of the variable and is used by Python to identify it's location in memory when the data inside the variable is used.  

We can check for the address of a variable using the **id()** keyword. The syntax is `id(some_variable)`. Remember, if two or more variables have the same id, then it means they are pointing to the same location in memory.  

However, if two or more variables have the same data, it does not mean that they will have the same address in memory.


```python
a = 4
b = 4
c = "string"
d = 45.0
e = "string"
f = 45.0

print("a:", a)
print("id(a)", id(a))
print()

print("b:", b) 
print("id(b)", id(b))
print()

print("c:", c)
print("id(c)", id(c))
print()


print("d:", d)
print("id(d)", id(d))
print()

print("e:", e)
print("id(e)", id(e))
print()

print("f:", f)
print("id(f)", id(f))
print()
```

    a: 4
    id(a) 4337591936
    
    b: 4
    id(b) 4337591936
    
    c: string
    id(c) 4342214128
    
    d: 45.0
    id(d) 4401023408
    
    e: string
    id(e) 4342214128
    
    f: 45.0
    id(f) 4401022576
    


### Important Links

- [Python Variables](https://realpython.com/python-variables/)

## [2] Numbers

There are two types of numeric data types supported by Python - **int** (represents integers) and **float** (represents decimal values). It is possible to perform mathematical operations on numeric data types using BODMAS rules. 


```python
# This is an integer value
age = 25
print(age)
print(type(age)) # The datatype of the variable

print()

# This is a floating point value
bmi = 27.825
print(bmi)
print(type(bmi)) # The datatype of the variable
```


```python
# A simple mathematical expression; resulting value will be an integer
result_1 = 45 * 12 - 56 * 8 + 2
print(result_1)
```

    94



```python
# A simple mathematical expression; the resulting value will be a decimal (because of the division operation)
result_2 = 45 * 12 - 56 / 8 + 2
print(result_2)
```

    535.0



```python
t1 = 20
t2 = -30
t3 = 100
t4 = 0.25
t5 = 0.001

# A mathematical expression from variables
expr_1 = ((t1 + t2 + t3) / (t4 * 25)) / t5
print(expr_1)

# Combining the results of expr_1 with previous variables
expr_2 = (expr_1 * result_1) / result_2
print(expr_2)
```

    14400.0
    2530.0934579439254


### Integer And Floating Point Division


By default, Python always produces a decimal value as a result of division. Any subsequent operations performed after that using integer values are automatically promoted to decimal values. It is also possible to force the Python interpreter to ignore the decimal part (by removing it altogether!) using the characters **//** for example `EXPR_A // EXPR_B`

However, it is important to note that to sucessfully perform integer division, both `EXPR_A` and `EXPR_B` in the above expression must be integer values. This means that the _left-hand-side_ (lhs) and the _right-hand-side_ values of the **//** symbol **must always evaluate to an integer** or in other words, the results of evaluating `EXPR_A` and `EXPR_B` should be integers. 


- If either of `EXPR_A` or `EXPR_B` is a decimal, the result will be decimal but any fractional part is removed (pt. **a**)
- If both `EXPR_A` or `EXPR_B` are integers, then the result will be integer (pt. **b**)


```python
expr_a = 25 * 10 - 7 + 32
expr_b = 56 - 100 + 85

# Performing decimal division
result_decimal = expr_a / expr_b
print(result_decimal)

# Performing integer division
# This is a demonstration of pt. b from above
result_integer = expr_a // expr_b
print(result_integer)
```

    6.7073170731707314
    6



```python
# Floating point division (default expected behavior)
t = 5 / 3
print(t)

# Integer division
# Both LHS and RHS of // are integers; result will also be integer
t = 5 // 3
print(t)

# Floating point division
# Both LHS and RHS of / are decimals; result will be a floating point number
t = 5.5 / 3.2
print(t)

# Integer division
# LHS and RHS of // are decimals; result will be a floating point number with fractional part removed
t = 5.5 // 3.2
print(t)

# Integer division
# LHS is a floating point number; result will be a floating point number with fractional part removed
t = 5.5 // 3
print(t)

# Integer division
# RHS is a floating point number; result will be a floating point number with fractional part removed
t = 5 // 3.2
print(t)
```

    1.6666666666666667
    1
    1.71875
    1.0
    1.0
    1.0



```python
result_decimal = expr_1 / expr_2
print(result_decimal)

# Both LHS (expr_1) and RHS (expr_2) do not evaluate to integer the result is decimal 
# But the fractional part is removed
# This is a demonstration of pt. a from above
result_integer = expr_1 // expr_2
print(result_integer)
```

    5.691489361702128
    5.0


### Modulo Operator

The modulo operator **%** in Python is used to calculate the remainder for the operation `A / b` i.e. `A % b` gives the remainder when **A** is divided by **b**.  
Note that `A % b` is not the same as `b % A` though in some cases the results of the operation maybe the same. It is also possible to chain together the results of multiple modulo expressions together as shown below.


```python
number_1 = 56
number_2 = 8
number_3 = 5
number_4 = 12

print(number_1 % number_2) # output should be 0
print(number_1 % number_3) # output should be 1
print(number_1 % number_4) # output should be 8

t = (number_1 % number_4) % number_2 # output should be 0
print(t)

t = (number_1 % number_4) % number_3 # output should be 3
print(t)

t = number_3 % number_2 # if x < y for x % y then the result is always x
print(t)
```

    0
    1
    8
    0
    3
    5


### Power Operator

This operator is denoted by the symbol `**` and the syntax is `a ** b` which basically means **a** raised to the power **b**. 


```python
# Two raised to 5; result is 32
print(2 ** 5)

# 5 raised to 2; result is 125
print(5 ** 3)
```

    32
    125


### Operator Precedence

Some operators are more important than others when evaluating an expression (similar to BODMAS)
for example `20 - 3 * 4` is **8** and NOT **68**.  
This is because `3 * 4` is evaluated first and this result is subtracted from **20**. Hence the result is `20 - 12 = 8`

The operator precedence of some of the commonly used mathematical operators are:  

- `()`
- `**`
- `*` and `/` _same level of importance_
- `+` and `-` _same level of importance_  


### Number Representation

Numbers - integers and floating point (both) are actually stored in the memory as BINARY NUMBERS i.e. they are converted into 1's and 0's and stored - because a computer at a hardware level can only understand binary instructions.  

Remember, for floating point numbers, for example **25.125** the value is broken up into two parts - **25** and **125** and both these numbers are stored in two separate locations in the memory (as binary)!! When the program needs to access the value, they are converted back into the original form again!  

We can convert an integer into the binary form using the keyword `bin()` and we can convert the binary back to **decimal** integer using `int()`  



### Statements And Expressions

In programming, anything that evaluates to a value and assigned on the right hand side of the `=` operator is called an **expression**. A **statement** in programming is considered an entire line of code. Consider the below snippet:

```python
p = 100
res = 200 * 0.05 / p
res = res ** 2
print(res)
```  

In the above example, the lines 
- `p = 100` 
- `res = 200 * 0.05 / p` 
- `res = res ** 2` 
- `print(res)`   

all are statements. The part `200 * 0.05 / p` (2nd line of code) and `res ** 2` (3rd line of code) both are expressions as these evaluate to a value.


### Self Variable Assignment

It is possible to assign an already defined variable to the same variable after applying some calculations on it. When this happens, the last saved value of the variable is used for calculations and the new value is updated to the variable. In this operation, the variable is assigned to a new memory location.  
Also, it is important to remember that for this to work, the variable must be defined first.    

```python
a = 200
print('value:', a)
print('address:', id(a)) # Current memory location of variable 'a'

print() # Print an empty line for better output representation

a = a * 10 # 200 * 10 = 2000
print('value:', a)
print('address:', id(a)) 

print()

a = a / 5 # 2000 / 5 = 400.0
print('value:', a)
print('address:', id(a))

print()

a = a - 10 * a / 1000 # 400.0 - 10 * 400.0 / 1000 = 400.0 - 10 * 0.4 = 400.0 - 4.0 = 396.0
print('value:', a)
print('address:', id(a))
```  

As evident from the example above, every statement is using the current value of the variable `a` to evaluate the expression and after every evaluation the variable `a` is assigned a new memory location. This can be verified with the help of the keyword `id()` which gives the current memory address of the variable `a`.  


### Augmented Assignment Operator

This is just a shortcut or a better way to represent the statement `a = a + 10` and we do it by compacting it to the format: `a += 10`.  

This means that `a += 10` is the same as `a = a + 10` but for this to work, a has to be defined in prior otherwise it will lead to an error.  

This is also possible with other mathematical operators like `*` `+` `-` `/` etc.


```python
a = 5

# Convert the int to binary
b = bin(a)

# Convert the binary back to int
# To convert back to decimal integer, we also need to specify the base (in this case 2)
i = int(b, 2)

print("binary: ", b)
print("integer:", i)
```

    binary:  0b101
    integer: 5



```python
a = 200
print('value:', a)
print('address:', id(a)) # Current memory location of variable 'a'

print() # Print an empty line for better output representation

a = a * 10 # 200 * 10 = 2000
print('value:', a)
print('address:', id(a)) 

print()

a = a / 5 # 2000 / 5 = 400.0
print('value:', a)
print('address:', id(a))

print()

a = a - 10 * a / 1000 # 400.0 - 10 * 400.0 / 1000 = 400.0 - 10 * 0.4 = 400.0 - 4.0 = 396.0
print('value:', a)
print('address:', id(a))
```

    value: 200
    address: 4306829056
    
    value: 2000
    address: 4410227536
    
    value: 400.0
    address: 4410228496
    
    value: 396.0
    address: 4410226128



```python
a = 10
a /= 2
print(a)

a = 20
a *= 5
print(a)
```

    5.0
    100


### Important Links

- [Floating Point Numbers](https://www.youtube.com/watch?v=PZRI1IfStY0)
- [Floating Point Arithmetic: Issues And Limitations](https://docs.python.org/3/tutorial/floatingpoint.html)
- [Numbers](https://realpython.com/python-numbers/)

## [3] Strings

A string is a sequence of alpha-numeric characters enclosed within a pair of **' '** or **" "** symbols. Simply explained, a string is nothing more than a piece of text (of finite length). Strings in Python are described by the type **str**. 

When creating a string the characters must be enclosed within a pair of single, double or tripple quotes. While single and double quoted strings only spread over a single line, the tripple quoted strings spread over multiple lines. Hence they are used to create multi line strings and comments. 


```python
# Single quoted string
string_1 = '[1]. hello world'
print(string_1)

# Double quoted string
string_2 = "[2]. hello world again!"
print(string_2)

# Multi line string
string_3 = '''[3]. This is a multi line string
that is spread over many lines, this being the second line
but definitely not the last there will also be one more line.
This is the last line of the multi-line string'''
print(string_3)
```

    [1]. hello world
    [2]. hello world again!
    [3]. This is a multi line string
    that is spread over many lines, this being the second line
    but definitely not the last there will also be one more line.
    This is the last line of the multi-line string



```python
# To check for the type 
print(type(string_1))
```

    <class 'str'>


### Concatenation

Strings can be joined together using the **+** operator; this is called as **concatenation** of strings. By using multiple strings as operands on either side of **+** operator, we can join these different strings into a single string.

One point to remember here, while numbers can be concatenated with strings, they need to be represented as strings first. A number of type **int** or **float** cannot be concatenated with a string. In concatenation, the order of concatenation matters.  

F


```python
B = "hello"
C = "world"

# Concatenate string C to string B
A = B + C
print(A)

# Concatenate string B to string C
A = C + B
print(A)
```

    helloworld
    worldhello



```python
# String can be concatenated with a number that is represented as a string
my_string = "hello" + " " + "world" + " " + "101"
print(my_string)

# Numbers represented as strings get concatenated
my_string = "101" + "10"
print(my_string)
```

    hello world 101
    10110



```python
# String CANNOT be concatenated with a number that is NOT represented as a string
# This will result in a runtime error
my_string = "hello" + " " + "world" + " " + 101
print(my_string)
```


    ---------------------------------------------------------------------------

    TypeError                                 Traceback (most recent call last)

    Input In [63], in <cell line: 3>()
          1 # String CANNOT be concatenated with a number that is NOT represented as a string
          2 # This will result in a runtime error
    ----> 3 my_string = "hello" + " " + "world" + " " + 101
          4 print(my_string)


    TypeError: can only concatenate str (not "int") to str


### Type Conversion

The process of converting the data type of a value from one type to the other is called as **type conversion**. For example, converting an integer value **10** to the string representation **"10"** is type conversion. The reverse is also true.  

Type conversion from string to integer is required if the input number we recieve is represented as a string but we need to perform mathematical operations on it. For example, we have a website that returns us the temperature in celsius (but this data is in string format) and we need to convert it to farenheit, we first need to convert the celsius to integer or float.  

The syntax for type conversion from string to integer is `int("100")`  and the syntax to convert integer to string is `str(100)`  

we can also perform type conversion on other data types.


```python
my_string = "hello" + " " + str(125)
print(my_string)

my_string = str(101) + str(919)
print(my_string)
```

    hello 125
    101919



```python
# Integer type conversion
my_number = int(my_string)
my_number *= 100
print('number:', my_number)

# Type conversion from number to float
my_float = float(my_number)
print('float:', my_float)

print()

d1 = 23.989
d2 = 23.125

# Type conversion from float to number
print('number:', int(d1))
print('number:', int(d2))
```

    number: 10191900
    float: 10191900.0
    
    number: 23
    number: 23


### String Multiplication

Python strings support another mathematical operator - the **\*** operator. This operator allows us to repeat a string for desired number of times. The syntax is `some_string * N` where **N** is the number of repetetions of the string we want. For example, `"hello " * 3 means hello hello hello`


```python
my_string = "hello " * 3
print(my_string)
```

    hello hello hello 



```python
my_string = (("A" * 5) + " ") * 3
print(my_string)
```

    AAAAA AAAAA AAAAA 


### String Length

Every string in Python has a length associated - it gives a count of the number of characters present in the string. The characters in a string are **0-indexed** (i.e. the first character occurs at index **0**, the next at index **1** and so on). To calculate the length of the string we use the **len()** keyword. For example `len("help")` outputs 4 (denoting the length of the string is **4** i.e. it is 4 characters long).


```python
# Check the length of the string
my_string = "help"
print(my_string)
print(len(my_string))

print()

# Update the current string; length will also get updated
my_string = my_string + "ME!"
print(my_string)
print(len(my_string))
```

    help
    4
    
    helpME!
    7


### Escape Sequences 

An escape sequence is a sequence of characters that does not represent itself when used inside a character or string but is translated to another character or keyword that may be difficult to represent directly.  

In Python the escape sequence starts with the character **\\** and it tells Python that the character immediately following this is to be treated as a string. This allows us to print special characters as a string.  

```python
string = 'today is teacher\'s day'
print(string) # Output is today is teacher's day
```  

Also, some characters following the **\\** have a special meaning and do not get represented as a part of the string directly. Some examples of this are **\n**, **\t** etc. 


```python
# The escape sequence \ tells python to consider the following character as a string
string = 'today is teacher\'s day'
print(string)

# The escape sequence \n tells Python to print a newline immediately after
string = 'hello\nworld'
print(string)

# The escape sequence \t tells Python to print a tab immediately after
string = '\thello\tworld'
print(string)
```

    today is teacher's day
    hello
    world
    	hello	world


### Formatted Strings

String formatting is a technique that allows us to create a _template_ of a string and then later dynamically create the actual string by passing in some of the information to the template through variables.  

Formatted strings in Python can be created using **f-string**.
The f-string starts with the letter **f** followed by the string in double quotes **" "** and in between whatever variable we want to pass enclosed in a pair of curly braces **{ }**  


```python
i = "world"
m = f"hello {i}"
print(m) # Output is hello world
```

Here, the f-string is `f"hello {i}"` and the value of the variable `i` gets filled into the f-string during creation. The final result (stored in the variable `m`) is the actual string created using f-string and variable.


```python
name = "Bob"

# Creating a simple f-string using a variable
greeting = f"Hello, {name}"
print(greeting)

# Updating the variable does not update the original f-string
name = "David"
print(greeting)
```

    Hello, Bob
    Hello, Bob



```python
# F-string works with numbers without type conversion
age = 23
message = f"Bob is {age} years old"
print(message)
```

    Bob is 23 years old


There is another way to create formatted strings in Python. Though this is an older format for creatting formatted strings, it is still useful to know as many Python projects still use this approach.  

In this format, instead of using the **f" "** approach, we use the **format()** keyword at the end of the string and specify the variables inside **format()** in the order that we want them to be present in the formatted string. The template string will have empty curly braces **{}** in this case.    

```python
template = "Hello {} {}"
message = template.format("Cruel", "World")
print(message) # Output is Hello Cruel World
```  

We can also specify a format string in Python with variable names inside the curly braces using the same approach as above.  

```python
template = "Hello {first_name} {last_name}"
message = template.format(first_name="John", last_name="Doe")
print(message) # Output is Hello John Doe
```  

In this approach, the variable name is not specified during template string creation, rather we just specify an empty set of **{ }** and at the time of actual string creation, we pass the data to the template.


```python
name = "Eugene"

# Creating a template string
template = "How are you {}?"
message_1 = template.format(name)

# Creating a new string by updating the variable used in the template string
name = "Max"
message_2 = template.format(name)

print(message_1)
print(message_2)
```

    How are you Eugene?
    How are you Max?



```python
message_title = "Charles"
message_body = "Hello there"
message_footer = "Good day to you!"

# A formatted string using multiple variables
template = "{} {}, {}"

# Creating the first string from template
message_1 = template.format(message_body, message_title, message_footer)

message_title = "Joseph"
message_body = "Good evening"
message_footer = "Welcome Back!"

# Updating the variables and creating a new string from template
message_2 = template.format(message_body, message_title, message_footer)

print(message_1)
print(message_2)
```

    Hello there Charles, Good day to you!
    Good evening Joseph, Welcome Back!



```python
# If variable names are not specified in the template, the order is important
template = "Hello {} {}"

# Printing in the order in which the values are provided
message_1 = template.format("Anish", "Pal")
message_2 = template.format("Pal", "Anish")

print(message_1)
print(message_2)
```

    Hello Anish Pal
    Hello Pal Anish



```python
# Formatted string using format() and variable names
template = "Hello {first_name} {last_name}"
greeting_1 = template.format(first_name="Anish", last_name="Pal")
print(greeting_1)

greeting_2 = template.format(first_name="John", last_name="Doe")
print(greeting_2)

# Using this approach the order of variables in template does not matter 
greeting_3 = template.format(last_name="Beckham", first_name="David")
print(greeting_3)
```

    Hello Anish Pal
    Hello John Doe
    Hello David Beckham



```python
# Template strings
inner_template = "inside inner template {}"
outer_template = "INSIDE OUTER TEMPLATE {} {}"

# Create a string using nested template strings
buffer_1 = outer_template.format(inner_template.format("<INNER>"), "<OUTER>")
buffer_2 = outer_template.format("<OUTER>", inner_template.format("<INNER>"))

print(buffer_1)
print(buffer_2)
```

    INSIDE OUTER TEMPLATE inside inner template <INNER> <OUTER>
    INSIDE OUTER TEMPLATE <OUTER> inside inner template <INNER>



```python
# Template string with named variables
template = "Hi there, I am {name}, from {country} and I am {age} years old"

# Create the string from the template
message = template.format(name="Anish", country="India", age=28)
print(message)
```

    Hi there, I am Anish, from India and I am 28 years old


We can also use template strings directly inside **print()** function to print dynamic results. Also, we can create expressions that evaluate to a value inside a template strings before printing them


```python
number = 13
print(f"The square of {number} is {number ** 2}")
print("The cube of {} is {}".format(number, number ** 3))
```

    The square of 13 is 169
    The cube of 13 is 2197


### String Indexing

A string is stored in memory as a sequence of characters. Below is a representation of how a string is stored in memory. The last character **\0** is denoted as a string termination symbol and is used internally by programming languages to mark the end of the string. This symbol is not a part of the string when the string variable is used.  

This is how a string is stored in memory:

                |    |    |    |    |    |    |    |    |    |    |    |    |    |
                |  h |  e |  l |  l |  l |  o |    |  w |  o |  r |  l |  d | \0 |
                |    |    |    |    |    |    |    |    |    |    |    |    |    |
                1000 1001 1002 1003 1004 1005 1006 1007 1008 1009 1010 1011 1012

Whenever a string is stored in memory, each individual cell of that memory stores a single character. In the above example, the cells are the memory locations `1000` `1001` `1002`...`1011`. Each of these memory locations can be accessed individually in any programming language through a special notation called **indexing**.  

Indexing allows us to individually access the characters of the string without having to specify their exact location in memory. What this means is we can access the character **W** in the above string without having to specify the exact address of the memory cell which is `1006`. Instead we use simple numbers like **1**, **2**, **3** etc. to represent these memory locations and access the individual character. Each of this number that represents the location of a character, is called an **index**.  

In Python, the first character of the string is located at index **0**, the second character is located at index **1**, the third character is located at index **2** and so on. The last character is always indexed as **one less than the length of the string**.  

To index a character in a string, we use the string variable followed by square brackets **[i]** where **i** represents the location we want to index.  

```python
string = "hello world"
print(string[0]) # Index the first character
```

                             
      Memory Address      -> 1003  4050  7099  8888  1001  7710  
                             |     |     |     |     |     |     |
                             |  p  |  y  |  t  |  h  |  o  |  n  |
                             |     |     |     |     |     |     |
      Front Index         ->    0     1     2     3     4     5     
      Reverse Index       ->   -6    -5    -4    -3    -2    -1
                               

The above is an image of how Python stores a string and how indexing works in Python. Remember, in Python the individual characters of the string are not stored in contiguous memory locations!  

We can verify this by checking `id(string[0])` `id(string[1]` `id(string[2])` etc.


```python
string = "hello world"

# Index the first character
print(f'string[0]: {string[0]}')

# Index the second character
print(f'string[1]: {string[1]}')

# Index the 5th character
print(f'string[4]: {string[4]}')

# Index the last character
print(f'string[10]: {string[10]}')

# Index the last character by calculating
print(f"string[10]: {string[len(string) - 1]}")
```

    string[0]: h
    string[1]: e
    string[4]: o
    string[10]: d
    string[10]: d



```python
string = "python"

print(f"{string[0]} -> {id(string[0])}")
print(f"{string[1]} -> {id(string[1])}")
print(f"{string[2]} -> {id(string[2])}")
print(f"{string[3]} -> {id(string[3])}")
print(f"{string[4]} -> {id(string[4])}")
print(f"{string[5]} -> {id(string[5])}")
```

    p -> 4368604784
    y -> 4372479408
    t -> 4370824240
    h -> 4371258672
    o -> 4370830256
    n -> 4371114736


### Reverse Indexing

In Python it is also possible to index a string from the end, i.e. identify the memory location of the last character of the string and work our way backwards to the first character of the string. The last index in this case is denoted by **-1**, the second last index as **-2** and so on. The first index (i.e. index **0**) is denoted as the **-(length of the string)**.


```python
string = "$12345"

# Print the last index using reverse index
print(f"string[-1]: {string[-1]}")

# Print the 3rd index using reverse index
print(f"string[-3]: {string[-3]}")

# Print the 1st index using reverse index
print(f"string[-6]: {string[-6]}")

# Print the 1st index using reverse index by calcuating
print(f"string[-6]: {string[-len(string)]}")
```

    string[-1]: 5
    string[-3]: 3
    string[-6]: $
    string[-6]: $


### String Slicing

Slicing means to extract a portion of the string from the main string based on a starting index and an ending index. The general syntax is `string[start_index : end_index]` and it is important to note that slicing can also include the whole string.  

Remember, the character at **end_index** is not actually considered for slicing. If we want to include the character at **end_index** for slicing then we have to specify the slice as `string[start_index : end_index + 1]`  

Also remeber, just like regular indexing, it is also possible to slice the string using reverse indexing methods. This means that we can specify negative integers for the slices and the strings will be sliced accordingly.


```python
string = "01234567"

# Slice the first 4 characters of the string
print(f"string[0:3]: {string[0:4]}")

# Slice from the 4th character to the end of the string
print(f"string[3:6]: {string[3:7]}")

# Slice using reverse indexing from 4th character to end of string
print(f"string[3:6]: {string[-5:-1]}")
```

    string[0:3]: 0123
    string[3:6]: 3456
    string[3:6]: 3456


We can choose to leave out either the **start_index** or the **end_index** empty during string slicing. If the **start_index** is empty, then the string will slice from index **0** to the **end_index**. The syntax for this is `string[:end_index]`  

If the **end_index** is empty then it will start slicing from the **start_index** upto the end of the string. The syntax for this is `string[start_index:]`  


If both are left empty, then the whole string is sliced. The syntax for this is `string[:]`


```python
string = "0123456789"

# Slice from 4th index onwards
print(f"string[4:]\t{string[4:]}")

# Slice upto the 4th index
print(f"string[:4]\t{string[:4]}")

# Slice the whole string
print(f"string[:]\t{string[:]}")
```

    string[4:]	456789
    string[:4]	0123
    string[:]	0123456789


We can also slice strings by specifying a **step**. A step basically means the amount by which to increase the index when the slicing operation takes place. The syntax for this is `string[start_index:end_index:step]`  

By default the step value is set to 1 which means index increases by 1 starting from the **start_index**. If we set the step as **3** then after **start_index** the next index considered for slicing will be **start_index + 3** and so on. 


```python
string = "0123456789 ABCDEFGHIJ"
print(string)
print()

# Slice with a step of 3 in the range [2,12]
print(f"string[2:12:3]\n{string[2:12:3]}")
print()

# Slice with a step of 5 in the range[:]
print(f"string[::5]\n{string[::5]}")
print()

# Reverse a string 
print(f"string[::-1]\n{string[::-1]}")
print()

# Print from index -10 to index -1 in reverse 
print(f"string[-1:-10:-1]\n{string[-1:-11:-1]}")
print()

# Print from index -10 to index -1 in forward 
print(f"string[-10:-1]\n{string[-10:-1]}")
print()
```

    0123456789 ABCDEFGHIJ
    
    string[2:12:3]
    258A
    
    string[::5]
    05 EJ
    
    string[::-1]
    JIHGFEDCBA 9876543210
    
    string[-1:-10:-1]
    JIHGFEDCBA
    
    string[-10:-1]
    ABCDEFGHI
    


### Immutability 

In Python, strings are immutable. This means that the contents of a string cannot be changed once it has been stored in the memory. We can modify that string and it will get assigned to a new location, we can entirely erase the contents of the variable holding the string and replace it with new one but it is not possible to alter the string itself.  

For example, if we have a string `string = "python"` then we cannot modify this string at it's memory location by changing it's contents. We can assign a new value to the variable `string` but this will get stored in a new memory address but the original string **python** cannot be modified at source. 


```python
string = "python"
print(f"{string} -> {id(string)}")

# This modification is allowed as it does not mutate the existing string
string = "pyThon"
print(f"{string} -> {id(string)}")

# This modification is allowed as it does not mutate the existing string
string = string + "."
print(f"{string} -> {id(string)}")

# This modification is not allowed as it mutates the existing string
# This will lead to an error
my_string = "python"
my_string[0] = "P"
print(my_string)
```

    python -> 4389337136
    pyThon -> 4418297264
    pyThon. -> 4418313968



    ---------------------------------------------------------------------------

    TypeError                                 Traceback (most recent call last)

    Input In [36], in <cell line: 15>()
         12 # This modification is not allowed as it mutates the existing string
         13 # This will lead to an error
         14 my_string = "python"
    ---> 15 my_string[0] = "P"
         16 print(my_string)


    TypeError: 'str' object does not support item assignment


### Built In Functions And Methods

**Functions** in Python consist of a sequence of characters followed by the paranthesis **()** for example `hello()`, `foo()` etc. Python provides many in-built functions that have pre-defined behavior and we cannot use them for anything else. Some examples of in-built functions are `print()`, `len()`, `type()`  


**Methods** in Python are functions that start with the dot operator **.** and are appended to the end of a variable that represents a class, a string, a list etc. For example `string.replace()`, `string.isupper()` etc are some in built Python methods that extend the functionality of the existing string data type



```python
string_1 = "THE QUICK BROWN FOX"
string_2 = "jumps over the lazy dog"
string_3 = 2.355

print(f"{string_1}.isupper ? {string_1.isupper()}\n")
print(f"{string_1}.lower ? {string_1.lower()}\n")
print(f"{string_2}.upper ? {string_2.upper()}\n")
print(f"{string_3} with a precision of 5 ? {format(string_3, f'0.5f')}")
```

    THE QUICK BROWN FOX.isupper ? True
    
    THE QUICK BROWN FOX.lower ? the quick brown fox
    
    jumps over the lazy dog.upper ? JUMPS OVER THE LAZY DOG
    
    2.355 with a precision of 5 ? 2.35500


In built string methods create a new string in memory. This is because strings in Python are immutable. If the changes from the methods are not assigned to a variable, the changes will become in-accessible in memory as there is no way to know the address where they are stored! 


```python
string = "the quick brown fox jumps over the lazy dog"
print(id(string))
print()

# New address of the string variable after replace()
string = string.replace("fox", "bear")
print(id(string))
print()

# New address of string variable after upper()
string = string.upper()
print(id(string))
print()

string = "python programming"
print(f"before modification -> ", string)
print()

# The result of replace() is not assigned to a variable
# After executing print function, the changes will not be accessible
print(string.replace("python", "javascript"))
print(f"after modification -> {string}")
```

    4417653616
    
    4699507760
    
    4417653712
    
    before modification ->  python programming
    
    javascript programming
    after modification -> python programming


### Important Links

- [Strings And Characters](https://realpython.com/python-strings/)
- [String Formatting](https://realpython.com/lessons/string-formatting/)
- [String Formatting Best Practices](https://realpython.com/python-string-formatting/)
- [Mutability And Immutability](https://www.educative.io/answers/what-are-mutable-and-immutable-objects-in-python3)


## [4] Working With User Input

Working with user data is very important - the code that we write should be able to take data from an external source, process it and return the results back to the user. In Python, user inputs are collected using the **input( )** keyword.  

It is important to note that in Python, user inputs are always collected as string data type. Therefore, any value entered by the user is captured by Python in string format. Some type conversion is required if we want to perform mathematical operations on the user inputs. In such a case, the entered value is either converted into an integer or a floating point value.  

Consider the following example:

```python
# User input
v = input()

# User input with prompt
v = input("enter name: ")

# Input with prompt and type conversion
v = int(input("enter number: "))
```  


```python
# Taking user input with a prompt
t = input("name? ")

message = f"hello {t}, wish you a good day!"
print(message)
```

    name? Anish
    hello Anish, wish you a good day!



```python
# Type conversion of user input
t = int(input("number? "))

t_square = t ** 2
message = f"square({t}) is {t_square}"
print(message)
```

    number?  13


    square(13) is 169


### Important Links

- [Python Inputs - Documentation](https://docs.python.org/3/tutorial/inputoutput.html)

## [5] Boolean

Booleans are data types that can take either of the two values only - **True** or **False**. Any given boolean data type will either be set to `True` or `False` at any given point of time but not both. Boolean values are very important from a programming point of view as they are used extensively to check for conditions and take appropriate actions (for example, if the result of an operation is `False`, the code may send an alert to the user).  


```python
# A simple example on boolean data type
flag = True
print(type(flag))
```

    <class 'bool'>


### Important Links

- [bool() Type](https://www.programiz.com/python-programming/methods/built-in/bool)
