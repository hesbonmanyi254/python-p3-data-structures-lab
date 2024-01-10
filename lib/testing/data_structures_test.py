# data_structures_test.py

from data_structures import get_names, get_spiciest_foods, print_spicy_foods

class TestDataStructures:
    SPICY_FOODS = [
        {'cuisine': 'Thai', 'heat_level': 9, 'name': 'Green Curry'},
        {'cuisine': 'American', 'heat_level': 3, 'name': 'Buffalo Wings'},
        {'cuisine': 'Sichuan', 'heat_level': 6, 'name': 'Mapo Tofu'},
    ]

    def test_get_names(self):
        """Test get_names function."""
        assert get_names(self.SPICY_FOODS) == ['Green Curry', 'Buffalo Wings', 'Mapo Tofu']

    def test_get_spiciest_foods(self):
        """Test get_spiciest_foods function."""
        assert get_spiciest_foods(self.SPICY_FOODS) == [{'cuisine': 'Thai', 'heat_level': 9, 'name': 'Green Curry'}]

    # You can add more test functions if needed

if __name__ == "__main__":
    # You can add code to run tests here if needed
    pass
