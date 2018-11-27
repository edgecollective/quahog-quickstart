
import time
import utime
from micropython import const
from machine import Pin

_RH_RF95_REG_00_FIFO                              = const(0x00)
_RH_RF95_REG_01_OP_MODE                           = const(0x01)
_RH_RF95_REG_02_RESERVED                          = const(0x02)
_RH_RF95_REG_03_RESERVED                          = const(0x03)
_RH_RF95_REG_04_RESERVED                          = const(0x04)
_RH_RF95_REG_05_RESERVED                          = const(0x05)
_RH_RF95_REG_06_FRF_MSB                           = const(0x06)
_RH_RF95_REG_07_FRF_MID                           = const(0x07)
_RH_RF95_REG_08_FRF_LSB                           = const(0x08)
_RH_RF95_REG_09_PA_CONFIG                         = const(0x09)
_RH_RF95_REG_0A_PA_RAMP                           = const(0x0a)
_RH_RF95_REG_0B_OCP                               = const(0x0b)
_RH_RF95_REG_0C_LNA                               = const(0x0c)
_RH_RF95_REG_0D_FIFO_ADDR_PTR                     = const(0x0d)
_RH_RF95_REG_0E_FIFO_TX_BASE_ADDR                 = const(0x0e)
_RH_RF95_REG_0F_FIFO_RX_BASE_ADDR                 = const(0x0f)
_RH_RF95_REG_10_FIFO_RX_CURRENT_ADDR              = const(0x10)
_RH_RF95_REG_11_IRQ_FLAGS_MASK                    = const(0x11)
_RH_RF95_REG_12_IRQ_FLAGS                         = const(0x12)
_RH_RF95_REG_13_RX_NB_BYTES                       = const(0x13)
_RH_RF95_REG_14_RX_HEADER_CNT_VALUE_MSB           = const(0x14)
_RH_RF95_REG_15_RX_HEADER_CNT_VALUE_LSB           = const(0x15)
_RH_RF95_REG_16_RX_PACKET_CNT_VALUE_MSB           = const(0x16)
_RH_RF95_REG_17_RX_PACKET_CNT_VALUE_LSB           = const(0x17)
_RH_RF95_REG_18_MODEM_STAT                        = const(0x18)
_RH_RF95_REG_19_PKT_SNR_VALUE                     = const(0x19)
_RH_RF95_REG_1A_PKT_RSSI_VALUE                    = const(0x1a)
_RH_RF95_REG_1B_RSSI_VALUE                        = const(0x1b)
_RH_RF95_REG_1C_HOP_CHANNEL                       = const(0x1c)
_RH_RF95_REG_1D_MODEM_CONFIG1                     = const(0x1d)
_RH_RF95_REG_1E_MODEM_CONFIG2                     = const(0x1e)
_RH_RF95_REG_1F_SYMB_TIMEOUT_LSB                  = const(0x1f)
_RH_RF95_REG_20_PREAMBLE_MSB                      = const(0x20)
_RH_RF95_REG_21_PREAMBLE_LSB                      = const(0x21)
_RH_RF95_REG_22_PAYLOAD_LENGTH                    = const(0x22)
_RH_RF95_REG_23_MAX_PAYLOAD_LENGTH                = const(0x23)
_RH_RF95_REG_24_HOP_PERIOD                        = const(0x24)
_RH_RF95_REG_25_FIFO_RX_BYTE_ADDR                 = const(0x25)
_RH_RF95_REG_26_MODEM_CONFIG3                     = const(0x26)

_RH_RF95_REG_40_DIO_MAPPING1                      = const(0x40)
_RH_RF95_REG_41_DIO_MAPPING2                      = const(0x41)
_RH_RF95_REG_42_VERSION                           = const(0x42)

_RH_RF95_REG_4B_TCXO                              = const(0x4b)
_RH_RF95_REG_4D_PA_DAC                            = const(0x4d)
_RH_RF95_REG_5B_FORMER_TEMP                       = const(0x5b)
_RH_RF95_REG_61_AGC_REF                           = const(0x61)
_RH_RF95_REG_62_AGC_THRESH1                       = const(0x62)
_RH_RF95_REG_63_AGC_THRESH2                       = const(0x63)
_RH_RF95_REG_64_AGC_THRESH3                       = const(0x64)

