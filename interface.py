import tkinter as tk
import data_processing
import data_analysis
from tkinter import messagebox


class app():
    """ Load the interface and its components """
    def __init__(self):
        self.root = tk.Tk()
        self.load_data_text = tk.StringVar()
        self.loaded_data = {"data": None}

        heading = tk.Label(self.root, text = "DM data processing and visualisation", font = ('calibre', 15, 'bold'))
        heading.grid(row = 0, column = 2)

        load_data_label = tk.Label(self.root, text = "Enter JSON name:")
        load_data_label.grid(row = 1, column = 0)

        load_data_path = tk.Entry(self.root, textvariable = self.load_data_text)
        load_data_path.grid(row = 2, column = 0)

        load_data_button = tk.Button(self.root, text = "Load JSON", command = self.load_data_clicked, width = 15)
        load_data_button.grid(row = 2, column = 1)

        self.root.geometry("800x400")
        self.root.title("DM data processing and visualisation")

        self.root.mainloop()


    def load_data_clicked(self):
        """ Runs when JSON submitted """
        file_path = self.load_data_text.get()

        if not file_path.endswith(".json"):
            file_path += ".json"

        try:
            self.loaded_data["data"] = data_processing.load_json(file_path)
            messagebox.showinfo("Success", "File successfully loaded")

        except FileNotFoundError:
            messagebox.showwarning("Error", "Invalid file name")
        return
    

