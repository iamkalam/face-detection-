import tkinter as tk
from tkinter import filedialog, ttk
from tkcalendar import DateEntry

# Functions for the application logic
def upload_image():
    file_path = filedialog.askopenfilename()
    if file_path:
        file_label.config(text=file_path)

def search_text():
    search_query = search_entry.get()
    selected_date_from = date_from_entry.get_date()
    selected_date_to = date_to_entry.get_date()
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
    print("Exploring Google Earth...")

def save_data():
    print("Saving data...")

# Function to verify login credentials
def login():
    username = username_entry.get()
    password = password_entry.get()
    if username == "admin" and password == "password":
        root.destroy()  # Close login window
        open_data_entry_page()
    else:
        error_label.config(text="Invalid username or password")

# Function to open the data entry page
def open_data_entry_page():
    data_entry_page = tk.Toplevel()
    data_entry_page.title("Data Entry")
    data_entry_page.geometry("800x600")

    # Create a Canvas widget and a vertical scrollbar
    canvas = tk.Canvas(data_entry_page)
    scrollbar = tk.Scrollbar(data_entry_page, orient="vertical", command=canvas.yview)
    canvas.configure(yscrollcommand=scrollbar.set)

    # Create a frame inside the canvas
    data_frame = tk.Frame(canvas)
    canvas.create_window((0, 0), window=data_frame, anchor="nw")

    # Configure scrolling region
    data_frame.bind("<Configure>", lambda event: canvas.configure(scrollregion=canvas.bbox("all")))

    # Pack the canvas and scrollbar
    canvas.pack(side="left", fill="both", expand=True)
    scrollbar.pack(side="right", fill="y")

    global file_label, search_entry, picture_label  # Declare as global to use in respective functions

    # Create and place the Upload Image button and file label
    upload_button = tk.Button(data_frame, text="Upload Image", command=upload_image)
    upload_button.grid(row=0, column=0, padx=5, pady=5)

    file_label = tk.Label(data_frame, text="No file selected")
    file_label.grid(row=0, column=1, padx=5, pady=5)

    # Create and place the Search by Text label, entry field, and Search button
    search_label = tk.Label(data_frame, text="Search by Text")
    search_label.grid(row=0, column=2, padx=5, pady=5)

    search_entry = tk.Entry(data_frame)
    search_entry.grid(row=0, column=3, padx=5, pady=5)

    search_button = tk.Button(data_frame, text="Search", command=search_text)
    search_button.grid(row=0, column=4, padx=5, pady=5)

    # Create a frame for the Data Entry section
    data_entry_frame1 = tk.Frame(data_frame, bd=1, relief="solid")
    data_entry_frame1.grid(row=1, column=0, padx=20, pady=20, sticky="w", columnspan=5)

    # Data Entry heading part 1
    data_entry_heading1 = tk.Label(data_entry_frame1, text="Data Entry Part 1", font=("Arial", 10))
    data_entry_heading1.grid(row=0, column=0, columnspan=8, pady=10)

    # Create and place labels and entry fields for Data Entry Part 1
    fields1 = ["Date", "Time", "Org", "Sub Org", "Name", "Cmds", "Brief/Description"]
    entries1 = {}

    for idx, field in enumerate(fields1):
        label = tk.Label(data_entry_frame1, text=field, font=("Arial", 10))
        label.grid(row=1, column=idx, sticky="w", padx=5, pady=5)

        entry = tk.Entry(data_entry_frame1, font=("Arial", 8), width=12)
        entries1[field] = entry
        entry.grid(row=2, column=idx, padx=3, pady=3, sticky="w")

    # Data Entry heading part 2
    data_entry_frame2 = tk.Frame(data_frame, bd=1, relief="solid")
    data_entry_frame2.grid(row=2, column=0, padx=20, pady=20, sticky="w", columnspan=5)

    data_entry_heading2 = tk.Label(data_entry_frame2, text="Data Entry Part 2", font=("Arial", 10))
    data_entry_heading2.grid(row=0, column=0, columnspan=8, pady=10)

    # Create and place labels and entry fields for Data Entry Part 2
    fields2 = ["Upload Picture", "Area", "Type of Incident", "Cas", "Lng", "Latitude"]
    entries2 = {}

    for idx, field in enumerate(fields2):
        label = tk.Label(data_entry_frame2, text=field, font=("Arial", 10))
        label.grid(row=1, column=idx, sticky="w", padx=5, pady=5)

        if field == "Type of Incident":
            incident_var = tk.StringVar()
            incident_combobox = ttk.Combobox(data_entry_frame2, textvariable=incident_var, values=["Fire Raid", "Tat Killing", "SB Attk", "IDE Attk", "Ambush", "Polio Incidents", "Abduction", "Extortion", "Robberies"], font=("Arial", 10), width=15)
            incident_combobox.grid(row=2, column=idx, padx=5, pady=5, sticky="w")
            incident_combobox.current(0)  # Set default selection
            entries2[field] = incident_var
        else:
            if field == "Upload Picture":
                entry = tk.Button(data_entry_frame2, text="Upload Picture", command=upload_picture, font=("Arial", 8))
                picture_label = tk.Label(data_entry_frame2, text="No picture selected", font=("Arial", 8))
                entries2[field] = picture_label
            else:
                entry = tk.Entry(data_entry_frame2, font=("Arial", 8), width=12)
                entries2[field] = entry
            entry.grid(row=2, column=idx, padx=3, pady=3, sticky="w")
            if field == "Upload Picture":
                picture_label.grid(row=2, column=idx + 1, padx=3, pady=3)

    # Pictures Frame
    pictures_frame = tk.Frame(data_frame, bd=2, relief="solid", width=30, height=40)
    pictures_frame.grid(row=3, column=0, padx=50, pady=25, sticky="n", columnspan=5)

    tk.Label(pictures_frame, text="Pictures Match").pack(pady=10)
    for i in range(3):
        row_frame = tk.Frame(pictures_frame)
        row_frame.pack()
        for j in range(5):
            picture = tk.Label(row_frame, text="Picture", relief="solid", width=10, height=6)
            picture.pack(side="left", padx=5, pady=5)

    # Next Button
    next_button = tk.Button(data_frame, text="Next", command=lambda: open_main_app(data_entry_page))
    next_button.grid(row=4, column=0, columnspan=5, pady=10)

