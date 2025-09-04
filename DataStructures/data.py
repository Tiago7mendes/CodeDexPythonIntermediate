# Task 1: Create Player Data
players_data = [
    {"name": "Lionel Messi", "position": "Forward", "jersey_number": 10, "goals": 850, "assists": 480},
    {"name": "Kevin De Bruyne", "position": "Midfielder", "jersey_number": 17, "goals": 200, "assists": 320},
    {"name": "Virgil van Dijk", "position": "Defender", "jersey_number": 4, "goals": 1, "assists": 0},
    {"name": "Alisson Becker", "position": "Goalkeeper", "jersey_number": 1, "goals": 0, "assists": 1},
]

# Extract player names
names = [player["name"] for player in players_data]
print("Player Names:", names)

# Task 2: Analyze Player Positions
positions = [player["position"] for player in players_data]
print("Player Positions:", positions)

# Task 3: Update Player Statistics
# Messi scores another goal and makes another assist
players_data[0]["goals"] += 1
players_data[0]["assists"] += 1

# Task 4: Calculate Average Stats
average_goals = sum(player["goals"] for player in players_data) / len(players_data)
average_assists = sum(player["assists"] for player in players_data) / len(players_data)

print("Average Goals:", average_goals)
print("Average Assists:", average_assists)

# Task 5: Filter players who scored at least 1 goal
scorers = [player["name"] for player in players_data if player["goals"] > 0]
print("Players Who Scored At Least 1 Goal:", scorers)

# Task 6: Create a Function to print Player Summary
def print_player_summary(player):
    print(f"{player['name']} ({player['position']} #{player['jersey_number']}) - Goals: {player['goals']}, Assists: {player['assists']}")

print("\nPlayer Summaries:")
for player in players_data:
    print_player_summary(player)

# Task 7: find the Top Scorer
top_scorer = max(players_data, key=lambda p: p["goals"])
print(f"\nTop Scorer: {top_scorer['name']} with {top_scorer['goals']} goals.")