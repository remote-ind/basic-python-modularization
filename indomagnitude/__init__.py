import requests
from bs4 import BeautifulSoup

def data_extc():

    try:
        content = requests.get('https://www.bmkg.go.id/')
    except Exception:
        return None


    if content.status_code == 200:
        soup = BeautifulSoup(content.text, 'html.parser')
        result = soup.find('div', {'class': 'col-md-6 col-xs-6 gempabumi-detail no-padding'})
        result = result.findChildren('li')

        #VARIABLE FOR FILLING CONTENT
        i = 0
        dateTime = None
        date = None
        time = None
        magnitude = None
        depth = None
        coord = None
        ltd = None
        lon = None
        position = None
        scala = None

        for fill in result:
            i = i + 1

            if i == 1:
                dateTime = fill.text.split(', ')
                date = dateTime[0]
                time = dateTime[1]
            elif i == 2:
                magnitude = fill.text
            elif i == 3:
                depth = fill.text
            elif i == 4:
                coord = fill.text.split(' - ')
                ltd = coord[0]
                lon = coord[1]
            elif i == 5:
                position = fill.text
            elif i == 6:
                scala = fill.text


        show = dict()
        show['date'] = date
        show['time'] = time
        show['magnitude'] = magnitude
        show['depth'] = depth
        show['coord'] = {'ltd': ltd, 'lon': lon}
        show['position'] = position
        show['scala'] = scala
        return show
    else:
        return None


def data_vis(result):
    print('ATTENTION!!! INDONESIAN EARTHQUAKE UPDATE :')
    print(f"Date : {result['date']}")
    print(f"Time : {result['time']}")
    print(f"Magnitude : {result['magnitude']}")
    print(f"Depth : {result['depth']}")
    print(f"Coordination : LTD : {result['coord']['ltd']} LON : {result['coord']['lon']}")
    print(f"Position : {result['position']}")
    print(f"Scala : {result['scala']}")
