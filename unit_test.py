import pytest
from library_item import LibraryItem


def test_library_item_initialization():
    item = LibraryItem("Test Song", "Test Artist", 3)
    assert item.name == "Test Song"
    assert item.artist == "Test Artist"
    assert item.rating == 3
    assert item.play_count == 0


def test_library_item_default_rating():
    item = LibraryItem("Test Song", "Test Artist")
    assert item.rating == 0
    assert item.play_count == 0


def test_library_item_info():
    item = LibraryItem("Test Song", "Test Artist", 3)
    expected_info = "Test Song - Test Artist ***"
    assert item.info() == expected_info


def test_library_item_stars():
    test_cases = [
        (0, ""),
        (1, "*"),
        (3, "***"),
        (5, "*****")
    ]

    for rating, expected_stars in test_cases:
        item = LibraryItem("Test Song", "Test Artist", rating)
        assert item.stars() == expected_stars


def test_play_count_increment():
    item = LibraryItem("Test Song", "Test Artist")
    assert item.play_count == 0
    item.play_count += 1
    assert item.play_count == 1


def test_rating_modification():
    item = LibraryItem("Test Song", "Test Artist", 3)
    assert item.rating == 3
    item.rating = 4
    assert item.rating == 4
    assert item.stars() == "****"


@pytest.mark.parametrize("name,artist,rating", [
    ("", "", 0),
    ("Song", "", 1),
    ("", "Artist", 2),
    ("Song", "Artist", 5)
])
def test_library_item_various_inputs(name, artist, rating):
    item = LibraryItem(name, artist, rating)
    assert item.name == name
    assert item.artist == artist
    assert item.rating == rating