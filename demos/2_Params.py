"""
Reports friendly cats and uses parameters from the user
"""

from arcpy import AddMessage
from arcpy import GetParameterAsText
from arcpy.da import SearchCursor

feature_cats = GetParameterAsText(0)  # Feature Layer
friendly_field = GetParameterAsText(1)  # String

where_clause = '{0} = 1'.format(friendly_field)
field_names = ['OID@', 'Type']

output = ''

with SearchCursor(feature_cats, field_names, where_clause) as sc:
    output += '\nFriendly Cats:\n'
    for row in sc:
        output += '    OID: {0} -- {1} cat\n'.format(*row)
        
AddMessage(output)
