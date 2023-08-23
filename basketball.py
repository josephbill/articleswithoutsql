def game_dict():
    return {
        "home": {
            "team_name": "Cleveland Cavaliers",
            "colors": ["Wine", "Gold"],
            "players": [
                {
                    "name": "Jarrett Allen",
                    "number": 31,
                    "position": "Center",
                    "points_per_game": 16.1,
                    "rebounds_per_game": 10.8,
                    "assists_per_game": 1.6,
                    "steals_per_game": 0.8,
                    "blocks_per_game": 1.3,
                    "career_points": 3945,
                    "age": 24,
                    "height_inches": 82,
                    "shoe_brand": "Nike",
                },
                {
                    "name": "Darius Garland",
                    "number": 10,
                    "position": "Point Guard",
                    "points_per_game": 21.7,
                    "rebounds_per_game": 3.3,
                    "assists_per_game": 8.6,
                    "steals_per_game": 1.3,
                    "blocks_per_game": 0.1,
                    "career_points": 3142,
                    "age": 22,
                    "height_inches": 73,
                    "shoe_brand": "Nike",
                },
                {
                    "name": "Evan Mobley",
                    "number": 4,
                    "position": "Center",
                    "points_per_game": 15.0,
                    "rebounds_per_game": 8.3,
                    "assists_per_game": 2.5,
                    "steals_per_game": 0.8,
                    "blocks_per_game": 1.7,
                    "career_points": 1034,
                    "age": 21,
                    "height_inches": 83,
                    "shoe_brand": "Adidas",
                },
                {
                    "name": "Kevin Love",
                    "number": 0,
                    "position": "Power Forward",
                    "points_per_game": 13.6,
                    "rebounds_per_game": 7.2,
                    "assists_per_game": 2.2,
                    "steals_per_game": 0.4,
                    "blocks_per_game": 0.2,
                    "career_points": 14305,
                    "age": 34,
                    "height_inches": 80,
                    "shoe_brand": "Nike",
                },
                {
                    "name": "Isaac Okoro",
                    "number": 35,
                    "position": "Small Forward",
                    "points_per_game": 8.8,
                    "rebounds_per_game": 3.0,
                    "assists_per_game": 1.8,
                    "steals_per_game": 0.8,
                    "blocks_per_game": 0.3,
                    "career_points": 1234,
                    "age": 21,
                    "height_inches": 77,
                    "shoe_brand": "Nike",
                },
                {
                    "name": "Ricky Rubio",
                    "number": 99,
                    "position": "Point Guard",
                    "points_per_game": 13.1,
                    "rebounds_per_game": 4.1,
                    "assists_per_game": 6.6,
                    "steals_per_game": 1.4,
                    "blocks_per_game": 0.2,
                    "career_points": 7399,
                    "age": 31,
                    "height_inches": 74,
                    "shoe_brand": "Adidas",
                },
            ],
        },
            
        "away": {
            "team_name": "Washington Wizards",
            "colors": ["Red", "White", "Navy Blue"],
            "players": [   
                {
                    "name": "Bradley Beal",
                    "number": 3,
                    "position": "Shooting Guard",
                    "points_per_game": 23.2,
                    "rebounds_per_game": 4.7,
                    "assists_per_game": 6.6,
                    "steals_per_game": 0.9,
                    "blocks_per_game": 0.4,
                    "career_points": 14231,
                    "age": 29,
                    "height_inches": 76,
                    "shoe_brand": "Nike",
                },
                {
                    "name": "Kyle Kuzma",
                    "number": 33,
                    "position": "Power Forward",
                    "points_per_game": 17.1,
                    "rebounds_per_game": 8.5,
                    "assists_per_game": 3.5,
                    "steals_per_game": 0.6,
                    "blocks_per_game": 0.9,
                    "career_points": 5336,
                    "age": 27,
                    "height_inches": 81,
                    "shoe_brand": "Puma",
                },
                {
                    "name": "Kentavious Caldwell-Pope",
                    "number": 1,
                    "position": "Shooting Guard",
                    "points_per_game": 13.2,
                    "rebounds_per_game": 3.4,
                    "assists_per_game": 1.9,
                    "steals_per_game": 1.1,
                    "blocks_per_game": 0.3,
                    "career_points": 7911,
                    "age": 29,
                    "height_inches": 77,
                    "shoe_brand": "Nike",
                },
                {
                    "name": "Davis Bertans",
                    "number": 42,
                    "position": "Power Forward",
                    "points_per_game": 5.6,
                    "rebounds_per_game": 2.1,
                    "assists_per_game": 0.6,
                    "steals_per_game": 0.3,
                    "blocks_per_game": 0.3,
                    "career_points": 3165,
                    "age": 29,
                    "height_inches": 82,
                    "shoe_brand": "Nike",
                },
                {
                    "name": "Kristaps Porzingis",
                    "number": 6,
                    "position": "Power Forward",
                    "points_per_game": 22.1,
                    "rebounds_per_game": 8.8,
                    "assists_per_game": 2.9,
                    "steals_per_game": 0.7,
                    "blocks_per_game": 1.5,
                    "career_points": 6371,
                    "age": 27,
                    "height_inches": 87,
                    "shoe_brand": "Adidas",
                },
                {
                    "name": "Rui Hachimura",
                    "number": 8,
                    "position": "Power Forward",
                    "points_per_game": 11.3,
                    "rebounds_per_game": 3.8,
                    "assists_per_game": 1.1,
                    "steals_per_game": 0.5,
                    "blocks_per_game": 0.2,
                    "career_points": 1913,
                    "age": 24,
                    "height_inches": 80,
                    "shoe_brand": "Jordan",
                },
            ]
        }
    }


