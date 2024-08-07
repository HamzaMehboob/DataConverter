import sys
import os

# Add the parent directory to the sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import DataConverter

csv_data = """name,age,city
John Doe,29,New York
Jane Smith,34,Los Angeles
Bob Johnson,45,Chicago
"""

converter = DataConverter.DataConverter()

# CSV to XML
print("\nCSV to XML:")
print(converter.csv_to_xml(csv_data))