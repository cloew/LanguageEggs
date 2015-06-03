from .inflection_rule import InflectionRule
from .inflection_dimension import InflectionDimension

from kao_factory.factory import Factory
from kao_factory.Parameter.complex_parameter import ComplexParameter
from kao_factory.Parameter.primitive_parameter import PrimitiveParameter

DimensionFactory = Factory(InflectionDimension, [PrimitiveParameter("name")])
InflectionRuleFactory = Factory(InflectionRule, [PrimitiveParameter("name"),
                                                 ComplexParameter("dimensions", DimensionFactory.loadAll, optional=True, default=[])])