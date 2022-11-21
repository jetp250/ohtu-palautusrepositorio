import requests
from player import Player

def main():
    print("Test")
    url = "https://studies.cs.helsinki.fi/nhlstats/2021-22/players"
    response = requests.get(url).json()

    #print("JSON-muotoinen vastaus:")
    #print(response)

    players = []

    for player_dict in response:
        player = Player(
            player_dict['name'],
            player_dict['team'],
            player_dict['nationality'],
            player_dict['goals'],
            player_dict['assists']
        )

        players.append(player)

    #print("Oliot:")

    finnish_players_sorted = [player for player in players if player.nationality == "FIN"]
    finnish_players_sorted.sort(reverse=True, key=lambda player: player.goals + player.assists)

    for player in finnish_players_sorted:
        print(player)

if __name__ == "__main__":
    main()

# {"name":"P.K. Subban","nationality":"CAN","assists":17,"goals":5,"penalties":82,"team":"NJD","games":77}