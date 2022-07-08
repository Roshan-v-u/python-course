# Data Structures In Python

A data structure is a container that holds a collection of data and allows us to modify the data in different ways. It also provides us with extra functionality to access or store data efficiently.  

The most common data structures in Python are lists, dictionaries, tuples and sets.

## [1] Lists

Lists are **ordered collection** of items. An ordered collection means that the items are stored in the data structure in the same way as they were entered. Therfore, the order of the elements is said to be **preserved**. When we print the contents of the list, the items get printed in the same order they were specified when creating the list (unless we have modified the list in some way).  

A list can contain items of different data types. Therefore, the items inside a list can be integer, float, boolean, string etc. or any combinatation of these. We can also store other data structures inside a list.  

A list begins in Python can be created by the square brackets **[ ]** or **list( )** commands. The syntax is  

```python

# An empty list
list_a = []

# Another empty list
list_b = list()
```

While creating a list using **[ ]** is straightforward, the **list( )** approach takes in a list as input! There are many similarities between a list and a string in Python and many of the operations that can be done on a string can also be performed on a list.


```python
# Create empty list using []
list_a = []
print(list_a)

# Create empty list using list()
list_b = list()
print(list_b)

# To calculate the length of a list
print(f'len([]): {len(list_a)}')
print(f'len([]): {len(list_b)}')
```


```python
# Create a non-empty list using []
list_a = [10, 20, True, "hello", "world"]
print(list_a)
print(f'length: {len(list_a)}')

print()

# Create a non empty list using list()
# list() takes only one parameter - the list that we want to create
list_b = list([78, "Python Programming!", -0.0042, False])
print(list_b)
print(f'length: {len(list_b)}')
```

### List Of Lists

It is also possible to create a list of lists in Python. This means the items inside the list can be lists themselves. The standard format of this looks like:  

```python
[
    [10, 20, 30, 40], 
    [0.1, 0.2, 0.3, 0.4], 
    ["h", "e", "l", "l", "o"]
]
```  

When creating a list of lists in Python, the nested lists need not be of the same length. We can have a list that is of length 2, another that is of length 5 and so on. We can even have an empty list as a list item. It is also important to remember that apart from lists, we can also add elements directly inside a list of lists.  

We can even nest further by adding the list of list inside another list: a list of list as an item of a list!


```python
# Create a list of lists
a = [
    [10, 20, 30, 40], 
    [0.1, 0.2, 0.3, 0.4], 
    ["hello", "world", "welcome", "to", "Python"]]
print(a)
print()

list1 = [10, 20, 30, 40, 50]
list2 = [100, 200, 300, 400]
list3 = [0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.9, 1.11, 1.5]

# Create a list of lists from other lists
matrix = [list1, list2, list3]
print(matrix)
print()

# Create a list of lists with mixed items
mixed_list = [list1, 23, 45, "Python Programming", list3, "Hello", "World" , list2]
print(mixed_list)
print()

# Neting a list of list inside another list
third_dimension = [matrix, mixed_list, -3, -1, 0, list1]
print(third_dimension)
```

### Indexing

Accessing the elements of a list using the position of the elements inside them is called as indexing. Lists can be indexed much the same way as strings, both from front and end. Indexing a list that does not have any nested lists is pretty straight forward - we use the index operator **[ i ]** to access the item at the index **i** of the list. 

Consider the example: 

```python
numbers = [10, 20, 30, 40, 50, 60]
print(numbers[4]) # The result will be 50
print(numbers[-1]) # The result will be 60 as lists support negative indexing
```

Indexing lists that have nested lists inside them is however a bit tricky - only using the **[ i ]** operator is not enough. This is because the single indexing operator returns the entire list at the index **i** and if we want to access the elements inside that list we need to specify another indexing operator **[ j ]**.  

Consider the example:

```python
pixels = [[0.1, 0.2, 0.5, 0.7], [0.11, 0.20, 0.45, 0.0], 10, 20, 30, [0.76, 0.42, 0.01]]
print(pixels[1]) # This will return the entire list [0.11, 0.20, 0.45, 0.0] at the index 1
print(pixels[3]) # This will return the value 20
print(pixels[1][2]) # This will return the item at index 2 of the list [0.11, 0.20, 0.45, 0.0]
```  

If there are more nested lists, then we need to provide an indexing operator **[k(i)]** for every level of nesting **i**


```python
list_a = [0.76, 0.42, 0.01]
list_b = ["hello", "world", "welcome", "to", "Python", "Programming"]

# Indexing the first item of list
print(f'list_a[0] is {list_a[0]}')

# Indexing the last item of the list
print(f'list_b[-1] is {list_b[-1]}')

print()

pixels = [[0.1, 0.2, 0.5, 0.7], [0.11, 0.20, 0.45, 0.0], 10, 20, 30, [0.76, 0.42, 0.01]]
print(pixels[1]) 
print(pixels[3]) 
print(pixels[1][2])
print()

points = [[0.1, 0.2, 0.5, 0.7], [0.11, 0.20, 0.45, 0.0], 10, 20, 30, [0.76, [0, 2, 4, 5, 7, 8, 9], 0.056, 0.71]]
print(f'points\n{points}')
print()

# Return the item present at the last index
print(f'points[-1]\n{points[-1]}')
print()

# Return the list present at index 1 of the last item
print(f'points[-1][1]\n{points[-1][1]}')
print()

# Return the last item present in the innermost list
print(f'points[-1][1][-1]\n{points[-1][1][-1]}')
```

**Note**  

When there are lists present inside a main list **L** and we calculate the length of the list, this value is actually the count of the items of **L** only. It does not count the items present inside the nested list. Remember, for the main list **L** any nested list **l(i)** is considered as a single item.  


```python
pixels = [[0.1, 0.2, 0.5, 0.7], [0.11, 0.20, 0.45, 0.0], 10, 20, 30, [0.76, 0.42, 0.01]]

# Calculate the length of the main list
count = len(pixels)
print(f'main list length: {count}')

# Calculate the length of the last inner most list
count = len(pixels[-1])
print(f'innermost list length: {count}')
```

### Mutability Of Lists

In Python, lists are mutable data structures. This means that we can modify the contents of the list at the existing memory location and the list is not assigned a new memory location. This behavior is unlike strings which are immutable and any changes to the string contents results in the string getting assigned to a new memory location.


```python
words = ["hello", "world", "welcome", "to", "python", "programming"]
print(words)
print(id(words))
print()

# Modify the contents of the string
words[0] = "Hi!"
words[-2] = "JavaScript"
print(words)
print(id(words)) # Memory location remains unchanged
```


```python
pixels = [[0.1, 0.2, 0.5, 0.7], [0.11, 0.20, 0.45, 0.0], 10, 20, 30, [0.76, 0.42, 0.01]]
print(pixels)
print(id(pixels))
print()

# To edit a single item in the nested listed we need to index accordingly
pixels[0][-1] = "XX"
print(pixels)
print(id(pixels)) # Memory location remains unchanged
print()

# Incorrect indexing of nested list will replace the entire list
pixels[-1] = "YYYY"
print(pixels)
print(id(pixels)) # Memory location remains unchanged
```

