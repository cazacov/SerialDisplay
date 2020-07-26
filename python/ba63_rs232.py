import serial


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

    def write(self, text):
        self.port.write(str.encode(text))