# RH_RF95_REG_01_OP_MODE                             0x01
_RH_RF95_LONG_RANGE_MODE                     = const(0x80)
_RH_RF95_ACCESS_SHARED_REG                   = const(0x40)
_RH_RF95_MODE                                = const(0x07)
_RH_RF95_MODE_SLEEP                          = const(0x00)
_RH_RF95_MODE_STDBY                          = const(0x01)
_RH_RF95_MODE_FSTX                           = const(0x02)
_RH_RF95_MODE_TX                             = const(0x03)
_RH_RF95_MODE_FSRX                           = const(0x04)
_RH_RF95_MODE_RXCONTINUOUS                   = const(0x05)
_RH_RF95_MODE_RXSINGLE                       = const(0x06)
_RH_RF95_MODE_CAD                            = const(0x07)

# RH_RF95_REG_09_PA_CONFIG                           0x09
_RH_RF95_PA_SELECT                           = const(0x80)
_RH_RF95_MAX_POWER                           = const(0x70)
_RH_RF95_OUTPUT_POWER                        = const(0x0f)

# RH_RF95_REG_0A_PA_RAMP                             0x0a
_RH_RF95_LOW_PN_TX_PLL_OFF                   = const(0x10)
_RH_RF95_PA_RAMP                             = const(0x0f)
_RH_RF95_PA_RAMP_3_4MS                       = const(0x00)
_RH_RF95_PA_RAMP_2MS                         = const(0x01)
_RH_RF95_PA_RAMP_1MS                         = const(0x02)
_RH_RF95_PA_RAMP_500US                       = const(0x03)
_RH_RF95_PA_RAMP_250US                       = const(0x04)
_RH_RF95_PA_RAMP_125US                       = const(0x05)
_RH_RF95_PA_RAMP_100US                       = const(0x06)
_RH_RF95_PA_RAMP_62US                        = const(0x07)
_RH_RF95_PA_RAMP_50US                        = const(0x08)
_RH_RF95_PA_RAMP_40US                        = const(0x09)
_RH_RF95_PA_RAMP_31US                        = const(0x0a)
_RH_RF95_PA_RAMP_25US                        = const(0x0b)
_RH_RF95_PA_RAMP_20US                        = const(0x0c)
_RH_RF95_PA_RAMP_15US                        = const(0x0d)
_RH_RF95_PA_RAMP_12US                        = const(0x0e)
_RH_RF95_PA_RAMP_10US                        = const(0x0f)

# RH_RF95_REG_0B_OCP                                 0x0b
_RH_RF95_OCP_ON                              = const(0x20)
_RH_RF95_OCP_TRIM                            = const(0x1f)

# RH_RF95_REG_0C_LNA                                 0x0c
_RH_RF95_LNA_GAIN                            = const(0xe0)
_RH_RF95_LNA_BOOST                           = const(0x03)
_RH_RF95_LNA_BOOST_DEFAULT                   = const(0x00)
_RH_RF95_LNA_BOOST_150PC                     = const(0x11)

# RH_RF95_REG_11_IRQ_FLAGS_MASK                      0x11
_RH_RF95_RX_TIMEOUT_MASK                     = const(0x80)
_RH_RF95_RX_DONE_MASK                        = const(0x40)
_RH_RF95_PAYLOAD_CRC_ERROR_MASK              = const(0x20)
_RH_RF95_VALID_HEADER_MASK                   = const(0x10)
_RH_RF95_TX_DONE_MASK                        = const(0x08)
_RH_RF95_CAD_DONE_MASK                       = const(0x04)
_RH_RF95_FHSS_CHANGE_CHANNEL_MASK            = const(0x02)
_RH_RF95_CAD_DETECTED_MASK                   = const(0x01)

# RH_RF95_REG_12_IRQ_FLAGS                           0x12
_RH_RF95_RX_TIMEOUT                          = const(0x80)
_RH_RF95_RX_DONE                             = const(0x40)
_RH_RF95_PAYLOAD_CRC_ERROR                   = const(0x20)
_RH_RF95_VALID_HEADER                        = const(0x10)
_RH_RF95_TX_DONE                             = const(0x08)
_RH_RF95_CAD_DONE                            = const(0x04)
_RH_RF95_FHSS_CHANGE_CHANNEL                 = const(0x02)
_RH_RF95_CAD_DETECTED                        = const(0x01)

