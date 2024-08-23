import tkinter as tk
from tkinter import messagebox
from tkinter import ttk

# Dummy credentials for the login check
CORRECT_USERNAME = "admin"
CORRECT_PASSWORD = "password"

class LoginApp(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Login Application")
        self.geometry("683x600")  # Width x Height in pixels
        self.configure(bg="lightgray")

        # Initialize the frames
        self.login_frame = None
        self.dashboard_frame = None
        self.search_page = None
        
        # Show the login page initially
        self.show_login_page()

    def show_login_page(self):
        """Displays the login page."""
        if self.dashboard_frame:
            self.dashboard_frame.pack_forget()  # Hide the dashboard frame if it's visible

        self.login_frame = tk.Frame(self, bg="lightgray")
        self.login_frame.pack(expand=True)

        # Logo/Header
        header_label = tk.Label(
            self.login_frame, text="Logo comes here", font=("Arial", 32), bg="lightgray"
        )
        header_label.pack(pady=20)

        # Login Section
        login_section = tk.Frame(self.login_frame, bg="lightblue")
        login_section.pack(pady=20, padx=20)

        login_label = tk.Label(
            login_section, text="Login", font=("Arial", 32), bg="lightblue"
        )
        login_label.pack(pady=(40, 20))

        # Username
        self.username_entry = tk.Entry(login_section, font=("Arial", 18), bg="lightgray")
        self.username_entry.pack(pady=(20, 10), padx=20, fill=tk.X)

        # Password
        self.password_entry = tk.Entry(login_section, font=("Arial", 18), show="*", bg="lightgray")
        self.password_entry.pack(pady=(10, 20), padx=20, fill=tk.X)

        # Login Button
        login_button = tk.Button(
            login_section, text="Log in", font=("Arial", 18), command=self.on_submit, bg="lightgray"
        )
        login_button.pack(pady=(20, 20))

    def show_dashboard(self):
        """Displays the dashboard page after successful login."""
        self.login_frame.pack_forget()  # Hide the login frame

        self.dashboard_frame = tk.Frame(self, bg="lightgray")
        self.dashboard_frame.pack(expand=True, fill=tk.BOTH)

        # Header
        header_frame = tk.Frame(self.dashboard_frame, bg="lightgray")
        header_frame.pack(pady=(0, 20), padx=20)

        logo_label = tk.Label(
            header_frame, text="Logo comes here", font=("Arial", 32), bg="lightgray"
        )
        logo_label.pack(pady=20)

        # Navigation
        nav_frame = tk.Frame(header_frame, bg="lightgray")
        nav_frame.pack()

        # Search Button
        search_button = tk.Button(
            nav_frame,
            text="Search",
            font=("Arial", 18),
            command=self.on_search,
            bg="lightgray",
            relief=tk.RAISED,
            padx=16,
            pady=8,
            width=20,
        )
        search_button.pack(pady=(80, 7), fill=tk.X)

        # Upload Button
        upload_button = tk.Button(
            nav_frame,
            text="Upload",
            font=("Arial", 18),
            command=self.on_upload,
            bg="lightgray",
            relief=tk.RAISED,
            padx=16,
            pady=8,
            width=20,
        )
        upload_button.pack(pady=7, fill=tk.X)

        # Exit Button
        exit_button = tk.Button(
            nav_frame,
            text="Exit",
            font=("Arial", 18),
            command=self.on_exit,
            bg="lightgray",
            relief=tk.RAISED,
            padx=16,
            pady=8,
            width=20,
        )
        exit_button.pack(pady=7, fill=tk.X)

    def show_search_page(self):
        """Displays the search page."""
        if self.search_page:
            self.search_page.destroy()  # Destroy the previous search page instance if it exists

        self.search_page = SearchPage(self)
        self.search_page.mainloop()  # Start the SearchPage main loop

    def on_submit(self):
        username = self.username_entry.get()
        password = self.password_entry.get()
        
        # Check credentials
        if username == CORRECT_USERNAME and password == CORRECT_PASSWORD:
            self.show_dashboard()
        else:
            messagebox.showerror("Login Failed", "Invalid username or password")

    def on_search(self):
        # Show the search page when the search button is clicked
        self.show_search_page()

    def on_upload(self):
        # Logic for upload action
        print("Upload button clicked")

    def on_exit(self):
        # Logic for exit action
        print("Exit button clicked")
        self.quit()

class SearchPage(tk.Tk):
    def __init__(self, parent):
        super().__init__()

        self.parent = parent  # Reference to the parent (LoginApp) to switch back
        self.title("Search Page")
        self.geometry("1024x768")
        self.configure(bg="lightgray")

        self.create_header()
        self.create_content()

    def create_header(self):
        """Create the header with the search tab and main menu."""
        header_frame = tk.Frame(self, bg="lightgray", pady=10)
        header_frame.pack(fill=tk.X)

        # Search Page Title
        title_label = tk.Label(header_frame, text="Search Page", font=("Arial", 24), bg="lightgray")
        title_label.pack()

        # Search Tab
        self.create_search_tab(header_frame)

        # Main Menu
        self.create_main_menu(header_frame)

    def create_search_tab(self, parent):
        """Create the search tab."""
        search_tab_frame = tk.Frame(parent, bg="#E7E5E4", padx=10, pady=10)
        search_tab_frame.pack(fill=tk.X, pady=10)

        upload_button = tk.Button(search_tab_frame, text="Upload Picture", font=("Arial", 14), bg="#F5F5F4")
        upload_button.pack(side=tk.LEFT, padx=5)

        search_button1 = tk.Button(search_tab_frame, text="Search", font=("Arial", 14), bg="#F5F5F4")
        search_button1.pack(side=tk.LEFT, padx=5)

        search_entry = tk.Entry(search_tab_frame, font=("Arial", 14), bg="#F5F5F4")
        search_entry.pack(side=tk.LEFT, padx=5, fill=tk.X, expand=True)

        search_button2 = tk.Button(search_tab_frame, text="Search", font=("Arial", 14), bg="#F5F5F4")
        search_button2.pack(side=tk.LEFT, padx=5)

    def create_main_menu(self, parent):
        """Create the main menu button."""
        main_menu_frame = tk.Frame(parent, bg="lightgray")
        main_menu_frame.pack(side=tk.RIGHT)

        main_menu_button = tk.Button(main_menu_frame, text="Main Menu", font=("Arial", 14), bg="#F5F5F4", command=self.on_main_menu)
        main_menu_button.pack(padx=5)

    def create_content(self):
        """Create the main content area with different search options and results."""
        content_frame = tk.Frame(self, bg="lightgray")
        content_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

        # Left Sidebar
        left_sidebar_frame = tk.Frame(content_frame, bg="lightgray", width=200)
        left_sidebar_frame.pack(side=tk.LEFT, fill=tk.Y, padx=(0, 10))

        self.create_date_search(left_sidebar_frame)
        self.create_case_id_search(left_sidebar_frame)
        self.create_quantity_matched(left_sidebar_frame)

        # Activity Logs (now positioned below the Quantity of Pictures Matched)
        self.create_activity_logs(left_sidebar_frame)

        # Center Content
        center_frame = tk.Frame(content_frame, bg="lightgray", width=600)
        center_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=(0, 10))

        # Photo Preview
        self.create_photo_preview(center_frame)

        # Right Sidebar
        right_sidebar_frame = tk.Frame(content_frame, bg="lightgray", width=200)
        right_sidebar_frame.pack(side=tk.RIGHT, fill=tk.Y)

        self.create_incident_list(right_sidebar_frame)

    def create_date_search(self, parent):
        """Create the date search section."""
        date_search_frame = tk.LabelFrame(parent, text="Search Incidents by Date", font=("Arial", 14), bg="#E7E5E4", padx=10, pady=10)
        date_search_frame.pack(fill=tk.X, pady=10)

        from_label = tk.Label(date_search_frame, text="Search from", font=("Arial", 12), bg="#E7E5E4")
        from_label.grid(row=0, column=0, padx=5, pady=5)

        from_date = tk.Entry(date_search_frame, font=("Arial", 12), bg="#F5F5F4")
        from_date.grid(row=0, column=1, padx=5, pady=5)

        to_label = tk.Label(date_search_frame, text="Search to", font=("Arial", 12), bg="#E7E5E4")
        to_label.grid(row=1, column=0, padx=5, pady=5)

        to_date = tk.Entry(date_search_frame, font=("Arial", 12), bg="#F5F5F4")
        to_date.grid(row=1, column=1, padx=5, pady=5)

        options = ttk.Combobox(date_search_frame, values=["Incident Options"], font=("Arial", 12), background="#F5F5F4")
        options.grid(row=2, column=0, columnspan=2, padx=5, pady=10, sticky="ew")

        search_button = tk.Button(date_search_frame, text="Search", font=("Arial", 12), bg="#F5F5F4")
        search_button.grid(row=3, column=0, columnspan=2, padx=5, pady=10)

    def create_case_id_search(self, parent):
        """Create the case ID search section."""
        case_id_search_frame = tk.LabelFrame(parent, text="Search by Case ID #", font=("Arial", 14), bg="#E7E5E4", padx=10, pady=10)
        case_id_search_frame.pack(fill=tk.X, pady=10)

        case_id_label = tk.Label(case_id_search_frame, text="Case ID# :", font=("Arial", 12), bg="#E7E5E4")
        case_id_label.grid(row=0, column=0, padx=5, pady=5)

        case_id_entry = tk.Entry(case_id_search_frame, font=("Arial", 12), bg="#F5F5F4")
        case_id_entry.grid(row=0, column=1, padx=5, pady=5)

        search_button = tk.Button(case_id_search_frame, text="Search", font=("Arial", 12), bg="#F5F5F4")
        search_button.grid(row=1, column=0, columnspan=2, padx=5, pady=10, sticky="e")

    def create_quantity_matched(self, parent):
        """Create the quantity matched section."""
        quantity_matched_frame = tk.LabelFrame(parent, text="Quantity of Pictures Matched", font=("Arial", 14), bg="#E7E5E4", padx=10, pady=10)
        quantity_matched_frame.pack(fill=tk.X, pady=10)

        quantity_entry = tk.Entry(quantity_matched_frame, font=("Arial", 12), bg="#F5F5F4")
        quantity_entry.pack(fill=tk.X, padx=5, pady=5)

    def create_activity_logs(self, parent):
        """Create the activity logs section as a horizontal bar below the Quantity of Pictures Matched."""
        activity_logs_frame = tk.LabelFrame(parent, text="Activity Logs", font=("Arial", 14), bg="#E7E5E4", padx=10, pady=5)
        activity_logs_frame.pack(fill=tk.X, pady=10)

        logs_canvas = tk.Canvas(activity_logs_frame, bg="#F5F5F4", height=60)
        logs_canvas.pack(side=tk.LEFT, fill=tk.X, expand=True)

        logs_scrollbar = tk.Scrollbar(activity_logs_frame, orient=tk.HORIZONTAL, command=logs_canvas.xview)
        logs_scrollbar.pack(side=tk.BOTTOM, fill=tk.X)

        logs_canvas.configure(xscrollcommand=logs_scrollbar.set)

        # Create a frame to contain the logs on the canvas
        logs_content_frame = tk.Frame(logs_canvas, bg="#F5F5F4")
        logs_canvas.create_window((0, 0), window=logs_content_frame, anchor="nw")

        # Add example log entries
        for i in range(20):
            log_entry = tk.Label(logs_content_frame, text=f"Log {i+1}", bg="#F5F5F4", padx=10)
            log_entry.pack(side=tk.LEFT, padx=2)

        # Update the scroll region
        logs_content_frame.update_idletasks()
        logs_canvas.config(scrollregion=logs_canvas.bbox("all"))

    def create_photo_preview(self, parent):
        """Create the photo preview section with 15 photo placeholders."""
        photo_preview_frame = tk.Frame(parent, bg="lightgrey", height=500)
        photo_preview_frame.pack(fill=tk.BOTH, expand=True, pady=(0, 10))

        for i in range(15):
            photo_label = tk.Label(photo_preview_frame, text=f"Photo {i+1}", font=("Arial", 10), bg="#D9D9D9", width=15, height=6)
            photo_label.grid(row=i//5, column=i%5, padx=5, pady=5)

    def create_incident_list(self, parent):
        """Create the incident list section."""
        incident_list_frame = tk.LabelFrame(parent, text="Incident List", font=("Arial", 14), bg="#E7E5E4", padx=10, pady=10)
        incident_list_frame.pack(fill=tk.Y, pady=10)

        # Incident list items
        incidents = ["Fire Raid", "Tgt Killing", "SB Attack", "IED Attack", "Ambush", 
                     "Polio Incident", "Abduction", "Extortion", "Robberies"]
        
        for incident in incidents:
            incident_button = tk.Button(incident_list_frame, text=incident, font=("Arial", 12), bg="#F5F5F4", anchor="w")
            incident_button.pack(fill=tk.X, padx=5, pady=5)

    def on_main_menu(self):
        """Return to the main menu (LoginApp)."""
        self.destroy()
        self.parent.show_dashboard()

if __name__ == "__main__":
    app = LoginApp()
    app.mainloop()
