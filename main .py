print("""
▓█████  ███▄ ▄███▓ ▄▄▄       ██▓ ██▓                                 
▓█   ▀ ▓██▒▀█▀ ██▒▒████▄    ▓██▒▓██▒                                 
▒███   ▓██    ▓██░▒██  ▀█▄  ▒██▒▒██░                                 
▒▓█  ▄ ▒██    ▒██ ░██▄▄▄▄██ ░██░▒██░                                 
░▒████▒▒██▒   ░██▒ ▓█   ▓██▒░██░░██████▒                             
░░ ▒░ ░░ ▒░   ░  ░ ▒▒   ▓▒█░░▓  ░ ▒░▓  ░                             
 ░ ░  ░░  ░      ░  ▒   ▒▒ ░ ▒ ░░ ░ ▒  ░                             
   ░   ░      ░     ░   ▒    ▒ ░  ░ ░                                
   ░  ░       ░         ░  ░ ░      ░  ░                             
                                                                     
 ▄▄▄       ███▄    █  ▄▄▄       ██▓   ▓██   ██▓  ██████  ██▓  ██████ 
▒████▄     ██ ▀█   █ ▒████▄    ▓██▒    ▒██  ██▒▒██    ▒ ▓██▒▒██    ▒ 
▒██  ▀█▄  ▓██  ▀█ ██▒▒██  ▀█▄  ▒██░     ▒██ ██░░ ▓██▄   ▒██▒░ ▓██▄   
░██▄▄▄▄██ ▓██▒  ▐▌██▒░██▄▄▄▄██ ▒██░     ░ ▐██▓░  ▒   ██▒░██░  ▒   ██▒
 ▓█   ▓██▒▒██░   ▓██░ ▓█   ▓██▒░██████▒ ░ ██▒▓░▒██████▒▒░██░▒██████▒▒
 ▒▒   ▓▒█░░ ▒░   ▒ ▒  ▒▒   ▓▒█░░ ▒░▓  ░  ██▒▒▒ ▒ ▒▓▒ ▒ ░░▓  ▒ ▒▓▒ ▒ ░
  ▒   ▒▒ ░░ ░░   ░ ▒░  ▒   ▒▒ ░░ ░ ▒  ░▓██ ░▒░ ░ ░▒  ░ ░ ▒ ░░ ░▒  ░ ░
  ░   ▒      ░   ░ ░   ░   ▒     ░ ░   ▒ ▒ ░░  ░  ░  ░   ▒ ░░  ░  ░  
      ░  ░         ░       ░  ░    ░  ░░ ░           ░   ░        ░  
                                       ░ ░                             
""")

print("""
+-+-+-+-+ +-+-+ +-+-+-+-+-+-+-+-+-+-+-+
|m|a|d|e| |b|y| |H|A|C|K|E|R|O|R|8|2|8|
+-+-+-+-+ +-+-+ +-+-+-+-+-+-+-+-+-+-+-+
""")



import sys
import os
import re
from email.parser import BytesParser
from email import policy
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QPushButton
from PyQt5.QtGui import QPixmap

class SecureApplication(QApplication):
    def applicationSupportsSecureRestorableState(self):
        return True

def read_eml_file(file_path):
    try:
        with open(file_path, 'rb') as eml_file:
            # Parse the EML file
            msg = BytesParser(policy=policy.default).parse(eml_file)
            
            # Extract headers
            headers_text = ""
            for header_name, header_value in msg.items():
                headers_text += f"{header_name}: {header_value}\n"

            # Extract body
            body_text = ""
            if msg.is_multipart():
                for part in msg.walk():
                    content_type = part.get_content_type()
                    if content_type == 'text/plain':
                        body_text += part.get_payload(decode=True).decode(part.get_content_charset()) + "\n"
            else:
                body_text += msg.get_payload(decode=True).decode(msg.get_content_charset()) + "\n"

            return headers_text, body_text

    except FileNotFoundError:
        return "File not found.", ""
    except Exception as e:
        return "An error occurred: " + str(e), ""

def show_popup(file_path):
    app = SecureApplication(sys.argv)
    popup = QWidget()
    popup.setWindowTitle("EML File Viewer")

    layout = QVBoxLayout()

    headers_label = QLabel()
    body_label = QLabel()

    headers_text, body_text = read_eml_file(file_path)

    headers_label.setText(headers_text)
    body_label.setText(body_text)

    layout.addWidget(QLabel("Headers:"))
    layout.addWidget(headers_label)
    layout.addWidget(QLabel("Message Body:"))
    layout.addWidget(body_label)

    # Check if the keyword "EXPLOSION" is in the body
    if "EXPLOSION" in body_text:
        # If the keyword is found, display an explosion image
        explosion_label = QLabel()
        explosion_pixmap = QPixmap("explosion.gif")
        explosion_label.setPixmap(explosion_pixmap)
        layout.addWidget(explosion_label)

    button = QPushButton("Close")
    button.clicked.connect(popup.close)
    layout.addWidget(button)

    popup.setLayout(layout)
    popup.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    file_path = input("Enter the file path: ")
    file_path = rf"{file_path}"
    if os.path.isfile(file_path):
        show_popup(file_path)
    else:
        print("File not found.")
