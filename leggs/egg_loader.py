from .symbol import Symbol
from .word import Word

from .inflection import InflectionRuleFactory

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
    def __init__(self, language, symbols, words, inflectionRules):
        self.language = language
        self.symbols = symbols
        self.words = words
        self.inflectionRules = inflectionRules
        
parameters = [PrimitiveParameter("language"), ComplexParameter("symbols", SymbolFactory.loadAll, optional=True, default=[]),
                                              ComplexParameter("words", WordFactory.loadAll, optional=True, default=[]),
                                              ComplexParameter("inflectionRules", InflectionRuleFactory.loadAll, optional=True, default=[])]

def LoadEggs(eggFilename):
    """ Loads the eggs from the file and returns them """
    return DataSourceFactory(Egg, parameters, JsonSource(eggFilename)).loadAll()