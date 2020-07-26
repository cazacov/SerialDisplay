from ba63_rs232 import BA63

display = BA63('COM1')
display.delete_display()

for line in range(1, 3):
    for column in range(1, 21):
        if (line + column) % 2 == 0:
            display.position_cursor(line, column)
            display.write("X")
