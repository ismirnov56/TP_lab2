from xml.dom import minidom
import xml.etree.ElementTree as ET

def create_xml(cyclist1, cyclist2):

    cyclists = ET.Element('cyclists')

    cyclist1_element = ET.SubElement(cyclists,'cyclist')

    id_element = ET.SubElement(cyclist1_element, 'id')
    id_element.text = str(1)
    coordinate_element = ET.SubElement(cyclist1_element, 'coordinate')
    coordinate_element.text = str(cyclist1.getCoordinate())
    speed_element = ET.SubElement(cyclist1_element, 'speed')
    speed_element.text = str(cyclist1.getSpeed())

    cyclist2_element = ET.SubElement(cyclists, 'cyclist')

    id_element = ET.SubElement(cyclist2_element, 'id')
    id_element.text = str(2)
    coordinate_element = ET.SubElement(cyclist2_element, 'coordinate')
    coordinate_element.text = str(cyclist2.getCoordinate())
    speed_element = ET.SubElement(cyclist2_element, 'speed')
    speed_element.text = str(cyclist2.getSpeed())

    filename = 'cyclists.xml'
    save_file_xml(filename, cyclists)

def save_file_xml(filename, xml_code):
    xml_string = ET.tostring(xml_code).decode()

    xml_prettyxml = minidom.parseString(xml_string).toprettyxml()
    with open(filename, 'w') as xml_file:
        xml_file.write(xml_prettyxml)