### Slicing

Lists can be sliced much like strings. The format for list slicing is **[start_index : end_index : step]** where **start_index** refers to the index at which the list is sliced and **end_index** refers to the point upto which the slicing is continued. The element at the index **end_index** is not considered for slicing.  

The **step** refers to the value by which the current index is incremented. At the start of the slicing operation, the **start_index** is the current index.  


```python
temp = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
print(f'temp\n{temp}\n')

# Slice the list from the first to the fifth index
slice1 = temp[0:5]
print(f'temp[0:5]\n{slice1}\n')

# Slice the list from the fourth last to the last index
slice2 = temp[-4:-1]
print(f'temp[-4:-1]\n{slice2}\n')

# Slice the list from last index to fourth last index
slice3 = temp[-1:-4:-1]
print(f'temp[-1:-4:-1]\n{slice3}\n')

# Print the list in reverse
reverse = temp[::-1]
print(f'reverse\n{reverse}\n')
```

List slicing can also be carried out on nested lists but we need to properly index them first. For example if the list was

```python
a = [10, 20, [0.1, 0.2, 0.3, 0.4, 0.5, 0.6], 30, 40]
```

and we wanted to slice upto the fourth element of the inner list starting from the first element of the inner list the syntax would be  

```python
a[2][:4]
```

It is not recommended to use list slicing for nested lists as it is a tedious process to slice an inner list along with items that are not lists.  

For example if we wanted to slice the above list from the first index of main list (item **10** at index 0) to the fourth index of the inner list (item **0.5** at index 4) this would not be possible using standard list slicing operations.  If we used the syntax `a[0:3][:4]` to get the result, the value returned will not be what we were expecting.  

This is because when a list is sliced, a new list is returned and the next slicing operation is carried out on that returned list. Therefore for the code `a[0:3][:4]` what happens is `a[0:3]` is executed first which returns the list  

**[10, 20, [0.1, 0.2, 0.3, 0.4, 0.5, 0.6]]**  

and then the next part of the slice `[:4]` is applied to the above returned list. The result remains the same in this case as above. However if the second part of the slice was `[:2]` then the final list returned would be  

**[10, 20]**  

**Note**  

The slicing operation `a[0:3][:4]` on the list **a** can be demonstrated through the code example below:  

```python
a = [10, 20, [0.1, 0.2, 0.3, 0.4, 0.5, 0.6], 30, 40]

# First the slice a[0:3] happens
first_slice = a[0:3]

# Then the slice temp[:4] happens
second_slice = first_slice[:4]
```


```python
a = [10, 20, [0.1, 0.2, 0.3, 0.4, 0.5, 0.6], 30, 40] 
print(f'a\n{a}\n')

# Slice the inner list upto the fourth index
inner_slice = a[2][:4]
print(f'a[2][:4]\n{inner_slice}\n')

# Slice the list using a[0:3][:4]
inner_slice = a[0:3][:4]
print(f'a[0:3][:4]\n{inner_slice}\n')

# Slice the list using a[0:3][:2]
inner_slice = a[0:3][:2]
print(f'a[0:3][:2]\n{inner_slice}\n')
```

**Note**

Since the slicing operation on a list always returns a list we can keep stacking up slices like  

`a[i:j][m:n][p:q][x:y]`  

and so on as long as each previous slice returns a list.  
In other words, if **a[i:j]** returns a list, then **[m:n]** can be applied to the returned list and if the result is another list, then the slice **[p:q]** can also be applied and so on.


```python
a = [10, 20, [0.1, 0.2, 0.3, 0.4, 0.5, 0.6], 30, 40] 
print(f'a\n{a}\n')

# Chain two slicing operations together
inner_slice = a[2][:4]
print(f'a[2][:4]\n{inner_slice}\n')

# Chain three slicing operations together
inner_slice = a[2][:4][:3]
print(f'a[2][:4][:3]\n{inner_slice}\n')

# Chain four slicing operations together
inner_slice = a[2][:4][:3][:2]
print(f'a[2][:4][:3][:2]\n{inner_slice}\n')

# A really complex slicing operation
inner_slice = a[0:3][-2:][1][-1:-4:-1]
print(f'a[0:3][:3][-2:][1][-1:-4:-1]\n{inner_slice}\n')
```

### List Methods

These are methods that are available on list (or rather, the **List Class** in Python) and are used to modify the list in place. They work by appending the dot operator **.** after the list and then using the appropriate method.  

When working with methods, there is a concept of **in-place** changes and **out-of-place** changes. In case of **in-place** changes, the modifications are directly done on the original data structure (in this case lists) without creating a new copy at a new memory location. For **out-of-place** changes, the original data structure is left intact and a new one is returned with the modifications. This newly returned data structure is stored in a new memory location.  


#### Append 

This method is used to add a new item **X** to the end of the list. This is an in-place method and hence the changes reflect directly on the original list. The return value is **None**. This method can only insert items at the end of the list.  

The syntax is `list.append(X)`  
                                  
#### Insert 

This method is used to add a new item **X** at the index **i** of the list. If an item already exists at the index **i** then it is replaced by the newly inserted item **X**. If the index **i** does not exist then the item is added at the end of the list. The **insert** method is an in-place method and returns **None**.  

The syntax is `list.insert(X, i)`  

#### Extend

This method is used to increase the contents of the current list by adding another list **L**. The original list is **extended** or _expanded_ to include the elements of the new list. This is an in-place method and the return value is **None**.  

The syntax is `list.extend(L)`  

#### Pop 

This method is used to remove an item from the list at index **i**. This method is an in-place method and changes are applied on the original list itself. The return value is the removed element.  

The syntax is `list.pop(i)`  

If nothing is specified inside the **pop(i)** then by default, the last item of the list is removed. If the user specifies the method as **pop(i)** then the item at index **i** is removed. If **i** is outside the valid range of the list index then an error occurs.  

#### Remove

This method is used to remove an item **X** from the list. This is an in-place method and the return value is **None**. If the element is not present in the list, an error occurs.  

The syntax is `list.remove(X)`  

The difference between **list.pop(i)** and **list.remove(X)** is that **pop()** takes in an index from which the item has to be removed whereas **remove()** takes in the item that has to be removed.  

#### Clear

This method removes every element from the array. This is an in-place method and the return value is **None**. This method does not take any arguments.  

The syntax is `list.clear()`

**Note** In all the cases pertaining to list methods where indexes are required, we can also use negative indexing to access the list items. 


```python
# Code Examples
l = [10, 20, 30, 40, 50, 60, 70, 40, 50, 40, 10, 40, 50]
d = l.count(-19)
print(d)
```

#### Index

This method returns the index of the item **X** between the indices **i** and **j**. The return value is the index of the item. This method performs a search operation on the list and therefore does not modify the list in any way.  
If the indices **i** and **j** are not specified then the whole list is considered for searching. If the item **X** is not in the list or not between the indices **i** and **j** then an error occurs. 

The syntax is `list.index(X, i, j)`  

