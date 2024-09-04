import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QLineEdit, QPushButton, QVBoxLayout, QWidget, QMessageBox, QSizePolicy, QCheckBox, QDesktopWidget
from PyQt5.QtCore import Qt  # Import Qt for alignment
from PyQt5.QtGui import QPixmap # For resizing the image according to the screen size


class LoginWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # Window size dynamically changed according to screen size
        self.setWindowTitle("Login Page")
        self.resize_to_screen

        # Create central widget and main layout
        self.central_widget = QWidget()
        self.main_layout = QVBoxLayout(self.central_widget)
        
        # Add QLabel for background image which automatically scales the image according to screen size
        self.background_label = QLabel(self)
        self.background_label.setGeometry(0, 0, self.width(), self.height())
        self.background_label.setPixmap(QPixmap('Images/Background.jpg'))
        self.background_label.setScaledContents(True)

        # Left logo
        self.left_logo = QLabel(self)
        self.left_logo.setPixmap(QPixmap('Images/left_logo.png').scaled(170, 170, Qt.KeepAspectRatio))

        # border: 2px solid red; for checking the size of container
        # Heading label with absolute positioning and inliine styling
        self.heading_label = QLabel("Golden Eye", self)
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
        self.container_layout = QVBoxLayout(self.container_widget)

        # Username label and text field
        self.username_input = QLineEdit(self)
        self.username_input.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        self.username_input.setMinimumWidth(400)
        self.username_input.setPlaceholderText("Username")  # Set placeholder text for username
        self.username_input.setAlignment(Qt.AlignCenter)  # Center the text
        self.container_layout.addWidget(self.username_input, alignment=Qt.AlignCenter)

        # Password label and text field
        self.password_input = QLineEdit(self)
        self.password_input.setEchoMode(QLineEdit.Password)
        self.password_input.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        self.password_input.setMinimumWidth(400)
        self.password_input.setPlaceholderText("Password")  # Set placeholder text for password
        self.password_input.setAlignment(Qt.AlignCenter)  # Center the text
        self.container_layout.addWidget(self.password_input, alignment=Qt.AlignCenter)

        # Login button
        self.login_button = QPushButton("Login", self)
        self.login_button.setToolTip("Click to login")  # Add tooltip to the login button
        self.login_button.clicked.connect(self.check_login)
        self.login_button.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        self.login_button.setMinimumWidth(150)
        self.container_layout.addWidget(self.login_button, alignment=Qt.AlignCenter)

        # Remember Me checkbox
        self.remember_me_checkbox = QCheckBox("Remember Me", self)
        self.container_layout.addWidget(self.remember_me_checkbox, alignment=Qt.AlignCenter)

        # Add the container widget to the main layout
        self.main_layout.addWidget(self.container_widget, alignment=Qt.AlignCenter)
        self.setCentralWidget(self.central_widget)

        # Apply stylesheets
        self.apply_styles()

    def apply_styles(self):
        self.setStyleSheet("""
            QMainWindow {
                background-image: url('Background.jpg');  /* Add this line with correct path */
                background-repeat: no-repeat;  /* Ensure that your image does not repeat */
                background-position: center;  /* Center your image in the window */
                background-size: cover;  /* Cover the entire window with the image */
                background-attachment: fixed;  /* Keep the background fixed */
            }
            QLabel {
                font-family: 'Sitka Small';  /* Set the font family */
                font-size: 20px;  /* Set the font size of labels */
                font-weight: bold;  /* Set the font weight of labels to bold */
                color: white;  /* Set the text color of labels to white */
            }
            QLineEdit {
                font-family: 'Sitka Small';  /* Set the font family */
                font-size: 20px;  /* Set the font size of line edits */
                padding: 11px;  /* Add padding inside the line edits */
                border: 2px solid #ccc;  /* Set the border color and width of line edits */
                border-radius: 15px;  /* Set the border radius of line edits */
                border-color: #EEBC1D; /* Set the border color of buttons */
                text-align: center;  /* Center the text */
                font-weight: bold;  /* Make the text bold */
            }
            QLineEdit::placeholder {
                color: gray;  /* Set the placeholder text color to gray */
            }
            QPushButton {
                font-family: 'Sitka Small';  /* Set the font family */
                font-size: 20px;  /* Increase the font size of buttons */
                font-weight: bold;  /* Make the button text bold */
                background-color: white;  /* Set the background color of buttons */
                color: black;  /* Set the text color of buttons */
                padding: 15px;  /* Increase padding inside the buttons */
                border: 2px solid #4CAF50;  /* Set the border color and width of buttons */
                border-radius: 15px;  /* Set the border radius of buttons */
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
            QCheckBox {
                font-family: 'Sitka Small';  /* Set the font family */
                font-size: 15px;  /* Set the font size */
                font-weight: bold;  /* Make the text bold */
                color: white;  /* Set the text color to white */
            }
            QWidget#container_widget {
                background-color: rgba(255, 255, 255, 0);  /* Fully transparent background */
                border: none;  /* Remove the border */
                border-radius: 10px;  /* Set the border radius of the container */
                padding: 100px;  /* Add padding inside the container */
                min-width: 400px;  /* Set the minimum width of the container */
                min-height: 300px;  /* Set the minimum height of the container */
            }
        """)

    # Changed according to the dynamic screen size changing. 
    # Previous implementation was not bringing up message in popins
    def check_login(self):
        username = self.username_input.text()
        password = self.password_input.text()
        remember_me = self.remember_me_checkbox.isChecked()

        # Simple validation (replace with actual validation logic)
        if username == "admin" and password == "password":
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Information)
            msg.setWindowTitle("Login Successful")
            if remember_me:
                msg.setText("Welcome! (Remember Me checked)")
            else:
                msg.setText("Welcome!")
            msg.exec_()
        else:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Warning)
            msg.setWindowTitle("Login Failed")
            msg.setText("Invalid username or password")
            msg.exec_()

    # Size resizing function to resize according to screen
    def resize_to_screen(self):
        screen = QDesktopWidget().screenGeometry()
        self.setGeometry(0, 0, screen.width(), screen.height())
        self.background_label.setGeometry(0, 0, screen.width(), screen.height())
        self.left_logo.setGeometry(20, 20, 170, 170)    # Adjust left logo position on resize
        self.heading_label.setGeometry(5, 20, self.width(), 125)   # Adjust the heading position on resize
        self.right_logo.setGeometry(self.width() - 185, 17, 170, 170)  # Adjust right logo position on resize


    # Overriding the resizeEvent class to resize accroding to every screen
    def resizeEvent(self, event):
        self.resize_to_screen()
        super().resizeEvent(event)

# Run the application
app = QApplication(sys.argv)
window = LoginWindow()
window.show()
sys.exit(app.exec_())