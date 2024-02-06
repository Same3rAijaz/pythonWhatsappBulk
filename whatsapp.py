import pywhatkit
import pandas as pd
from datetime import datetime
df = pd.read_excel('ContactInfo.xlsx')
for index, row in df.iterrows():
    num_str = str(row['Contact'])
    country_code = str(row['CountryCode'])
    message = str(row['Message'])
    name = str(row['Name'])
    hour = datetime.now().hour
    minute = datetime.now().minute + 1
    if num_str.startswith('0'):
        num_str = "+" + country_code + num_str
    elif num_str.startswith('+'):
        num_str = num_str
    else:
        num_str = "+" + country_code + num_str
    print(num_str)
    pywhatkit.sendwhatmsg(
        num_str, "Hello " + name + "," + message, hour, minute, 32, tab_close=True)
