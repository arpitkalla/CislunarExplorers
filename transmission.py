# import _ax5043

def init():
	return None

def set_mode(is_tranmission):
	return None

def write_packets(data):
	data_byte = bytearray(data)
	for byte in data_byte:
		hex_byte = hex(byte)
		print(hex_byte)
		# _ax5043.write(hex_byte)

def read_packets():
	return None


if __name__ == "__main__":
	write_packets("HelloWorld")