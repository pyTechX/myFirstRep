formatter = "%r %r %r %r"
print formatter % (1, 2, 3, 4)
print formatter % ("one", "two", "three", "four")
print formatter % (True, False, False, True)
print formatter % (formatter, formatter, formatter, formatter)
print formatter % (
		"I had this thing.",
		"That you could type up right.",
		"But it didn't sing.",
		"So I said goodnight."
	)
	# %r format character is for row variable data. We can use it to put into a string
	# both string, numbers and booleans
	# it also return string with single or double-quote
    #	(it depends whether there is a single-quote inside the variable')
	
	# %d format require a number values
	
	# %s format character can be used as a %r but it returns string without quotes