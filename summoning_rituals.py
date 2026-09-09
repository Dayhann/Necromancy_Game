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
        self.__starting_power = self.__validate_stat(starting_power, Undead.MIN_POWER, Undead.MAX_POWER)

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
        if (isinstance(value, int) and not isinstance(value, bool) and value >= SummoningRitual.MIN_COST):
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

    def create_undead(self, unit_id):
        return Undead(unit_id, self.__undead_name, self.__starting_health, self.__starting_power)

    def get_name(self):
        return self.__name

    def get_undead_name(self):
        return self.__undead_name

    def get_starting_health(self):
        return self.__starting_health   

    def get_starting_power(self):
        return self.__starting_power

    def get_necrotic_cost(self):
        return self.__necrotic_cost

    def get_spirit_cost(self):
        return self.__spirit_cost
    
    def get_bone_cost(self):
        return self.__bone_cost

    def get_flesh_cost(self):
        return self.__flesh_cost

    def get_ectoplasm_cost(self):
        return self.__ectoplasm_cost

    name = property(get_name)
    undead_name = property(get_undead_name)
    starting_health = property(get_starting_health)
    starting_power = property(get_starting_power)
    necrotic_cost = property(get_necrotic_cost)
    spirit_cost = property(get_spirit_cost)
    bone_cost = property(get_bone_cost)
    flesh_cost = property(get_flesh_cost)
    ectoplasm_cost = property(get_ectoplasm_cost)

    def __str__(self):
        return (f"{self.__name}: summons {self.__undead_name} "
                f"(Health {self.__starting_health}, "
                f"Power {self.__starting_power}) | Cost - "
                f"Necrotic {self.__necrotic_cost}, "
                f"Spirit {self.__spirit_cost}, "
                f"Bone {self.__bone_cost}, "
                f"Flesh {self.__flesh_cost}, "
                f"Ectoplasm {self.__ectoplasm_cost}")

    def __repr__(self):
        return (f"SummoningRitual(name='{self.__name}', "
                f"undead_name='{self.__undead_name}', "
                f"starting_health={self.__starting_health}, "
                f"starting_power={self.__starting_power}, "
                f"necrotic_cost={self.__necrotic_cost}, "
                f"spirit_cost={self.__spirit_cost}, "
                f"bone_cost={self.__bone_cost}, "
                f"flesh_cost={self.__flesh_cost}, "
                f"ectoplasm_cost={self.__ectoplasm_cost})")
    


    


        