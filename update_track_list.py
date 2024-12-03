import  tkinter as tk
import json

class Frame3(tk.Frame):
    def __init__(self, parent, track_number_entry):
        super().__init__(parent)
        self.track_number_entry = track_number_entry
        self.tracks = [
            {"name": "Attention - Charlie Puth", "rating": 4, "plays": 0},
            {"name": "We Don't Talk Anymore - Charlie Puth", "rating": 5, "plays": 0},
            {"name": "IDGAF - Dua Lipa", "rating": 2, "plays": 0},
            {"name": "Shape of You - Ed Sheeran", "rating": 2, "plays": 0},
            {"name": "Safari - Serena", "rating": 1, "plays": 0}
        ]

        self.UI()

    def UI(self):
        # Label for track number input
        tk.Label(self, text="Enter Track Number:").grid(row=0, column=0, padx=10, pady=10)
        self.track_number_entry = tk.Entry(self)
        self.track_number_entry.grid(row=0, column=1, padx=10, pady=10)

        # Label for new rating input
        tk.Label(self, text="Enter New Rating (1-5):").grid(row=1, column=0, padx=10, pady=10)
        self.entry_new_rating = tk.Entry(self)
        self.entry_new_rating.grid(row=1, column=1, padx=10, pady=10)

        # Button to update track rating
        tk.Button(self, text="Update Rating", command=self.update).grid(row=2, column=0, columnspan=2, pady=10)

        # Label to display results or error messages
        self.result_label = tk.Label(self, text="", wraplength=300)
        self.result_label.grid(row=3, column=0, columnspan=2, padx=10, pady=10)
        
    #Load existing tracks from tracks.json.
    def load_tracks_from_json(self):
        try:
            with open('tracks.json', 'r') as file:
                data = json.load(file)
                return data['tracks']
        except (FileNotFoundError, KeyError):
            return []
    #Save the updated tracks to tracks.json
    def save_to_json(self, updated_tracks):
        with open('tracks.json', 'w') as file:
            json.dump({'tracks': updated_tracks}, file, indent=2)

    def update(self):
        track_number = self.track_number_entry.get().strip()
        new_rating = self.entry_new_rating.get().strip()

        if not track_number.isdigit() or not new_rating.isdigit():
            self.result_label.config(text="Error: Invalid input. Please enter numbers only.")
            return

        track_index = int(track_number) - 1
        new_rating = int(new_rating)

        if not (1 <= new_rating <= 5):
            self.result_label.config(text="Error: Invalid rating. Please enter a number between 1 and 5.")
            return

        tracks = self.load_tracks_from_json()

        if 0 <= track_index < len(tracks):
            # Update the rating while preserving play count
            tracks[track_index]['rating'] = new_rating
            self.save_to_json(tracks)

            track = tracks[track_index]
            result_message = f"Track: {track['name']}\nNew Rating: {track['rating']}\nPlay Count: {track['plays']}"
            self.result_label.config(text=result_message)
        else:
            self.result_label.config(text=f"Error: Invalid track number. Must be between 1 and {len(tracks)}.")
    
if __name__ == "__main__":
    #main application window
    root = tk.Tk()
    root.title("Track Rating Updater")  #the window title
    root.geometry("300x150") #window size

    #Initialize Frame3 and add to the root window
    app = Frame3(root, None)  #without enter track number input (it's created before)
    app.pack(expand=True, fill='both')  #Add the frame and expand it to fit the window

    #Start the Tkinter main loop
    root.mainloop()