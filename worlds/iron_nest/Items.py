from BaseClasses import Item

class INItem(Item):
    game: str = "IRON NEST: Heavy Turret Simulator"

# ID specs
# 914XYYY
# 914 --> Game
# X --> Type (0: progression, 1: utility, 2: filler, 3: traps)
# YYY --> Item

progression_items = {
    "Punchcard - AP Shell": 9140001,
    "Punchcard - SMK Shell": 9140002,
    "Punchcard - TEAR Shell": 9140003,
    "Punchcard - ATMC Shell": 9140004,
    "Punchcard - Powder Charges": 9140005,
    "Punchcard - Scout Plane": 9140006,
    "Punchcard - Emergency Move": 9140007,
}

utility_items = {
    "Punchcard - Spotter": 9141001,
    "Requisition - Spotter": 9141002,
    "Punchcard - Location Report": 9141003,
    "Requisition - Location Report": 9141004,
    "Punchcard - HE Shell": 9141005,
    "Punchcard - STAR Shell": 9141006,
    "Punchcard - INCN Shell": 9141007,
    "Punchcard - HCHE Shell": 9141008,
    "Punchcard - DRIL Shell": 9141009,
    "Punchcard - LE Shell": 9141010,
    "Punchcard - PHGN Shell": 9141011,
    "Punchcard - WP Shell": 9141012,
    "Punchcard - PCLM Shell": 9141013,
    "Punchcard - APHE Shell": 9141014,
    "Punchcard - FLCH Shell": 9141015,
    "Punchcard - PRPG Shell": 9141016,
    "Punchcard - THRM Shell": 9141017,
    "Punchcard - CYAN Shell": 9141018,
    "Punchcard - EQKE Shell": 9141019,
}

filler_items = {
    "Requisition - Powder Charges": 9142001,
    "Requisition - Requisition Points": 9142002,
}

trap_items = {
    "Trap - Emergency Move": 9143001,
    "Trap - Magazine Filler": 9143002,
    "Trap - Sabotage": 9143003,
    "Trap - Counter-Battery": 9143004,
}

support_items = {
    "Punchcard - Spotter",
    "Requisition - Spotter",
    "Punchcard - Location Report",
    "Requisition - Location Report",
}

demoted_cards = set(utility_items) - support_items

all_items = {
    **progression_items,
    **utility_items,
    **filler_items,
    **trap_items,
}
