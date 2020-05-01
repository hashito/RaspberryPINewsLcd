import i2clcda
# import i2clcdb.py
import feedparser
import time
import sys
char_max=16
url=sys.argv[1]

def rolling_string(str,line):
    str_len=len(str)
    if(str_len<=char_max):
        i2clcda.lcd_string(str,line)
        time.sleep(1)
        return

    for i in range(str_len - char_max):
        i2clcda.lcd_string(str[i:],line)
        time.sleep(0.2)
#    i2clcda.lcd_string("Osoyoo.com        <",i2clcda.LCD_LINE_2)
#"> http://osoyoo."
# 1234567890123456 ->16

while True:
    for i in feedparser.parse(url).entries:
        print(i.title)
        rolling_string(i.title[:int(len(i.title)/2)],i2clcda.LCD_LINE_1)
        rolling_string(i.title[int(len(i.title)/2):],i2clcda.LCD_LINE_2)