# RH_RF95_REG_18_MODEM_STAT                          0x18
_RH_RF95_RX_CODING_RATE                      = const(0xe0)
_RH_RF95_MODEM_STATUS_CLEAR                  = const(0x10)
_RH_RF95_MODEM_STATUS_HEADER_INFO_VALID      = const(0x08)
_RH_RF95_MODEM_STATUS_RX_ONGOING             = const(0x04)
_RH_RF95_MODEM_STATUS_SIGNAL_SYNCHRONIZED    = const(0x02)
_RH_RF95_MODEM_STATUS_SIGNAL_DETECTED        = const(0x01)

# RH_RF95_REG_1C_HOP_CHANNEL                         0x1c
_RH_RF95_PLL_TIMEOUT                         = const(0x80)
_RH_RF95_RX_PAYLOAD_CRC_IS_ON                = const(0x40)
_RH_RF95_FHSS_PRESENT_CHANNEL                = const(0x3f)

# RH_RF95_REG_1D_MODEM_CONFIG1                       0x1d
_RH_RF95_BW                                  = const(0xc0)
_RH_RF95_BW_125KHZ                           = const(0x00)
_RH_RF95_BW_250KHZ                           = const(0x40)
_RH_RF95_BW_500KHZ                           = const(0x80)
_RH_RF95_BW_RESERVED                         = const(0xc0)
_RH_RF95_CODING_RATE                         = const(0x38)
_RH_RF95_CODING_RATE_4_5                     = const(0x00)
_RH_RF95_CODING_RATE_4_6                     = const(0x08)
_RH_RF95_CODING_RATE_4_7                     = const(0x10)
_RH_RF95_CODING_RATE_4_8                     = const(0x18)
_RH_RF95_IMPLICIT_HEADER_MODE_ON             = const(0x04)
_RH_RF95_RX_PAYLOAD_CRC_ON                   = const(0x02)
_RH_RF95_LOW_DATA_RATE_OPTIMIZE              = const(0x01)

# RH_RF95_REG_1E_MODEM_CONFIG2                       0x1e
_RH_RF95_SPREADING_FACTOR                    = const(0xf0)
_RH_RF95_SPREADING_FACTOR_64CPS              = const(0x60)
_RH_RF95_SPREADING_FACTOR_128CPS             = const(0x70)
_RH_RF95_SPREADING_FACTOR_256CPS             = const(0x80)
_RH_RF95_SPREADING_FACTOR_512CPS             = const(0x90)
_RH_RF95_SPREADING_FACTOR_1024CPS            = const(0xa0)
_RH_RF95_SPREADING_FACTOR_2048CPS            = const(0xb0)
_RH_RF95_SPREADING_FACTOR_4096CPS            = const(0xc0)
_RH_RF95_TX_CONTINUOUS_MOE                   = const(0x08)
_RH_RF95_AGC_AUTO_ON                         = const(0x04)
_RH_RF95_SYM_TIMEOUT_MSB                     = const(0x03)

# RH_RF95_REG_4D_PA_DAC                              0x4d
_RH_RF95_PA_DAC_DISABLE                      = const(0x04)
_RH_RF95_PA_DAC_ENABLE                       = const(0x07)

# The crystal oscillator frequency of the module
_RH_RF95_FXOSC = 32000000.0

# The Frequency Synthesizer step = RH_RF95_FXOSC / 2^^19
_RH_RF95_FSTEP = (_RH_RF95_FXOSC / 524288)

# RadioHead specific compatibility constants.
_RH_BROADCAST_ADDRESS = const(0xFF)

# User facing constants:
SLEEP_MODE   = 0b000
STANDBY_MODE = 0b001
FS_TX_MODE   = 0b010
TX_MODE      = 0b011
FS_RX_MODE   = 0b100
RX_MODE      = 0b101
# pylint: enable=bad-whitespace

