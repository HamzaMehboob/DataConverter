import csv
import json
import xml.etree.ElementTree as ET
from io import StringIO

class DataConverter:
    
    @staticmethod
    def csv_to_json(csv_data):
        data = []
        csv_reader = csv.DictReader(StringIO(csv_data))
        for row in csv_reader:
            data.append(row)
        return json.dumps(data, indent=4)
    
    @staticmethod
    def csv_to_xml(csv_data):
        csv_reader = csv.DictReader(StringIO(csv_data))
        root = ET.Element("root")
        for row in csv_reader:
            item = ET.Element("item")
            for key, value in row.items():
                element = ET.SubElement(item, key)
                element.text = value
            root.append(item)
        return ET.tostring(root, encoding="unicode")

    @staticmethod
    def json_to_csv(json_data):
        data = json.loads(json_data)
        if not data:
            return ""
        
        csv_output = StringIO()
        csv_writer = csv.DictWriter(csv_output, fieldnames=data[0].keys())
        csv_writer.writeheader()
        for row in data:
            csv_writer.writerow(row)
        return csv_output.getvalue()

    @staticmethod
    def json_to_xml(json_data):
        data = json.loads(json_data)
        root = ET.Element("root")
        for item_data in data:
            item = ET.Element("item")
            for key, value in item_data.items():
                element = ET.SubElement(item, key)
                element.text = str(value)
            root.append(item)
        return ET.tostring(root, encoding="unicode")

    @staticmethod
    def xml_to_csv(xml_data):
        root = ET.fromstring(xml_data)
        items = root.findall('item')
        
        if not items:
            return ""

        # Extract fieldnames from the first item
        fieldnames = [child.tag for child in items[0]]
        
        output = StringIO()
        csv_writer = csv.DictWriter(output, fieldnames=fieldnames)
        csv_writer.writeheader()

        for item in items:
            row_data = {child.tag: child.text for child in item}
            csv_writer.writerow(row_data)

        return output.getvalue()

    @staticmethod
    def xml_to_json(xml_data):
        root = ET.fromstring(xml_data)
        items = []
        for item in root:
            item_data = {child.tag: child.text for child in item}
            items.append(item_data)
        return json.dumps(items, indent=4)