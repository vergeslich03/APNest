from BaseClasses import MultiWorld

def set_connection_rules(world: MultiWorld, options, player: int):
    menu_region = world.get_region("Menu", player)
    mission_1_region = world.get_region("Mission 1: Calibration Fire", player)
    mission_2_region = world.get_region("Mission 2: Fire and Light", player)
    mission_3_region = world.get_region("Mission 3: Liberation", player)
    mission_4_region = world.get_region("Mission 4: Counter-Battery", player)
    mission_5_region = world.get_region("Mission 5: Iron Road", player)
    mission_6_region = world.get_region("Mission 6: Siege of Cartagena", player)
    mission_7_region = world.get_region("Mission 7: The Gorge", player)
    mission_8_region = world.get_region("Mission 8: Rock of Gibraltar", player)
    mission_9_region = world.get_region("Mission 9: Dead Reckoning", player)
    mission_10_region = world.get_region("Mission 10: Fire on Call", player)
    mission_11_region = world.get_region("Mission 11: High Tide", player)
    mission_12_region = world.get_region("Mission 12: Blind Fire", player)
    mission_13_region = world.get_region("Mission 13: Phantom Battery", player)
    mission_14_region = world.get_region("Mission 14: Final Harvest", player)
    mission_15_region = world.get_region("Mission 15: White Shells", player)

    menu_region.connect(connecting_region=mission_1_region)
    mission_1_region.connect(
        connecting_region=mission_2_region,
    )
    mission_2_region.connect(
        connecting_region=mission_3_region,
        rule=lambda state: state.has_all(
            ["Punchcard - AP Shell", "Punchcard - Powder Charges"],
            player,
        ),
    )
    mission_3_region.connect(
        connecting_region=mission_4_region
    )
    mission_4_region.connect(
        connecting_region=mission_5_region,
    )
    mission_5_region.connect(
        connecting_region=mission_6_region,
        rule=lambda state: state.has("Punchcard - SMK Shell", player),
    )
    mission_6_region.connect(
        connecting_region=mission_7_region,
    )
    mission_7_region.connect(
        connecting_region=mission_8_region,
    )
    mission_8_region.connect(
        connecting_region=mission_9_region,
        rule=lambda state: state.has("Punchcard - TEAR Shell", player),
    )
    mission_9_region.connect(
        connecting_region=mission_10_region,
    )
    mission_10_region.connect(
        connecting_region=mission_11_region,
    )
    mission_11_region.connect(
        connecting_region=mission_12_region,
    )
    mission_12_region.connect(
        connecting_region=mission_13_region,
        rule=lambda state: state.has_all(
            ["Punchcard - Emergency Move", "Punchcard - Scout Plane"],
            player,
        ),
    )
    mission_13_region.connect(
        connecting_region=mission_14_region,
    )
    mission_14_region.connect(
        connecting_region=mission_15_region,
        rule=lambda state: state.has("Punchcard - ATMC Shell", player),
    )

    world.completion_condition[player] = lambda state: state.can_reach(
        "Mission 15: White Shells",
        'Location',
        player,
    )