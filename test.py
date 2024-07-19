import tkinter as tk
from tkinter import ttk
from tkinter import filedialog
from tkinter import messagebox
from tkcalendar import DateEntry

class App(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Test Date")
        self.geometry("1024x768")

        # Data Entry
        data_entry_frame = tk.Frame(self)
        data_entry_frame.pack(fill=tk.X, padx=10, pady=10)

        tk.Label(data_entry_frame, text="Date:").grid(row=0, column=0)
        self.date_entry = DateEntry(data_entry_frame)
        self.date_entry.grid(row=0, column=1)

        tk.Label(data_entry_frame, text="Time:").grid(row=0, column=2)
        self.time_entry = tk.Entry(data_entry_frame)
        self.time_entry.grid(row=0, column=3)

        tk.Label(data_entry_frame, text="Org:").grid(row=0, column=4)
        self.org_entry = tk.Entry(data_entry_frame)
        self.org_entry.grid(row=0, column=5)

        tk.Label(data_entry_frame, text="Sub Org:").grid(row=1, column=0)
        self.sub_org_entry = tk.Entry(data_entry_frame)
        self.sub_org_entry.grid(row=1, column=1)

        tk.Label(data_entry_frame, text="Name:").grid(row=1, column=2)
        self.name_entry = tk.Entry(data_entry_frame)
        self.name_entry.grid(row=1, column=3)

        tk.Label(data_entry_frame, text="Comds:").grid(row=1, column=4)
        self.comds_entry = tk.Entry(data_entry_frame)
        self.comds_entry.grid(row=1, column=5)

        tk.Label(data_entry_frame, text="Brief/Description:").grid(row=2, column=0)
        self.desc_entry = tk.Entry(data_entry_frame, width=50)
        self.desc_entry.grid(row=2, column=1, columnspan=5)

        tk.Label(data_entry_frame, text="Upload Picture:").grid(row=3, column=0)
        self.upload_button = tk.Button(data_entry_frame, text="Browse", command=self.upload_picture)
        self.upload_button.grid(row=3, column=1)

        tk.Label(data_entry_frame, text="Area:").grid(row=3, column=2)
        self.area_entry = tk.Entry(data_entry_frame)
        self.area_entry.grid(row=3, column=3)

        tk.Label(data_entry_frame, text="Type of Incident:").grid(row=3, column=4)
        self.incident_var = tk.StringVar()
        self.incident_options = ["Fire Raid", "Tgt Killing", "SB Attk", "IED Attk", "Ambush", "Polio Incidents", "Abduction", "Extortion", "Robberies"]
        self.incident_menu = ttk.Combobox(data_entry_frame, textvariable=self.incident_var, values=self.incident_options)
        self.incident_menu.grid(row=3, column=5)

        tk.Label(data_entry_frame, text="Cas:").grid(row=4, column=0)
        self.cas_entry = tk.Entry(data_entry_frame)
        self.cas_entry.grid(row=4, column=1)

        tk.Label(data_entry_frame, text="Ing:").grid(row=4, column=2)
        self.ing_entry = tk.Entry(data_entry_frame)
        self.ing_entry.grid(row=4, column=3)

        tk.Label(data_entry_frame, text="Longitude, Latitude:").grid(row=4, column=4)
        self.long_lat_entry = tk.Entry(data_entry_frame)
        self.long_lat_entry.grid(row=4, column=5)

        self.save_button = tk.Button(data_entry_frame, text="Save Data", command=self.save_data)
        self.save_button.grid(row=5, column=0, columnspan=6)

        # Pictures Match
        pictures_match_frame = tk.LabelFrame(self, text="Pictures Match")
        pictures_match_frame.pack(fill=tk.X, padx=10, pady=10)

        self.pictures_canvas = tk.Canvas(pictures_match_frame, height=200)
        self.pictures_canvas.pack(fill=tk.X)

        # Incidents
        incidents_frame = tk.LabelFrame(self, text="Incidents")
        incidents_frame.pack(fill=tk.X, padx=10, pady=10)

        tk.Label(incidents_frame, text="Incidents:").grid(row=0, column=0)
        self.incidents_entry = tk.Entry(incidents_frame)
        self.incidents_entry.grid(row=0, column=1)

        tk.Label(incidents_frame, text="Search From:").grid(row=1, column=0)
        self.search_from_entry = DateEntry(incidents_frame)
        self.search_from_entry.grid(row=1, column=1)

        tk.Label(incidents_frame, text="Search To:").grid(row=2, column=0)
        self.search_to_entry = DateEntry(incidents_frame)
        self.search_to_entry.grid(row=2, column=1)

        tk.Label(incidents_frame, text="Quantity Of Pictures:").grid(row=3, column=0)
        self.quantity_entry = tk.Entry(incidents_frame)
        self.quantity_entry.grid(row=3, column=1)

        self.search_button = tk.Button(incidents_frame, text="Search", command=self.search)
        self.search_button.grid(row=4, column=0, columnspan=2)

        # Activity Logs
        activity_logs_frame = tk.LabelFrame(self, text="Activity Logs")
        activity_logs_frame.pack(fill=tk.X, padx=10, pady=10)

        columns = ("S#", "Date", "Time", "Org", "Sub Org", "Name", "Comds", "Watch List", "Brief/Description", "Picture", "Area", "Type of Incident", "Cas", "Longitude, Latitude", "Google Earth")
        self.activity_tree = ttk.Treeview(activity_logs_frame, columns=columns, show='headings')
        for col in columns:
            self.activity_tree.heading(col, text=col)
            self.activity_tree.column(col, minwidth=0, width=80)
        self.activity_tree.pack(fill=tk.X)

    def upload_picture(self):
        file_path = filedialog.askopenfilename()
        if file_path:
            messagebox.showinfo("Selected File", file_path)

    def save_data(self):
        messagebox.showinfo("Save Data", "Data has been saved!")

    def search(self):
        messagebox.showinfo("Search", "Search initiated!")

if __name__ == "__main__":
    app = App()
    app.mainloop()
