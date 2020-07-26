from ba63_rs232 import BA63, Charset

display = BA63('COM1')
display.delete_display()

display.position_cursor(1, 1)
display.set_country_code(Charset.Cyrillic)
display.write("Здравствуй, мир!", "cp866")

display.position_cursor(2, 1)
display.set_country_code(Charset.Germany)
display.write("Käsesoßenrührlöffel", "cp850")