A better way to search for an item in a list is using the **in** keyword. This returns **True** if the item is found in the list and **False** otherwise.  

The syntax is `item in my_list`  

The syntax to search for an item in the list between the indices **i** and **j** is `item in my_list[i:j]`  
  
#### Count

This method returns the count of the item **X** in the list, i.e. it returns how many times the item **X** is present in the list. This method does not modify the list in any way. If the item is not present in the list, then the return value is **0**  

The syntax is `list.count(X)`  

#### Sort

This method sorts the list in place. The return value is **None**. By default the sort order is increasing order (i.e. the items are arranged from smallest to largest). This method takes in two optional paramters
- **key** which lets us implement our own sorting function
- **reverse** which sorts the list in decreasing order (i.e. the items are arranged from largest to smallest)  

The syntax is `list.sort()` or `list.sort(key=some_key, reverse=True)`  

To return a sorted list without modifying the original list - use **sorted()**. This method also sorts the list but it is an out-of-place sort and therefore the original list is not modified.  

#### Reverse

This method reverses the order of the items in the list. This is an in-place method and the return value is **None**.  
The syntax for the same is `list.reverse()`


```python
# Code Examples
```

**list(range(i, j))** generates numbers between [i, j) and adds them to the list. This is a very useful function to populate a list of numbers quickly.  

For example `list(range(10, 15))` will return **[10, 11, 12, 13, 14]**


**"H".join(L)** joins the list items into a single string using the character **#** as a separator between list items. This method returns a new list.  

For example `"$".join([10, 20, 30, 40, 50])` will return **10H20H30H40H50H**

**Note**
Lists can be concatenated into a new list using the **+** operator much like strings. 

### List Unpacking

List unpacking is a technique of extracting individual items of the list and saving them to variables. The number of variables being used for extraction should be the same as the number of items in the list.  

The syntax is 
```python 
a, b, c = [10, 20, 30]
```  

Here the list items **10**, **20** and **30** are unpacked into the variables `a`, `b` and `c`.  

There is another way to unpack the list and that is using the **\*** operator. This operator takes a slice of the list that are not unpacked into individual variables. If this is the only operator present, then the entire list is sliced.

Consider the example  

```python
a, b, *others = [10, 20, 30, 40, 50, 60, 70, 80]
x, y, *others, z = [10, 20, 30, 40, 50, 60, 70, 80]
```  

In the first case the list items **10** and **20** are unpacked into the variables `a` and `b` while the rest of the list `[30, 40, 50, 60, 70, 80]` is unpacked into `others`.  

In the second case, the list items **10**, **20** and **80** are unpacked into the variables `x`, `y` and `z` while the rest of the list `[30, 40, 50, 60, 70]` are unpacked into `others`. 

**Note** The **\*** operator allows us to unpack a list safely without having to specify the exact number of variables as the items in the list.


```python
# A standard list slice
a, b, c = [10, 20, 30]
print(a)
print(b)
print(c)
```


```python
# Number of variables lesser than the items in list to unpack leads to error
a, b = [10, 20, 30, 40]
print(a)
print(b)
```


```python
# Number of variables more than the items in list to unpack leads to error
a, b, c, d, e, f = [10, 20, 30, 40]
print(a)
print(b)
```


```python
# Unpacking using the * operator
a, b, *others = [10, 20, 30, 40, 50, 60, 70, 80]
print(a)
print(b)
print(others)
```


```python
# Unpacking using the * operator
x, y, *others, z = [10, 20, 30, 40, 50, 60, 70, 80]
print(x)
print(y)
print(others)
print(z)
```

### Important Links

