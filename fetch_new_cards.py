import json

# ==============================================================================
# In a real-world scenario, this is where you would connect to a live community
# CSV or API. For example:
#
# import requests
# import pandas as pd
# 
# url = "https://raw.githubusercontent.com/community/fc26-db/main/players.csv"
# df = pd.read_csv(url)
# ... formatting logic ...
# ==============================================================================

# For this tutorial, we will generate a clean list of dummy data. 
# Whenever this script runs, it writes these players into a Javascript file
# so your website can instantly read it.

mock_data = [
    {"id": 1, "name": "Mbappé", "rating": 91, "position": "ST", "club": "Real Madrid", "nation": "France"},
    {"id": 2, "name": "Haaland", "rating": 91, "position": "ST", "club": "Man City", "nation": "Norway"},
    {"id": 3, "name": "Bellingham", "rating": 90, "position": "CAM", "club": "Real Madrid", "nation": "England"},
    {"id": 4, "name": "Vinícius Jr.", "rating": 90, "position": "LW", "club": "Real Madrid", "nation": "Brazil"},
    {"id": 5, "name": "De Bruyne", "rating": 90, "position": "CM", "club": "Man City", "nation": "Belgium"},
    {"id": 6, "name": "Saka", "rating": 88, "position": "RW", "club": "Arsenal", "nation": "England"},
    {"id": 7, "name": "Saliba", "rating": 87, "position": "CB", "club": "Arsenal", "nation": "France"},
    {"id": 8, "name": "Foden", "rating": 88, "position": "RW", "club": "Man City", "nation": "England"}
]

# Create (or overwrite) the players.js file
file_content = f"const playersData = {json.dumps(mock_data)};\n"

with open('players.js', 'w', encoding='utf-8') as f:
    f.write(file_content)

print("Successfully fetched data and created players.js!")
