import tkinter as tk
from tkinter import messagebox

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
        self.table_frame = None
        
        # Show the login page initially
        self.show_login_page()

    def show_login_page(self):
        """Displays the login page."""
        if self.dashboard_frame:
            self.dashboard_frame.pack_forget()  # Hide the dashboard frame if it's visible
        if self.table_frame:
            self.table_frame.pack_forget()  # Hide the table frame if it's visible

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
        if self.table_frame:
            self.table_frame.pack_forget()  # Hide the table frame if it's visible

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

    def show_table(self):
        """Displays the incident table when search is clicked."""
        self.dashboard_frame.pack_forget()  # Hide the dashboard frame

        self.table_frame = tk.Frame(self, bg="lightgray")
        self.table_frame.pack(expand=True, fill=tk.BOTH, pady=20, padx=20)

        # Table headers
        headers = ["SR#", "Date", "Time", "Org", "Sub Org", "Name"]
        for idx, header in enumerate(headers):
            header_label = tk.Label(
                self.table_frame,
                text=header,
                font=("Arial", 12, "bold"),
                bg="lightgray",
                width=10,
                relief=tk.RAISED
            )
            header_label.grid(row=0, column=idx, padx=5, pady=5)

        # Sample data
        sample_data = [
            {"SR#": "1", "Date": "01/01/2024", "Time": "10:00 AM", "Org": "Org A", "Sub Org": "Sub A", "Name": "John Doe"},
            {"SR#": "2", "Date": "02/01/2024", "Time": "11:00 AM", "Org": "Org B", "Sub Org": "Sub B", "Name": "Jane Doe"},
            {"SR#": "3", "Date": "03/01/2024", "Time": "12:00 PM", "Org": "Org C", "Sub Org": "Sub C", "Name": "Jim Doe"},
            {"SR#": "4", "Date": "04/01/2024", "Time": "01:00 PM", "Org": "Org D", "Sub Org": "Sub D", "Name": "Jill Doe"},
        ]

        # Table rows
        for row_idx, row_data in enumerate(sample_data, start=1):
            for col_idx, (key, value) in enumerate(row_data.items()):
                cell = tk.Label(
                    self.table_frame,
                    text=value,
                    font=("Arial", 10),
                    bg="lightgray",
                    width=10,
                    relief=tk.SUNKEN
                )
                cell.grid(row=row_idx, column=col_idx, padx=5, pady=5)

    def on_submit(self):
        username = self.username_entry.get()
        password = self.password_entry.get()
        
        # Check credentials
        if username == CORRECT_USERNAME and password == CORRECT_PASSWORD:
            self.show_dashboard()
        else:
            messagebox.showerror("Login Failed", "Invalid username or password")

    def on_search(self):
        # Show the incident table when the search button is clicked
        self.show_table()

    def on_upload(self):
        # Logic for upload action
        print("Upload button clicked")

    def on_exit(self):
        # Logic for exit action
        print("Exit button clicked")
        self.quit()

if __name__ == "__main__":
    app = LoginApp()
    app.mainloop()
