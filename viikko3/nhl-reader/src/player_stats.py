class PlayerStats:
    def __init__(self, reader):
        self.reader = reader

    def top_scorers_by_nationality(self, nationality):
        player_list = self.reader.get_players()
        filtered_player_list = [player for player in player_list if player.nationality == nationality]
        filtered_player_list.sort(reverse=True, key=lambda player: player.goals + player.assists)

        return filtered_player_list