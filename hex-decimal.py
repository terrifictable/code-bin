# Code by TerrificTable (https://github.com/TerrificTable)

def encode_hex(vars):
	valHex = []
	for var in vars:
		valHex.append(hex(ord(var)).replace("0x", "").upper())

	print(*valHex)

def encode_decimal(vars):
	valDecimal = []
	for var in vars:
		var = hex(ord(var))
		valDecimal.append(int(var, 16))
	print(*valDecimal)

def decode_hex(vars):
	valDecoded = "\\x" + vars.replace("0x", "\\x").replace(" ", "\\x")
	exec(f"print('{valDecoded}')")

def decode_decimal(vars):
	valDecoded = []
	vars = vars.split(" ")
	for var in vars:
		if var != " ":
			var = chr(int(var))
			valDecoded.append(var)
	print(*valDecoded)
	

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
