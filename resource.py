class Resource:

    MIN_QUANTITY = 0

    def __init__(self, necrotic=0, spirit=0, bone=0, flesh=0, ectoplasm=0):
        self.__necrotic = self.__validate_quantity(necrotic)
        self.__spirit = self.__validate_quantity(spirit)
        self.__bone = self.__validate_quantity(bone)
        self.__flesh = self.__validate_quantity(flesh)
        self.__ectoplasm = self.__validate_quantity(ectoplasm)

    def collect_resources(self, necrotic, spirit, bone, flesh, ectoplasm):
        quantities = (necrotic, spirit, bone, flesh, ectoplasm)
        for q in quantities:
            if not self.__is_valid_quantity(q):
                print("Invalid resource quantities: collection rejected")
                return False

        self.__necrotic += necrotic
        self.__spirit += spirit
        self.__bone += bone
        self.__flesh += flesh
        self.__ectoplasm += ectoplasm
        return True
    
# refuses invalid quantities:
    def __is_valid_quantity(self, quantity):
        return (isinstance(quantity, int) and not isinstance(quantity, bool)
                and quantity >= Resource.MIN_QUANTITY)

# repairs invalid quantities, uses default value of 0 instead:
    def __validate_quantity(self, quantity):
        if self.__is_valid_quantity(quantity):
            return quantity
        return Resource.MIN_QUANTITY

    def meets_requirements(self, necrotic, spirit, bone, flesh, ectoplasm):
        return (self.__necrotic >= necrotic and
        self.__spirit >= spirit and 
        self.__bone >= bone and
        self.__flesh >= flesh and
        self.__ectoplasm >= ectoplasm)

    def spend_resources(self, necrotic, spirit, bone, flesh, ectoplasm):
        quantities = (necrotic, spirit, bone, flesh, ectoplasm)
        for q in quantities:
            if not self.__is_valid_quantity(q):
                print("Invalid resource quantities: spending rejected")
                return False
            
        if not self.meets_requirements(necrotic, spirit, bone, flesh, ectoplasm):
            print("Not enough resources: nothing spent")
            return False

        self.__necrotic -= necrotic
        self.__spirit -= spirit
        self.__bone -= bone
        self.__flesh -= flesh
        self.__ectoplasm -= ectoplasm
        return True

    def get_necrotic_runes(self):
        return self.__necrotic

    def get_spirit_runes(self):
        return self.__spirit

    def get_bone_runes(self):
        return self.__bone

    def get_flesh_runes(self):
        return self.__flesh

    def get_ectoplasm_runes(self):
        return self.__ectoplasm





# resources = Resource(2,4,2,4,2)
# print(resources)
 
