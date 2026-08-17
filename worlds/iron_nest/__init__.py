from ..AutoWorld import World, WebWorld
from .Items import all_items, progression_items, utility_items, filler_items, trap_items, INItem
from .Locations import all_locations
from .Regions import mission_regions, medal_regions
from .Rules import set_connection_rules
from BaseClasses import Item, ItemClassification

class INWeb(WebWorld):
    pass

class INWorld(World):
    game: str = "IRON NEST: Heavy Turret Simulator"
    topology_present = False
    web = INWeb()

    item_name_to_id = all_items
    location_name_to_id = all_locations

    def create_regions(self) -> None:
        # TODO Add as Options
        mission_regions(self.multiworld, self.player)
        medal_regions(self.multiworld, self.player)

    def set_rules(self) -> None:
        set_connection_rules(self.multiworld, None, self.player)

    def create_item(self, name: str) -> Item:
        classification = ItemClassification.filler
        if name in progression_items:
            classification = ItemClassification.progression
        elif name in utility_items:
            classification = ItemClassification.useful
        elif name in trap_items:
            classification = ItemClassification.trap
        return INItem(name, classification, all_items[name], self.player)

    def create_items(self) -> None:
        self.multiworld.itempool += [self.create_item(item) for item in all_items]
        needed_fillers = len(self.multiworld.get_unfilled_locations(self.player)) - len(all_items)
        self.multiworld.itempool += [self.create_filler() for _ in range(needed_fillers)]