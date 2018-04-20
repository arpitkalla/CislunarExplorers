import _ax5043
import time

usleep = lambda x: time.sleep(x/1000000.0)

class AX5043():

	def init(self):
		status = _ax5043.read_reg(AX_REG_PWRMODE)
	    print("Power mode : {}".format(status))

	    version = _ax5043.read_reg(AX_REG_SILICONREVISION)
	    print("Silicon Revision : {}".format(version))
	    
	    state = _ax5043.read_reg(AX_REG_RADIOSTATE)
	    print("Radio State : {}".format(state))
	    
		# turn off receiver
		_ax5043.write_reg(AX_REG_PWRMODE,PWRMODE_STANDBY)
		usleep(100)
		
		# release FIFO ports
		_ax5043.write_reg(AX_REG_PWRMODE,PWRMODE_FIFOON)
		usleep(100)

		# Init Transceiver
		_ax5043.init()

	def set_mode(is_tranmission):
		if(is_tranmission):
			# ax5043_TX();
		else:
			# ax5043_RX();

	def write_packets(data):
		data_byte = bytearray(data)
		for byte in data_byte:
			hex_byte = hex(byte)
			# print(hex_byte)
			_ax5043.write(hex_byte)

	def read_packets():
		return None


if __name__ == "__main__":
	write_packets("HelloWorld")