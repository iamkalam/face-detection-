from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QLineEdit, QVBoxLayout, QGridLayout, QWidget, QPushButton, QCheckBox, QGroupBox, QHBoxLayout, QSpacerItem, QSizePolicy, QFileDialog, QFrame, QScrollArea
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt


class LowDownPage(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("LOW DOWN - Ts")
        self.setGeometry(100, 100, 800, 600)
        self.setup_ui()

    def setup_ui(self):
        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        main_layout = QHBoxLayout(central_widget)

        # Scroll Area
        scroll_area = QScrollArea()
        scroll_area.setWidgetResizable(True)
        main_layout.addWidget(scroll_area)

        # Scroll Area Content
        scroll_content = QWidget()
        scroll_area.setWidget(scroll_content)

        # Main Frame Layout
        frame_layout = QVBoxLayout(scroll_content)

        # Title Label
        title_label = QLabel("LOW DOWN - Ts")
        title_label.setAlignment(Qt.AlignCenter)
        title_label.setStyleSheet("font-size: 24px; font-weight: bold; margin-bottom: 20px;")
        frame_layout.addWidget(title_label)

        # Grid layout for quarters
        grid_layout = QGridLayout()
        frame_layout.addLayout(grid_layout)

        # Create quarters with QGroupBox
        quarter1_group = QGroupBox("Personal Information")
        quarter1_layout = QVBoxLayout()
        quarter1_group.setLayout(quarter1_layout)

        quarter2_group = QGroupBox("Social Media & Passport Details")
        quarter2_layout = QVBoxLayout()
        quarter2_group.setLayout(quarter2_layout)

        quarter3_group = QGroupBox("Other Information & Family Details")
        quarter3_layout = QVBoxLayout()
        quarter3_group.setLayout(quarter3_layout)

        quarter4_group = QGroupBox("In-Laws & Criminal Activities")
        quarter4_layout = QVBoxLayout()
        quarter4_group.setLayout(quarter4_layout)

        grid_layout.addWidget(quarter1_group, 0, 0)
        grid_layout.addWidget(quarter2_group, 0, 1)
        grid_layout.addWidget(quarter3_group, 1, 0)
        grid_layout.addWidget(quarter4_group, 1, 1)

        # Fields for each quarter
        fields_q1 = [
            "Name", "Alias", "Father Name", "Mother Name", "Religion", "Sect/Sub Sect",
            "Caste", "Sub Caste", "Nationality", "CNIC", "Date of Birth", "Age", "Civ Edn",
            "Complexion", "Contact Nos"
        ]

        social_media_fields = ["Facebook", "Twitter", "Tik Tok", "E-mail Address"]

        passport_fields = [
            "Passport No", "Bank Acct Details", "Temp Address", "Perm Address",
            "Detail of Visit foreign countries", "Areas of Influence", "Active Since",
            "Likely Loc", "Tier", "Affil with Ts Gp"
        ]

        other_fields = [
            "Political Affl", "Religious Affl", "Occupation", "Mother Name", "Source of Income",
            "Property Details", "Marital Status", "Detail of Children"
        ]

        family_fields = ["Brothers", "Sisters", "Uncles", "Aunts", "Cousins"]

        inlaws_fields = ["Father in Law", "Mother in Law", "Brother in Law", "Sister in Law"]

        criminal_activities = [
            "Criminal Activities", "Extortion Languages", "Attitude towards Govt", 
            "Attitude towards State", "Attitude towards SFs", "Gen Habbits", 
            "Reputation among locals", "FIR Status"
        ]

        # Adding labels and entry widgets for personal information in quarter 1
        for field in fields_q1:
            label = QLabel(f"{field}:")
            label.setStyleSheet("font-weight: bold;")
            quarter1_layout.addWidget(label)
            entry = QLineEdit()
            entry.setStyleSheet("margin-bottom: 10px; border-radius: 5px; padding: 5px;")
            entry.setFixedHeight(30)
            quarter1_layout.addWidget(entry)

        # Social Media Details in quarter 2
        social_media_label = QLabel("Social Media Details")
        social_media_label.setStyleSheet("font-size: 16px; font-weight: bold; margin-top: 20px;")
        quarter2_layout.addWidget(social_media_label)

        for field in social_media_fields:
            label = QLabel(f"{field}:")
            label.setStyleSheet("font-weight: bold;")
            quarter2_layout.addWidget(label)
            entry = QLineEdit()
            entry.setStyleSheet("margin-bottom: 10px; border-radius: 5px; padding: 5px;")
            entry.setFixedHeight(30)
            quarter2_layout.addWidget(entry)

        # Adding labels and entry widgets for passport and other information in quarter 2
        for field in passport_fields:
            label = QLabel(f"{field}:")
            label.setStyleSheet("font-weight: bold;")
            quarter2_layout.addWidget(label)
            entry = QLineEdit()
            entry.setStyleSheet("margin-bottom: 10px; border-radius: 5px; padding: 5px;")
            entry.setFixedHeight(30)
            quarter2_layout.addWidget(entry)

        # Adding labels and entry widgets for other information in quarter 3
        for field in other_fields:
            label = QLabel(f"{field}:")
            label.setStyleSheet("font-weight: bold;")
            quarter3_layout.addWidget(label)
            entry = QLineEdit()
            entry.setStyleSheet("margin-bottom: 10px; border-radius: 5px; padding: 5px;")
            entry.setFixedHeight(30)
            quarter3_layout.addWidget(entry)

        # Family Detail (Own) in quarter 3
        family_detail_label = QLabel("Family Detail (Own)")
        family_detail_label.setStyleSheet("font-size: 16px; font-weight: bold; margin-top: 20px;")
        quarter3_layout.addWidget(family_detail_label)

        for field in family_fields:
            label = QLabel(f"{field}:")
            label.setStyleSheet("font-weight: bold;")
            quarter3_layout.addWidget(label)
            entry = QLineEdit()
            entry.setStyleSheet("margin-bottom: 10px; border-radius: 5px; padding: 5px;")
            entry.setFixedHeight(30)
            quarter3_layout.addWidget(entry)

        # In Laws Detail in quarter 4
        inlaws_detail_label = QLabel("In Laws Detail")
        inlaws_detail_label.setStyleSheet("font-size: 16px; font-weight: bold; margin-top: 20px;")
        quarter4_layout.addWidget(inlaws_detail_label)

        for field in inlaws_fields:
            label = QLabel(f"{field}:")
            label.setStyleSheet("font-weight: bold;")
            quarter4_layout.addWidget(label)
            entry = QLineEdit()
            entry.setStyleSheet("margin-bottom: 10px; border-radius: 5px; padding: 5px;")
            entry.setFixedHeight(30)
            quarter4_layout.addWidget(entry)

        # Criminal Activities and General Remarks in quarter 4
        for activity in criminal_activities:
            label = QLabel(f"{activity}:")
            label.setStyleSheet("font-weight: bold;")
            quarter4_layout.addWidget(label)
            entry = QLineEdit()
            entry.setStyleSheet("margin-bottom: 10px; border-radius: 5px; padding: 5px;")
            entry.setFixedHeight(30)
            quarter4_layout.addWidget(entry)

        gen_remarks_label = QLabel("Gen Remarks:")
        gen_remarks_label.setStyleSheet("font-weight: bold;")
        quarter4_layout.addWidget(gen_remarks_label)
        gen_remarks_entry = QLineEdit()
        gen_remarks_entry.setStyleSheet("margin-bottom: 10px; border-radius: 5px; padding: 5px;")
        gen_remarks_entry.setFixedHeight(30)
        quarter4_layout.addWidget(gen_remarks_entry)

        # Right side layout for picture and buttons
        right_layout = QVBoxLayout()
        main_layout.addLayout(right_layout)

        # Picture display container
        self.picture_label = QLabel()
        self.picture_label.setFixedSize(200, 200)
        self.picture_label.setStyleSheet("border: 1px solid black;")
        right_layout.addWidget(self.picture_label)

        # Upload picture button
        upload_button = QPushButton("Upload Picture")
        upload_button.setStyleSheet("""
            QPushButton {
                background-color: #FFC107; 
                color: white; 
                padding: 10px; 
                border-radius: 5px;
            }
            QPushButton:hover {
                background-color: #FFB300;
            }
            QPushButton:pressed {
                background-color: #FFA000;
            }
        """)
        upload_button.clicked.connect(self.upload_picture)
        right_layout.addWidget(upload_button)

        # Buttons at the bottom in a vertical layout
        button_frame = QFrame()
        button_frame.setFrameShape(QFrame.StyledPanel)
        button_frame.setStyleSheet("border-radius: 15px;")
        button_layout = QVBoxLayout(button_frame)
        right_layout.addWidget(button_frame)

        save_button = QPushButton("Save Data")
        save_button.setStyleSheet("""
            QPushButton {
                background-color: #4CAF50; 
                color: white; 
                padding: 10px; 
                border-radius: 5px;
            }
            QPushButton:hover {
                background-color: #45A049;
            }
            QPushButton:pressed {
                background-color: #388E3C;
            }
        """)
        button_layout.addWidget(save_button)

        export_doc_button = QPushButton("Export as DOC")
        export_doc_button.setStyleSheet("""
            QPushButton {
                background-color: #2196F3; 
                color: white; 
                padding: 10px; 
                border-radius: 5px;
            }
            QPushButton:hover {
                background-color: #1E88E5;
            }
            QPushButton:pressed {
                background-color: #1976D2;
            }
        """)
        button_layout.addWidget(export_doc_button)

        export_pdf_button = QPushButton("Export as PDF")
        export_pdf_button.setStyleSheet("""
            QPushButton {
                background-color: #f44336; 
                color: white; 
                padding: 10px; 
                border-radius: 5px;
            }
            QPushButton:hover {
                background-color: #E53935;
            }
            QPushButton:pressed {
                background-color: #D32F2F;
            }
        """)
        button_layout.addWidget(export_pdf_button)

        # Add a vertical spacer to push the buttons to the top
        spacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)
        button_layout.addItem(spacer)

    def upload_picture(self):
        file_dialog = QFileDialog()
        file_path, _ = file_dialog.getOpenFileName(self, "Open Image File", "", "Image Files (*.png *.jpg *.bmp)")
        if file_path:
            pixmap = QPixmap(file_path)
            self.picture_label.setPixmap(pixmap.scaled(self.picture_label.size(), Qt.KeepAspectRatio, Qt.SmoothTransformation))

def open_low_down_page():
    app = QApplication([])
    window = LowDownPage()
    window.show()
    app.exec_()

open_low_down_page()