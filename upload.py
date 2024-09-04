import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QLineEdit, QVBoxLayout, QGridLayout, QWidget, QPushButton, QCheckBox, QGroupBox, QFileDialog, QDesktopWidget, QHBoxLayout
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # Window size dynamically changed according to screen size
        self.setWindowTitle("Data Entry Page")
        self.setup_ui()
        self.resize_to_screen()

    def setup_ui(self):
        # Create central widget and main layout
        self.central_widget = QWidget()
        self.main_layout = QVBoxLayout(self.central_widget)
        
        # Add QLabel for background image which automatically scales the image according to screen size
        self.background_label = QLabel(self)
        self.background_label.setPixmap(QPixmap('Images/Blur_Background.jpg'))
        self.background_label.setScaledContents(True)
        self.background_label.setGeometry(0, 0, self.width(), self.height())
        self.background_label.lower()  # Ensure the background is behind all other widgets

        # Create a layout for the logos and heading
        top_layout = QHBoxLayout()
        self.main_layout.addLayout(top_layout)

        # Left logo
        self.left_logo = QLabel(self)
        self.left_logo.setPixmap(QPixmap('Images/left_logo.png').scaled(170, 170, Qt.KeepAspectRatio))
        self.left_logo.setStyleSheet("""
            QLabel {
                border: 2px solid red;
            }
        """)
        top_layout.addWidget(self.left_logo)
        

        # Heading label
        self.heading_label = QLabel("Data Entry", self)
        self.heading_label.setAlignment(Qt.AlignCenter)
        self.heading_label.setStyleSheet("""
            QLabel {
                font-family: 'Sitka Small';
                font-size: 80px;
                font-weight: bold;
                color: #f8c55c;
                border: 2px solid red;
            }
        """)
        top_layout.addWidget(self.heading_label, alignment=Qt.AlignCenter)

        # Right logo
        self.right_logo = QLabel(self)
        self.right_logo.setPixmap(QPixmap('Images/right_logo.png').scaled(170, 170, Qt.KeepAspectRatio))
        self.right_logo.setStyleSheet("""
            QLabel {
                border: 2px solid red;
            }
        """)
        top_layout.addWidget(self.right_logo)

        # Grid layout for form fields
        grid_layout = QGridLayout()
        self.main_layout.addLayout(grid_layout)

        # Row 1
        grid_layout.addWidget(QLabel("Date"), 1, 0)
        grid_layout.addWidget(QLineEdit(), 1, 1)
        grid_layout.addWidget(QLabel("Time"), 1, 2)
        grid_layout.addWidget(QLineEdit(), 1, 3)

        # Row 2
        grid_layout.addWidget(QLabel("Organization"), 2, 0)
        grid_layout.addWidget(QLineEdit(), 2, 1)
        grid_layout.addWidget(QLabel("Sub Organization"), 2, 2)
        grid_layout.addWidget(QLineEdit(), 2, 3)

        # Row 3
        grid_layout.addWidget(QLabel("Name"), 3, 0)
        grid_layout.addWidget(QLineEdit(), 3, 1)
        grid_layout.addWidget(QLabel("Comds"), 3, 2)
        grid_layout.addWidget(QLineEdit(), 3, 3)

        # Row 4
        grid_layout.addWidget(QLabel("Brief Description"), 4, 0)
        grid_layout.addWidget(QLineEdit(), 4, 1)

        # Row 5
        grid_layout.addWidget(QLabel("Area"), 5, 0)
        grid_layout.addWidget(QLineEdit(), 5, 1)

        # Row 6
        grid_layout.addWidget(QLabel("Give Case ID #:"), 6, 0)
        grid_layout.addWidget(QLineEdit(), 6, 1)

        # Row 8
        grid_layout.addWidget(QLabel("Cas"), 8, 0)
        grid_layout.addWidget(QLineEdit(), 8, 1)

        # Row 9
        grid_layout.addWidget(QLabel("Martyred"), 9, 0)
        grid_layout.addWidget(QLineEdit(), 9, 1)
        grid_layout.addWidget(QLabel("Injured"), 9, 2)
        grid_layout.addWidget(QLineEdit(), 9, 3)

        # Row 10
        grid_layout.addWidget(QLabel("Longitude, Latitude"), 10, 0)
        grid_layout.addWidget(QLineEdit(), 10, 1)

        # Row 11
        grid_layout.addWidget(QLabel("Khwjari"), 11, 0)
        grid_layout.addWidget(QLineEdit(), 11, 1)

        # Row 12
        grid_layout.addWidget(QLabel("Killed"), 12, 0)
        grid_layout.addWidget(QLineEdit(), 12, 1)
        grid_layout.addWidget(QLabel("Injured"), 12, 2)
        grid_layout.addWidget(QLineEdit(), 12, 3)

        # Incident Type Checkbuttons
        grid_layout.addWidget(QLabel("Type of Incident"), 13, 0)
        types = ["Fire Raid", "Tgt Killing", "Sd attack", "IED Attack", "Ambush", "Police Incidents", "Abduction", "Extortion", "Robberies"]
        for i, t in enumerate(types):
            checkbox = QCheckBox(t)
            checkbox.setStyleSheet("background-color: #ffffe0;")
            grid_layout.addWidget(checkbox, 14 + i // 2, i % 2)

        # Upload, Save and LowDown Tab Frame
        upload_tab_frame = QGroupBox("Save Data")
        upload_tab_frame.setStyleSheet("""
            background-color: background-color: rgba(255, 255, 255, 0);  /* Fully transparent background */
            padding: 10px;
        """)
        upload_tab_layout = QVBoxLayout(upload_tab_frame)
        self.main_layout.addWidget(upload_tab_frame)

        button_style = """
            QPushButton {
                background-color: #a5d6a7;
                border: 1px solid #ccc;
                padding: 10px;
                font-size: 16px;
                border-radius: 20px;
            }
            QPushButton:hover {
                background-color: #81c784;
            }
        """

        import_button = QPushButton("Import GOE kmz")
        import_button.setStyleSheet(button_style)
        upload_tab_layout.addWidget(import_button)

        lowdown_button = QPushButton("Low Down")
        lowdown_button.setStyleSheet(button_style)
        upload_tab_layout.addWidget(lowdown_button)

        save_button = QPushButton("Save Data")
        save_button.setStyleSheet(button_style)
        upload_tab_layout.addWidget(save_button)

        self.setCentralWidget(self.central_widget)

        # Apply stylesheets
        self.apply_styles()

    def apply_styles(self):
        self.setStyleSheet("""
            QMainWindow {
                background-image: url('Blur_Background.jpg');  /* Add this line with correct path */
                background-repeat: no-repeat;  /* Ensure that your image does not repeat */
                background-position: center;  /* Center your image in the window */
                background-size: cover;  /* Cover the entire window with the image */
                background-attachment: fixed;  /* Keep the background fixed */
            }
            QPushButton {
                font-family: 'Sitka Small';  /* Set the font family */
                font-size: 28px;  /* Increase the font size of buttons */
                font-weight: bold;  /* Make the button text bold */
                background-color: white;  /* Set the background color of buttons */
                color: black;  /* Set the text color of buttons */
                padding: 15px;  /* Increase padding inside the buttons */
                border: 2px solid #4CAF50;  /* Set the border color and width of buttons */
                border-radius: 30px;  /* Set the border radius of buttons */
                border-color: #EEBC1D; /* Set the border color of buttons */
            }
            QPushButton:hover {
                background-color: #EEBC1D;  /* Set the background color of buttons when hovered */
                border-color: #EEBC1D;  /* Set the border color of buttons when hovered */
            }
            QPushButton:pressed {
                background-color: gold;  /* Set the background color of buttons when pressed */
                border-color: gold;  /* Set the border color of buttons when pressed */
            }
            QWidget#container_widget {
                background-color: rgba(255, 255, 255, 0);  /* Fully transparent background */
                border: none;  /* Remove the border */
                border-radius: 10px;  /* Set the border radius of the container */
                padding: 150px;  /* Add padding inside the container */
                min-width: 400px;  /* Set the minimum width of the container */
                min-height: 300px;  /* Set the minimum height of the container */
            }
        """)

    def upload_image(self):
        options = QFileDialog.Options()
        file_name, _ = QFileDialog.getOpenFileName(self, "Open Image File", "", "Image Files (*.png *.jpg *.bmp)", options=options)
        if file_name:
            pixmap = QPixmap(file_name)
            self.image_label.setPixmap(pixmap.scaled(self.image_label.size(), Qt.KeepAspectRatio, Qt.SmoothTransformation))

    def resize_to_screen(self):
        screen = QDesktopWidget().screenGeometry()
        self.setGeometry(0, 0, screen.width(), screen.height())
        self.background_label.setGeometry(0, 0, screen.width(), screen.height())
        self.left_logo.setGeometry(20, 20, 170, 170)    # Adjust left logo position on resize
        self.heading_label.setGeometry(0, 20, self.width(), 125)   # Adjust the heading position on resize
        self.right_logo.setGeometry(self.width() - 185, 17, 170, 170)  # Adjust right logo position on resize

    # Overriding the resizeEvent class to resize according to every screen
    def resizeEvent(self, event):
        self.resize_to_screen()
        super().resizeEvent(event)

# Run the application
app = QApplication(sys.argv)
window = MainWindow()
window.show()
sys.exit(app.exec_())