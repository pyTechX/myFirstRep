from sys import argv
genius = raw_input("Give the genius argument: ") 
perfect = raw_input("Give the perfect argument: ") 
bellisima = raw_input("Give the bellisima argument: ") 
 
script, first, second, third, forth = argv     #te argumenty podawane sa z linii komend i sa niezbedne do
																	#uruchomienia skryptu

print "The name of script is: ", script
print "The first arg is: ", first
print "The 2nd arg is: ", second
print "The 3rd  arg is: ", third
print "The 4th arg ", forth
print "\nThe genius argument's value is '%s'" % genius	 #te argumenty sa podawane podczas
print "The perfect argument's value is '%s'" % perfect    #wykonywania skryptu 
print "The bellisima argument's value is '%s'" % bellisima
