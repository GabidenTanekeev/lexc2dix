from parser import lex, yacc

def main():
	is_file_open = False
	file_name = r/''/
	try:
		my_file = open(file_name, mode = "r")
		is_file_open = True
	except FileNotFoundError:
		print("File not found!")
	except IOError:
		print("IOError!")
	except:
		print("Weird!!")

	multichar_symbols_parser()

def multichar_symbols_parser():
	"""The module to parse Multichar_symbols section"""
	print("Multichar_symbols")

if __name__ == '__main__':
	main()
