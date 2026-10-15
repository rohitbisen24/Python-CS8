
# try: 
#    fah = int(input("enter fah : "))
#    cel = (fah- 32) * 5/9 
#    print(int(cel))

# except: 
#    print(f"input glt hai plese enter vailed  fah.")  


# try: 
#    cel = int(input("enter celsius : "))
#    fah = (cel * 9/5) + 32
#    print(fah)

# except: 
#    print(f"input glt hai plese enter vailed  celsius.")  


## Types of Errors in Python

### 1. Syntax Error

# Error caused by incorrect Python syntax or rules.

# Common types:

# * Missing `:`
# * Wrong indentation
# * Missing brackets `()`, `[]`
# * Missing quotes `" "`
# * Misspelled keywords

# Example:

# ```python
# if age > 18
#     print("Eligible")
# ```

# ### 2. Runtime Error (Exceptions)

# Error that occurs while the program is running.

# Common types:

# * `ValueError` — Invalid value
# * `TypeError` — Wrong data type
# * `ZeroDivisionError` — Division by zero
# * `IndexError` — Invalid list index
# * `KeyError` — Invalid dictionary key
# * `NameError` — Undefined variable
# * `FileNotFoundError` — File does not exist

# ### 3. Logical Error

# The program runs successfully, but produces an incorrect result.

# Common causes:

# * Wrong formula
# * Wrong condition
# * Wrong operator
# * Wrong calculation
# * Incorrect logic

# Example:

# ```python
# a = 10
# b = 20

# print(a - b)   # Wrong if we wanted addition
# ```



