import pandas as pd
from xml.etree import ElementTree as ET

tree = ET.parse('artifacts/xml_response.xml')
root = tree.getroot()

print(root.text)