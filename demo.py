import tkinter as tk
from tkinter import filedialog
from tkinter import ttk  # Import ttk for themed widgets
from tkcalendar import DateEntry  # Import DateEntry widget from tkcalendar

def upload_image():
    file_path = filedialog.askopenfilename()
    if file_path:
        file_label.config(text=file_path)

def search_text():
    search_query = search_entry_incident.get()
    selected_date_from = date_from_entry.get_date()
    selected_date_to = date_to_entry.get_date()
    # Perform search operation with search_query, selected_date_from, and selected_date_to
    print(f"Searching for: {search_query} from {selected_date_from} to {selected_date_to}")

def upload_picture():
    picture_path = filedialog.askopenfilename()
    if picture_path:
        picture_label.config(text=picture_path)

def upload_kmz():
    kmz_path = filedialog.askopenfilename(filetypes=[("KMZ files", "*.kmz")])
    if kmz_path:
        kmz_label.config(text=kmz_path)

def explore_google_earth():
    # Replace with your logic to open Google Earth or perform related action
    print("Exploring Google Earth...")

def save_data():
    # Replace with your logic to save the data from the entry fields
    print("Saving data...")

def configure_scroll_region(event):
    canvas.configure(scrollregion=canvas.bbox("all"))

# Create the main window
root = tk.Tk()
root.title("Test Date")
root.geometry("1200x1200")

# Create a Canvas widget and a vertical scrollbar
canvas = tk.Canvas(root)
scrollbar = tk.Scrollbar(root, orient="vertical", command=canvas.yview)
canvas.configure(yscrollcommand=scrollbar.set)

# Create a frame inside the canvas
main_frame = tk.Frame(canvas)
canvas.create_window((0, 0), window=main_frame, anchor="nw")

# Configure scrolling region
main_frame.bind("<Configure>", configure_scroll_region)

# Pack the canvas and scrollbar
canvas.pack(side="left", fill="both", expand=True)
scrollbar.pack(side="right", fill="y")

# Create a frame to center the elements
center_frame = tk.Frame(main_frame, bd=1, relief="solid")
center_frame.grid(row=0, column=0, padx=20, pady=20)

# Create and place the Upload Image button and file label
upload_button = tk.Button(center_frame, text="Upload Image", command=upload_image)
upload_button.grid(row=0, column=0, padx=5, pady=5)

file_label = tk.Label(center_frame, text="No file selected")
file_label.grid(row=0, column=1, padx=5, pady=5)

# Create and place the Search by Text label, entry field, and Search button
search_label = tk.Label(center_frame, text="Search by Text")
search_label.grid(row=0, column=2, padx=5, pady=5)

search_entry = tk.Entry(center_frame)
search_entry.grid(row=0, column=3, padx=5, pady=5)

search_button = tk.Button(center_frame, text="Search", command=search_text)
search_button.grid(row=0, column=4, padx=5, pady=5)

# Create a frame for the Data Entry section
data_entry_frame = tk.Frame(main_frame, bd=1, relief="solid")
data_entry_frame.grid(row=1, column=0, padx=20, pady=20, sticky="w")

# Data Entry heading
data_entry_heading = tk.Label(data_entry_frame, text="Data Entry", font=("Arial", 10))
data_entry_heading.grid(row=0, column=0, columnspan=8, pady=10)

# Create and place labels and entry fields for Data Entry
fields = ["Date", "Time", "Org", "Sub Org", "Name", "Cmds", "Brief/Description", "Upload Picture", "Area", "Type of Incident", "Cas", "Lng", "Latitude"]
entries = {}

for idx, field in enumerate(fields):
    label = tk.Label(data_entry_frame, text=field, font=("Arial", 10))
    label.grid(row=1, column=idx, sticky="w", padx=5, pady=5)

    if field == "Type of Incident":
        # Create a Combobox for Type of Incident
        incident_var = tk.StringVar()
        incident_combobox = ttk.Combobox(data_entry_frame, textvariable=incident_var, values=["Fire Raid", "Tat Killing", "SB Attk", "IDE Attk", "Ambush", "Polio Incidents", "Abduction", "Extortion", "Robberies"], font=("Arial", 10), width=15)
        incident_combobox.grid(row=2, column=idx, padx=5, pady=5, sticky="w")
        incident_combobox.current(0)  # Set default selection
        entries[field] = incident_var
    else:
        if field == "Upload Picture":
            entry = tk.Button(data_entry_frame, text="Upload Picture", command=upload_picture, font=("Arial", 8))
            picture_label = tk.Label(data_entry_frame, text="No picture selected", font=("Arial", 8))
            entries[field] = picture_label
        elif field == "Area":
            entry = tk.Entry(data_entry_frame, font=("Arial", 8), width=12)
            entries[field] = entry
            # Adjust padding to move the Area field to the right
            label.grid_configure(padx=(0, 20))  # Add right padding to the label
            entry.grid_configure(padx=(0, 20))  # Add right padding to the entry widget
        else:
            entry = tk.Entry(data_entry_frame, font=("Arial", 8), width=12)
            entries[field] = entry
        entry.grid(row=2, column=idx, padx=3, pady=3, sticky="w")
        if field == "Upload Picture":
            picture_label.grid(row=2, column=idx + 1, padx=3, pady=3)

