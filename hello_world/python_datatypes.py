# A data type is an attribute associated with a piece of data
# that tells a computer system how to interpret its value
# TO DETERMINE A TYPE OF VARIABLE PYTHON ALSO PROVIDES A FUNCTION NAMES TYPE.
print(type("hello"))

# LITERALS: 1.Numeric, 2.Sequence, 3.Dictionary, 4.Boolean and 5.Set.

# NUMERIC: Integer-Float-Complex Number
a, b = 10, -10  # integer
a, b = 10.5, -10.5  # float
a = 10+10j  # complex number

# SEQUENCE: Lists-Strings-Tuples
name = "Jesse"  # string
example_list = [1, "hello", 4.5, 'A']  # list
print(type(example_list))
# tuples are similar to lists but only that they cannot be changed i.e an element of the sequence cannot be re-assigned.

# DICTIONARY: Key-Value Pair.
ed = {'a': 22, 'b': 44.4}
ed['a']

# BOOLEAN: True-False Statement.

# SET: unordered and non-indexed collection of non-repeated values.
example_set = {1, "hello", 4.5, 'A'}
print(type(example_set))

# Python automatically infers the DataType when the variable is being assigned! 