def open_main_app(previous_page):
    previous_page.destroy()  # Close the previous page
    
    main_app_page = tk.Toplevel()
    main_app_page.title("Main Application")
    main_app_page.geometry("1200x800")

    # Create a Canvas widget and a vertical scrollbar
    canvas = tk.Canvas(main_app_page)
    scrollbar = tk.Scrollbar(main_app_page, orient="vertical", command=canvas.yview)
    canvas.configure(yscrollcommand=scrollbar.set)

    # Create a frame inside the canvas
    main_frame = tk.Frame(canvas)
    canvas.create_window((0, 0), window=main_frame, anchor="nw")

    # Configure scrolling region
    main_frame.bind("<Configure>", lambda event: canvas.configure(scrollregion=canvas.bbox("all")))

    # Pack the canvas and scrollbar
    canvas.pack(side="left", fill="both", expand=True)
    scrollbar.pack(side="right", fill="y")

    # Incident Frame
    incident_frame = tk.Frame(main_frame, bd=1, relief="solid")
    incident_frame.grid(row=0, column=0, columnspan=8, padx=20, pady=20, sticky="w")

    incident_heading = tk.Label(incident_frame, text="Incident", font=("Arial", 12, "bold"))
    incident_heading.pack(pady=10)

    search_date_frame = tk.Frame(incident_frame)
    search_date_frame.pack(pady=10, padx=20, anchor="w")

    search_entry_incident = tk.Entry(search_date_frame, width=30, font=("Arial", 10))
    search_entry_incident.grid(row=0, column=0, padx=5, pady=5)

    search_button_incident = tk.Button(search_date_frame, text="Search", command=search_text, font=("Arial", 10))
    search_button_incident.grid(row=0, column=1, padx=5, pady=5)

    tk.Label(incident_frame, text="Incidents").pack(pady=10)
    incident_combobox = ttk.Combobox(incident_frame, values=["ABCD"], width=20)
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

    # Activity Logs Frame
    activity_logs_frame = tk.Frame(main_frame, bd=1, relief="solid")
    activity_logs_frame.grid(row=1, column=0, columnspan=8, padx=20, pady=20, sticky="w")

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
    developed_by_label.grid(row=2, column=0, padx=20, pady=10, sticky="w")

    # Back Button
    back_button = tk.Button(main_app_page, text="Back", command=lambda: go_back(main_app_page, open_data_entry_page))
    back_button.pack(pady=10)

def go_back(current_page, open_previous_page):
    current_page.destroy()
    open_previous_page()

# Login Window
root = tk.Tk()
root.title("Login")
root.geometry("300x150")

tk.Label(root, text="Username:").grid(row=0, column=0, padx=10, pady=10)
username_entry = tk.Entry(root)
username_entry.grid(row=0, column=1, padx=10, pady=10)

tk.Label(root, text="Password:").grid(row=1, column=0, padx=10, pady=10)
password_entry = tk.Entry(root, show="*")
password_entry.grid(row=1, column=1, padx=10, pady=10)

login_button = tk.Button(root, text="Login", command=login)
login_button.grid(row=2, column=0, columnspan=2, pady=10)

error_label = tk.Label(root, text="", fg="red")
error_label.grid(row=3, column=0, columnspan=2)

root.mainloop()
