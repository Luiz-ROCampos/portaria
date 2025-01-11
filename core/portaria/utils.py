from PySide6.QtWidgets import QMainWindow, QMenu, QWidget, QMessageBox

#******************** Mensagens ********************
def mensagem(titulo, mensagens):
    msg = QMessageBox()
    msg.setIcon(QMessageBox.Warning)
    msg.setWindowTitle(titulo)
    msg.setText(mensagens)
    msg.exec_()

def mensagem_sucesso(titulo, mensagens):
    msg = QMessageBox()
    msg.setIcon(QMessageBox.Information)
    msg.setWindowTitle(titulo)
    msg.setText(mensagens)
    msg.exec_()
