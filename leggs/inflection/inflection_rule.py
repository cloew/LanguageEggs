
class InflectionRule:
    """ Represents a rule for linguistic inflection in a language """

    def __init__(self, name):
        """ Initialize the Inflection Rule with a name for the rule """
        self.name = name
        
    def __unicode__(self):
        """ Return the string representation of the Rule """
        return unicode(self.name)