print("SLEEP_MODE=",SLEEP_MODE)
print("STANDBY_MODE=",STANDBY_MODE)
# Disable the too many instance members warning.  Pylint has no knowledge
# of the context and is merely guessing at the proper amount of members.  This
# is a complex chip which requires exposing many attributes and state.  Disable
# the warning to work around the error.
# pylint: disable=too-many-instance-attributes

class RFM9x:
    # Global buffer to hold data sent and received with the chip.  This must be
    # at least as large as the FIFO on the chip (256 bytes)!  Keep this on the
    # class level to ensure only one copy ever exists (with the trade-off that
    # this is NOT re-entrant or thread safe code by design).
    _BUFFER = bytearray(10)

    class _RegisterBits:
        # Class to simplify access to the many configuration bits avaialable
        # on the chip's registers.  This is a subclass here instead of using
        # a higher level module to increase the efficiency of memory usage
        # (all of the instances of this bit class will share the same buffer
        # used by the parent RFM69 class instance vs. each having their own
        # buffer and taking too much memory).

        # Quirk of pylint that it requires public methods for a class.  This
        # is a decorator class in Python and by design it has no public methods.
        # Instead it uses dunder accessors like get and set below.  For some
        # reason pylint can't figure this out so disable the check.
        # pylint: disable=too-few-public-methods

        # Again pylint fails to see the true intent of this code and warns
        # against private access by calling the write and read functions below.
        # This is by design as this is an internally used class.  Disable the
        # check from pylint.
        # pylint: disable=protected-access

        def __init__(self, address, *, offset=0, bits=1):
            assert 0 <= offset <= 7
            assert 1 <= bits <= 8
            assert (offset + bits) <= 8
            self._address = address
            self._mask = 0
            for _ in range(bits):
                self._mask <<= 1
                self._mask |= 1
            self._mask <<= offset
            self._offset = offset

        def __get__(self, obj, objtype):
            reg_value = obj._read_u8(self._address)
            return (reg_value & self._mask) >> self._offset

        def __set__(self, obj, val):
            reg_value = obj._read_u8(self._address)
            reg_value &= ~self._mask
            reg_value |= (val & 0xFF) << self._offset
            obj._write_u8(self._address, reg_value)

    operation_mode = _RegisterBits(_RH_RF95_REG_01_OP_MODE, bits=3)

    low_frequency_mode = _RegisterBits(_RH_RF95_REG_01_OP_MODE, offset=3, bits=1)

    modulation_type = _RegisterBits(_RH_RF95_REG_01_OP_MODE, offset=5, bits=2)

    # Long range/LoRa mode can only be set in sleep mode!
    long_range_mode = _RegisterBits(_RH_RF95_REG_01_OP_MODE, offset=7, bits=1)

    output_power = _RegisterBits(_RH_RF95_REG_09_PA_CONFIG, bits=4)

    max_power = _RegisterBits(_RH_RF95_REG_09_PA_CONFIG, offset=4, bits=3)

    pa_select = _RegisterBits(_RH_RF95_REG_09_PA_CONFIG, offset=7, bits=1)

    pa_dac = _RegisterBits(_RH_RF95_REG_4D_PA_DAC, bits=3)

    dio0_mapping = _RegisterBits(_RH_RF95_REG_40_DIO_MAPPING1, offset=6, bits=2)

    tx_done = _RegisterBits(_RH_RF95_REG_12_IRQ_FLAGS, offset=3, bits=1)

    rx_done = _RegisterBits(_RH_RF95_REG_12_IRQ_FLAGS, offset=6, bits=1)

    def __init__(self, spi, cs, resetNum, frequency, *, preamble_length=8,
                 high_power=True, baudrate=5000000):
        self.spi=spi
        self.high_power = high_power
        self.cs=cs
        #self.reset=reset
        self.reset=Pin(resetNum,Pin.PULL_UP)
        self.reset()
        self.packet=None
        try:
            # Set sleep mode, wait 10s and confirm in sleep mode (basic device check).
            # Also set long range mode (LoRa mode) as it can only be done in sleep.
            self.sleep()
            self.long_range_mode = True
            #self._write_u8(_RH_RF95_REG_01_OP_MODE, 0b10001000)
            time.sleep(0.1)
            val = self._read_u8(_RH_RF95_REG_01_OP_MODE)
            print('op mode: {0}'.format(bin(val)))
            if self.operation_mode != SLEEP_MODE or not self.long_range_mode:
                print(self.operation_mode)
                print(SLEEP_MODE)
                print(self.long_range_mode)
                raise RuntimeError('Failed to configure radio for LoRa mode, check wiring!')
        except OSError:
            raise RuntimeError('Failed to communicate with radio, check wiring!')
        # clear default setting for access to LF registers if frequency > 525MHz
        if frequency > 525:
            self.low_frequency_mode = 0
        # Setup entire 256 byte FIFO
        self._write_u8(_RH_RF95_REG_0E_FIFO_TX_BASE_ADDR, 0x00)
        self._write_u8(_RH_RF95_REG_0F_FIFO_RX_BASE_ADDR, 0x00)
        # Set mode idle
        self.idle()
        # Set modem config to RadioHead compatible Bw125Cr45Sf128 mode.
        # Note no sync word is set for LoRa mode either!
        self._write_u8(_RH_RF95_REG_1D_MODEM_CONFIG1, 0x72)  # Fei msb?
        self._write_u8(_RH_RF95_REG_1E_MODEM_CONFIG2, 0x74)  # Fei lsb?
        self._write_u8(_RH_RF95_REG_26_MODEM_CONFIG3, 0x00)  # Preamble lsb?
        # Set preamble length (default 8 bytes to match radiohead).
        self.preamble_length = preamble_length
        # Set frequency
        self.frequency_mhz = frequency
        # Set TX power to low defaut, 13 dB.
        self.tx_power = 13

    def _read_into(self, address, buf, length=None):
        self.cs.value(1) # reset to default
        self.cs.value(0) # pull low for self.spi access
        # Read a number of bytes from the specified address into the provided
        # buffer.  If length is not specified (the default) the entire buffer
        # will be filled.
        if length is None:
            length = len(buf)
        self._BUFFER[0] = address & 0x7F
        #print("before:\n",self._BUFFER)
        self.spi.write(bytearray([self._BUFFER[0]]))
        #print("middle:\n",self._BUFFER)
        newbuf=buf[0:length]
        self.spi.readinto(newbuf)
        buf[0:len(newbuf)]=newbuf
        #print("after:\n",self._BUFFER)
        self.cs.value(1) # reset to default
        
    def _read_u8(self, address):
        # Read a single byte from the provided address and return it.
        self._read_into(address, self._BUFFER, length=1)
        return self._BUFFER[0]

    def _write_from(self, address, buf, length=None):
        self.cs.value(1) # reset to default
        self.cs.value(0) # pull low for self.spi access
        if length is None:
            length = len(buf)
        self._BUFFER[0] = (address | 0x80) & 0xFF  # Set top bit 
        self.spi.write(bytearray([self._BUFFER[0]]))
        self.spi.write(buf[0:length])
        self.cs.value(1) # reset to default
        
    def _write_u8(self, address, val):
        self.cs.value(1) # reset to default
        self.cs.value(0) # pull low for self.spi access
        self._BUFFER[0] = (address | 0x80) & 0xFF
        self._BUFFER[1] = val & 0xFF
        self.spi.write(self._BUFFER[0:2])
        self.cs.value(1) # reset to default

    def reset(self):
        """Perform a reset of the chip."""
        # See section 7.2.2 of the datasheet for reset description.
        self.reset=Pin(resetNum,Pin.OUT)
        self.reset.value(0)
        time.sleep(0.0001)  # 100 us
        self.reset=Pin(resetNum,Pin.PULL_UP)
        time.sleep(0.005)   # 5 ms

    def idle(self):
        """Enter idle standby mode."""
        self.operation_mode = STANDBY_MODE

    def sleep(self):
        """Enter sleep mode."""
        self.operation_mode = SLEEP_MODE

    def listen(self):
        """Listen for packets to be received by the chip.  Use :py:func:`receive`
        to listen, wait and retrieve packets as they're available.
        """
        self.operation_mode = RX_MODE
        self.dio0_mapping = 0b00  # Interrupt on rx done.

    def transmit(self):
        """Transmit a packet which is queued in the FIFO.  This is a low level
        function for entering transmit mode and more.  For generating and
        transmitting a packet of data use :py:func:`send` instead.
        """
        self.operation_mode = TX_MODE
        self.dio0_mapping = 0b01  # Interrupt on tx done.

    @property
    def preamble_length(self):
        """The length of the preamble for sent and received packets, an unsigned
        16-bit value.  Received packets must match this length or they are
        ignored! Set to 8 to match the RadioHead RFM95 library.
        """
        msb = self._read_u8(_RH_RF95_REG_20_PREAMBLE_MSB)
        lsb = self._read_u8(_RH_RF95_REG_21_PREAMBLE_LSB)
        return ((msb << 8) | lsb) & 0xFFFF

    @preamble_length.setter
    def preamble_length(self, val):
        assert 0 <= val <= 65535
        self._write_u8(_RH_RF95_REG_20_PREAMBLE_MSB, (val >> 8) & 0xFF)
        self._write_u8(_RH_RF95_REG_21_PREAMBLE_LSB, val & 0xFF)

    @property
    def frequency_mhz(self):
        """The frequency of the radio in Megahertz. Only the allowed values for
        your radio must be specified (i.e. 433 vs. 915 mhz)!
        """
        msb = self._read_u8(_RH_RF95_REG_06_FRF_MSB)
        mid = self._read_u8(_RH_RF95_REG_07_FRF_MID)
        lsb = self._read_u8(_RH_RF95_REG_08_FRF_LSB)
        frf = ((msb << 16) | (mid << 8) | lsb) & 0xFFFFFF
        frequency = (frf * _RH_RF95_FSTEP) / 1000000.0
        return frequency

    @frequency_mhz.setter
    def frequency_mhz(self, val):
        assert 240 <= val <= 960
        # Calculate FRF register 24-bit value.
        frf = int((val * 1000000.0) / _RH_RF95_FSTEP) & 0xFFFFFF
        # Extract byte values and update registers.
        msb = frf >> 16
        mid = (frf >> 8) & 0xFF
        lsb = frf & 0xFF
        self._write_u8(_RH_RF95_REG_06_FRF_MSB, msb)
        self._write_u8(_RH_RF95_REG_07_FRF_MID, mid)
        self._write_u8(_RH_RF95_REG_08_FRF_LSB, lsb)

    @property
    def tx_power(self):
        """The transmit power in dBm. Can be set to a value from 5 to 23 for
        high power devices (RFM95/96/97/98, high_power=True) or -1 to 14 for low
        power devices. Only integer power levels are actually set (i.e. 12.5
        will result in a value of 12 dBm).
        The actual maximum setting for high_power=True is 20dBm but for values > 20
        the PA_BOOST will be enabled resulting in an additional gain of 3dBm.
        The actual setting is reduced by 3dBm.
        The reported value will reflect the reduced setting.
        """
        if self.high_power:
            return self.output_power + 5
        return self.output_power - 1

    @tx_power.setter
    def tx_power(self, val):
        val = int(val)
        if self.high_power:
            assert 5 <= val <= 23
            # Enable power amp DAC if power is above 20 dB.
            # Lower setting by 3db when PA_BOOST enabled - see Data Sheet  Section 6.4
            if val > 20:
                self.pa_dac = _RH_RF95_PA_DAC_ENABLE
                val -= 3
            else:
                self.pa_dac = _RH_RF95_PA_DAC_DISABLE
            self.pa_select = True
            self.output_power = (val - 5) & 0x0F
        else:
            assert -1 <= val <= 14
            self.pa_select = False
            self.max_power = 0b111  # Allow max power output.
            self.output_power = (val + 1) & 0x0F
            

    @property
    def rssi(self):
        """The received strength indicator (in dBm) of the last received message."""
        # Read RSSI register and convert to value using formula in datasheet.
        # Remember in LoRa mode the payload register changes function to RSSI!
        return self._read_u8(_RH_RF95_REG_1A_PKT_RSSI_VALUE) - 137

    def send(self, data, timeout=2.):
        """Send a string of data using the transmitter.  You can only send 252
        bytes at a time (limited by chip's FIFO size and appended headers). Note
        this appends a 4 byte header to be compatible with the RadioHead library.
        The timeout is just to prevent a hang (arbitrarily set to 2 Seconds).
        """
        # Disable pylint warning to not use length as a check for zero.
        # This is a puzzling warning as the below code is clearly the most
        # efficient and proper way to ensure a precondition that the provided
        # buffer be within an expected range of bounds.  Disable this check.
        # pylint: disable=len-as-condition
        assert 0 < len(data) <= 252
        # pylint: enable=len-as-condition
        self.idle()  # Stop receiving to clear FIFO and keep it clear.
        # Fill the FIFO with a packet to send.
        self._write_u8(_RH_RF95_REG_0D_FIFO_ADDR_PTR, 0x00)  # FIFO starts at 0.
        # Write header bytes.
        self._write_u8(_RH_RF95_REG_00_FIFO, _RH_BROADCAST_ADDRESS) # txHeaderTo
        self._write_u8(_RH_RF95_REG_00_FIFO, _RH_BROADCAST_ADDRESS) # txHeaderFrom
        self._write_u8(_RH_RF95_REG_00_FIFO, 0x00) # txHeaderId
        self._write_u8(_RH_RF95_REG_00_FIFO, 0x00) # txHeaderFlags
        # Write payload.
        self._write_from(_RH_RF95_REG_00_FIFO, data)
        # Write payload and header length.
        self._write_u8(_RH_RF95_REG_22_PAYLOAD_LENGTH, len(data) + 4)
        # Turn on transmit mode to send out the packet.
        self.transmit()
        # Wait for tx done interrupt with explicit polling (not ideal but
        # best that can be done right now without interrupts).
        start = utime.ticks_ms()
        timed_out = False
        while not timed_out and not self.tx_done:
            if (utime.ticks_ms() - start)/1000. >= timeout:
                timed_out = True
        # Go back to idle mode after transmit.
        self.idle()
        # Clear interrupts.
        self._write_u8(_RH_RF95_REG_12_IRQ_FLAGS, 0xFF)
        if timed_out:
            raise RuntimeError('Timeout during packet send')

    def receive(self, timeout=0.5, keep_listening=True):
        """Wait to receive a packet from the receiver. Will wait for up to
        timeout amount of seconds for a packet to be received and decoded. If
        a packet is found the payload bytes are returned, otherwise None is
        returned (which indicates the timeout elapsed with no reception). Note
        this assumes a 4-byte header is prepended to the data for compatibilty
        with the RadioHead library (the header is not validated nor returned).
        If keep_listening is True (the default) the chip will immediately enter
        listening mode after reception of a packet, otherwise it will fall back
        to idle mode and ignore any future reception.
        """
        # Make sure we are listening for packets.
        self.listen()
        # Wait for the rx done interrupt.  This is not ideal and will
        # surely miss or overflow the FIFO when packets aren't read fast
        # enough, however it's the best that can be done from Python without
        # interrupt supports.
                
        start = utime.ticks_ms()
        timed_out = False
        while not timed_out and not self.rx_done:
            if (utime.ticks_ms() - start)/1000. >= timeout:
                timed_out = True
                
        # Payload ready is set, a packet is in the FIFO.
        self.packet = None
        if not timed_out:
            # Grab the length of the received packet and check it has at least 5
            # bytes to indicate the 4 byte header and at least 1 byte of user data.
            length = self._read_u8(_RH_RF95_REG_13_RX_NB_BYTES)
            if length < 5:
                self.packet = None
            else:
                # Have a good packet, grab it from the FIFO.
                # Reset the fifo read ptr to the beginning of the packet.
                current_addr = self._read_u8(_RH_RF95_REG_10_FIFO_RX_CURRENT_ADDR)
                self._write_u8(_RH_RF95_REG_0D_FIFO_ADDR_PTR, current_addr)
                self.packet = bytearray(length)
                # Read the packet.
                self._read_into(_RH_RF95_REG_00_FIFO, self.packet)
                # strip off the header
                self.packet = self.packet[4:]
            # Listen again if necessary and return the result packet.
        if keep_listening:
            self.listen()
        else:
        # Enter idle mode to stop receiving other packets.
            self.idle()
        # Clear interrupt.
        self._write_u8(_RH_RF95_REG_12_IRQ_FLAGS, 0xFF)
        return self.packet




