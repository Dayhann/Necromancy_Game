from resource import Resource
from undead import Undead

class SummoningRitual:

    MIN_COST = 0 
    MIN_ECTOPLASM_COST = 1

    def __init__(self, name, undead_name, starting_health, starting_power,
                 necrotic_cost=0, spirit_cost=0, bone_cost=0, flesh_cost=0, ectoplasm_cost=0):

        if isinstance(name, str):
            self.__name = name
        else:
            self.__name = ""

        if isinstance(undead_name, str):
            self.__undead_name = undead_name
        else:
            self.__undead_name = ""

        self.__starting_health = self.__validate_stat(starting_health, Undead.MIN_HEALTH, Undead.MAX_HEALTH)
        self.__starting_power = self.__validate_stat(starting_power, Undead.MIN_POWER, Undead.MAX_HEALTH)

        self.__necrotic_cost = self.__validate_cost(necrotic_cost)
        self.__spirit_cost = self.__validate_cost(spirit_cost)
        self.__bone_cost  = self.__validate_cost(bone_cost)
        self.__flesh_cost = self.__validate_cost(flesh_cost)

        self.__ectoplasm_cost = max(self.__validate_cost(ectoplasm_cost), 
                                    SummoningRitual.MIN_ECTOPLASM_COST)


    def __validate_stat(self, value, minimum, maximum):
        if not isinstance(value, int) or isinstance(value, bool):
            return minimum
        return max(minimum, min(value, maximum))

    def __validate_cost(self, value):
        if (isinstance(value, int) and isinstance(value, bool) and value >= SummoningRitual.MIN_COST):
            return value
        return SummoningRitual.MIN_COST

    def can_perfom_ritual(self, resource):
        if not isinstance(resource, Resource):
            print("Invalid resource pool: a Resource 'object' is required.")
            return False
        return resource.meets_requirements(
            self.__necrotic_cost, self.__spirit_cost, self.__bone_cost, self.__flesh_cost, self.__ectoplasm_cost
        )

    def consume_resources(self, resource):
        if not isinstance(resource, Resource):
            print("Invalid resource pool: a Resource 'object' is required.")
            return False
        return resource.spend_resources(
            self.__necrotic_cost, self.__spirit_cost, self.__bone_cost, self.__flesh_cost, 
            self.__ectoplasm_cost
        )

    


    


        