from BaseClasses import MultiWorld, Region
from .Locations import INLocation, medal_locations, mission_locations

def mission_regions(world: MultiWorld, player: int):
    world.regions.append(Region("Menu", player, world))

    for mission_name, mission_id in mission_locations.items():
        region = Region(mission_name, player, world)
        region.locations += [
            INLocation(player, mission_name, mission_id, region)
        ]
        world.regions.append(region)

def medal_regions(world: MultiWorld, player: int):
    for mission_name in mission_locations.keys():
        region = world.get_region(mission_name, player)
        region.locations += [
            INLocation(player, medal_name, medal_id, region)
            for medal_name, medal_id
            in medal_locations.items()
            if medal_name.startswith(mission_name)
        ]