import smbus2
import logging

I2C_ADDR  = (0X53)
I2C_BUS = 1

LTR390_MAIN_CTRL = (0x00)  # Main control register
LTR390_MEAS_RATE = (0x04)  # Resolution and data rate
LTR390_GAIN = (0x05)  # ALS and UVS gain range
LTR390_PART_ID = (0x06)  # Part id/revision register
LTR390_MAIN_STATUS = (0x07)  # Main status register
LTR390_ALSDATA = (0x0D)  # ALS data lowest byte, 3 byte
LTR390_UVSDATA = (0x10)  # UVS data lowest byte, 3 byte
LTR390_INT_CFG = (0x19)  # Interrupt configuration
LTR390_INT_PST = (0x1A)  # Interrupt persistance config
LTR390_THRESH_UP = (0x21)  # Upper threshold, low byte, 3 byte
LTR390_THRESH_LOW = (0x24)  # Lower threshold, low byte, 3 byte

#ALS/UVS measurement resolution, Gain setting, measurement rate
RESOLUTION_20BIT_TIME400MS = (0X00)
RESOLUTION_19BIT_TIME200MS = (0X10)
RESOLUTION_18BIT_TIME100MS = (0X20)#default
RESOLUTION_17BIT_TIME50MS  = (0x3)
RESOLUTION_16BIT_TIME25MS  = (0x40)
RESOLUTION_13BIT_TIME12_5MS  = (0x50)
RATE_25MS = (0x0)
RATE_50MS = (0x1)
RATE_100MS = (0x2)# default
RATE_200MS = (0x3)
RATE_500MS = (0x4)
RATE_1000MS = (0x5)
RATE_2000MS = (0x6)

# measurement Gain Range.
GAIN_1  = (0x0)
GAIN_3  = (0x1)# default
GAIN_6 = (0x2)
GAIN_9 = (0x3)
GAIN_18 = (0x4)

class LTR390:
    def __init__(self, address = I2C_ADDR, bus = I2C_BUS) -> None:
        self.logger = logging.getLogger(f"EnvironmentLog.UV")
        self.i2c = smbus2.SMBus(bus)
        self.address = address
        self.Id = self._readByte(LTR390_PART_ID)

        if(self.Id != 0xB2):
            self.logger.error("read Id failed, check hardware")
            return
        
        self._writeByte(LTR390_MAIN_CTRL, 0x0A) # UVS active mode
        self._writeByte(LTR390_MEAS_RATE, RESOLUTION_20BIT_TIME400MS | RATE_2000MS) # Resolution=18bits, Meas Rate = 100ms
        self._writeByte(LTR390_GAIN, GAIN_3) #  Gain Range=3.
        # self.Write_Byte(LTR390_INT_CFG, 0x34) # UVS_INT_EN=1, Command=0x34
		# self.Write_Byte(LTR390_GAIN, GAIN_3) #  Resolution=18bits, Meas Rate = 100ms

    def _readByte(self, cmd):
        return self.i2c.read_byte_data(self.address, cmd)

    def _writeByte(self, cmd, val):
        self.i2c.write_byte_data(self.address, cmd, val)

    def getUV(self):
        Data1 = self._readByte(LTR390_UVSDATA)
        Data2 = self._readByte(LTR390_UVSDATA + 1)
        Data3 = self._readByte(LTR390_UVSDATA + 2)
        uv =  (Data3 << 16)| (Data2 << 8) | Data1
        UVS = Data3*65536+Data2*256+Data1
        return UVS

    def getALS(self):
        data = self._readByte(LTR390_ALSDATA)
        data2 = self._readByte(LTR390_ALSDATA + 1)
        data3 = self._readByte(LTR390_ALSDATA + 2)
        return data