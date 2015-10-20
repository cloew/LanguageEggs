from .symbol import Symbol
from .word import Word

from kao_factory.data_source_factory import DataSourceFactory
from kao_factory.factory import Factory
from kao_factory.Parameter.complex_parameter import ComplexParameter
from kao_factory.Parameter.primitive_parameter import PrimitiveParameter
from kao_factory.Source.json_source import JsonSource

word_parameters = [PrimitiveParameter("concept"),
                   PrimitiveParameter("text")]
                   
SymbolFactory = Factory(Symbol, word_parameters)
WordFactory = Factory(Word, word_parameters)

class Egg:
    def __init__(self, language, symbols, words):
        self.language = language
        self.symbols = symbols
        self.words = words
        
parameters = [PrimitiveParameter("language"), ComplexParameter("symbols", SymbolFactory.loadAll, optional=True, default=[]),
                                              ComplexParameter("words", WordFactory.loadAll, optional=True, default=[])]

def LoadEggs(eggFilename, encoding="utf8"):
    """ Loads the eggs from the file and returns them """
    return DataSourceFactory(Egg, parameters, JsonSource(eggFilename, encoding=encoding)).loadAll()