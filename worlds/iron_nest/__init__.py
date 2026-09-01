from ..AutoWorld import World, WebWorld
from .Items import (
    INItem,
    all_items,
    demoted_cards,
    filler_items,
    progression_items,
    support_items,
    trap_items,
    utility_items,
)
from .Locations import all_locations
from .Regions import mission_regions, medal_regions
from .Rules import set_connection_rules
from .Options import INOptions
from BaseClasses import Item, ItemClassification
from Options import OptionError

class INWeb(WebWorld):
    pass

class INWorld(World):
    game: str = "IRON NEST: Heavy Turret Simulator"
    topology_present = False
    web = INWeb()

    options_dataclass = INOptions
    options: INOptions

    item_name_to_id = all_items
    location_name_to_id = all_locations

    def generate_early(self) -> None:
        if not self.options.include_medals and self.options.goal != "mission_15":
            raise OptionError(
                f"{self.player_name}: goal '{self.options.goal.current_key}' requires medal "
                f"locations, but include_medals is off."
            )

    def create_regions(self) -> None:
        mission_regions(self.multiworld, self.player)
        if self.options.include_medals:
            medal_regions(self.multiworld, self.player)

    def set_rules(self) -> None:
        set_connection_rules(self.multiworld, self.options, self.player)

    def create_item(self, name: str) -> Item:
        classification = ItemClassification.filler
        if name in progression_items:
            classification = ItemClassification.progression
        elif name in utility_items:
            classification = ItemClassification.useful
        elif name in trap_items:
            classification = ItemClassification.trap
        return INItem(name, classification, all_items[name], self.player)

    def create_trap(self) -> Item:
        return self.create_item(self.random.choice(sorted(trap_items)))

    def create_items(self) -> None:
        locations = len(self.multiworld.get_unfilled_locations(self.player))
        pool = [self.create_item(name) for name in progression_items]

        optional = sorted(demoted_cards)
        if self.options.include_utility:
            optional += sorted(support_items)

        if self.options.include_medals:
            pool += [self.create_item(name) for name in optional]
        else:
            free = locations - len(pool)
            if self.options.traps and free > 0:
                pool.append(self.create_trap())
                free -= 1
            if self.options.filler and free > 0:
                pool.append(self.create_filler())
                free -= 1
            pool += [
                self.create_item(name)
                for name in self.random.sample(optional, min(free, len(optional)))
            ]

        remaining = locations - len(pool)
        traps = round(remaining * self.options.trap_percentage / 100) if self.options.traps else 0
        pool += [self.create_trap() for _ in range(traps)]
        pool += [self.create_filler() for _ in range(remaining - traps)]

        self.multiworld.itempool += pool

    def get_filler_item_name(self) -> str:
        return self.random.choice(sorted(filler_items))

    def fill_slot_data(self) -> dict:
        return {
            "goal": self.options.goal.current_key,
            "medal_tier": self.options.medal_tier.current_key,
            "include_medals": bool(self.options.include_medals),
        }
