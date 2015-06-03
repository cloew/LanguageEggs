
class InflectionDimension:
    """ Represents a dimension that affects this inflection rule """

    def __init__(self, name):
        """ Initialize the inflection dimension """
        self.name = name
        
    def __unicode__(self):
        """ Return the string representation of the Dimension """
        return unicode(self.name)