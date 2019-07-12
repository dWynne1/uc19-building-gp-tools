"""
Print out only "friendly" cats
"""
import os

from arcpy.da import SearchCursor

in_table = r"C:\Users\andr7495\Desktop\ESRI\UC 2018\Intro to GP Python Tools\Intro_GP_Script_Tools_2018\Intro_GP_Script_Tools_2018.gdb\Cat_Data"
field_names = ['OID@', 'Type']
sql = "friendly = 1"

output = '\nFriendly Cats:\n'

with SearchCursor(in_table, field_names, sql) as sc:
    for row in sc:
        output += 'OID: {0} -- {1} cat\n'.format(*row)
        
print(output)
arcpy.AddMessage(output)

