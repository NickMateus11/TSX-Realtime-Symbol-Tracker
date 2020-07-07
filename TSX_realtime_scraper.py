import re
import requests
from bs4 import BeautifulSoup


symbol = 'SHOP'
URL = f'https://web.tmxmoney.com/quote.php?qm_symbol={symbol}&locale=EN'

page = requests.get(URL)
soup = BeautifulSoup(page.content, 'html.parser')

price = soup.find('span', class_='price').find('span').text # this span includes the symbol's price
result = soup.find('p') # This is the paragraph that includes the Real-time date and time
realtime_date = re.sub(', [0-9]{4}', '', result.text.split('|')[1].strip()) if 'TSX Exchange' in result.text else 'parseError' # remove year from the date

print('$' + price)
print(realtime_date)

