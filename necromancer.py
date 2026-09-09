from resource import Resource
from summoning_rituals import SummoningRitual


class Necromancer:

    MAX_CONTROLLED_UNDEAD = 5

    def __init__(self, name, necrotic_runes=0, spirit_runes=0, bone_runes=0,
                 flesh_runes=0, ectoplasm=0):
        if isinstance(name, str):
            self.__name = name
        else:
            self.__name = ""

        self.__resources = Resource(necrotic_runes, spirit_runes,
                                    bone_runes, flesh_runes, ectoplasm)

        self.__controlled_undead = []
        self.__next_unit_id = 1

    def collect_resources(self, necrotic_runes, spirit_runes, bone_runes,
                          flesh_runes, ectoplasm):
        return self.__resources.collect_resources(
            necrotic_runes, spirit_runes, bone_runes, flesh_runes, ectoplasm)

    def summon(self, ritual):
        if not isinstance(ritual, SummoningRitual):
            print("Invalid ritual: a SummoningRitual object is required.")
            return None

        if len(self.__controlled_undead) >= Necromancer.MAX_CONTROLLED_UNDEAD:
            print(f"{self.__name} cannot control more than "
                  f"{Necromancer.MAX_CONTROLLED_UNDEAD} undead.")
            return None

        if not ritual.can_perform(self.__resources):
            print(f"{self.__name} does not have enough resources "
                  f"to perform {ritual.name}.")
            return None

        if not ritual.consume_resources(self.__resources):
            return None

        undead = ritual.create_undead(self.__next_unit_id)
        self.__next_unit_id += 1
        self.__controlled_undead.append(undead)
        print(f"{self.__name} summoned {undead.name} "
              f"(Unit #{undead.unit_id}).")
        return undead

    def dismiss(self, unit_id):
        undead = self.__find_undead(unit_id)
        if undead is None:
            print(f"No controlled undead has the unit identifier "
                  f"{unit_id}.")
            return False

        self.__controlled_undead.remove(undead)
        print(f"{undead.name} (Unit #{undead.unit_id}) has been dismissed.")
        return True

    def level_up_undead(self, unit_id):
        undead = self.__find_undead(unit_id)
        if undead is None:
            print(f"No controlled undead has the unit identifier "
                  f"{unit_id}.")
            return False
        return undead.level_up()

    def get_name(self):
        return self.__name

    def get_resources(self):
        return self.__resources

    def get_controlled_undead(self):
        return list(self.__controlled_undead)

    name = property(get_name)
    resources = property(get_resources)
    controlled_undead = property(get_controlled_undead)

    def __find_undead(self, unit_id):
        if not isinstance(unit_id, int) or isinstance(unit_id, bool):
            return None
        for undead in self.__controlled_undead:
            if undead.unit_id == unit_id:
                return undead
        return None

    def __str__(self):
        lines = [f"Necromancer: {self.__name}",
                 f"Resources: {self.__resources}",
                 f"Controlled undead ({len(self.__controlled_undead)}/"
                 f"{Necromancer.MAX_CONTROLLED_UNDEAD}):"]
        if not self.__controlled_undead:
            lines.append("  None")
        for undead in self.__controlled_undead:
            lines.append(f"  {undead}")
        return "\n".join(lines)

    def __repr__(self):
        return (f"Necromancer(name='{self.__name}', "
                f"necrotic_runes={self.__resources.necrotic_runes}, "
                f"spirit_runes={self.__resources.spirit_runes}, "
                f"bone_runes={self.__resources.bone_runes}, "
                f"flesh_runes={self.__resources.flesh_runes}, "
                f"ectoplasm={self.__resources.ectoplasm})")
