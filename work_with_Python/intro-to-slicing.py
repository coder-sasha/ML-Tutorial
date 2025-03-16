"""
This script demonstrates the work of Python strings and lists slicing
The script output:
Work with strings:
	First 15: 'a string which ',
	Middle 20: 'which contains no me',
	Last 10: 'ignificant'
	Find the place of 'message': 39
	Find the place of 'next message': 39
	Find the place of ' a ': -1
	Replace by 'informative':
	 a string which contains no meaning, no message nor anything meaningful or informative

Work with lists:
	This is a new made list: ['a', 'string', 'which', 'contains', 'no', 'meaning,', 'no', 'message', 'nor', 'anything', 'meaningful', 'or', 'significant'] of 13 elements
	Basic list slicing example: (indices 2 to 4): ['which', 'contains', 'no']
	Slicing with a step example (every 2nd element): ['a', 'which', 'no', 'no', 'nor', 'meaningful', 'significant']
	Negative indexing example (last three items): ['meaningful', 'or', 'significant']
	Reverse slicing - reverse the list example (reversed list): ['significant', 'or', 'meaningful', 'anything', 'nor', 'message', 'no', 'meaning,', 'no', 'contains', 'which', 'string', 'a']
	Get the first half of the list example (first half of list): ['a', 'string', 'which', 'contains', 'no', 'meaning,']

"""

# slicing strings
main_string = "a string which contains no meaning, no message nor anything meaningful or significant"

# basic slicing 
first_15 = main_string[0:15]
mid_20 = main_string[9:29]

# negative indexing - get the last 10 characters
last_10 = main_string[-10:]
print("Work with strings:")
print(f"\tFirst 15: '{first_15}',\n\tMiddle 20: '{mid_20}',\n\tLast 10: '{last_10}'")

# search for substring
print(f"\tFind the place of 'message': {main_string.find('message')}")
print(f"\tFind the place of 'next message': {main_string.find('message', 3)}")
print(f"\tFind the place of ' a ': {main_string.find(' a ')}")

# 
print("\tReplace by 'informative':\n\t", main_string.replace("significant", "informative"))

# slicing lists
print("\nWork with lists:")
main_list = main_string.split()
print(f"\tThis is a new made list: {main_list} of {len(main_list)} elements")

# basic slicing 
slice1 = main_list[2:5]
print("\tBasic list slicing example: (indices 2 to 4):", slice1)

# slicing with a step - get every second element from the list
slice2 = main_list[::2]
print("\tSlicing with a step example (every 2nd element):", slice2)

# negative indexing - get the last three items
slice3 = main_list[-3:]
print("\tNegative indexing example (last three items):", slice3)

# reverse slicing - reverse the list
slice4 = main_list[::-1]
print("\tReverse slicing - reverse the list example (reversed list):", slice4)

# slicing to get the first half of the list
half_index = len(main_list) // 2
slice5 = main_list[:half_index]
print("\tGet the first half of the list example (first half of list):", slice5)

print("\n\nthat's all   :) ")
"""
First 10: a string w, Middle 10: hich conta, Last Five Chars: ignificant
find 'message': {main_string.find('message')}
find 'next message': {main_string.find('message', 3)}
find ' a ': {main_string.find(' a ')}
replace by meaningful: a string which contains no meaning, no message nor anything meaningful or meaningful
This is a new made list: ['a', 'string', 'which', 'contains', 'no', 'meaning,', 'no', 'message', 'nor', 'anything', 'meaningful', 'or', 'significant'] of 13 elements
basic slicing example: (indices 2 to 4): ['which', 'contains', 'no']
slicing with a step example (every 2nd element): ['a', 'which', 'no', 'no', 'nor', 'meaningful', 'significant']
negative indexing example (last three items): ['meaningful', 'or', 'significant']
reverse slicing - reverse the list example (reversed list): ['significant', 'or', 'meaningful', 'anything', 'nor', 'message', 'no', 'meaning,', 'no', 'contains', 'which', 'string', 'a']
get the first half of the list example (first half of list): ['a', 'string', 'which', 'contains', 'no', 'meaning,']
that's all :) 
"""


