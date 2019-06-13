****************************************
#                Tests                 *
****************************************

>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
## 1. Base Class (base.py, __init__.py)          #
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
1. Test valid id
2. Test multiple ids
3. Test the exact ids __Important__
4. Test `str` as parameter
5. Test `list` as parameter
6. Test `tuple` as parameter
7. Test `dict` as parameter
8. Test `None` as parameter
9. Test `set` as parameter
10. Test `float` as parameter
11. Test `functions` as parameter
12. Test `inf` as parameter
13. Test if `__nb_objects` is private class attribute

>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
## 2. First Rectangle (rectangle.py)             #
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
1. Test valid id, call _super()_
2. Test multiple ids
3. Test valid parameters to __init__
4. Test default values for `x` and `y`
5. Test whether all parameters are private
6. Test getters and setters
7. Test if wrong number of arguments are provided `(0, 1, 6) arguments`

>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
## 3. Validate attributes (rectangle.py)         #
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
1. Test `str` as parameter
2. Test `list` as parameter
3. Test `tuple` as parameter
4. Test `dict` as parameter
5. Test `None` as parameter
6. Test `set` as parameter
7. Test `float` as parameter
8. Test `functions` as parameter
9. Test if you are calling setters in __init__
10. `Nan`
10. `Frozen set`

>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
## 4. Area Frist (rectangle.py)                  #
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
1. Test area() with valid parameters

>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
## 5. Display #0 (rectangle.py)                  #
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
1. Test display() without x and y
2. Test display() with different sizes

>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
## 6. __str__ (rectangle.py)                     #
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
1. Test valid params
2. Test default params

>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
## 7. Display #1 (rectangle.py)                  #
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
1. Test defaults params
2. Test with `x` and `y`

>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
## 8. Update #0 (rectangle.py)                   #
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
1. Test correct order of args
2. Test corect types of args
3. Test if value is > 0

>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
## 9. Update #1 (rectangle.py)                   #
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
1. Test correct order of `kwargs`
2. Test skip the `kwargs` if `args` is not empty
3. Test to assign only valid `keys`
4. Test correct types of `kwargs`

>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
## 10. And now, the Square! (square.py)          #
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
1. Test whether `Square` uses __init__ logic of `Rectangle`
2. Test whether new attribute not created
3. Test arg validation inherited from `Rectangle`
4. Test __str__ method

>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
## 11. Square size (square.py)                   #
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
1. Test setters and getters for `size`
2. Test whether exception msg show `width`
3. Test size validation

>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
## 12. Square update (square.py)                 #
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
1. 1. Test correct order of args
2. Test coorect types of args, value > 0
3. Test correct order of `kwargs`
4. Test skip the `kwargs` if `args` is not empty
5. Test to assign only valid `keys`
6. Test correct types of `kwargs`

>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
## 13. Rectangle dictionary (rectangle.py)       #
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
1. Test whether dictionary contains correct attributes
2. Test whether return object is `dict`

>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
## 14. Square dictionary (square.py)             #
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
1. Test whether dictionary contains correct attributes
`id, size, x, y`
2. Test whether return object is `dict`

>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
## 15. Square dictionary (square.py)             #
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
1. Test if arg is a list of dicts
2. Test with many dicts
3. Test if the return object is str
4. Convert to JSON and test

>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
## 16. JSON string to file (square.py)           #
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
1. Test if the arg is list of instances
2. Test if list_objs is None save empty list
3. Test filename
4. Test whether file is overwritten or created

