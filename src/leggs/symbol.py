
class Symbol:
    """ Represents a language symbol """
    
    def __init__(self, conceptId, text):
        """ Initialize the symbol with its concept id and the text """
        self.conceptId = conceptId
        self.text = text
        
    def __unicode__(self):
        """ Return the string representation of the Symbol """
        return unicode(self.text)