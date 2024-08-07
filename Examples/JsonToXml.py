import sys
import os

# Add the parent directory to the sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import DataConverter

json_data = """
[
    {
        "name": "John Doe",
        "age": "29",
        "city": "New York"
    },
    {
        "name": "Jane Smith",
        "age": "34",
        "city": "Los Angeles"
    },
    {
        "name": "Bob Johnson",
        "age": "45",
        "city": "Chicago"
    }
]
"""


converter = DataConverter.DataConverter()


# JSON to XML
print("\nJSON to XML:")
print(converter.json_to_xml(json_data))