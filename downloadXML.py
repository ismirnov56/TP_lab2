import xml.etree.ElementTree as ET

def download(cyclist1 ,cyclist2):
    #тут проиходит загрузка xml файла
    tree = ET.parse('cyclists.xml')
    root = tree.getroot()
    for cyclists in root.findall('cyclist'):
        if cyclists.find('id').text == '1':
            cyclist1.setCoordinate(float(cyclists.find('coordinate').text))
            cyclist1.setSpeed(float(cyclists.find('speed').text))
        if cyclists.find('id').text == '2':
            cyclist2.setCoordinate(float(cyclists.find('coordinate').text))
            cyclist2.setSpeed(float(cyclists.find('speed').text))