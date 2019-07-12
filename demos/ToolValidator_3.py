import arcpy

class ToolValidator(object):
    """
    Class for validating a tool's parameter values and controlling
    the behavior of the tool's dialog.
    """

    def __init__(self):
        """
        Setup arcpy and the list of tool parameters.
        """
        self.params = arcpy.GetParameterInfo()

    def initializeParameters(self):
        """
        Refine the properties of a tool's parameters. This method is 
        called when the tool is opened.
        """
        self.params[1].enabled = False

    def updateParameters(self):
        """
        Modify the values and properties of parameters before internal
        validation is performed. This method is called whenever a parameter
        has been changed.
        """
        if self.params[0].value:
            relevant_fields = {f.name: f.type for f in arcpy.Describe(self.params[0].value).fields if f.type == "SmallInteger"}
            if relevant_fields:
                self.params[1].enabled = True
                self.params[1].filter.list = list(relevant_fields.keys())
            else:
                self.params[1].enabled = False
                self.params[0].clearMessage()

    def updateMessages(self):
        """
        Modify the messages created by internal validation for each tool
        parameter. This method is called after internal validation.
        """
        if not self.params[0].value:
            self.params[0].clearMessage()
            self.params[0].setWarningMessage('Select a Feature Layer with a "Friendly" field in it.')
        elif not {f.name: f.type for f in arcpy.Describe(self.params[0].value).fields if f.type == "SmallInteger"}:
            self.params[0].setErrorMessage("Could not find a field-type of SmallInteger. Please select a new feature class.")
        else:
            self.params[0].clearMessage()
