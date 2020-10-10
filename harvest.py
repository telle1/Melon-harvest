############
# Part 1   #
############


class MelonType(object):
    """A species of melon at a melon farm."""

    def __init__(self, code, first_harvest, color, is_seedless, is_bestseller, 
                 name):
        """Initialize a melon."""
        self.pairings = []
        self.code = code
        self.first_harvest = first_harvest
        self.color = color
        self.is_seedless = is_seedless
        self.is_bestseller = is_bestseller
        self.name = name

    def add_pairing(self, pairing):
        """Add a food pairing to the instance's pairings list."""
        self.pairings.append(pairing)
    def update_code(self, new_code):
        """Replace the reporting code with the new_code."""
        self.code = new_code

def make_melon_types():
    """Returns a list of current melon type instances."""
    all_melon_types = []
    # FIX VARIABLES
    muskmelon = MelonType('musk', '1998', 'green', 'seedless', 'bestseller', "Muskmelon")
    casaba = MelonType('cas', '2003', 'orange', 'has seeds', "not a bestseller", "Casaba")
    crenshaw = MelonType('cren', '1996', 'green', 'has seeds', "not a bestseller", "Crenshaw")
    yellow_watermelon = MelonType('yw', '2013', 'yellow', 'has seeds', 'bestseller', "Yellow Watermelon")

    all_melon_types.extend([muskmelon, casaba, crenshaw, yellow_watermelon])
 
    #Add pairings
    muskmelon.add_pairing("mint")
    casaba.add_pairing("mint")
    casaba.add_pairing("strawberries")
    crenshaw.add_pairing("proscuitto")
    yellow_watermelon.add_pairing("ice cream")

    return all_melon_types

def print_pairing_info(melon_types):
    """Prints information about each melon type's pairings."""
    for melon in melon_types:
        print(f"{melon.name} pairs with {melon.pairings}")

def make_melon_type_lookup(melon_types):
    """Takes a list of MelonTypes and returns a dictionary of melon type by code."""
    melon_code = {}

    for melon in melon_types: 
        melon_code[melon.code] = melon
    
    
    return melon_code 


# make_melon_type_lookup(make_melon_types())
# {'musk': 'Muskmelon', 'cas': 'Casaba', 'cren': 'Crenshaw', 'yw': 'Yellow Watermelon'}

############
# Part 2   #
############

class Melon(object):
    """A melon in a melon harvest."""
    def __init__(self, melon_type, shape_rating, color_rating, field, harvester):
        self.melon_type = melon_type
        self.shape_rating = shape_rating
        self.color_rating = color_rating
        self.field = field
        self.harvester = harvester

    def is_sellable(self):
        if (self.shape_rating > 5 and self.color_rating > 5 and self.field != 3):
            return True
        else:
            return False
#take an intsance of melon type and store it as an attribute of melon instance
def make_melons(melon_types): #make_melons(make_melon_types()) <- make_melon_types is a list of melon type instances
    """Returns a list of Melon objects."""
                 #make_melon_type_lookup(make_melon_types())
    melon_by_id = make_melon_type_lookup(melon_types) #{'musk': <__main__.MelonType object at 0x7fe206d4a908>}
    #print(melon_by_id)

    Melon1 = Melon(melon_by_id['yw'], 8, 7, 2, "Sheila")
    Melon2 = Melon(melon_by_id['yw'], 3, 4, 2, "Sheila")
    Melon3 = Melon(melon_by_id['yw'], 9, 8, 3, "Sheila")
    Melon4 = Melon(melon_by_id['cas'], 10, 6, 35, "Sheila")
    Melon5 = Melon(melon_by_id['cren'], 8, 9, 35, "Michael")
    Melon6 = Melon(melon_by_id['cren'], 8, 2, 35, "Michael")
    Melon7 = Melon(melon_by_id['cren'], 2, 3, 4, "Michael")
    Melon8 = Melon(melon_by_id['musk'], 6, 17, 4, "Michael")
    Melon9 = Melon(melon_by_id['yw'], 7, 10, 3, "Sheila")

    melon_harvest = []
    melon_harvest.extend([Melon1, Melon2, Melon3, Melon4, Melon5, Melon6, Melon7, Melon8, Melon9])

    # for melon in melon_harvest:
    #     print(melon.shape_rating)
    #print(melon_harvest)
    return melon_harvest

def get_sellability_report(melons): #get_sellability_report(make_melons(make_melon_types()))
    """Given a list of melon object, prints whether each one is sellable."""

    # for melon in melons:
    #     if melon.is_sellable:
    #         print(f"Harvested by {melon.harvested_by} from Field {melon.harvest_field} (CAN BE SOLD)")
    #     else:
    #         print(f"Harvested by {melon.harvested_by} from Field {melon.harvest_field} (NOT SELLABLE)")
    for melon in melons:
        harvested_by = f'Harvested by {melon.harvester}'
        field_num = f'Field #{melon.field}'
        status = 'CAN BE SOLD' if melon.is_sellable() else 'NOT SELLABLE'
        print(f'{harvested_by} from {field_num} {status}')
    # Fill in the rest 
#is_sellable(self, sellability):

#Melon1 = MelonType('musk', '1998', 'green', 'seedless', 'bestseller', 'Muskmelon')