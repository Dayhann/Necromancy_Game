class Undead:

    MIN_HEALTH = 1
    MAX_HEALTH = 100
    MIN_POWER = 1
    MAX_POWER = 99
    MAX_LEVEL = 100
    HEALTH_PER_LEVEL = 10
    POWER_PER_LEVEL = 5

    def __init__(self, unit_id, name, health, power):
        if isinstance(unit_id, int) and not isinstance(unit_id, bool) and unit_id > 0: 
            self.__unit_id = unit_id
        else:
            self.__unit_id = 0

        if isinstance(name, str):
            self.__name = name
        else:
            self.__name = ""

        self.__health = self.__validate_stat(health, Undead.MIN_HEALTH, Undead.MAX_HEALTH)
        self.__power = self.__validate_stat(power, Undead.MIN_POWER, Undead.MAX_POWER)
        self.__level = 1

    def __validate_stat(self, value, minimum, maximum):
        if not isinstance(value, int) or isinstance(value, bool):
            return minimum
        # min(value, maximum) : value, but never more than maximum - ceiling
        # max(minimum, that) : that result, but never less than minimum - floor
        return max(minimum, min(value, maximum))

    def level_up(self):
        if self.__level >= Undead.MAX_LEVEL:
            print(f"{self.name} is already at the max level of {Undead.MAX_LEVEL}")
            return False

        self.__level += 1
        self.__health = min(self.__health + Undead.HEALTH_PER_LEVEL, Undead.MAX_HEALTH)
        self.__power = min(self.__power + Undead.POWER_PER_LEVEL, Undead.MAX_POWER)

        print(f"{self.__name} has levelled up to level: {self.__level}")
        return True 

    def get_unit_id(self):
        return self.__unit_id

    def get_name(self):
        return self.__name

    def get_health(self):
        return self.__health

    def get_power(self):
        return self.__power

    def get_level(self):
        return self.__level

    unit_id = property(get_unit_id)
    name = property(get_name)
    health = property(get_health)
    power = property(get_power)
    level = property(get_level)

    


    