def num_points_per_game(player_name):
    game_data = game_dict()
    for team in game_data.values():
        for player in team['players']:
            if player['name'] == player_name:
                return player['points_per_game']
    return None

def player_age(player_name):
    game_data = game_dict()
    for team in game_data.values():
        for player in team['players']:
            if player['name'] == player_name:
                return player['age']
    return None

def team_colors(team_name):
    game_data = game_dict()
    for team in game_data.values():
        if team['team_name'] == team_name:
            return team.get('colors', [])
    return []

def team_names():
    game_data = game_dict()
    return [team['team_name'] for team in game_data.values()]

def player_numbers(team_name):
    game_data = game_dict()
    for team in game_data.values():
        if team['team_name'] == team_name:
            return [player['jersey_number'] for player in team['players']]
    return []

def player_stats(player_name):
    game_data = game_dict()
    for team in game_data.values():
        for player in team['players']:
            if player['name'] == player_name:
                return player
    return None

def average_rebounds_by_shoe_brand():
    game_data = game_dict()
    brand_rebounds = {}
    
    for team in game_data.values():
        for player in team['players']:
            brand = player['shoe_brand']
            rebounds = player.get('rebounds_per_game', 0)
            
            if brand not in brand_rebounds:
                brand_rebounds[brand] = []
            brand_rebounds[brand].append(rebounds)
    
    for brand, rebounds_list in brand_rebounds.items():
        avg_rebounds = sum(rebounds_list) / len(rebounds_list)
        print(f"{brand}: {avg_rebounds:.2f}")

def player_with_most_career_points():
    game_data = game_dict()
    max_career_points = 0
    max_career_player = None
    
    for team in game_data.values():
        for player in team['players']:
            if player['career_points'] > max_career_points:
                max_career_points = player['career_points']
                max_career_player = player['name']
    
    return max_career_player

def shared_jersey_numbers():
    game_data = game_dict()
    all_jersey_numbers = set()
    shared_numbers = []
    
    for team in game_data.values():
        for player in team['players']:
            if 'jersey_number' in player:
                jersey_number = player['jersey_number']
                if jersey_number in all_jersey_numbers:
                    shared_numbers.append(jersey_number)
                else:
                    all_jersey_numbers.add(jersey_number)
    
    return shared_numbers

def player_with_longest_name():
    game_data = game_dict()
    longest_name = ''
    
    for team in game_data.values():
        for player in team['players']:
            name = player['name']
            if len(name) > len(longest_name):
                longest_name = name
    
    return longest_name

# Testing the functions
print(num_points_per_game("LeBron James"))
print(player_age("Stephen Curry"))
print(team_colors("Cleveland Cavaliers"))
print(team_names())
print(player_numbers("Golden State Warriors"))
print(player_stats("Darius Garland"))
average_rebounds_by_shoe_brand()
print(player_with_most_career_points())
print(shared_jersey_numbers())
print(player_with_longest_name())
