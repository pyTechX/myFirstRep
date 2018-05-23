print """
Backslash \\ blabla
Single-quote \' blabla
Double-quote \" blabla
ASCII bell (BEL) \a blabla
ASCII backspace (BS) \b blabla
ASCII formfeed (FF) \f blabla
ASCII linefeed (LF) \n blabla
Character named name in the Unicode database (Unicode only) \N {name}  blabla
carriage return (CR) \r ASCII  blabla
ASCII horizontal tab \t  blabla
Character with 16-bit hex value xxxx (Unicode only) \uxxxx blabla
Character with 32-bit hex value xxxxxxxx (Unicode only) \Uxxxxxxxx blabla
ASCII vertical tab (VT) \v blabla
Character with octal value oo \ooo blabla
"""
# Character with hex value hh \xhh blabla ---- doesn't work

while True:
	for i in ["/","-","|","//","|"]:
		print "%s\r"  % i,

