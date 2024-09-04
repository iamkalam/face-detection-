import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QVBoxLayout, QWidget, QSizePolicy, QLabel, QDesktopWidget
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap # For resizing the image according to the screen size


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # Window size dynamically changed according to screen size
        self.setWindowTitle("Home Page")
        self.resize_to_screen

        # Create central widget and main layout
        self.central_widget = QWidget()
        self.main_layout = QVBoxLayout(self.central_widget)
        
        # Add QLabel for background image which automatically scales the image according to screen size
        self.background_label = QLabel(self)
        self.background_label.setGeometry(0, 0, self.width(), self.height())
        self.background_label.setPixmap(QPixmap('Images/Blur_Background.jpg'))
        self.background_label.setScaledContents(True)

        # Left logo
        self.left_logo = QLabel(self)
        self.left_logo.setPixmap(QPixmap('Images/left_logo.png').scaled(170, 170, Qt.KeepAspectRatio))

        # border: 2px solid red; for checking the size of container
        # Heading label with absolute positioning and inliine styling
        self.heading_label = QLabel("Main Page", self)
        self.heading_label.setAlignment(Qt.AlignCenter)
        
        self.heading_label.setStyleSheet("""
            QLabel {
                font-family: 'Sitka Small';
                font-size: 80px;
                font-weight: bold;
                color: #f8c55c;
                position: absolute;
                top: 20px;
                right: 50%;        
            }
        """)
        
        # Right logo
        self.right_logo = QLabel(self)
        self.right_logo.setPixmap(QPixmap('Images/right_logo.png').scaled(170, 170, Qt.KeepAspectRatio))

        # Create a container widget with a fixed size
        self.container_widget = QWidget()
        self.container_widget.setObjectName("container_widget")  # Set object name for styling
        self.container_widget.setFixedSize(200, 250)  # Increase the height of the container
        self.container_layout = QVBoxLayout(self.container_widget)
        self.container_layout.setContentsMargins(20, 20, 20, 20)  # Increase margins to create space

        # Data Entry button
        self.data_entry_button = QPushButton("Data Entry", self)
        self.data_entry_button.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        self.data_entry_button.setMinimumWidth(400)
        self.container_layout.addWidget(self.data_entry_button, alignment=Qt.AlignCenter)

        # Search button
        self.search_button = QPushButton("Search", self)
        self.search_button.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        self.search_button.setMinimumWidth(400)
        self.container_layout.addWidget(self.search_button, alignment=Qt.AlignCenter)

        # Search button
        self.search_button = QPushButton("Low-Down", self)
        self.search_button.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        self.search_button.setMinimumWidth(400)
        self.container_layout.addWidget(self.search_button, alignment=Qt.AlignCenter)

        # Exit button
        self.exit_button = QPushButton("Exit", self)
        self.exit_button.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        self.exit_button.setMinimumWidth(400)
        self.exit_button.clicked.connect(self.close)
        self.container_layout.addWidget(self.exit_button, alignment=Qt.AlignCenter)

        # Add the container widget to the main layout
        self.main_layout.addWidget(self.container_widget, alignment=Qt.AlignCenter)
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

    def resize_to_screen(self):
        screen = QDesktopWidget().screenGeometry()
        self.setGeometry(0, 0, screen.width(), screen.height())
        self.background_label.setGeometry(0, 0, screen.width(), screen.height())
        self.left_logo.setGeometry(20, 20, 170, 170)    # Adjust left logo position on resize
        self.heading_label.setGeometry(0, 20, self.width(), 125)   # Adjust the heading position on resize
        self.right_logo.setGeometry(self.width() - 185, 17, 170, 170)  # Adjust right logo position on resize


    # Overriding the resizeEvent class to resize accroding to every screen
    def resizeEvent(self, event):
        self.resize_to_screen()
        super().resizeEvent(event)

# Run the application
app = QApplication(sys.argv)
window = MainWindow()
window.show()
sys.exit(app.exec_())