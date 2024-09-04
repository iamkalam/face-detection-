from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QLineEdit, QVBoxLayout, QGridLayout, QWidget, QPushButton, QGroupBox, QHBoxLayout, QSpacerItem, QSizePolicy, QFileDialog, QFrame, QScrollArea, QComboBox, QListWidget
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt


class SearchPage(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Search Page")
        self.setGeometry(100, 100, 800, 600)
        self.setup_ui()

    def setup_ui(self):
        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        main_layout = QVBoxLayout(central_widget)

        # Search Tab
        search_tab_frame = QFrame()
        search_tab_frame.setStyleSheet("background-color: #E7E5E4; padding: 10px; border: 2px solid #333;")
        main_layout.addWidget(search_tab_frame)

        search_tab_layout = QHBoxLayout(search_tab_frame)

        upload_button = QPushButton("Upload Picture")
        upload_button.setStyleSheet("""
            QPushButton {
                font: 14px Arial;
                background-color: #F5F5F4;
                padding: 10px;
                border-radius: 5px;
                border: 2px solid #333;
            }
            QPushButton:hover {
                background-color: #E0E0E0;
            }
            QPushButton:pressed {
                background-color: #D0D0D0;
            }
        """)
        upload_button.clicked.connect(self.upload_picture)
        search_tab_layout.addWidget(upload_button)

        search_button1 = QPushButton("Search")
        search_button1.setStyleSheet("""
            QPushButton {
                font: 14px Arial;
                background-color: #F5F5F4;
                padding: 10px;
                border-radius: 5px;
                border: 2px solid #333;
            }
            QPushButton:hover {
                background-color: #E0E0E0;
            }
            QPushButton:pressed {
                background-color: #D0D0D0;
            }
        """)
        search_tab_layout.addWidget(search_button1)

        search_entry = QLineEdit()
        search_entry.setStyleSheet("font: 14px Arial; background-color: #F5F5F4; padding: 10px; border-radius: 5px; border: 2px solid #333;")
        search_tab_layout.addWidget(search_entry)

        search_button2 = QPushButton("Search")
        search_button2.setStyleSheet("""
            QPushButton {
                font: 14px Arial;
                background-color: #F5F5F4;
                padding: 10px;
                border-radius: 5px;
                border: 2px solid #333;
            }
            QPushButton:hover {
                background-color: #E0E0E0;
            }
            QPushButton:pressed {
                background-color: #D0D0D0;
            }
        """)
        search_tab_layout.addWidget(search_button2)

        # Main Menu Button
        main_menu_frame = QFrame()
        main_menu_frame.setStyleSheet("background-color: lightgray; border: 2px solid #333;")
        main_layout.addWidget(main_menu_frame, alignment=Qt.AlignRight)

        main_menu_button = QPushButton("Main Menu")
        main_menu_button.setStyleSheet("""
            QPushButton {
                font: 14px Arial;
                background-color: #F5F5F4;
                padding: 10px;
                border-radius: 5px;
                border: 2px solid #333;
            }
            QPushButton:hover {
                background-color: #E0E0E0;
            }
            QPushButton:pressed {
                background-color: #D0D0D0;
            }
        """)
        main_menu_button.clicked.connect(self.on_main_menu)
        main_menu_frame.layout = QVBoxLayout(main_menu_frame)
        main_menu_frame.layout.addWidget(main_menu_button)

        # Content Area
        content_frame = QFrame()
        content_frame.setStyleSheet("background-color: lightgray; padding: 10px; border: 2px solid #333;")
        main_layout.addWidget(content_frame)

        content_layout = QHBoxLayout(content_frame)

        # Left Sidebar
        left_sidebar_frame = QFrame()
        left_sidebar_frame.setStyleSheet("background-color: lightgray; width: 200px; border: 2px solid #333;")
        content_layout.addWidget(left_sidebar_frame)

        left_sidebar_layout = QVBoxLayout(left_sidebar_frame)
        self.create_date_search(left_sidebar_layout)
        self.create_case_id_search(left_sidebar_layout)
        self.create_quantity_matched(left_sidebar_layout)
        self.create_activity_logs(left_sidebar_layout)

        # Center Content
        center_frame = QFrame()
        center_frame.setStyleSheet("background-color: lightgray; width: 600px; border: 2px solid #333;")
        content_layout.addWidget(center_frame)

        center_layout = QVBoxLayout(center_frame)
        self.create_photo_preview(center_layout)

        # Right Sidebar
        right_sidebar_frame = QFrame()
        right_sidebar_frame.setStyleSheet("background-color: lightgray; width: 200px; border: 2px solid #333;")
        content_layout.addWidget(right_sidebar_frame)

        right_sidebar_layout = QVBoxLayout(right_sidebar_frame)
        self.create_incident_list(right_sidebar_layout)

    def create_date_search(self, layout):
        date_search_frame = QGroupBox("Search Incidents by Date")
        date_search_frame.setStyleSheet("font: 14px Arial; background-color: #E7E5E4; padding: 10px; border: 2px solid #333;")
        layout.addWidget(date_search_frame)

        date_search_layout = QGridLayout(date_search_frame)

        from_label = QLabel("Search from")
        from_label.setStyleSheet("font: 12px Arial; background-color: #E7E5E4;")
        date_search_layout.addWidget(from_label, 0, 0)

        from_date = QLineEdit()
        from_date.setStyleSheet("font: 12px Arial; background-color: #F5F5F4; padding: 5px; border-radius: 5px; border: 2px solid #333;")
        date_search_layout.addWidget(from_date, 0, 1)

        to_label = QLabel("Search to")
        to_label.setStyleSheet("font: 12px Arial; background-color: #E7E5E4;")
        date_search_layout.addWidget(to_label, 1, 0)

        to_date = QLineEdit()
        to_date.setStyleSheet("font: 12px Arial; background-color: #F5F5F4; padding: 5px; border-radius: 5px; border: 2px solid #333;")
        date_search_layout.addWidget(to_date, 1, 1)

        options = QComboBox()
        options.addItems(["Fire Raid", "Tgt Killing", "SB Attack", "IED Attack", "Ambush", "Polio Incident", "Abduction", "Extortion", "Robberies"])
        options.setStyleSheet("font: 12px Arial; background-color: #F5F5F4; padding: 5px; border-radius: 5px; border: 2px solid #333;")
        date_search_layout.addWidget(options, 2, 0, 1, 2)

        search_button = QPushButton("Search")
        search_button.setStyleSheet("""
            QPushButton {
                font: 12px Arial;
                background-color: #F5F5F4;
                padding: 10px;
                border-radius: 5px;
                border: 2px solid #333;
            }
            QPushButton:hover {
                background-color: #E0E0E0;
            }
            QPushButton:pressed {
                background-color: #D0D0D0;
            }
        """)
        date_search_layout.addWidget(search_button, 3, 0, 1, 2)

    def create_case_id_search(self, layout):
        case_id_frame = QGroupBox("Search Incidents by Case ID")
        case_id_frame.setStyleSheet("font: 14px Arial; background-color: #E7E5E4; padding: 10px; border: 2px solid #333;")
        layout.addWidget(case_id_frame)

        case_id_layout = QVBoxLayout(case_id_frame)

        case_id_entry = QLineEdit()
        case_id_entry.setStyleSheet("font: 14px Arial; background-color: #F5F5F4; padding: 10px; border-radius: 5px; border: 2px solid #333;")
        case_id_layout.addWidget(case_id_entry)

        search_button = QPushButton("Search")
        search_button.setStyleSheet("""
            QPushButton {
                font: 14px Arial;
                background-color: #F5F5F4;
                padding: 10px;
                border-radius: 5px;
                border: 2px solid #333;
            }
            QPushButton:hover {
                background-color: #E0E0E0;
            }
            QPushButton:pressed {
                background-color: #D0D0D0;
            }
        """)
        case_id_layout.addWidget(search_button)

    def create_quantity_matched(self, layout):
        quantity_frame = QGroupBox("Quantity of Pictures Matched")
        quantity_frame.setStyleSheet("font: 14px Arial; background-color: #E7E5E4; padding: 10px; border: 2px solid #333;")
        layout.addWidget(quantity_frame)

        quantity_layout = QVBoxLayout(quantity_frame)

        quantity_label = QLabel("0")
        quantity_label.setStyleSheet("font: 24px Arial; background-color: #F5F5F4; padding: 10px; border-radius: 5px; border: 2px solid #333;")
        quantity_layout.addWidget(quantity_label)

    def create_activity_logs(self, layout):
        logs_frame = QGroupBox("Activity Logs")
        logs_frame.setStyleSheet("font: 14px Arial; background-color: #E7E5E4; padding: 10px; border: 2px solid #333;")
        layout.addWidget(logs_frame)

        logs_layout = QVBoxLayout(logs_frame)

        logs_list = QListWidget()
        logs_list.setStyleSheet("font: 14px Arial; background-color: #F5F5F4; padding: 10px; border-radius: 5px; border: 2px solid #333;")
        logs_layout.addWidget(logs_list)

    def create_photo_preview(self, layout):
        preview_frame = QGroupBox("Photo Preview")
        preview_frame.setStyleSheet("font: 14px Arial; background-color: #E7E5E4; padding: 10px; border: 2px solid #333;")
        layout.addWidget(preview_frame)

        preview_layout = QVBoxLayout(preview_frame)

        self.preview_label = QLabel("Photo will be displayed here")
        self.preview_label.setStyleSheet("font: 18px Arial; background-color: #F5F5F4; padding: 10px; border-radius: 5px; border: 2px solid #333;")
        preview_layout.addWidget(self.preview_label)

    def create_incident_list(self, layout):
        incident_frame = QGroupBox("Incident List")
        incident_frame.setStyleSheet("font: 14px Arial; background-color: #E7E5E4; padding: 10px; border: 2px solid #333;")
        layout.addWidget(incident_frame)

        incident_layout = QVBoxLayout(incident_frame)

        incidents = ["Fire Raid", "Tgt Killing", "SB Attack", "IED Attack", "Ambush", 
                     "Polio Incident", "Abduction", "Extortion", "Robberies"]
        
        for incident in incidents:
            incident_button = QPushButton(incident)
            incident_button.setStyleSheet("""
                QPushButton {
                    font: 12px Arial;
                    background-color: #F5F5F4;
                    padding: 10px;
                    border-radius: 5px;
                    text-align: left;
                    border: 2px solid #333;
                }
                QPushButton:hover {
                    background-color: #E0E0E0;
                }
                QPushButton:pressed {
                    background-color: #D0D0D0;
                }
            """)
            incident_layout.addWidget(incident_button)

    def upload_picture(self):
        file_dialog = QFileDialog()
        file_path, _ = file_dialog.getOpenFileName(self, "Open Image File", "", "Image Files (*.png *.jpg *.bmp)")
        if file_path:
            pixmap = QPixmap(file_path)
            self.preview_label.setPixmap(pixmap.scaled(self.preview_label.size(), Qt.KeepAspectRatio, Qt.SmoothTransformation))

    def on_main_menu(self):
        """Return to the main dashboard (login page)."""
        self.close()  # Close the search page window
        # Assuming there is a method to show the dashboard in the parent class
        # self.parent.show_dashboard()  # Show the dashboard again


def open_search_page():
    app = QApplication([])
    window = SearchPage()
    window.show()
    app.exec_()

open_search_page()