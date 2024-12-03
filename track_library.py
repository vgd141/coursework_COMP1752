from library_item import LibraryItem
import json

library = {}
library["01"] = LibraryItem("Attention", "Charlie Puth", 4)
library["02"] = LibraryItem("We Don't Talk Anymore", "Charlie Puth", 5)
library["03"] = LibraryItem("IDGAF", "Dua Lipa", 2)
library["04"] = LibraryItem("Shape of You", "Ed Sheeran", 1)
library["05"] = LibraryItem("Safari", "Serena", 3)


def read_tracks_from_json():
    try:
        with open('tracks.json', 'r') as file:
            data = json.load(file)
            tracks = data[tracks]
            output = ""
            for i, track in enumerate(tracks, 1):
                track_number = str(i).zfill(2)
                stars = "*" * track["rating"]
                output += f"{track_number} {track['name']} {stars}\n"
            return output
    except FileNotFoundError:
        return None


def list_all():
    json_tracks = read_tracks_from_json()
    if json_tracks is not None:
        return json_tracks

    output = ""
    for key in library:
        item = library[key]
        output += f"{key} {item.info()}\n"
    return output


def get_track_from_json(track_number):
    try:
        with open('tracks.json', 'r') as file:
            data = json.load(file)
            tracks = data['tracks']
            if 1 <= track_number <= len(tracks):
                return tracks[track_number - 1]
    except FileNotFoundError:
        return None
    return None


def get_name(key):
    # First try to get from JSON
    track_number = int(key) if key.isdigit() else 0
    track = get_track_from_json(track_number)
    if track:
        name = track['name'].split(' - ')[0]
        return name

    #Fallback to library
    try:
        item = library[key]
        return item.name
    except KeyError:
        return None


def get_artist(key):
    #First try to get from JSON
    track_number = int(key) if key.isdigit() else 0
    track = get_track_from_json(track_number)
    if track:
        artist = track['name'].split(' - ')[1]
        return artist

    #Fallback to library
    try:
        item = library[key]
        return item.artist
    except KeyError:
        return None


def get_rating(key):
    # First try to get from JSON
    track_number = int(key) if key.isdigit() else 0
    track = get_track_from_json(track_number)
    if track:
        return track['rating']

    # Fallback to library
    try:
        item = library[key]
        return item.rating
    except KeyError:
        return -1


def get_play_count(key):
    # First try to get from JSON
    track_number = int(key) if key.isdigit() else 0
    track = get_track_from_json(track_number)
    if track:
        return track['plays']

    # Fallback to library
    try:
        item = library[key]
        return item.play_count
    except KeyError:
        return -1


def increment_play_count(key):
    track_number = int(key) if key.isdigit() else 0
    try:
        with open('tracks.json', 'r') as file:
            data = json.load(file)
            if 1 <= track_number <= len(data['tracks']):
                data['tracks'][track_number - 1]['plays'] += 1
                with open('tracks.json', 'w') as write_file:
                    json.dump(data, write_file, indent=2)
                return
    except FileNotFoundError:
        pass

    # Fallback to library
    try:
        item = library[key]
        item.play_count += 1
    except KeyError:
        return


def set_rating(key, rating):
    track_number = int(key) if key.isdigit() else 0
    try:
        with open('tracks.json', 'r') as file:
            data = json.load(file)
            if 1 <= track_number <= len(data['tracks']):
                data['tracks'][track_number - 1]['rating'] = rating
                with open('tracks.json', 'w') as write_file:
                    json.dump(data, write_file, indent=2)
                return
    except FileNotFoundError:
        pass

    # Fallback to library
    try:
        item = library[key]
        item.rating = rating
    except KeyError:
        return
#find tracks by artist
def find_tracks_by_artist(artist_name):
    tracks_by_artist = []
    for key, item in library.items():
        if item.artist.lower() == artist_name.lower():
            tracks_by_artist.append(item)
    return tracks_by_artist
# find tracks by track name
def find_tracks_by_name(track_name):
    tracks_by_name = []
    for key, item in library.items():
        if item.name.lower() == track_name.lower():
            tracks_by_name.append(item)
    return tracks_by_name