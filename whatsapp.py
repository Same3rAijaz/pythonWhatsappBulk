import pywhatkit
import pandas as pd
from datetime import datetime
df = pd.read_excel('ContactInfo.xlsx')
for i in df['Contact']:
    num_str = str(i)
    hour = datetime.now().hour
    minute = datetime.now().minute + 1
    if num_str.startswith('0'):
        num_str = '+92' + str(i[1:])
    elif num_str.startswith('+'):
        num_str = str(0)
    else:
        num_str = '+92' + str(i)
    print(i)
    pywhatkit.sendwhatmsg(
        num_str, "Hello automated world", hour, minute, 32, tab_close=True)

