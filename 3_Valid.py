"""
Reports friendly cats, but uses validation to check parameters before running the script
"""

import os

from arcpy import AddField_management, AddMessage, CreateFeatureclass_management, GetParameterAsText
from arcpy.da import InsertCursor, SearchCursor

in_table = GetParameterAsText(0)  # Feature Layer
friendly_value = GetParameterAsText(1)  # Integer
output = GetParameterAsText(2)  # Feature Layer

# Get data from input-table
where_clause = '{0} = 1'.format(friendly_value)
field_names = ['SHAPE@XY', 'Type']
rows = list()
with SearchCursor(in_table, field_names, where_clause) as sc:
    for row in sc:
        rows.append(row)

# Create new feature class
path = '\\'.join(in_table.split('\\')[:-1])
output_name = output.split('\\')[-1]
CreateFeatureclass_management(path, output_name, 'POINT')

# Add fields to the new feature class
fields = [
    ('Type', 'TEXT'),
    ('Friendly', 'SHORT')
]
for f in fields:
    AddField_management(output, f[0], f[1])

# Write rows to the table
AddMessage(os.path.join(path, in_table))
with InsertCursor(output, field_names) as icursor:
    for row in rows:
        icursor.insertRow(row)
