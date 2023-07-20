import requests
import argparse
import xmltodict

parser = argparse.ArgumentParser()
parser.add_argument('--date',
                    type=str,
                    required=True,
                    help='date in format dd/mm/yyyy')
parser.add_argument('--code',
                    type=str,
                    required=True,
                    help='currency code')
args = parser.parse_args()
my_date = args.date
my_currency = args.code

url_curr_codes = f'http://www.cbr.ru/scripts/XML_daily.asp?date_req={my_date}'
res = requests.get(url=url_curr_codes)
resp_xml_content = res.content
dict_data = xmltodict.parse(resp_xml_content)['ValCurs']['Valute']
for currency_info in dict_data:
    currency_full_name = currency_info['Name']
    currency_price = currency_info['Value']
    currency_name = currency_info['CharCode']
    if currency_name == my_currency:
        print(f'{currency_name} ({currency_full_name}): {currency_price}')
        break
else:
    print('Invalid currency code')