from PySide6.QtWidgets import QApplication
from index import Login
import sys

app = QApplication(sys.argv)
window = Login()
window.show()
app.exec()