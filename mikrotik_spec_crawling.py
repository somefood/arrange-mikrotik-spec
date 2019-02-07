import requests
from bs4 import BeautifulSoup


kc_list = [
    'hEX Lite',
    'hEX',
    'RB2011iL-RM',
    'RB2011UiAS-RM',
    'CCR1009-7G-1C-1S+',
    'CCR1016-12G',
    'CCR1016-12S-1S+',
    'CCR1036-12G-4S',
    'CCR1036-8G-2S+',
    'CCR1072-1G-8S+',
    'RB450',
    'RB450G',
    'CRS326-24G-2S+RM',
    'CRS317-1G-16S+RM',
    'wAP',
]


html = requests.get('https://mikrotik.com/products/matrix').text
soup = BeautifulSoup(html,'html.parser')

description_list = []
product_list = []

for th_tag in soup.select('thead th'):
    description_list.append(th_tag.text)

for tr_tag in soup.select('tbody tr'):
    product_name = tr_tag.find('a').text
    if product_name not in kc_list:
        continue
    detail_list=[]
    for td_tag in tr_tag.select('td'):
        # if td_tag.text == '' or 'No': 이렇게 하면 'No'는 bool True니 참으로 값이 되더라
        if td_tag.text == '' or td_tag.text == 'No' or td_tag.text == '0':
            detail_list.append('None')
        else:
            detail_list.append(td_tag.text)
    product_list.append(dict(zip(description_list, detail_list)))

for i in product_list:
    del_key_list = ['CPU', 'Suggested price (USD)']
    del_key_list += [value_is_none for value_is_none in i.keys() if i[value_is_none] == 'None']
    for del_key in del_key_list:
        print(i['Product name'] ,del_key,'will be removed')
        try:
            del i[del_key]
        except:
            pass
    print('=========valuable keys========')
    print(i['Product name'])
    for j,k in i.items():
        print(j,':',k, type(k))
    print('\n')