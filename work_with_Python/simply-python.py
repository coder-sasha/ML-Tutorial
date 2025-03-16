"""
This script demonstrates some basic Python idioms
The output:
=== using variables swap:
a=42 and b=foo
after swap: a=foo and b=42

=== using function zip():
('x', 3, ':)')
('y', 5, ':>)')
('z', 7, '-)')

=== using enumerate:
word Programming is #0
word in is #1
word Python is #2
word is is #3
word fun is #4
word and is #5
word profit is #6

=== using _:
Programming In Python Is Fun And Profit

=== using range():
word Programming is #0
word in is #1
word Python is #2
word is is #3
word fun is #4
word and is #5
word profit is #6

=== list comprehension:
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even list after comprehension
[2, 4, 6, 8, 10]

===  dictionary comprehension:
new_dict:
{1: 'number one', 2: 'number two', 3: 'number three', 4: 'number four', 5: 'number five'}

=== flatten list using comprehension:
nested list:[[1, 2, 3], [4, 5], [6], [7, 8], [9, 10, 11]]
new flat list: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]

=== sort a dictionary by values:
unsorted dictionary: {'X': 10, 'XXXXII': 42, 'III': 3, 'XV': 15, 'M': 100, 'IV': 4}
sorted by values:[('III', 3), ('IV', 4), ('X', 10), ('XV', 15), ('XXXXII', 42), ('M', 100)]
...and sorted in reverse order:[('M', 100), ('XXXXII', 42), ('XV', 15), ('X', 10), ('IV', 4), ('III', 3)]
"""

# usage of variables swap 
print("=== using variables swap:")
a = 42
b = "foo"
print(f"a={a} and b={b}")

a, b = b, a 
print(f"after swap: a={a} and b={b}")

# usage of zip()
print("\n=== using function zip():")
l1 = ["x", "y", "z"]
l2 = [3, 5, 7, 9]
l3 = [":)", ":>)", "-)"]
for l in zip(l1, l2, l3):
	print(l)

# usage of enumerate	
print("\n=== using enumerate:")
words = ["Programming", "in", "Python", "is", "fun", "and", "profit"]
for num, wrd in enumerate(words):
	print(f"word {wrd} is #{num}")

# usage of Python special variable '_'
print("\n=== using _:")
for _ in words:
	print(_.title(), end=' ')
print()

# usage of range()
print("\n=== using range():")
for num in range(len(words)):
	print(f"word {words[num]} is #{num}")

	
# list comprehension
print("\n=== list comprehension:")
init_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_list = [l for l in init_list if l % 2 == 0]
print(f"{init_list}\neven list after comprehension\n{even_list}")

# dictionary comprehension
print("\n===  dictionary comprehension:")
or_dict = {1: 'one', 2: 'two', 3: 'three', 4: 'four', 5: 'five'}
new_dict = {key:'number ' + value for (key, value) in or_dict.items()}
print(f"new_dict:\n{new_dict}")

# using list comprehension to flatten a list
print("\n=== flatten list using comprehension:")
nested_list = [[1, 2, 3], [4, 5], [6], [7, 8], [9, 10, 11]]
flat_list = [item for sub_list in nested_list for item in sub_list]
print(f"nested list:{nested_list}\nnew flat list: {flat_list}")

# sort a dictionary by values
print("\n=== sort a dictionary by values:")
d_unsorted = {'X': 10, 'XXXXII': 42, 'III': 3, 'XV': 15, 'M': 100, 'IV': 4}
d_sorted = sorted(d_unsorted.items(), key=lambda k_v: k_v[1])
print(f"unsorted dictionary: {d_unsorted}\nsorted by values:{d_sorted}")

# ...and in reverse order:
d_sorted = sorted(d_unsorted.items(), key=lambda k_v: k_v[1], reverse=True)
print(f"...and sorted in reverse order:{d_sorted}")

with open('havefun.txt', 'r') as f:
    print(f.read())
    