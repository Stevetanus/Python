import webbrowser
import sys
import requests
import bs4

city = {'NewTaipei': '65', 'Taipei': '63', 'Taoyuan': '68',
        'Taichung': '66', 'Tainan': '67', 'Kaosiung': '64',
        '基隆市': '10017', '新北市': '65', '臺北市': '63', '桃園市': '68', '新竹縣': '10004', '新竹市': '10018', '苗栗縣': '10005', '臺中市': '66', '南投縣': '10008', '彰化縣': '10007', '雲林縣': '10009', '嘉義縣': '10010', '嘉義市': '10020', '臺南市': '67', '高雄市': '64', '屏東縣':
        '10013', '臺東縣': '10014', '花蓮縣': '10015', '宜蘭縣': '10002', '澎湖縣': '10016', '金門縣': '09020', '連江縣': '09007'}
if len(sys.argv) > 1:
    # Get address from command line.
    searchPlace = sys.argv[1]
    address = 'County.html?CID=' + city[searchPlace]
else:
    # Get address of all cities.
    address = 'index.html'

webbrowser.open('https://www.cwb.gov.tw/V8/C/W/County/' + address)
# ## getting cities dictionary
# res = requests.get('https://www.cwb.gov.tw/V8/C/W/County/' + address)
# res.raise_for_status
# weatherSoup = bs4.BeautifulSoup(res.text,'html.parser')
# all_g_tags = weatherSoup.find_all('g')
# list_of_inner_text = [x.text for x in all_g_tags]
# county = [w[:-2] for w in list_of_inner_text]
# list_of_g_attrs = [x.attrs['id'] for x in all_g_tags]
# cid = [w[1:] for w in list_of_g_attrs]
# weather_dict = {}
# for i in range(len(county)):
#     weather_dict.setdefault(county[i], cid[i])
# import json # json.dumps(dict)
# # print out and copy paste on the top of the file.
# for i in range(len(weatherSoup.find_all('g'))):
#     print(weatherSoup.g.attrs, weatherSoup.desc.get_text())
