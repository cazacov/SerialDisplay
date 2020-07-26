import serial
from enum import IntEnum


class Charset(IntEnum):
    USA = 0
    France = 1
    Germany = 2
    GreatBritain = 3
    Denmark1 = 4
    Sweden = 5
    Italy = 6
    Spain = 7
    Japan = 8
    Norway = 9
    Denmark2 = 0x0A
    Spain2 = 0x0B
    LatinAmerica = 0x0C
    Cyrillic = 0x35
    Greek737 = 0x36
    Hebrew = 0x37


class BA63:
    def __init__(self, com_port):
        self.port = serial.Serial(com_port, 9600, timeout=0, parity=serial.PARITY_ODD)
        self.delete_display()
        self.position_cursor(1, 1)
        self.port.write(str.encode("Hello World!"))

    def delete_display(self):
        self.port.write(str.encode("\x1B[2J"))

    def position_cursor(self, line, column):
        command = f"\x1B[{line};{column}H"
        self.port.write(str.encode(command))

    def write(self, text, enc=None):
        if not enc:
            command = str.encode(text)
        else:
            command = str.encode(text, encoding=enc)
        self.port.write(command)

    def set_country_code(self, charset):
        command = "\x1BR" + chr(charset)
        self.port.write(str.encode(command))
