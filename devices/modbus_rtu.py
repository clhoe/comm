
import serial

class modbus_rtu:

    def __init__(self, serialport, baudrate, parity, stopbits):

        self.serial = serial.Serial(
            port=serialport,
            baudrate=baudrate,
            parity=parity,
            stopbits=stopbits
        )

        self.mb = mb_rtu.RtuMaster(self.serial)
        mb.set_timeout(1)


    def read(self, addr, fn, reg):
        r=mb.execute(addr, fn, reg) 
        pass

    def write(self, addr, fn, reg, value):
        r=mb.execute(addr, fn, reg, value) 
        pass



