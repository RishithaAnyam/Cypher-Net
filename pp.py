import sys
import csv
import subprocess
import time
from PyQt5.QtWidgets import QApplication, QMainWindow, QSplashScreen, QWidget, QPushButton, QTextEdit, QVBoxLayout, QMessageBox, QGridLayout, QLabel
from PyQt5.QtGui import QFont, QPixmap, QPalette, QImage, QBrush
from PyQt5.QtCore import Qt, QTimer

class AnimationWindow:
    def __init__(self):
        self.app = QApplication(sys.argv)
        self.app.setStyleSheet("QPushButton{font-size: 14pt;}")
        splash_pixmap = QPixmap(r"loading screen2.jpg")
        self.splash = QSplashScreen(splash_pixmap, Qt.WindowStaysOnTopHint)
        self.splash.setMask(splash_pixmap.mask())
        self.splash.show()

        # Simulate a loading delay (you can replace this with your actual loading process)
        QTimer.singleShot(1691, self.load) 
    def load(self):
        self.window = QMainWindow()
        self.window.setWindowTitle("Authentication")
        self.window.setGeometry(100, 100, 1800, 1200)
        # Load your custom background image here
        background_image = QImage(r"authentication.jpg")
        background_image = background_image.scaled(1950, 1000)  # Scale to match window size
        palette = QPalette()
        palette.setBrush(QPalette.Background, QBrush(background_image))
        self.window.setPalette(palette)

        self.central_widget = QWidget()
        self.window.setCentralWidget(self.central_widget)

        self.create()
    def create(self):
        layout = QVBoxLayout()

        grid_layout = QVBoxLayout()
        lp_button = QPushButton("Login")
        lp_button.setFont(QFont("Arial", 18))
        lp_button.clicked.connect(self.open_login)
        lp_button.setStyleSheet("background-color: rgba(0, 0, 0, 0); color: white; border: 2px solid white; padding: 10px; text-align: center;")
        lp_button.setCursor(Qt.PointingHandCursor)  
        lp_button.setObjectName("login_button")
        lp_button.adjustSize()
        grid_layout.addWidget(lp_button)

        reg_button = QPushButton("Register")
        reg_button.setFont(QFont("Arial", 18))
        reg_button.clicked.connect(self.open_register)
        reg_button.setStyleSheet("background-color: rgba(0, 0, 0, 0); color: white; border: 2px solid white; padding: 10px; text-align: center;")
        reg_button.setCursor(Qt.PointingHandCursor)  # Change cursor on hover
        reg_button.setObjectName("register_button")
        lp_button.adjustSize()
        grid_layout.addWidget(reg_button)

        grid_layout.setSpacing(40)
        
        

        layout.addLayout(grid_layout)
        self.central_widget.setLayout(layout)
        
    
        self.window.closeEvent = self.confirm_quit
        
        self.window.show()
    def open_login(self):
        self.lp_window = QMainWindow()
        self.lp_window.setWindowTitle("Login Page")
        self.lp_window.setGeometry(200, 200, 500, 500)

        central_widget = QWidget()
        self.lp_window.setCentralWidget(central_widget)

        layout = QVBoxLayout()
        self.label1=QLabel()
        self.label1.setText("Enter user name:")
        self.label1.resize(2,10)
        layout.addWidget(self.label1)
        self.name_entry = QTextEdit()
        self.name_entry.resize(280,40)
        layout.addWidget(self.name_entry)
        self.label2=QLabel()
        self.label2.setText("Enter password:")
        self.label2.resize(2,10)
        layout.addWidget(self.label2)
        self.post_entry = QTextEdit()
        layout.addWidget(self.post_entry)

        create_button = QPushButton("login")
        create_button.clicked.connect(self.readfile)
        layout.addWidget(create_button)

        clear_button = QPushButton("Clear")
        clear_button.clicked.connect(self.clear_fields)
        layout.addWidget(clear_button)

        central_widget.setLayout(layout)

        self.lp_window.show()

    def readfile(self):
        name = self.name_entry.toPlainText()  # Use toPlainText() to get text
        post = self.post_entry.toPlainText()
        c=0
        with open("users.txt","r") as file:
            file_reader = csv.reader(file)
            for i in file_reader:
                if i[0]==name:
                    us=[i[0],i[1]]
                    if us[1]==post:
                        c=1
                        break
        if c==1:
            QMessageBox.information(self.lp_window,"login is successful","you are an authenticated user!")
            self.load_main_window()
        else:
            QMessageBox.information(self.lp_window,"error","error in username/password")
            self.clear_fields()

    def clear_fields(self):
        self.name_entry.clear()
        self.post_entry.clear()

    def open_register(self):
        self.reg_window = QMainWindow()
        self.reg_window.setWindowTitle("Registration Page")
        self.reg_window.setGeometry(200, 200, 500, 500)

        central_widget = QWidget()
        self.reg_window.setCentralWidget(central_widget)

        layout = QVBoxLayout()
        self.label1=QLabel()
        self.label1.setText("Enter user name:")
        layout.addWidget(self.label1)
        self.name_entry = QTextEdit()
        layout.addWidget(self.name_entry)
        self.label2=QLabel()
        self.label2.setText("Enter password:")
        layout.addWidget(self.label2)

        self.post_entry = QTextEdit()
        layout.addWidget(self.post_entry)

        create_button = QPushButton("register")
        create_button.clicked.connect(self.savefile)
        layout.addWidget(create_button)

        clear_button = QPushButton("Clear")
        clear_button.clicked.connect(self.clear_fields)
        layout.addWidget(clear_button)
        back_button = QPushButton("Back")
        back_button.clicked.connect(self.load)
        layout.addWidget(back_button)

        central_widget.setLayout(layout)

        self.reg_window.show()
    def savefile(self,):
        name = self.name_entry.toPlainText()  # Use toPlainText() to get text
        post = self.post_entry.toPlainText()
        file_path = "users.txt"
        with open(file_path, "a") as file:
            file.write(f"{name},{post}\n")
        QMessageBox.information(self.lp_window,"Registration is successful","Registration  done successfully")
    def load_main_window(self):
        self.window = QMainWindow()
        self.window.setWindowTitle("CIPHER NET")
        self.window.setGeometry(100, 100, 1800, 1200)
      

        # Load your custom background image here
        background_image = QImage(r"homepage.png")
        background_image = background_image.scaled(1950, 1000)  # Scale to match window size
        palette = QPalette()
        palette.setBrush(QPalette.Background, QBrush(background_image))
        self.window.setPalette(palette)

        self.central_widget = QWidget()
        self.window.setCentralWidget(self.central_widget)

        self.create_main_window()

    def create_main_window(self):
        layout = QVBoxLayout()

        grid_layout = QGridLayout()
        community_post_button = QPushButton("Community Post")
        community_post_button.setFont(QFont("Arial", 18))
        community_post_button.clicked.connect(self.open_community_post)
        community_post_button.setStyleSheet("background-color: rgba(0, 0, 0, 0); color: white; border: 2px solid white; padding: 10px; text-align: center;")
        community_post_button.setCursor(Qt.PointingHandCursor)  
        community_post_button.setObjectName("community_button")
        grid_layout.addWidget(community_post_button, 0, 0, 1, 1, Qt.AlignLeft)

        toolkit_button = QPushButton("Toolkit")
        toolkit_button.setFont(QFont("Arial", 18))
        toolkit_button.clicked.connect(self.open_toolkit)
        toolkit_button.setStyleSheet("background-color: rgba(0, 0, 0, 0); color: white; border: 2px solid white; padding: 10px; text-align: center;")
        toolkit_button.setCursor(Qt.PointingHandCursor)  # Change cursor on hover
        toolkit_button.setObjectName("toolkit_button")
        grid_layout.addWidget(toolkit_button, 1, 0, 1, 1, Qt.AlignLeft)
        grid_layout.setSpacing(40)
        
        

        layout.addLayout(grid_layout)
        self.central_widget.setLayout(layout)
        
    
        self.window.closeEvent = self.confirm_quit
        
        self.window.show()
        
    def confirm_quit(self, event):
        confirm = QMessageBox.question(self.window, 'Exit Confirmation', 'Are you sure you want to quit?',
                                       QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        if confirm == QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()



    def open_community_post(self):
        self.community_post_window = QMainWindow()
        self.community_post_window.setWindowTitle("Community Post(beta)")
        self.community_post_window.setGeometry(100, 100, 400, 300)

        central_widget = QWidget()
        self.community_post_window.setCentralWidget(central_widget)

        layout = QVBoxLayout()

        self.name_entry = QTextEdit()
        layout.addWidget(self.name_entry)

        self.post_entry = QTextEdit()
        layout.addWidget(self.post_entry)

        create_button = QPushButton("Create Post")
        create_button.clicked.connect(self.create_post)
        layout.addWidget(create_button)

        read_button = QPushButton("Read Post")
        read_button.clicked.connect(self.read_post)
        layout.addWidget(read_button)

        clear_button = QPushButton("Clear Fields")
        clear_button.clicked.connect(self.clear_fields)
        layout.addWidget(clear_button)

        central_widget.setLayout(layout)

        self.community_post_window.show()

    def create_post(self):
        name = self.name_entry.toPlainText()  # Use toPlainText() to get text
        post = self.post_entry.toPlainText()
        if name and post:
            self.save_post(name, post)
            QMessageBox.information(self.community_post_window, "Success", "Post created and saved successfully.")
            self.clear_fields()
        else:
            QMessageBox.critical(self.community_post_window, "Error", "Please enter both name and post.")

    def save_post(self, name, post):
        file_path = "community_posts.txt"
        with open(file_path, "a") as file:
            file.write(f"Name: {name}\n")
            file.write(f"Post: {post}\n\n")

    def read_post(self):
        file_path = "community_posts.txt"
        with open(file_path, "r") as file:
            self.post_entry.setPlainText(file.read())  # Set text using setPlainText

    def clear_fields(self):
        self.name_entry.clear()
        self.post_entry.clear()

    def open_toolkit(self):
        self.toolkit_window = QMainWindow()
        self.toolkit_window.setWindowTitle("Toolkit")
        self.toolkit_window.setGeometry(100, 100, 600, 400)
        
        background_image = QPixmap(r"toolkit back.jpg")
        background_image = background_image.scaled(1900, 900)
        palette = QPalette()
        palette.setBrush(QPalette.Background, QBrush(background_image))
        self.toolkit_window.setPalette(palette)
        
        central_widget = QWidget()
        self.toolkit_window.setCentralWidget(central_widget)

        layout = QVBoxLayout()
        layout.setAlignment(Qt.AlignCenter)

        password_manager_button = QPushButton("Password Manager")
        password_manager_button.setFont(QFont("Arial", 14))
        password_manager_button.clicked.connect(self.password_manager)
        password_manager_button.setStyleSheet("background-color: #5733FF; color: white; border: none; padding: 10px; text-align: center;")
        password_manager_button.setCursor(Qt.PointingHandCursor)  # Change cursor on hover
        password_manager_button.setObjectName("Password Manager")
        layout.addWidget(password_manager_button)

        password_generator_button = QPushButton("Password Generator")
        password_generator_button.setFont(QFont("Arial", 14))
        password_generator_button.clicked.connect(self.password_generator)
        password_generator_button.setStyleSheet("background-color: #5733FF; color: white; border: none; padding: 10px; text-align: center;")
        password_generator_button.setCursor(Qt.PointingHandCursor)  # Change cursor on hover
        password_generator_button.setObjectName("Password Generator")
        layout.addWidget(password_generator_button)

        password_strength_checker_button = QPushButton("Password Strength Checker")
        password_strength_checker_button.setFont(QFont("Arial", 14))
        password_strength_checker_button.clicked.connect(self.password_strength_checker)
        password_strength_checker_button.setStyleSheet("background-color: #5733FF; color: white; border: none; padding: 10px; text-align: center;")
        password_strength_checker_button.setCursor(Qt.PointingHandCursor)  # Change cursor on hover
        password_strength_checker_button.setObjectName("Password Strength Checker")
        layout.addWidget(password_strength_checker_button)

        ip_lookup_button = QPushButton("IP Lookup")
        ip_lookup_button.setFont(QFont("Arial", 14))
        ip_lookup_button.clicked.connect(self.ip_look)
        ip_lookup_button.setStyleSheet("background-color: #5733FF; color: white; border: none; padding: 10px; text-align: center;")
        ip_lookup_button.setCursor(Qt.PointingHandCursor)  # Change cursor on hover
        ip_lookup_button.setObjectName("IP Lookup")
        layout.addWidget(ip_lookup_button)

        encryption_decryption_button = QPushButton("Encryption/Decryption")
        encryption_decryption_button.setFont(QFont("Arial", 14))
        encryption_decryption_button.clicked.connect(self.encryption_decryption)
        encryption_decryption_button.setStyleSheet("background-color: #5733FF; color: white; border: none; padding: 10px; text-align: center;")
        encryption_decryption_button.setCursor(Qt.PointingHandCursor)  # Change cursor on hover
        encryption_decryption_button.setObjectName("Encryption/Decryption")
        layout.addWidget(encryption_decryption_button)

        back_button = QPushButton("Back")
        back_button.setFont(QFont("Arial", 14))
        back_button.clicked.connect(self.toolkit_window.close)
        back_button.setStyleSheet("background-color: #000000; color: white; border: none; padding: 10px; text-align: center;")
        back_button.setCursor(Qt.PointingHandCursor)  # Change cursor on hover
        back_button.setObjectName("Back")
        layout.addWidget(back_button)

        central_widget.setLayout(layout)
        

        self.toolkit_window.show()

    def password_manager(self):
        subprocess.Popen(["python", r"password_manager.py"])

    def password_generator(self):
        subprocess.Popen(["python", r"password_generator.py"])

    def password_strength_checker(self):
        subprocess.Popen(["python", r"password_strength.py"])

    def ip_look(self):
        subprocess.Popen(["python", r"ip_lookup_latest.py"])

    def encryption_decryption(self):
        subprocess.Popen(["python", r"encry_decry.py"])

    def run(self):
        sys.exit(self.app.exec_())
if __name__ == "__main__":
    app = AnimationWindow()
    app.run()

