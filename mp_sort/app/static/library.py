from org.transcrypt.stubs.browser import *
import random

array = []

def gen_random_int(number, seed):
    my_list = [i for i in range(number)]
    random.seed(seed)
    random.shuffle(my_list)
    result = my_list
    return result

def generate():
	global array

	number = 10
	seed = 200

	gen_random_int(number, seed)

	# call gen_random_int() with the given number and seed
	# store it to the global variable array

	array = gen_random_int(number, seed)

	# convert the items into one single string 
	# the number should be separated by a comma
	# and a full stop should end the string.
	
	array_str = ','.join([str(i) for i in array]) + '.'

	console.log(array, "\n", array_str)

	# This line is to placed the string into the HTML
	# under div section with the id called "generate"	
	document.getElementById("generate").innerHTML = array_str
	

def sortnumber1():
	'''	This function is used in Exercise 1.
		The function is called when the sort button is clicked.

		You need to do the following:
		- get the list of numbers from the global variable array and 
			copy it to a new list
		- call your sort function, either bubble sort or insertion sort
		- create a string of the sorted numbers and store it in array_str
	'''
	n = len(array)
	for i in range(1, n):
		for j in range(1, n):
			first_num_index = j - 1
			second_num_index = j
			if array[first_num_index] > array[second_num_index]:
				array[first_num_index], array[second_num_index] = array[second_num_index], array[first_num_index]

	array_str = ','.join([str(i) for i in array]) + '.'
		
	document.getElementById("sorted").innerHTML = array_str


def sortnumber2():
	'''	This function is used in Exercise 2.
		The function is called when the sort button is clicked.

		You need to do the following:
		- Get the numbers from a string variable "value".
		- Split the string using comma as the separator and convert them to 
			a list of numbers
		- call your sort function, either bubble sort or insertion sort
		- create a string of the sorted numbers and store it in array_str
	'''
	# The following line get the value of the text input called "numbers"
	value = document.getElementsByName("numbers")[0].value

	# Throw alert and stop if nothing in the text input
	if value == "":
		window.alert("Your textbox is empty")
		return
	else:
		value = value.split(",")

	# Your code should start from here
	# store the final string to the variable array_str
	
	n = len(array)
	for i in range(1, n):
		for j in range(1, n):
			first_num_index = j - 1
			second_num_index = j
			if array[first_num_index] > array[second_num_index]:
				array[first_num_index], array[second_num_index] = array[second_num_index], array[first_num_index]

	if array == "":
		window.alert("Your textbox is empty")
		return

	array_str = ','.join([str(i) for i in array]) + '.'

	document.getElementById("sorted").innerHTML = array_str