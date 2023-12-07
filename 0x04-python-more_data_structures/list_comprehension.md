1. **Basic Transformation:**

   Creating a new list by applying a transformation to each element of an iterable.

   ```python
   new_list = [expression for item in iterable]
   ```

   Example:
   ```python
   numbers = [1, 2, 3, 4, 5]
   squared_numbers = [x ** 2 for x in numbers]
   ```

2. **Filtering with a Condition:**

   Creating a new list by filtering elements from an iterable based on a condition.

   ```python
   new_list = [expression for item in iterable if condition]
   ```

   Example:
   ```python
   numbers = [1, 2, 3, 4, 5]
   even_numbers = [x for x in numbers if x % 2 == 0]
   ```

3. **Combining Two Lists:**

   Creating a new list by combining elements from two or more iterables.

   ```python
   new_list = [expression for item1, item2 in zip(iterable1, iterable2)]
   ```

   Example:
   ```python
   names = ["Alice", "Bob", "Charlie"]
   ages = [25, 30, 28]
   person_info = [(name, age) for name, age in zip(names, ages)]
   ```

4. **Nested List Comprehensions:**

   Creating a new list that involves nested iterations.

   ```python
   new_list = [expression for item1 in iterable1 for item2 in iterable2]
   ```

   Example:
   ```python
   matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
   flattened_matrix = [x for row in matrix for x in row]
   ```

5. **Conditional Transformation:**

   Applying different transformations based on a condition.

   ```python
   new_list = [expression1 if condition else expression2 for item in iterable]
   ```

   Example:
   ```python
   numbers = [1, 2, 3, 4, 5]
   modified_numbers = [x if x % 2 == 0 else x * 2 for x in numbers]
   ```

6. **Using Functions:**

   Applying a function to each element of an iterable.

   ```python
   new_list = [function(item) for item in iterable]
   ```

   Example:
   ```python
   words = ["apple", "banana", "cherry"]
   uppercase_words = [word.upper() for word in words]
   ```

These are just some of the common patterns for list comprehensions. List comprehensions are a powerful and concise way to create new lists in Python by performing various operations on iterables.
