import sys
from PyQt5.QWidgets import QLineEdit, QPushButton, QLabel, QApplication, QWidget, QMainWindow, QVBoxLayout

class App(QMainWindow):
    def __init__(self):
        super().__init__()
        
    def showText(self):
        self.label.setText(f"Tên của bạn là: {self.edit_text.getText()}")
    
    self.setWindowTitle("App")
    self.setGeometry(0,0,400,400)
    
    
    central_widget = QWidget()
    self.setCentralWidget(central_widget)
    
    self.edit_text = QLineEdit()    
    self.btn = QPushButton("Hiển thị")    
    self.label = QLabel()
    
    layout = QVBoxLayout()
    layout.addWidget(self.edit_text)
    layout.addWidget(self.btn)
    layout.addWidget(self.label)
    
    central_widget.setLayout(layout)
    
    self.btn.clicked.connect(showText)
    

def main():
    app = QApplication()
    new_app = App()
    new_app.show()
    sys.exit(app.exec())

if __name__ == "__main__":
   main()