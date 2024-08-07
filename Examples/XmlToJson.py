import sys
import os

# Add the parent directory to the sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import DataConverter

xml_data = """
<root>
    <item>
        <name>John Doe</name>
        <age>29</age>
        <city>New York</city>
    </item>
    <item>
        <name>Jane Smith</name>
        <age>34</age>
        <city>Los Angeles</city>
    </item>
    <item>
        <name>Bob Johnson</name>
        <age>45</age>
        <city>Chicago</city>
    </item>
</root>
"""

converter = DataConverter.DataConverter()
# XML to JSON
print("\nXML to JSON:")
print(converter.xml_to_json(xml_data))