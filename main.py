import tkinter as tk
from view_tracks import Frame1
from create_track_list import Frame2
from update_track_list import Frame3
from track_library import find_tracks_by_artist, find_tracks_by_name  #Import the functions

class App:
    def __init__(self, root):
        self.root = root
        self.root.title("Gia Dat JukeBox")

        #search text area(Artists or Tracks)
        self.search_entry = tk.Entry(root, width=40)
        self.search_entry.grid(row=0, column=1, padx=10, pady=10)

        #Create search button (Artists or Tracks)
        self.search_button = tk.Button(root, text="Search", command=self.search_tracks)
        self.search_button.grid(row=0, column=1,columnspan=2, padx=10, pady=10)

        #Create a label to display search results
        self.result_label = tk.Label(root, text="Results will be shown here.", anchor="w", justify="left", width=50)
        self.result_label.grid(row=1, column=1,columnspan=2, padx=10, pady=10)

        #Enter track number 
        enter_lbl = tk.Label(root, text="Enter Track Number")
        enter_lbl.grid(row=2, column=0, padx=5, pady=5)
        
        #Input Enter track number
        self.track_number_entry = tk.Entry(root, width=20)
        self.track_number_entry.grid(row=2, column=0,columnspan=2, padx=5, pady=5)

        #Initialize frames
        self.frame1 = Frame1(root, self.track_number_entry)
        self.frame2 = Frame2(root, self.track_number_entry)
        self.frame3 = Frame3(root, self.track_number_entry)

        self.frame1.grid(row=3, column=0, padx=10, pady=10)
        self.frame2.grid(row=3, column=1, padx=10, pady=10)
        self.frame3.grid(row=3, column=2, padx=10, pady=10)

    def search_tracks(self):
        search_query = self.search_entry.get()
        if search_query:
            #Search by artist 
            tracks_by_artist = find_tracks_by_artist(search_query)
            if tracks_by_artist:
                result_text = "Tracks by artist '" + search_query + "':\n"
                for track in tracks_by_artist:
                    result_text += f"- {track.info()}\n"
            else:
                #Search by track
                tracks_by_name = find_tracks_by_name(search_query)
                if tracks_by_name:
                    result_text = "Tracks named '" + search_query + "':\n"
                    for track in tracks_by_name:
                        result_text += f"- {track.info()}\n"
                else:
                    result_text = f"No tracks found for '{search_query}'."
            self.result_label.config(text=result_text)
        else:
            self.result_label.config(text="Please enter an artist or track name.")

#Create main window
if __name__ == "__main__":
    window =tk.Tk()
    App(window)
    window.mainloop()
