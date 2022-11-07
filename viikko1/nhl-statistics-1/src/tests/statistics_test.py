import unittest
from statistics import Statistics, SortBy
from player import Player

class PlayerReaderStub:
    def get_players(self):
        return [
            Player("Semenko", "EDM", 4, 12),
            Player("Lemieux", "PIT", 45, 54),
            Player("Kurri",   "EDM", 37, 53),
            Player("Yzerman", "DET", 42, 56),
            Player("Gretzky", "EDM", 35, 89)
        ]

class TestStatistics(unittest.TestCase):
    def setUp(self):
        self.statistics = Statistics(
            PlayerReaderStub()
        )

    def test_search_finds_all_players(self):
        self.assertEqual(self.statistics.search("Semenko"), Player("Semenko", "EDM", 4, 12))
        self.assertEqual(self.statistics.search("Lemieux"), Player("Lemieux", "PIT", 45, 54)),
        self.assertEqual(self.statistics.search("Kurri"),   Player("Kurri",   "EDM", 37, 53)),
        self.assertEqual(self.statistics.search("Yzerman"), Player("Yzerman", "DET", 42, 56)),
        self.assertEqual(self.statistics.search("Gretzky"), Player("Gretzky", "EDM", 35, 89))
    
    def test_search_returns_none_for_unknown_name(self):
        self.assertEqual(self.statistics.search("Martin"), None)

    def test_team_returns_correct_players(self):
        # I implemented __eq__ (and __ne__ by convention) for Player to make this easier
        self.assertEqual(self.statistics.team("EDM"), [
            Player("Semenko", "EDM", 4, 12),
            Player("Kurri",   "EDM", 37, 53),
            Player("Gretzky", "EDM", 35, 89)
        ])
        self.assertEqual(self.statistics.team("PIT"), [
            Player("Lemieux", "PIT", 45, 54),
        ])
        self.assertEqual(self.statistics.team("DET"), [
            Player("Yzerman", "DET", 42, 56),
        ])
        
    def test_unknown_team_is_empty(self):
        self.assertEqual(0, len(self.statistics.team("PHI")))

    def test_top_players_are_in_correct_order(self):
        self.assertEqual(self.statistics.top(5, SortBy.POINTS), [
            Player("Gretzky", "EDM", 35, 89),
            Player("Lemieux", "PIT", 45, 54),
            Player("Yzerman", "DET", 42, 56),
            Player("Kurri",   "EDM", 37, 53),
            Player("Semenko", "EDM", 4, 12),
        ])

        self.assertEqual(self.statistics.top(5, SortBy.GOALS), [
            Player("Lemieux", "PIT", 45, 54),
            Player("Yzerman", "DET", 42, 56),
            Player("Kurri",   "EDM", 37, 53),
            Player("Gretzky", "EDM", 35, 89),
            Player("Semenko", "EDM", 4, 12),
        ])
        
        self.assertEqual(self.statistics.top(5, SortBy.ASSISTS), [
            Player("Gretzky", "EDM", 35, 89),
            Player("Yzerman", "DET", 42, 56),
            Player("Lemieux", "PIT", 45, 54),
            Player("Kurri",   "EDM", 37, 53),
            Player("Semenko", "EDM", 4, 12),
        ])

    def test_top_sorts_by_points_when_parameter_omitted(self):
        self.assertEqual(self.statistics.top(5, SortBy.POINTS), self.statistics.top(5))

    def test_top_respects_count(self):
        # Test that it only returns the top 3 if requested
        self.assertEqual(self.statistics.top(3), [
            Player("Gretzky", "EDM", 35, 89),
            Player("Lemieux", "PIT", 45, 54),
            Player("Yzerman", "DET", 42, 56),
        ])