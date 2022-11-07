class Player:
    def __init__(self, name, team, goals, assists):
        self.name = name
        self.team = team
        self.goals = goals
        self.assists = assists

    @property
    def points(self):
        return self.goals + self.assists

    def __str__(self):
        return f"{self.name} {self.team} {self.goals} + {self.assists} = {self.points}"

    def __eq__(self, o: object) -> bool:
        if isinstance(o, Player):
            return self.name == o.name and self.team == o.team and self.goals == o.goals and self.assists == o.assists
        return False

    def __ne__(self, o: object) -> bool:
        return not self.__eq__(o)
