
# This is definitely going overboard but not sure what is expected
MIN_POINTS_TO_WIN = 4
MIN_LEAD_TO_WIN = 2

class TennisGame:
    def __init__(self, player_1_name: str, player_2_name: str):
        self._player_1_name = player_1_name
        self._player_2_name = player_2_name
        self._player_1_score = 0
        self._player_2_score = 0

    def won_point(self, player_name: str):
        if player_name == self._player_1_name:
            self._player_1_score += 1
        elif player_name == self._player_2_name:
            self._player_2_score += 1

    def get_score(self) -> str:
        if self._player_1_score == self._player_2_score:
            return self._get_draw_score()

        if self._player_1_score >= MIN_POINTS_TO_WIN or self._player_2_score >= MIN_POINTS_TO_WIN:
            return self._get_past_deuce_score()
            
        calls = ["Love", "Fifteen", "Thirty", "Forty"]
        return calls[self._player_1_score] + "-" + calls[self._player_2_score]

    def _get_draw_score(self) -> str:
        calls = ["Love-All", "Fifteen-All", "Thirty-All"]

        if self._player_1_score >= len(calls):
            return "Deuce"
        return calls[self._player_1_score]

    def _get_past_deuce_score(self) -> str:
        if self._player_1_score >= self._player_2_score + MIN_LEAD_TO_WIN:
            return "Win for " + self._player_1_name

        if self._player_2_score >= self._player_1_score + MIN_LEAD_TO_WIN:
            return "Win for " + self._player_2_name

        if self._player_1_score > self._player_2_score:
            return "Advantage " + self._player_1_name
        return "Advantage " + self._player_2_name