# Colourfull way to show love for Python
# This script will display the Text in 256 colors
import time
from colored import fg,attr
reset = attr('reset')
text = 'Happy Coding :)'
i = 1
while(i<256):
    col = fg(i)
    print(col + text + reset)
    time.sleep(0.5)
    i = i + 1