from dataclasses import dataclass
from Options import Choice, DefaultOnToggle, PerGameCommonOptions, Range, Toggle

class Goal(Choice):
    """
    Choose the goal for your run:
    - Mission 15: Complete misison 'White Shells'
    - All Medals: Get all Medals of a defined tier selected later (Bronze/Silver/Gold)
    - All Endings: Get all four endings of the game
    """
    display_name = "Goal"
    option_mission_15 = 0
    option_all_medals = 1
    option_all_endings = 2
    default = 0

class IncludeMedals(DefaultOnToggle):
    """Include medals in the location pool -- required for 'All Medals' and 'All Endings' goals"""
    display_name = "Include Medals"

class MedalTier(Choice):
    """
    Medal Tier for the 'All Medals' Goal
    The 'gold' Tier might be broken and not possible on all missions.
    See here for more info: https://steamcommunity.com/sharedfiles/filedetails/?id=3779182733
    """
    display_name = "Medal Tier"
    option_bronze = 0
    option_silver = 1
    option_gold = 2
    default = 0

class IncludeUtility(DefaultOnToggle):
    """Include the Spotter and Location Report cards in the item pool"""
    display_name = "Include Utility Items"

class Traps(Toggle):
    """
    Include traps in the item pool.
    With medals off exactly one trap is added; with medals on the free slots are filled
    according to Trap Percentage.
    """
    display_name = "Traps"

class TrapPercentage(Range):
    """
    Share of the leftover locations that become traps rather than filler.
    Only used when medals are included and traps are enabled.
    """
    display_name = "Trap Percentage"
    range_start = 0
    range_end = 100
    default = 20

class Filler(DefaultOnToggle):
    """
    Include filler in the item pool.
    With medals off exactly one filler item is added; with medals on filler takes every
    leftover location that Trap Percentage does not claim.
    """
    display_name = "Filler"

@dataclass
class INOptions(PerGameCommonOptions):
    goal: Goal
    include_medals: IncludeMedals
    medal_tier: MedalTier
    include_utility: IncludeUtility
    traps: Traps
    trap_percentage: TrapPercentage
    filler: Filler
