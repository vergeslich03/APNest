from BaseClasses import Item

class INItem(Item):
    game: str = "IRON NEST: Heavy Turret Simulator"

# ID specs
# 914XYYY
# 914 --> Game
# X --> Type (0: progression, 1: utility, 2: filler, 3: traps)
# YYY --> Item

progression_items = {
    "Punchcard - HE Shell": 9140001,
    "Punchcard - STAR Shell": 9140002,
    "Punchcard - AP Shell": 9140003,
    "Punchcard - SMK Shell": 9140004,
    "Punchcard - TEAR Shell": 9140005,
    "Punchcard - INCN Shell": 9140006,
    "Punchcard - HCHE Shell": 9140007,
    "Punchcard - DRIL Shell": 9140008,
    "Punchcard - LE Shell": 9140009,
    "Punchcard - PHGN Shell": 9140010,
    "Punchcard - WP Shell": 9140011,
    "Punchcard - PCLM Shell": 9140012,
    "Punchcard - APHE Shell": 9140013,
    "Punchcard - FLCH Shell": 9140014,
    "Punchcard - PRPG Shell": 9140015,
    "Punchcard - THRM Shell": 9140016,
    "Punchcard - ATMC Shell": 9140017,
    "Punchcard - CYAN Shell": 9140018,
    "Punchcard - EQKE Shell": 9140019,
    "Punchcard - Powder Charges": 9140020,
    "Punchcard - Scout Plane": 9140021,
    "Punchcard - Emergency Move": 9140022,
}

utility_items = {
    "Punchcard - Spotter": 9141001,
    "Requisition - Spotter": 9141002,
    "Punchcard - Location Report": 9141003,
    "Requisition - Location Report": 9141004,
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

all_items = {
    **progression_items,
    **utility_items,
    **filler_items,
    **trap_items,
}