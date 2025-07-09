# utils/helpers.py
from PyQt6.QtWidgets import QMessageBox
import logging

def show_success(message):
    msg_box = QMessageBox()
    msg_box.setIcon(QMessageBox.Icon.Information)
    msg_box.setText(message)
    msg_box.setWindowTitle("Sucesso")
    msg_box.exec()

def show_error(message):
    logging.error(message)
    msg_box = QMessageBox()
    msg_box.setIcon(QMessageBox.Icon.Critical)
    msg_box.setText(message)
    msg_box.setWindowTitle("Erro")
    msg_box.exec()

def safe_action(success_message):
    def decorator(func):
        def wrapper(*args, **kwargs):
            try:
                func(*args, **kwargs)
                show_success(success_message)
            except Exception as e:
                show_error(f"Erro: {e}")
        return wrapper
    return decorator
