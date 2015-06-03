from .inflection_rule import InflectionRule
from kao_factory.factory import Factory
from kao_factory.Parameter.complex_parameter import ComplexParameter
from kao_factory.Parameter.primitive_parameter import PrimitiveParameter

InflectionRuleFactory = Factory(InflectionRule, [PrimitiveParameter("name")])