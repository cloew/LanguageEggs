
class InflectionDimension:
    """ Represents a dimension that affects this inflection rule """

    def __init__(self, name, values):
        """ Initialize the inflection dimension """
        self.name = name
        self.values = values
        
    def __unicode__(self):
        """ Return the string representation of the Dimension """
        return unicode("<InflectionDimension({0}, {1})>".format(self.name, self.values))