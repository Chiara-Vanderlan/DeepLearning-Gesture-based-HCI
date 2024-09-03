import sys
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QMainWindow, QApplication
from PyQt6.QtGui import QIcon
from PyQt6.QtCore import QTimer

import Tray_rc
from Tray import Ui_MainWindow as Ui_MinimizeTray

from SystemTrayChange import TraySelection, Auto_Manual_Selection, Dynamic_Static_Selection

sys.path.append('../10_Storage_and_utils')
from Payload import Payload

sys.path.append('../5_Mode_Selector')
from Mode_toggler import mode_toggler

payload = Payload()

class MinimizeWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MinimizeTray()
        self.ui.setupUi(self)

        # Hide the title bar
        self.setWindowFlags(Qt.WindowType.FramelessWindowHint)
        # Make the window draggable
        self.setAttribute(Qt.WidgetAttribute.WA_TranslucentBackground)
        self.dragPosition = None

        # Connect buttons to their respective slots
        self.ui.Close.clicked.connect(self.close)
        self.ui.Maximize.clicked.connect(self.open_main_window)
        self.main_window = None

        # Set the window icon
        self.setWindowIcon(QIcon('SystemTray/logo.png'))

        # Calling AutoMode ManualMode Button
        self.set_checkbox_state(self.ui.checkBox, Auto_Manual_Selection(payload.get_mode()))

        # Calling AutoMode ManualMode Button
        self.set_checkbox_state(self.ui.checkBox_2, Dynamic_Static_Selection(payload.get_gesture_type()))

        #Calling the system bar
        self.show_pages()

        #Binding
        self.ui.checkBox_2.stateChanged.connect(self.Static_Dynamic_Switch)
        self.ui.checkBox.stateChanged.connect(self.Auto_Manual_Switch)

    def Static_Dynamic_Switch(self):
        payload = Payload()
        current_gesture_type = payload.get_gesture_type()
        if current_gesture_type == 1:
            new_gesture_type = 2
            payload.set_gesture_type(new_gesture_type)
        else:
            new_gesture_type = 1
            payload.set_gesture_type(new_gesture_type)

    def Auto_Manual_Switch(self):
        payload = Payload()
        current_mode = payload.get_mode()
        if current_mode == 1:
            new_mode = 2
            payload.set_mode(new_mode)
        else:
            new_mode = 1
            payload.set_mode(new_mode)

    # Code to connect another window
    def open_main_window(self):
        from UI_main import MainWindow
        if self.main_window is None:
            self.main_window = MainWindow()
        self.set_AutoManual_state(payload.get_mode())
        self.set_StaticDynamic_state(payload.get_gesture_type())
        self.main_window.show()
        self.close()

    def set_AutoManual_state(self, value):
        Auto_Button = self.main_window.Get_Auto_Button()
        Manual_Button = self.main_window.Get_Manual_Button()

        # 0- Auto 1-Manual
        if value == 2:
            Auto_Button.setChecked(True)
            Manual_Button.setChecked(False)
        elif value == 1:
            Auto_Button.setChecked(False)
            Manual_Button.setChecked(True)

    def set_StaticDynamic_state(self, value):

        Static_Button = self.main_window.Get_Static_Button()
        Dynamic_Button = self.main_window.Get_Dynamic_Button()

        # 1- Static 2-Dynamic
        if value == 1:
            Static_Button.setChecked(True)
            Dynamic_Button.setChecked(False)
        elif value == 2:
            Static_Button.setChecked(False)
            Dynamic_Button.setChecked(True)

    def show_pages(self):
        # Initial
        self.ui.stackedWidget.setCurrentIndex(7)
        # after 2s
        payload = Payload()
        gesture_type = payload.get_gesture_type()
        mode = payload.get_mode()
        application = payload.get_application()
        QTimer.singleShot(2000, lambda: self.change_to_desired_tray(self.give_desired_tray_num(gesture_type, mode, 2)))

    def give_desired_tray_num(self, gesture_type, mode, application):
        return TraySelection(gesture_type, mode, application)

    def change_to_desired_tray(self, key):
        self.ui.stackedWidget.setCurrentIndex(key)

    # Code to window Draggable
    def mousePressEvent(self, event):
        if event.button() == Qt.MouseButton.LeftButton:
            self.dragPosition = event.globalPosition().toPoint() - self.frameGeometry().topLeft()
            event.accept()

    def mouseMoveEvent(self, event):
        if event.buttons() & Qt.MouseButton.LeftButton:
            if self.dragPosition is not None:
                self.move(event.globalPosition().toPoint() - self.dragPosition)
                event.accept()

    def mouseReleaseEvent(self, event):
        if event.button() == Qt.MouseButton.LeftButton:
            self.dragPosition = None
            event.accept()

    def set_checkbox_state(self, checkbox, checked):
        checkbox.setChecked(checked)

# Execute App
if __name__ =="__main__":
    app = QApplication(sys.argv)
    window = MinimizeWindow()
    window.show()
    sys.exit(app.exec())
