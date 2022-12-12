
from matchers import And, PlaysIn, HasFewerThan, HasAtLeast, Or

class QueryBuilder:
    def __init__(self):
        self._matchers = []

    def playsIn(self, team):
        self._matchers.append(PlaysIn(team))
        return self

    def hasAtLeast(self, value, attr):
        self._matchers.append(HasAtLeast(value, attr))
        return self

    def hasFewerThan(self, value, attr):
        self._matchers.append(HasFewerThan(value, attr))
        return self

    def oneOf(self, *matchers):
        self._matchers.append(Or(*matchers))
        return self

    def build(self):
        matchers = self._matchers
        self._matchers = []

        # And handles the case of zero matchers
        return And(*matchers)
    