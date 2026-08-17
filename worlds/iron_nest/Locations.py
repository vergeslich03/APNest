from BaseClasses import Location

class INLocation(Location):
    game: str = "IRON NEST: Heavy Turret Simulator"

# ID specs
# 914XYYY
# 914 --> Game
# X --> Goal (0: Missions, 1: Medals)
# YYY --> Location

mission_locations = {
    "Mission 1: Calibration Fire": 9140001,
    "Mission 2: Fire and Light": 9140002,
    "Mission 3: Liberation": 9140003,
    "Mission 4: Counter-Battery": 9140004,
    "Mission 5: Iron Road": 9140005,
    "Mission 6: Siege of Cartagena": 9140006,
    "Mission 7: The Gorge": 9140007,
    "Mission 8: Rock of Gibraltar": 9140008,
    "Mission 9: Dead Reckoning": 9140009,
    "Mission 10: Fire on Call": 9140010,
    "Mission 11: High Tide": 9140011,
    "Mission 12: Blind Fire": 9140012,
    "Mission 13: Phantom Battery": 9140013,
    "Mission 14: Final Harvest": 9140014,
    "Mission 15: White Shells": 9140015,
}

# abbreviation index
# OE --> Ordnance Efficiency Laurel
# MF --> Measured Fire Star
# MC --> Marksman's Cross
# UV --> Unbroken Volley Medal
# AS --> Austere Service Medal
# SC --> Salvo Commendation
# CB --> Counter-Battery Commendation
# NQ --> No Quarter Cross
medal_locations = {
    "Mission 1: Calibration Fire - OE Bronze": 9141001,
    "Mission 1: Calibration Fire - OE Silver": 9141002,
    "Mission 1: Calibration Fire - OE Gold": 9141003,
    "Mission 2: Fire and Light - OE Bronze": 9141004,
    "Mission 2: Fire and Light - OE Silver": 9141005,
    "Mission 2: Fire and Light - OE Gold": 9141006,
    "Mission 3: Liberation - MF Bronze": 9141007,
    "Mission 3: Liberation - MF Silver": 9141008,
    "Mission 3: Liberation - MF Gold": 9141009,
    "Mission 3: Liberation - MC Bronze": 9141010,
    "Mission 3: Liberation - MC Silver": 9141011,
    "Mission 3: Liberation - MC Gold": 9141012,
    "Mission 3: Liberation - UV Bronze": 9141013,
    "Mission 3: Liberation - UV Silver": 9141014,
    "Mission 3: Liberation - UV Gold": 9141015,
    "Mission 3: Liberation - AS Bronze": 9141016,
    "Mission 3: Liberation - AS Silver": 9141017,
    "Mission 3: Liberation - AS Gold": 9141018,
    "Mission 4: Counter-Battery - SC Bronze": 9141019,
    "Mission 4: Counter-Battery - SC Silver": 9141020,
    "Mission 4: Counter-Battery - SC Gold": 9141021,
    "Mission 4: Counter-Battery - CB Bronze": 9141022,
    "Mission 4: Counter-Battery - CB Silver": 9141023,
    "Mission 4: Counter-Battery - CB Gold": 9141024,
    "Mission 4: Counter-Battery - AS Bronze": 9141025,
    "Mission 4: Counter-Battery - AS Silver": 9141026,
    "Mission 4: Counter-Battery - AS Gold": 9141027,
    "Mission 4: Counter-Battery - NQ Bronze": 9141028,
    "Mission 4: Counter-Battery - NQ Silver": 9141029,
    "Mission 4: Counter-Battery - NQ Gold": 9141030,
}

all_locations = {
    **mission_locations,
    **medal_locations,
}