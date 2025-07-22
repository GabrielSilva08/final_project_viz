import pandas as pd
import re

def safe_int(x):
    try:
        return int(float(x))
    except (ValueError, TypeError):
        return pd.NA
    
def clean_name(name):
    if pd.isna(name):
        return ""
    # Remove colchetes, aspas, e espaços extras
    name = re.sub(r"[\[\]\(\)\"']", "", str(name))
    # Se houver vírgula, pega só o primeiro nome (antes da vírgula)
    name = name.split(",")[0].strip()
    return name

def fix_genre(genre):
    if genre == "Real time Strategy":
        return "Strategy"
    elif genre == "Board Games":
        return "Card & Board Game"
    elif genre == "Role-Playing":
        return "RPG"
    elif genre == "Action-Adventure":
        return "Adventure"
    elif genre == "Platformer":
        return "Platform"
    elif genre == "Brawler":
        return "Adventure"
    elif genre == "Simulator":
        return "Simulation"
    elif genre == "Massively Multiplayer":
        return "RPG"
    return genre