import requests
from bs4 import BeautifulSoup


def data_extc():

    try:
        content = requests.get('https://www.bmkg.go.id/')
    except Exception:
        return None


    if content.status_code == 200:
        soup = BeautifulSoup(content.text, 'html.parser')
        find = soup.find('span', {'class': 'waktu'})
        dateTime = find.text.split(', ')

        show = dict()
        show['date'] = dateTime[0]
        show['time'] = dateTime[1]
        show['magnitude'] = 3.1
        show['depth'] = "2 Km"
        show['location'] = {'ltd': 5.89, 'lon': 95.19}
        show['position'] = "The epicenter of the earthquake was in the sea 14 km southwest of Sabang City"
        show['scala'] = "MMI Scale at I-II Sabang City"
        return show
    else:
        return None


def data_vis(result):
    print('ATTENTION!!! INDONESIAN EARTHQUAKE UPDATE :')
    print(f"Date : {result['date']}")
    print(f"Time : {result['time']}")
    print(f"Magnitude : {result['magnitude']}")
    print(f"Depth : {result['depth']}")
    print(f"Location : LTD : {result['location']['ltd']} LON : {result['location']['lon']}")
    print(f"Position : {result['position']}")
