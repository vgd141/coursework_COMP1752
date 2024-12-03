import tkinter as tk
import tkinter.scrolledtext as tkst
import track_library as lib
import json

def set_text(text_area, content):       #inserts content into the text_area 
    text_area.delete("1.0", tk.END)     #first the existing content is deleted
    text_area.insert(tk.END, content)   #then the new content is inserted

class Frame1(tk.Frame):
    def __init__(self, parent, track_number_entry):
        super().__init__(parent)
        self.track_number_entry = track_number_entry

        #list All Tracks Button
        list_tracks_btn = tk.Button(self, text="List All Tracks", command=self.list_tracks_clicked)
        list_tracks_btn.grid(row=0, column=0, padx=10, pady=10)

        #view Track Button
        check_track_btn = tk.Button(self, text="View Track", command=self.view_tracks_clicked)
        check_track_btn.grid(row=0, column=3, padx=10, pady=10)

        #text area show list tracks
        self.list_txt = tkst.ScrolledText(self, width=48, height=12, wrap="none")
        self.list_txt.grid(row=1, column=0, columnspan=3, sticky="W", padx=10, pady=10)

        #text area show information of tracks 
        self.track_txt = tk.Text(self, width=24, height=4, wrap="none")
        self.track_txt.grid(row=1, column=3, sticky="NW", padx=10, pady=10)

        #Status Label
        self.status_lbl = tk.Label(self, text="", font=("Helvetica", 10))
        self.status_lbl.grid(row=2, column=0, columnspan=4, sticky="W", padx=10, pady=10)

        #auto show all list tracks when start
        #self.list_tracks_clicked()

    #function reload list after update rating
    def view_tracks_clicked(self):
        key = self.track_number_entry.get().strip().zfill(2)  
        name = lib.get_name(key)
        if name is not None:
            artist = lib.get_artist(key)
            rating = lib.get_rating(key)
            play_count = lib.get_play_count(key)
            track_details = f"{name}\n{artist}\nrating: {rating}\nplays: {play_count}"
            set_text(self.track_txt, track_details)
            self.status_lbl.configure(text="Track details displayed")
        else:
            set_text(self.track_txt, f"Track {key} not found")
            self.status_lbl.configure(text="Track not found")

    def list_tracks_clicked(self):
        try:
            #open json file and read data
            with open('tracks.json', 'r') as file:
                data = json.load(file)
                tracks = data['tracks']
                track_list = ""
                #load all list when clicked button view all
                for i, track in enumerate(tracks, 1):
                    track_list += f"{str(i).zfill(2)} {track['name']} {'*' * track['rating']}\n"
                set_text(self.list_txt, track_list)
                self.status_lbl.configure(text="Track list loaded")
        except FileNotFoundError:
            track_list = lib.list_all()
            set_text(self.list_txt, track_list)
            self.status_lbl.configure(text="Track list loaded from library!")


if __name__ == "__main__":
    window = tk.Tk()
    window.title("Track Viewer")

    #Track number input field
    track_number_entry = tk.Entry(window, width=5)
    track_number_entry.grid(row=0, column=1, padx=10, pady=10)
    tk.Label(window, text="Enter Track Number:").grid(row=0, column=0,columnspan=2, padx=10, pady=10)

    #Initialize Frame1
    frame = Frame1(window, track_number_entry)
    frame.grid(row=1, column=0, columnspan=4, padx=10, pady=10)

    window.mainloop()