print "How old are you?",
age = raw_input()
print "How tall are you?",
height = raw_input()
print "How much do you weight?",
weight = raw_input()

print "So, you're %r old, %r tall and %r heavy." % (age, height, weight), '\n\n'

print "Enter some string, because it's needed to prompt it by using '%r' clause"
someString = raw_input()
print "So, using that clause, entered input seems like %r" % someString
