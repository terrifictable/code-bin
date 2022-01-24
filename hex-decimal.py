# Code by TerrificTable (https://github.com/TerrificTable)

def encode_hex(vars):
	valHex = []
	for var in vars:
		valHex.append(hex(ord(var)).replace("0x", "").upper()) # Encode str(var) -> hex
	print(*valHex) # print content of list

def encode_decimal(vars):
	valDecimal = []
	for var in vars:
		var = hex(ord(var)) # encode str(var) -> hex
		valDecimal.append(int(var, 16)) # encode hex(var) -> int/decimal
	print(*valDecimal) # print list

def decode_hex(vars):
	valDecoded = "\\x" + vars.replace("0x", "\\x").replace(" ", "\\x") # add \x infront of hex...
	exec(f"print('{valDecoded}')") # execute printstatement which will NOT give you the \x2E for example it will give you "." 

def decode_decimal(vars):
	valDecoded = []
	vars = vars.split(" ") # split decimal
	for var in vars:
		if var != " ": # unnesesary if
			var = chr(int(var)) # int(var) -> chr
			valDecoded.append(var)
	print(*valDecoded) # print list
	

### ---"Menu"--- ###
print(" 1 > Encode Hex\n 2 > Encode Decimal\n 3 > Decode Hex\n 4 > Decode Decimal\n")
operation = input("OP > ")
vars = input("Hex/Decimal/String: ")


if operation == "1":
	encode_hex(vars)
elif operation == "2":
	encode_decimal(vars)
elif operation == "3":
	decode_hex(vars)
elif operation == "4":
	decode_decimal(vars)
else:
	print("Invalid Input")
