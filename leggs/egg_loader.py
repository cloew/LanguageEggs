from .symbol import Symbol
from .word import Word

from kao_factory import DataBoundFactory, Factory, FieldArg, StaticArg
from kao_factory.Source.json_source import JsonSource

form_parameters = [FieldArg("concept"),
                   FieldArg("text")]
                   
SymbolFactory = Factory(Symbol, *form_parameters)
WordFactory = Factory(Word, *form_parameters)

class Egg:
    def __init__(self, language, symbols=[], words=[]):
        self.language = language
        self.symbols = symbols
        self.words = words
        
EggFactory = Factory(Egg, FieldArg("language"), symbols=SymbolFactory.LoadAllArg("symbols"), words=WordFactory.LoadAllArg("words"))

def LoadEggs(eggFilename, encoding="utf8"):
    """ Loads the eggs from the file and returns them """
    return DataBoundFactory(EggFactory, JsonSource(eggFilename, encoding=encoding)).loadAll()