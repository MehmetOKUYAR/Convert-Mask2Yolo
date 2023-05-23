from PyQt5.QtWidgets import QApplication
from converter_codes import Converter

app = QApplication([])
window = Converter()
window.show()
app.exec_()