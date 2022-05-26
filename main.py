"""
INDONESIA EARTHQUAKE DETECTION APPLICATION
I use function modularization
"""

def data_extc():
    show = dict()
    show['date'] = "26 May 2022"
    show['time'] = "03:24:45 WIB"
    show['magnitude'] = 3.1
    show['depth'] = "2 Km"
    show['location'] = {'ltd': 5.89, 'lon': 95.19}
    show['position'] = "The epicenter of the earthquake was in the sea 14 km southwest of Sabang City"
    show['scala'] = "MMI Scale at I-II Sabang City"

    return show


def data_vis(result):
    print('ATTENTION!!! INDONESIAN EARTHQUAKE UPDATE :')
    print(f"Date : {result['date']}")
    print(f"Time : {result['time']}")
    print(f"Magnitude : {result['magnitude']}")
    print(f"Depth : {result['depth']}")
    print(f"Location : LTD : {result['location']['ltd']} LON : {result['location']['lon']}")
    print(f"Position : {result['position']}")


if __name__ == '__main__':
    print('Main Application')
    result = data_extc()
    data_vis(result)