- [List Methods](https://realpython.com/lessons/list-methods/)
- [Introduction To Lists](https://www.programiz.com/python-programming/list)
- [Python Documentation - Lists](https://docs.python.org/3/tutorial/datastructures.html)
- [Google For Education - Python Lists](https://developers.google.com/edu/python/lists)



## [2] Dictionary

A dictionary is an **ordered collection of items**. It represents data as a **key-value** pair i.e. every value stored in the dictionary has a unique key associated with it. Repeating keys are overwritten with their last value. From a data structure point of view, dictionaries in Python are used to resemble/mimic the role of hash maps. In Python, dictionary is often referred to by the name **dict** and the keyword to create one is also `dict`  

A Python dictionary pair looks as follows:  

```python
my_dict = {
    "key1": "value1",
    23: "value2",
    True: "value3",
    False: "value4"
}
```  

A Python dictionary consists of **key-value** pairs enclosed within a pair of **{ }** and every `key:value` pair represents a **dictionary item** (also called as key-value pair).  

The key-value pair is separated by **:** and the object on the LHS of **:** represents the **key** while the object on the RHS of **:** represents the **value**. While the values can be mutable or immutable objects, repeating values etc. the keys must be unique and immutable objects.


```python
# A Python dictionary
my_dict = {
    "key1": "value1",
    23: "value2",
    True: "value3",
    False: "value4",
    "_key5": "value5",
}
print(my_dict)

# The len keyword returns the number of items in the dictionary
print(len(my_dict))
```

Accessing the values in a dict is done through their keys. We can either use the **[ ]** notation to retrieve the value corresponding to the specified key or use in-built methods.  

The syntax for accessing the value using the **[ ]** notation is `dict[K]`. This will return the value **V** corresponding to the key **K**. If the key is not present in the dictionary, this results in an error.  

The opposite of this approach is however not true, i.e. `dict[V]` will not return the key **K** because `dict[V]` makes Python search for the key **V** (ie. it treats the value **V** as a key). If **V** is present as a key also, then the value corresponding to it is returned.  

**Note**  
It is possible to have the value as a key in the dict as long as the nature of the value is immutable and the value has previously not been used as a key before.


```python
# Get the value for the key "key1"
print(my_dict["key1"])

# Get the value for the key "23"
print(my_dict[23])

# Get the value for the key "False"
print(my_dict[False])
```


```python
my_dict = {
    "key": "value",
    "value": "another_value"
}
print(my_dict['key'])
print(my_dict['value'])
```


```python
# If the key is not present in the dictionary, it results in error
print(my_dict["hello_world"])
```

### Operating On Dicts

#### Modifying The Key Value

It is possible to assign new values to a dictionary key using the assignment operator **=**  
The syntax for the same is `my_dict[K] = V_NEW` where the key **K** is updated with the new value **V_NEW**. This is an in-place method and changes reflect on the dictionary directly.


```python
my_dict = {
    'key': 'value',
    20: 'even',
    51: 'odd',
    False: 0,
    True: 1
}
print(my_dict)

# Modify the values for the keys "key", "20", "False"
my_dict['key'] = 'new value'
my_dict[20] = 'not_odd'
my_dict[False] = -1

print(my_dict)
```


```python
# We can also assign an exsting key value to another key value
my_dict[True] = my_dict[False]
print(my_dict)
```

#### Adding A New Key

We can add a new key to the dictionary by using the **[ ]** notation and the **=** operator. If the key does not exist, it gets added to the dict otherwise the value of the existing key gets updated as shown above.  

The syntax for adding a new key to the dictionary is `my_dict[K_NEW] = V_NEW` i.e. a new key **K_NEW** for the value **V_NEW** is added to the dict.


```python
# Adding a new key to the dict
my_dict['new_key'] = "hello world"
print(my_dict)

# Adding a new key to the dict
my_dict[24] = 4000
print(my_dict)
```

#### Deleting An Existing Key

We can delete an existing key from the dict using the **del** keyword. This keyword however only deletes the key if it is present in the dict. This operation does not return any value. If the key specified does not exist, it results in an error.  

The syntax to delete a key from the dict is `del my_dict[K]` i.e. it deletes the key **K** from the dict.  

**Note**

This method not only works on dicts but other Python classes like lists, tuples etc. The syntax is `del my_list[i]` i.e. it will remove the item at index **i** from the list in-place. 


```python
# Delete the keys "24" and "new_key" from the dict
del my_dict[24]
del my_dict['new_key']

print(my_dict)
```


```python
# Trying to delete a non existent key results in error
del my_dict['some_random_key']
```

#### Mutability And Uniqueness

In Python dicts, the values associated with the keys have no restrictions - they can be mutable, immutable, unique and non-unique. Therefore, we can have strings, numbers, lists etc as values for the keys. Similarly, the same value may be used to associate with one or more keys, i.e. more than one key may have the same value.  

However, keys in dicts are bound by 2 restrictions:

- The keys must be immutable objects i.e. mutable objects like lists cannot be used as a key
- Every key must be unique, i.e. a key can have only one value in the dict at any given time  

**Note**  
If a key is repeated in Python dict, then the last value associated with that key is used for mapping and the previous values are overwritten.


```python
# A dict with mutable and repeating values
bd = {
    "k1": "value",
    "k2": "value",
    200: 'value',
    False: 0,
    True: [10, "Python", 0.01, True]
}
print(bd)
```


```python
# Cannot have a dict with mutable object as key
bd = {
    "k1": "value",
    "k2": 2000,
    [10, 20]: "List"
}
print(bd)
```


```python
# When keys are repeated last value is mapped
bd = {
    "k1": "value1",
    "k2": "value2",
    "k3": "value3",
    "k1": False,
    "k2": True,
    "k3": 0,
    "k1": [True, False, 0]
}
print(bd)
```

#### Working With Variables

We can create a dict from variables. The key and values can be assigned to variables and mapped dynamically at the time of creation. However, the rules for dict creation still remain valid - if a variable represents a mutable object then that variable cannot be used as a key for the dict.  

We can also have a dict inside a dict (nested dict) just like lists. But in this case, the dict must be a value and cannot be used as a key because dicts are mutable objects too. We can however, use a dict key or a dict value as a key to another dict as long as they are immutable objects.


```python
# Create an empty dict
sd = {}

var_key = "k1"
var_val = "_value"
var_list = [10, 20, 30, 40]
var_bool = True
var_num = 200

# Populate the dict with key value pairs using the variables
sd[var_key] = var_val
sd[var_val] = var_val
sd[var_num] = var_list
sd[var_bool] = var_key

print(sd)
```


```python
# Modifying the variable value does not update the dict
var_key = "_KEY"
var_val = "_VAL"

print(sd)

# Need to update the dict key manually to reflect updated values
sd[var_key] = var_val
sd[var_val] = var_val
sd[True] = var_key

print(sd)
```


```python
# As keys cannot be modified directly we have to remove the old keys
del sd["k1"]
del sd["_value"]

print(sd)
```


```python
# Cannot use a variable as a key when it holds a list (mutable)
sd[var_list] = var_bool
print(sd)
```


```python
# We can index a list item as a key to dictionary
sd[var_list[0]] = 111
sd[var_list[-1]] = 999

print(sd)
```


```python
# Use a dict as a value to key in another dict
di = {
    "k1": "v1",
    "k2": "v2",
    1001: [10, 20, 30, 40],
    False: 0
}
main = {
    "key": di,
    di["k1"]: di[False],
    di[False]: di[1001]
}

print(main)
```


```python
# Cannot use a dict value as key to another dict if value is list (mutable)
main[di[1001]] = "LIST"
```


```python
# Cannot use a dict value as key to another dict if value is dict (mutable)
main[di] = "DICT"
```

### Dictionary Methods

The dictionary class comes with in-built methods that allow us to perform operations on it. Some methods modify the list in-place while others do not.  

#### Get

The **get( )** method is used to fetch the value for a key in the dict. This method does not cause an error if the key does not exist. The object returned by this method is the value corresponding to the key (if exists) and **None** (if key does not exist). We can also specify the return value for a key that does not exist in the dict.

The syntax is  

```python
# Fetch a key that exists
val = dictionary.get('key1')

# Fetch a key that does not exist with default value
val = dictionary.get('xyz123', 111)
```  

#### Dict

This keyword is used to create a dict using the **dict** function. While this is not a dictionary class method, this method is unique to the dictionaries as it allows us an alternative way to create a dict. In this function the key value pairs are passed as **key=value** format and each key-value pair of the dict is separated by a comma.  

The syntax is  

```python
a = dict(key1="value1", key2="value2", key3="value3")
```  

The return value of this function is the prepared dict with the specified key-value pairs. If no values are specified, it returns an empty dict.

#### Keys, Values & Items

These are methods unique to the dict class and are denoted by: 

- **keys( )**  
    Returns all the keys in the dict as a special type - **dict_keys**. It is a special data type associated with the dict class where the keys are stored inside a list. It is not possible to directly access the individual keys using indexing. The syntax for this is `dict.keys()` 
    
- **values( )**  
    Returns all the values in the dict as a special type - **dict_values**. It is a special data type associated iwth dict class where all the values are stored inside a list. It is not possible to directly access the individual values using indexing. The syntax for this is `dict.values()`  
    
- **items( )**  
    Returns all the key-value pairs in the dict as a collection of tuples like **(key, value)**. The return value is a special type - **dict_items** which consists of a list of **tuples** where each tuple is a key-value pair. It is not possible to directly index the list to access the key-value pair.  
    
It is possible to convert the special types associated with dict class into a list and then index into that list to access the individual values.  

The syntax for **keys()** is `my_dict.keys()` and the syntax for **values** is `my_dict.values()`. The syntax for **items()** is `my_dict.items()`  

#### In

This keyword is used to search for a given key inside a dict. This is not a method from the dictionary class but can be used on dicts. This method returns **True** is the key is found and **False** otherwise. When applied directly on a dict, this keyword always searches for keys only.  

The syntax is `"some_key" in my_dict`  

This keyword can be combined with `dict.keys()` or `dict.values()` to search for a given key or value. Returns **True** if the search item is found and false otherwise.  

This keyword can also be combined with `dict.items()` to search for an entire item instead of an individual key or value. The syntax is  

```python
('key', 'value') in my_dict.items()
```  

It will return **True** if the entire key-value pair `('key', 'value')` is present inside the dict.

#### Pop and PopItem

The **pop("K")** method is used to remove the key-value pair for the specified key **K**. It returns the value **V** that was associated with the key **K** that was popped. Not specifying any key **K** inside the method leads to an error. This is an in-place method.  

The syntax is `dict.pop("K")`  

The **popitem()** method is used to remove the **last inserted key-value pair** int the dict. The return value is the entire key-value pair as **(key, value)**. This method does not take anything inside the method and passing values leads to error. This is an in-place method.  

The syntax is `dict.popitem()` 

#### Update

The **update(K, V')** method is used to update the value **V** of a given key **K** with the value **V'**. There are two ways to update the key.  

```python

# This will update each key-value pair
# Key value pairs are provided as key=value and separated by ,
my_dict.update(key1="value1", key2="value2", key3="value3")

# This will update each key-value pair
# Key value pairs are provided as key:value and separated by , 
# The entire list of key-value pairs to be updated are enclosed inside {}
my_dict.update({"key1": "value1", "key2": "value2", "key3": "value3"})
```  

This is an in-place method. If the key-value pairs in either of the above formats are not present in the dict, then a new entry for that key-value pair is created and stored.

#### Clear

This method removes all the items from the dict and returns an empty dict. This is an in-place method and therefore changes are applied on the dict itself. The syntax is `my_dict.clear()`  


```python
# Create a dict using the dict() fucntion
a = dict(first_name='john', last_name='doe', age=23, location='UK', sex='male')
print(a)

# An empty dictionary
e = dict()
print(e)
```

    {'first_name': 'john', 'last_name': 'doe', 'age': 23, 'location': 'UK', 'sex': 'male'}
    {}



```python
# Fetch a value using get() and default value - key exists
v = a.get('first_name', "DEFAULT")
print(v)

# Fetch a value using get() and default value - key not exists
v = a.get('some_random_key', "DEFAULT")
print(v)
```

    john
    DEFAULT



```python
# Get a list of keys using keys() and convert to list
keys = a.keys()
keys_list = list(keys)

print(f'{keys} TYPE: {type(keys)}')
print(f'{keys_list}, keys_list[0] {keys_list[0]}')
print()

# Get a list of values using values() and convert to list
values = a.values()
values_list = list(values)

print(f'{values} TYPE: {type(values)}')
print(f'{values_list}, values_list[-1] {values_list[-1]}')
print()

# Get a list of items using items() and convert to list
items = a.items()
items_list = list(items)

print(f'{items} TYPE: {type(items)}')
print(f'{items_list}, items_list[1] {items_list[1]}')
print()
```

    dict_keys(['first_name', 'last_name', 'age', 'location', 'sex']) TYPE: <class 'dict_keys'>
    ['first_name', 'last_name', 'age', 'location', 'sex'], keys_list[0] first_name
    
    dict_values(['john', 'doe', 23, 'UK', 'male']) TYPE: <class 'dict_values'>
    ['john', 'doe', 23, 'UK', 'male'], values_list[-1] male
    
    dict_items([('first_name', 'john'), ('last_name', 'doe'), ('age', 23), ('location', 'UK'), ('sex', 'male')]) TYPE: <class 'dict_items'>
    [('first_name', 'john'), ('last_name', 'doe'), ('age', 23), ('location', 'UK'), ('sex', 'male')], items_list[1] ('last_name', 'doe')
    



```python
# Check for the presence of keys
print('first_name' in keys)
print('first' in keys)
print()

# Check for the presence of values
print('john' in values)
print('max' in values)
print()

# Check for the presence of key-value pair
print(('first_name', 'john') in items)
print(('full_name', 'johndoe') in items)
```

    True
    False
    
    True
    False
    
    True
    False



```python
# Add a new key to dict
a['new_key'] = 'new_value'

print('LATEST DICT')
print(a)
print()

# Remove the last added key
s = a.popitem()

print('AFTER POPITEM')
print(s)
print(a)
print()

# Remove the next key that was added last
s = a.popitem()

print('AFTER POPITEM')
print(s)
print(a)
```

    LATEST DICT
    {'first_name': 'john', 'last_name': 'doe', 'age': 23, 'location': 'UK', 'sex': 'male', 'new_key': 'new_value'}
    
    AFTER POPITEM
    ('new_key', 'new_value')
    {'first_name': 'john', 'last_name': 'doe', 'age': 23, 'location': 'UK', 'sex': 'male'}
    
    AFTER POPITEM
    ('sex', 'male')
    {'first_name': 'john', 'last_name': 'doe', 'age': 23, 'location': 'UK'}



```python
# Remove the key 'last_name'
s = a.pop('last_name')
print(s)
print(a)
```

    doe
    {'first_name': 'john', 'age': 23, 'location': 'UK'}



```python
# Key not present leads to error
s = a.pop('no_key')
print(s)
print(a)
```


    ---------------------------------------------------------------------------

    KeyError                                  Traceback (most recent call last)

    Input In [7], in <cell line: 2>()
          1 # Key not present leads to error
    ----> 2 s = a.pop('no_key')
          3 print(s)
          4 print(a)


    KeyError: 'no_key'



```python
print('CURRENT DICT')
print(a)
print()

# Update the key for first_name and last_name
a.update(first_name="Max", last_name="Meyer")

print('AFTER UPDATE')
print(a)
```

    CURRENT DICT
    {'first_name': 'john', 'age': 23, 'location': 'UK'}
    
    AFTER UPDATE
    {'first_name': 'Max', 'age': 23, 'location': 'UK', 'last_name': 'Meyer'}



```python
print('CURRENT DICT')
print(a)
print()

# Update the key for first_name, last_name, age, sex
a.update({"first_name": "JOHN", "last_name": "DOE", "age": 55, "sex": "Male"})

print('AFTER UPDATE')
print(a)
```

    CURRENT DICT
    {'first_name': 'Max', 'age': 23, 'location': 'UK', 'last_name': 'Meyer'}
    
    AFTER UPDATE
    {'first_name': 'JOHN', 'age': 55, 'location': 'UK', 'last_name': 'DOE', 'sex': 'Male'}



```python
# Clear the dict
a.clear()
print(a)
```

    {}


### Important Links

- [Python Dicts - Complete Tutorial](https://realpython.com/python-dicts/)
- [Google For Education - Python Dicts](https://developers.google.com/edu/python/dict-files)

## [3] Tuples

A tuple is an **immutable ordered collection** of items. This means that once a tuple has been created the contents of that tuple cannot be modified. The elements in the tuple are stored in the same order in which they were specified at the time of tuple creation. A tuple is created using the pair of parenthesis **( )** enclosing the items inside it separated by a **,**  

The syntax to create a tuple is  

```python
# Tuple can hold multiple types of data 
t = (10, 20, 0, -100, 40, "hello", False, [19, 20, 45])
```  

Since a tuple is immutable by nature, therefore operations like sorting, reversing, deleting or adding new elements cannot be possible. This also makes tuple perform better than lists in general because the memory is fixed and the collection cannot be modified in any way.  

As tuples are very similar to lists (except for the immutability) operations that do not modify the tuple are the same as that on lists. The **len( )** keyword returns the number of items in the tuple and we can perform indexing operations on the tuple using **[i]** notation. We can perform slicing operations on the tuple using 
**[start_index : end_index : step]** notation.  

As tuples are immutable, they can be used as keys in a dictionary. The syntax is  

```python
# Create the tuple
t = (10, 20, "hello")

# Create the dict
d = {
    t: [10, 20, 30, 40, 50, 60]
}

# Access the values of the key in dict
print(d[t])

# Alternative access to the value of key
print(d[(10, 20, "hello")])
```


```python
# Create a tuple
t = (10, 20, 0, -100, 40, "hello", False, [19, 20, 45])

print(f"t = {t}")
print(f"len(t) = {len(t)}")
print(f"t[0] = {t[0]}")
print(f"t[-1] = {t[-1]}")
print()

# Slicing operations on tuple
slice1 = t[3:7]
slice2 = t[0:6:2]

print(f"t[3:7] is {slice1}")
print(f"t[0:6:2] is {slice2}") 
```

    t = (10, 20, 0, -100, 40, 'hello', False, [19, 20, 45])
    len(t) = 8
    t[0] = 10
    t[-1] = [19, 20, 45]
    
    t[3:7] is (-100, 40, 'hello', False)
    t[0:6:2] is (10, 0, 40)


We can also create a tuple using the **tuple( )** keyword. We can pass in a variable that contains a collection (for example another tuple or a list) or we can directly provide the values inside as a list or tuple of items. This keyword will only take one item inside the **( )** so the entire collection has to be passed.  

The syntax is  

```python
# Pass a list of items
t1 = tuple([10, 20, 30])

# Pass a tuple of items
t2 = tuple((1.5, 2.5, 3.5, 4.5))
```  

**Note**  
We can also leave the **( )** empty which results in an empty tuple. But this serves no purpose as tuple is immutable and therefore cannot be updated or modified!


```python
# Pass a list of items
t1 = tuple([10, 20, 30])

# Pass a tuple of items
t2 = tuple((1.5, 2.5, 3.5, 4.5))

print(t1)
print(t2)
```

    (10, 20, 30)
    (1.5, 2.5, 3.5, 4.5)



```python
# Empty tuple
et = tuple()
print(f"et {et} len(et) {len(et)}")

et[0] = 10
```

    et () len(et) 0



    ---------------------------------------------------------------------------

    TypeError                                 Traceback (most recent call last)

    Input In [37], in <cell line: 5>()
          2 et = tuple()
          3 print(f"et {et} len(et) {len(et)}")
    ----> 5 et[0] = 10


    TypeError: 'tuple' object does not support item assignment


### Tuple Methods

As tuples are immutable objects, there are only two methods available on the tuple class **count( )** and **index( )**  

#### Count

The **count(V)** method returns the number of times the value **V** occurs in the tuple. This method takes exactly one item inside the method - the value **V** that we want to count. If the item is present in the tuple, the count is returned as an integer. If the item is not present, the value returned is **0**  

The syntax is `tuple.count(10)` which will return the frequency (or count) of the value **10** in the tuple. If no value is specified, it leads to an error.

#### Index

The **index(V)** method returns the index of the item **V** in the tuple. Tuples are also **zero-indexed** which means the starting index of the tuple is **0** (i.e. the first element is at index 0 and so on). If **V** is present in the tuple, it returns the index as an integer. If **V** is not present, then it leads to an error. If no **V** is specified, it leads to an error.  

The syntax is `tuple.index(40)` which will return the index of the **first occurrence** of the value **40** in the list. 


```python
t = (10, 20, 10, 10, 10, 20, 30, 10, 20, 40, 60)

print(f"t = {t}\n")
print(f"t.count(10) = {t.count(10)}")
print(f"t.count(30) = {t.count(30)}")
print(f"t.count(100) = {t.count(100)}\n")

print(f"t.index(30) = {t.index(30)}")
print(f"t.index(20) = {t.index(20)}")
```

    t = (10, 20, 10, 10, 10, 20, 30, 10, 20, 40, 60)
    
    t.count(10) = 5
    t.count(30) = 1
    t.count(100) = 0
    
    t.index(30) = 6
    t.index(20) = 1


### Important Links

- [Introduction To Tuples](https://www.programiz.com/python-programming/tuple)
- [Lists And Tuples](https://realpython.com/python-lists-tuples/)

## [4] Sets

A set is an **unordered collection of unique** items. This means that in a set:

- The order in which the items are inserted is not preserved (**unordered**)
- There cannot be any repeating values in the collection (**unique**)

The notation to create a set is by enclosing the items within a pair of curly braces **{ }**. However it is important to remember, that while this is the similar syntax to create a dict, the difference is in set creation we do not provide key value pairs. We only provide a collection of items separated by a **,**  

The syntax is 

```python
s = {12, 10, "hello"}
```  

We can also create a set by using the keyword **set( )** and passing in the collection of items. The syntax is  

```python
# Create a set from a list
l = [10, 20, 30, 40]
s = set(l)

# Create a set from a tuple
t = (10, 20, 50, 100)
s = set(t)
```  

Since sets are unordered collection of items it is not possible to access the elements individually by indexing. Consider the example  

```python
s = {10, 20, 30, 40, 50, 60}

# This will work
print(s)

# This will not work
# Indexing is not possible in unordered collections
print(s[0])
print(s[-1])
```  

Since sets are **mutable** objects, we can modify them by adding items, removing items etc. However, we cannot update existing items to new value as it is not possible to individually access the element.  

Consider the set `s = {10, 20, 30, 40, 5, 60}` we cannot modify the value **5** to **50** directly by indexing. Consider the example  

```python
# A list of values - modify the value at index 4 to 50
l = [10, 20, 30, 40, 5, 60]
l[4] = 50 # No error - lists are mutable

# A set of values - modify the value at index 4 to 50
s = {10, 20, 30, 40, 5, 60}
s[4] = 50 # Error - sets are mutable but indexing is not possible
```  

Since sets do not allow duplicate values, when we create a set with duplicates, only the first occurrence of the value is considered and other copies are ignored. Consider the example  

```python
s = {10, 20, 30, 40, 10, 100, 20, 70, 30}
print(s) # Repeating values of 10, 20, 30 are ignored
```  

The **len( )** keyword is used to calculate the length of the set - the number of items inside the set.


```python
# A simple set - notice the lack of order
s = {12, -109, "hello", 0.1, False, "a", -89, 500, "Python Programming", 12, 0.1, False, -89}
print(s)
print(len(s))

# Converting the set to list - the order is the order of the original set
# When converting a set to list - first the set operations are applied, then converted to list
l = list({12, -109, "hello", 0.1, False, "a", -89, 500, "Python Programming", 12, 0.1, False, -89})
print(l)
print(len(l))
```

    {0.1, False, 'Python Programming', 'hello', -89, 12, -109, 'a', 500}
    9
    [0.1, False, 'Python Programming', 'hello', -89, 12, -109, 'a', 500]
    9



```python
# Create a set from a list
l = [10, 20, 30, 40]
s = set(l)
print(s)

# Create a set from a tuple
t = (10, 20, 50, 100)
s = set(t)
print(s)
```

    {40, 10, 20, 30}
    {100, 10, 20, 50}



```python
# A list of values - modify the value at index 4 to 50
l = [10, 20, 30, 40, 5, 60]
print(l)

l[4] = 50 # No error - lists are mutable
print(l)
print()

# A set of values - modify the value at index 4 to 50
s = {10, 20, 30, 40, 5, 60}
print(s)

s[4] = 50 # Error - sets are mutable but indexing is not possible
```

    [10, 20, 30, 40, 5, 60]
    [10, 20, 30, 40, 50, 60]
    
    {5, 40, 10, 20, 60, 30}



    ---------------------------------------------------------------------------

    TypeError                                 Traceback (most recent call last)

    Input In [62], in <cell line: 13>()
         10 s = {10, 20, 30, 40, 5, 60}
         11 print(s)
    ---> 13 s[4] = 50


    TypeError: 'set' object does not support item assignment


### Set Methods

While sets are unordered and do not allow duplicates, they are still mutable and therefore support a large number of methods on the set class. Here is a quick overview of some of the most popular ones.  

#### Add

The **add(V)** method adds the value **V** to the set. Since the order is not guaranteed, where the value **V** will be inserted cannot be determined. If the item **V** is already present in the set, the method will have no effect. The syntax is `set.add(200)` which will add the value **200** to the set. This is an in-place method.

#### Remove

The **remove(V)** method removes the item **V** from the set. The return value of this method is **None**. If the value **V** is not present in the set, it leads to an error. The syntax is `set.remove(100)` it removes the item 100 from the set if exists otherwise leads to an error.

#### Pop

The **pop( )** method is used to remove the first item of the set. While the index 0 position in a set does not exist, visually speaking, whatever is stored in the beginning of the set is printed.

Syntax is `a = set.pop()`  

This method returns the popped value as an integer. This is also an in-place method.  

---------------------------------

For the rest of these methods, sets operate like mathematical sets. We will use the below sets as examples  

```python
A = {1, 2, 3, 4, 5}
B = {4, 5, 6, 7, 8, 9, 10}
```

For every method below, the above two states of the variables **A** and **B** will be considered and all previous operations as a result of other examples shall be ignored.  


#### Difference

The **difference( )** method calculates the mathematical difference between two sets. It is equivalent to the mathematical operation $A - B$ (depending on the order) where A and B are two sets. This is not an in-place method. Consider the example  

```python
print(A.difference(B)) # Result is {1, 2, 3} because 4, 5 are common to both sets
print(B.difference(A)) # Result is {6, 7, 8, 9, 10} because 4, 5 are common to both sets
```

#### Discard

The **discard(V)** method removes the item **V** from the set if it exists. This is an in-place method. Consider the example  

```python
B.discard(10) # Result is {4, 5, 6, 7, 8, 9}
A.discard(10) # Leads to error
```

#### DifferenceUpdate

The **difference_update( )** method calculates the mathematical difference between two sets but also modifies the set in-place. The syntax is `A.difference_update(B)` and removes all the items from **A** which are common to **B**. Consider the example  

```python
A.difference_update(B) # The contents of set A is now {1, 2, 3} as 4, 5 common with set B
B.difference_update(A) # The contents of set B is {4, 5, 6, 7, 8, 9, 10} because no common items with set A
```  

Remember, this is an in-place method and therefore, when set **A** got updated in the first line (above example), the common items got removed and hence when this was used in second line, there was no common items left with set **B**  

#### Intersection

The **intersection( )** method calculates the common items between the two sets. The syntax is `A.intersection(B)` and it returns a set of items that are common to the sets **A** and **B**. For this method, `A.intersection(B)` is the same as `B.intersection(A)`. This is not an in-place method. Mathematically, this operation is equivalent to the set operation $A \bigcap\ B$  

Consider the example  

```python
print(A.intersection(B)) # Result is {4,5}
```

#### IsDisjoint

The **isdisjoint( )** method is used to check for intersection between two sets. The syntax is `A.isdisjoint(B)` and returns **False** if there are common items between the sets **A** and **B**. If there are no common items between the two sets, they are said to be disjoint and the value returned is **True**. This is not an in-place method and `A.isdisjoint(B)` is the same as `B.isdisjoint(A)`

#### IsSubset

The **issubset** method is used to check if a set is contained inside another set. The syntax is `A.issubset(B)` and it returns **True** if the items of set **A** are contained inside set **B**  
Similarly, `B.issubset(A)` returns **True** if the items of set **B** are contained inside the set **A**  

Mathematically this performs the set operation $A \subset\ B$ for `A.issubset(B)`  

Consider the example  

```python
T = {4, 5}
print(T.issubset(B)) # Result is True
```

#### IsSuperset

The **issuperset( )** method is used to check if a set is contains another set inside it. This is the opposite of the **issubset( )** method. The syntax is `A.issuperset(B)` and returns **True** if all the items of set **B** are contained inside set **A**  
Similarly, `B.issuperset(A)` returns **True** if all the items of set **A** are contained inside the set **B**  

Mathematically this performs the set operation $B \subset\ A$ for `A.issuperset(B)`  

Consider the example  

```python
T = {4, 5}
print(B.issuperset(T)) # Result is True
```

#### Union

The **union( )** method is used to create a new set from the sets **A** and **B** which combines all the unique items of these two sets. Common items in the sets are included only once. The syntax is `A.union(B)`. It is not an in-place method and returns a new set with all the unique items. Therefore, `B.union(A)` is the same as `A.union(B)`  

Mathematically, this operation is equivalent to the set operation $A \bigcup\ B$  
Consider the example below

```python
S = A.union(B)
print(S) # Result is {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
```


```python
s = {10, 20, 30, 40, 5, 60}
print(s)

# Add some items to the set
s.add(20)
s.add(200)
s.add(-20)
s.add(40)
s.add(40.0)
s.add(40.01)

print(s)
```

    {5, 40, 10, 20, 60, 30}
    {5, 40, 200, 10, 40.01, -20, 20, 60, 30}



```python
# Remove some items from the set
s.remove(200)
s.remove(40)
s.remove(30)

print(s)
```

    {5, 10, 40.01, -20, 20, 60}



```python
print(f"initial\n{s}\n")

# Pop operation on the set
v = s.pop()
print(f"popped {v} current\n{s}\n")

# Pop operation on the set
v = s.pop()
print(f"popped {v} current\n{s}\n")

# Pop operation on the set
v = s.pop()
print(f"popped {v} current\n{s}\n")
```

    initial
    {5, 10, 40.01, -20, 20, 60}
    
    popped 5 current
    {10, 40.01, -20, 20, 60}
    
    popped 10 current
    {40.01, -20, 20, 60}
    
    popped 40.01 current
    {-20, 20, 60}
    



```python
A = {1, 2, 3, 4, 5}
B = {4, 5, 6, 7, 8, 9, 10}

print(A.difference(B))
print(B.difference(A))
print()

# Original sets remain unchanged
print(A)
print(B)
```

    {1, 2, 3}
    {6, 7, 8, 9, 10}
    
    {1, 2, 3, 4, 5}
    {4, 5, 6, 7, 8, 9, 10}



```python
A = {1, 2, 3, 4, 5}
B = {4, 5, 6, 7, 8, 9, 10}

B.discard(10) 
print(B) # Set B is modified

A.discard(5)
print(A) # Set A is modified
```

    {4, 5, 6, 7, 8, 9}
    {1, 2, 3, 4}



```python
A = {1, 2, 3, 4, 5}
B = {4, 5, 6, 7, 8, 9, 10}

A.difference_update(B)
B.difference_update(A)

print(A)
print(B)
```

    {1, 2, 3}
    {4, 5, 6, 7, 8, 9, 10}



```python
A = {1, 2, 3, 4, 5}
B = {4, 5, 6, 7, 8, 9, 10}

print(A.intersection(B))
print(B.intersection(A))
```

    {4, 5}
    {4, 5}



```python
A = {1, 2, 3, 4, 5}
B = {4, 5, 6, 7, 8, 9, 10}
C = {100, 200, 300}

print(A.isdisjoint(B))
print(B.isdisjoint(C))
```

    False
    True



```python
T = {4, 5}
B = {4, 5, 6, 7, 8, 9, 10}

print(T.issubset(B))
print(B.issuperset(T))
```

    True
    True



```python
A = {1, 2, 3, 4, 5}
B = {4, 5, 6, 7, 8, 9, 10}
C = {100, 200, 300}

M = A.union(B)
N = M.union(C)

print(M)
print(N)
print()

print(A)
print(B)
print(C)
```

    {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
    {1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 200, 100, 300}
    
    {1, 2, 3, 4, 5}
    {4, 5, 6, 7, 8, 9, 10}
    {200, 100, 300}


### Important Links

- [Python Sets - Introduction](https://www.programiz.com/python-programming/set)
- [Python Sets - Complete Guide](https://realpython.com/python-sets/)

## [5] Shallow And Deep Copy

Consider a variable **var_1** in memory at a location `0x76000`  

Now, when the user creates a copy of the variable **var_1** it can be done in two ways:  

- Variable **var_1** and all copied objects point to the same memory location
- Varible **var_1** and all copied objects refer to different locations in memory (with same data initially)

Refer the diagram:  

**Initial State** 

                 ______________
                |    "hello"   |  ====> var_1
                |______________|
                0x76000  
                
**Copied Objects Refer To The Same Memory Location**

                 ______________
                |   "hello"    |  ====> var_1
                |______________|  ====> var_2 (copy of var_1)
                0x76000           
                                  
                               
**Copied Objects Refer To The Different Memory Locations** 

     ______________                   ______________
    |    "hello"   |  ====> var_1    |   "hello"    |  ====> var_2 (copy of var_1)
    |______________|                 |______________| 
    0x76000                          0x871246


### Shallow Copy

**Shallow Copy** means two or more objects are referring to the same address in memory and therfore, changes in one of the object automatically reflects in other objects. Changes in the original object reflect in the copied objects and changes in the copied objects also refer in the original objects.  


                 ______________
                |   "hello"    |  ====> var_1
                |______________|  ====> var_2 (copy of var_1)
                0x76000           
                                  


```python
# Consider the list
list_1 = [10, 20, 30, 40, 50, 60]

# Make three copies of the list
list_copy_1 = list_1
list_copy_2 = list_1
list_copy_3 = list_1

# Check the memory address of the lists
print(id(list_1))
print(id(list_copy_1))
print(id(list_copy_2))
print(id(list_copy_3))
```

    4388202432
    4388202432
    4388202432
    4388202432



```python
# Perform some operations on list_1
list_1.append(500)
list_1.insert(3, -199)
list_1.remove(50)

print(list_1)
print(list_copy_1)
print(list_copy_2)
print(list_copy_3)
```

    [10, 20, 30, -199, 40, 60, 500]
    [10, 20, 30, -199, 40, 60, 500]
    [10, 20, 30, -199, 40, 60, 500]
    [10, 20, 30, -199, 40, 60, 500]



```python
# Check the memory address of the lists
print(id(list_1))
print(id(list_copy_1))
print(id(list_copy_2))
print(id(list_copy_3))
```

    4388202432
    4388202432
    4388202432
    4388202432



```python
# Perform some operations on list_copy_1
list_copy_1.append(99)
list_copy_1.pop()

# Perform some operations on list_copy_3
list_copy_3.append(["hello", "world"])

print(list_1)
print(list_copy_1)
print(list_copy_2)
print(list_copy_3)
```

    [10, 20, 30, -199, 40, 60, 500, ['hello', 'world']]
    [10, 20, 30, -199, 40, 60, 500, ['hello', 'world']]
    [10, 20, 30, -199, 40, 60, 500, ['hello', 'world']]
    [10, 20, 30, -199, 40, 60, 500, ['hello', 'world']]


### Deep Copy

**Deep Copy** refers to objects that got copied but are stored in new memory location and do not point to the same address. Therefore, changes in any of the objects, do not reflect in the other objects. Each copied object starts out with it's fresh copy of the original data but in a new memory location.  

     ______________                   ______________
    |    "hello"   |  ====> var_1    |   "hello"    |  ====> var_2 (copy of var_1)
    |______________|                 |______________| 
    0x76000                          0x871246



```python
# Consider the list
list_1 = [10, 20, 30, 40, 50, 60]

# To make a deep copy we can use the [:] notation
# We can also make a deep copy of an object using the copy() keyword
list_copy_1 = list_1.copy()
list_copy_2 = list_1[:]

# Check the memory address of the lists
print(id(list_1))
print(id(list_copy_1))
print(id(list_copy_2))
```

    4388441344
    4388200512
    4364506304



```python
# Perform some operations on list_1
list_1.append(500)
list_1.insert(3, -199)
list_1.remove(50)

print(list_1)
print(list_copy_1)
print(list_copy_2)
```

    [10, 20, 30, -199, 40, 60, 500]
    [10, 20, 30, 40, 50, 60]
    [10, 20, 30, 40, 50, 60]



```python
# Check the memory address of the lists
print(id(list_1))
print(id(list_copy_1))
print(id(list_copy_2))
```

    4388441344
    4388200512
    4364506304



```python
# Perform some operations on list_copy_1
list_copy_1.append(99)
list_copy_1.append(0.005)
list_copy_1.append("hello")
list_copy_1.pop()

# Perform some operations on list_copy_2
list_copy_2.append(["hello", "world"])

print(list_1)
print(list_copy_1)
print(list_copy_2)
```

    [10, 20, 30, -199, 40, 60, 500]
    [10, 20, 30, 40, 50, 60, 99, 0.005]
    [10, 20, 30, 40, 50, 60, ['hello', 'world']]


**Note**  
It is important to remember that directly using the assignment operator **=** to copy objects may have unintended consequences! It is always safer to use deep copy than shallow copy especially when working with data structures or collections. 

### Important Links

- [Shallow And Deep Copy - Introduction](https://www.programiz.com/python-programming/shallow-deep-copy)
- [Shallow And Deep Copy - Python Documentation](https://docs.python.org/3/library/copy.html)