# Create a frame for the Google Earth and buttons
buttons_frame = tk.Frame(main_frame)
buttons_frame.grid(row=2, column=0, columnspan=8, pady=10, padx=20, sticky="w")  # Anchor to the west (left)

# Create and place the Explore Google Earth button
google_earth_button = tk.Button(buttons_frame, text="Explore Google Earth", command=explore_google_earth, font=("Arial", 10), relief="solid", padx=10, pady=5)
google_earth_button.pack(side="left", padx=5)

# Create and place the Upload KMZ button and label
upload_kmz_button = tk.Button(buttons_frame, text="Upload KMZ", command=upload_kmz, font=("Arial", 10))
upload_kmz_button.pack(side="left", padx=5)

kmz_label = tk.Label(buttons_frame, text="No KMZ file selected", font=("Arial", 10))
kmz_label.pack(side="left", padx=5)

# Create and place the LowDown button
lowdown_button = tk.Button(buttons_frame, text="LowDown", font=("Arial", 10), relief="solid", padx=10, pady=5)
lowdown_button.pack(side="left", padx=5)

# Create and place the Save Data button
save_button = tk.Button(buttons_frame, text="Save\nData", command=save_data, font=("Arial", 10), relief="solid", padx=15, pady=10)
save_button.pack(side="left", padx=5)

# Frame for incidents
incident_frame = tk.Frame(main_frame, bd=1, relief="solid")
incident_frame.grid(row=3, column=0, columnspan=8, padx=20, pady=20, sticky="w")

incident_heading = tk.Label(incident_frame, text="Incident", font=("Arial", 12, "bold"))
incident_heading.pack(pady=10)

# Frame for search and date selection
search_date_frame = tk.Frame(incident_frame)
search_date_frame.pack(pady=10, padx=20, anchor="w")

# Search by text field and Search button
search_entry_incident = tk.Entry(search_date_frame, width=30, font=("Arial", 10))
search_entry_incident.grid(row=0, column=0, padx=5, pady=5)

search_button_incident = tk.Button(search_date_frame, text="Search", command=search_text, font=("Arial", 10))
search_button_incident.grid(row=0, column=1, padx=5, pady=5)

# Incident Frame
tk.Label(incident_frame, text="Incidents").pack(pady=10)
incident_combobox = ttk.Combobox(incident_frame, values=["ABCD"] ,width=20)
incident_combobox.pack(pady=5)

date_from_label = tk.Label(incident_frame, text="Search From")
date_from_label.pack(pady=5)
date_from_entry = DateEntry(incident_frame, width=15)
date_from_entry.pack(pady=5)

date_to_label = tk.Label(incident_frame, text="Search To")
date_to_label.pack(pady=5)
date_to_entry = DateEntry(incident_frame, width=15)
date_to_entry.pack(pady=5)

quantity_label = tk.Label(incident_frame, text="Quantity of Pictures")
quantity_label.pack(pady=5)
quantity_entry = tk.Entry(incident_frame, width=18)
quantity_entry.pack(pady=5)

# Pictures Frame
pictures_frame = tk.Frame(main_frame, bd=2, relief="solid", width=30, height=40)
pictures_frame.grid(row=3, column=0, padx=50, pady=25, sticky="n")  # Place in column 1

tk.Label(pictures_frame, text="Pictures Match").pack(pady=10)
for i in range(3):
    row_frame = tk.Frame(pictures_frame)
    row_frame.pack()
    for j in range(5):
        picture = tk.Label(row_frame, text="Picture", relief="solid", width=10, height=6)
        picture.pack(side="left", padx=5, pady=5)

# Activity Logs
activity_logs_frame = tk.Frame(main_frame, bd=1, relief="solid")
activity_logs_frame.grid(row=4, column=0, columnspan=8, padx=20, pady=20, sticky="w")

activity_logs_heading = tk.Label(activity_logs_frame, text="Activity Logs", font=("Arial", 10))
activity_logs_heading.grid(row=0, column=0, columnspan=8, pady=10)

columns = ["S#", "Date", "Time", "Org", "Sub Org", "Name", "Cmds", "Brief/Description", "Picture", "Area", "Type of Incident", "Cas", "Longitude", "Latitude", "Google Earth"]

for idx, column in enumerate(columns):
    label = tk.Label(activity_logs_frame, text=column, font=("Arial", 8))
    label.grid(row=1, column=idx, padx=5, pady=5, sticky="w")

for i in range(5):  # Sample rows
    for j, column in enumerate(columns):
        entry = tk.Entry(activity_logs_frame, font=("Arial", 8), width=12)
        entry.grid(row=i+2, column=j, padx=5, pady=5, sticky="w")

# Developed by
developed_by_label = tk.Label(main_frame, text="kalamay codes", font=("Arial", 10))
developed_by_label.grid(row=5, column=0, padx=20, pady=10, sticky="w")

root.mainloop()
