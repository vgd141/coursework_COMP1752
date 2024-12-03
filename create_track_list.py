import tkinter as tk
import json

class Frame2(tk.Frame):
    def __init__(self, parent, track_number_entry):
        super().__init__(parent)
        self.track_number_entry = track_number_entry
        self.tracks = [
            "01 Attention - Charlie Puth",
            "02 We Don't Talk Anymore - Charlie Puth",
            "03 IDGAF - Dua Lipa",
            "04 Shape of You - Ed Sheeran",
            "05 Safari - Serena"
        ]
        self.playlist = []
        self.play_counts = {track: 0 for track in self.tracks}

        self.GUI()

    def GUI(self):

        #Button to add track
        tk.Button(self, text="Add to Playlist", command=self.add).grid(row=0, column=2, padx=10, pady=10)

        #Text area to display the playlist
        self.playlist_text = tk.Text(self, height=10, width=50)
        self.playlist_text.grid(row=1, column=0, columnspan=3, padx=10, pady=10)

        #Label are to display message
        self.lable_msg = tk.Label(self)
        self.lable_msg.grid(row=3, column=0, columnspan=3, padx=10, pady=10)

        #Button to play playlist
        tk.Button(self, text="Play Playlist", command=self.play_playlist).grid(row=2, column=0, padx=10, pady=10)

        #Button to reset playlist
        tk.Button(self, text="Reset Playlist", command=self.reset_playlist).grid(row=2, column=1, padx=10, pady=10)

    def add(self):
        track_number = self.track_number_entry.get().strip()
        if not track_number.isdigit():
            self.lable_msg.config(text="Invalid track number")
            return

        track_index = int(track_number) - 1
        if 0 <= track_index < len(self.tracks):
            track_name = self.tracks[track_index]
            if track_name not in self.playlist:
                self.playlist.append(track_name)
                self.update()
                self.track_number_entry.delete(0, tk.END)  
            else:
                self.lable_msg.config(text="Track already in playlist")
        else:
            self.lable_msg.config(text="Invalid track number")

    def update(self):
        self.playlist_text.delete(1.0, tk.END)  #Clear the text area
        for track in self.playlist:
            self.playlist_text.insert(tk.END, track + "\n")  #Display each track in the playlist


    def play_playlist(self):
        for track in self.playlist:
            self.play_counts[track] += 1  #Increment play count
        self.save_to_json()
        self.lable_msg.config(text="Playlist played")

    def reset_playlist(self):
        self.playlist.clear()
        self.playlist_text.delete(1.0, tk.END)  #Clear text area
        self.lable_msg.config(text="Playlist has been reset")
    def save_to_json(self):
        # Load existing tracks from JSON
        try:
            with open('tracks.json', 'r') as file:
                data = json.load(file)
        except FileNotFoundError:
            data = {'tracks': []}

        # Update play counts in the JSON data
        for track_name in self.playlist:
            track_index = int(track_name.split(" ")[0]) - 1  #Extract the track index from the name
            if 0 <= track_index < len(data['tracks']):
                data['tracks'][track_index]['plays'] += 1

        # Save updated data back to the JSON file
        with open('tracks.json', 'w') as file:
            json.dump(data, file, indent=2)

    #Main GUI Application
if __name__ == "__main__":
    #the main window
    window = tk.Tk()
    window.title("Track Playlist Manager")  #the window title

    #Label and Entry for Track Number
    tk.Label(window, text="Enter Track Number:").grid(row=0, column=0, padx=10, pady=10)
    track_number_entry = tk.Entry(window, width=10)
    track_number_entry.grid(row=0, column=1, padx=10, pady=10)
    
    #Initialize Frame2 (the Playlist Manager) and add it to the window
    frame2 = Frame2(window, track_number_entry)
    frame2.grid(row=1, column=0, columnspan=3, padx=10, pady=10)

    window.mainloop()