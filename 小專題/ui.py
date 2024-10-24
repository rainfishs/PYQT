# Form implementation generated from reading ui file '.\ui\main.ui'
#
# Created by: PyQt6 UI code generator 6.7.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 500)
        MainWindow.setMinimumSize(QtCore.QSize(800, 500))
        MainWindow.setMaximumSize(QtCore.QSize(800, 500))
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.clearUsbBtn = QtWidgets.QPushButton(parent=self.centralwidget)
        self.clearUsbBtn.setEnabled(True)
        self.clearUsbBtn.setGeometry(QtCore.QRect(110, 370, 191, 51))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Active, QtGui.QPalette.ColorRole.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(220, 1, 1))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Active, QtGui.QPalette.ColorRole.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Active, QtGui.QPalette.ColorRole.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Active, QtGui.QPalette.ColorRole.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(220, 1, 1))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Active, QtGui.QPalette.ColorRole.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(220, 1, 1))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Active, QtGui.QPalette.ColorRole.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Inactive, QtGui.QPalette.ColorRole.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(220, 1, 1))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Inactive, QtGui.QPalette.ColorRole.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Inactive, QtGui.QPalette.ColorRole.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Inactive, QtGui.QPalette.ColorRole.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(220, 1, 1))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Inactive, QtGui.QPalette.ColorRole.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(220, 1, 1))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Inactive, QtGui.QPalette.ColorRole.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Disabled, QtGui.QPalette.ColorRole.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(220, 1, 1))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Disabled, QtGui.QPalette.ColorRole.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Disabled, QtGui.QPalette.ColorRole.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Disabled, QtGui.QPalette.ColorRole.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(220, 1, 1))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Disabled, QtGui.QPalette.ColorRole.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(220, 1, 1))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Disabled, QtGui.QPalette.ColorRole.Window, brush)
        self.clearUsbBtn.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("等距更紗黑體 TC Xlight")
        font.setPointSize(25)
        self.clearUsbBtn.setFont(font)
        self.clearUsbBtn.setMouseTracking(False)
        self.clearUsbBtn.setStyleSheet("\n"
"QPushButton {\n"
"            background-color: rgb(220, 1, 1);     /* 靜態背景顏色 */\n"
"            color: rgb(255, 255, 255)\n"
"        }\n"
"        QPushButton:hover {\n"
"            background-color: rgb(255, 99, 60);        /* 懸浮時的背景顏色 */\n"
"            color: rgb(255, 255, 255)\n"
"        }\n"
"        QPushButton:pressed {\n"
"            background-color: rgb(229, 156, 9);    /* 按下時的背景顏色 */\n"
"            color: rgb(255, 255, 255)\n"
"        }")
        self.clearUsbBtn.setCheckable(False)
        self.clearUsbBtn.setObjectName("clearUsbBtn")
        self.line = QtWidgets.QFrame(parent=self.centralwidget)
        self.line.setGeometry(QtCore.QRect(60, 320, 301, 21))
        self.line.setFrameShape(QtWidgets.QFrame.Shape.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)
        self.line.setObjectName("line")
        self.widget = QtWidgets.QWidget(parent=self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(40, 20, 741, 228))
        self.widget.setObjectName("widget")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.widget)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label3 = QtWidgets.QLabel(parent=self.widget)
        font = QtGui.QFont()
        font.setFamily("等距更紗黑體 TC Xlight")
        font.setPointSize(24)
        self.label3.setFont(font)
        self.label3.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label3.setObjectName("label3")
        self.verticalLayout_2.addWidget(self.label3)
        spacerItem = QtWidgets.QSpacerItem(251, 68, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.verticalLayout_2.addItem(spacerItem)
        self.usbDriveList = QtWidgets.QListWidget(parent=self.widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.usbDriveList.sizePolicy().hasHeightForWidth())
        self.usbDriveList.setSizePolicy(sizePolicy)
        self.usbDriveList.setMinimumSize(QtCore.QSize(330, 150))
        font = QtGui.QFont()
        font.setPointSize(22)
        self.usbDriveList.setFont(font)
        self.usbDriveList.setObjectName("usbDriveList")
        self.verticalLayout_2.addWidget(self.usbDriveList)
        self.horizontalLayout_2.addLayout(self.verticalLayout_2)
        spacerItem1 = QtWidgets.QSpacerItem(178, 226, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem1)
        self.verticalLayout_5 = QtWidgets.QVBoxLayout()
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.label1 = QtWidgets.QLabel(parent=self.widget)
        font = QtGui.QFont()
        font.setFamily("等距更紗黑體 TC Xlight")
        font.setPointSize(24)
        self.label1.setFont(font)
        self.label1.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label1.setObjectName("label1")
        self.verticalLayout_5.addWidget(self.label1)
        spacerItem2 = QtWidgets.QSpacerItem(251, 68, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.verticalLayout_5.addItem(spacerItem2)
        self.grounpName = QtWidgets.QTextEdit(parent=self.widget)
        self.grounpName.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.grounpName.sizePolicy().hasHeightForWidth())
        self.grounpName.setSizePolicy(sizePolicy)
        self.grounpName.setMaximumSize(QtCore.QSize(250, 60))
        font = QtGui.QFont()
        font.setFamily("等距更紗黑體 TC Xlight")
        font.setPointSize(24)
        self.grounpName.setFont(font)
        self.grounpName.setAutoFillBackground(False)
        self.grounpName.setLineWrapMode(QtWidgets.QTextEdit.LineWrapMode.NoWrap)
        self.grounpName.setReadOnly(False)
        self.grounpName.setObjectName("grounpName")
        self.verticalLayout_5.addWidget(self.grounpName)
        spacerItem3 = QtWidgets.QSpacerItem(251, 68, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.verticalLayout_5.addItem(spacerItem3)
        self.startBackupBtn = QtWidgets.QPushButton(parent=self.widget)
        font = QtGui.QFont()
        font.setFamily("等距更紗黑體 TC Xlight")
        font.setPointSize(28)
        self.startBackupBtn.setFont(font)
        self.startBackupBtn.setMouseTracking(False)
        self.startBackupBtn.setStyleSheet("\n"
"QPushButton {\n"
"            background-color: lightgreen;     /* 靜態背景顏色 */\n"
"        }\n"
"        QPushButton:hover {\n"
"            background-color: rgb(15, 255, 247);        /* 懸浮時的背景顏色 */\n"
"        }\n"
"        QPushButton:pressed {\n"
"            background-color:rgb(19, 212, 255) ;    /* 按下時的背景顏色 */\n"
"        }")
        self.startBackupBtn.setObjectName("startBackupBtn")
        self.verticalLayout_5.addWidget(self.startBackupBtn)
        self.horizontalLayout_2.addLayout(self.verticalLayout_5)
        spacerItem4 = QtWidgets.QSpacerItem(178, 226, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem4)
        self.widget1 = QtWidgets.QWidget(parent=self.centralwidget)
        self.widget1.setGeometry(QtCore.QRect(380, 260, 402, 191))
        self.widget1.setObjectName("widget1")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.widget1)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.messageBox = QtWidgets.QTextEdit(parent=self.widget1)
        self.messageBox.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.messageBox.sizePolicy().hasHeightForWidth())
        self.messageBox.setSizePolicy(sizePolicy)
        self.messageBox.setMinimumSize(QtCore.QSize(400, 120))
        self.messageBox.setMaximumSize(QtCore.QSize(16777215, 120))
        font = QtGui.QFont()
        font.setFamily("等距更紗黑體 TC Xlight")
        font.setPointSize(18)
        self.messageBox.setFont(font)
        self.messageBox.setAutoFillBackground(False)
        self.messageBox.setLineWrapMode(QtWidgets.QTextEdit.LineWrapMode.NoWrap)
        self.messageBox.setReadOnly(True)
        self.messageBox.setObjectName("messageBox")
        self.verticalLayout_3.addWidget(self.messageBox)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.label2 = QtWidgets.QLabel(parent=self.widget1)
        font = QtGui.QFont()
        font.setFamily("等距更紗黑體 TC Xlight")
        font.setPointSize(16)
        self.label2.setFont(font)
        self.label2.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label2.setObjectName("label2")
        self.verticalLayout.addWidget(self.label2)
        self.labelTime = QtWidgets.QLabel(parent=self.widget1)
        font = QtGui.QFont()
        font.setFamily("等距更紗黑體 TC Xlight")
        font.setPointSize(16)
        self.labelTime.setFont(font)
        self.labelTime.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.labelTime.setObjectName("labelTime")
        self.verticalLayout.addWidget(self.labelTime)
        self.horizontalLayout.addLayout(self.verticalLayout)
        self.progressBar = QtWidgets.QProgressBar(parent=self.widget1)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.progressBar.sizePolicy().hasHeightForWidth())
        self.progressBar.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("微軟正黑體")
        font.setPointSize(13)
        self.progressBar.setFont(font)
        self.progressBar.setProperty("value", 24)
        self.progressBar.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.progressBar.setTextDirection(QtWidgets.QProgressBar.Direction.TopToBottom)
        self.progressBar.setObjectName("progressBar")
        self.horizontalLayout.addWidget(self.progressBar)
        self.verticalLayout_3.addLayout(self.horizontalLayout)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent=MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(parent=MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.clearUsbBtn.setText(_translate("MainWindow", "清空 USB"))
        self.label3.setText(_translate("MainWindow", "選擇 USB 儲存裝置"))
        self.label1.setText(_translate("MainWindow", "分類資料夾名稱"))
        self.startBackupBtn.setText(_translate("MainWindow", "開始備份"))
        self.label2.setText(_translate("MainWindow", "預測剩餘 | 已經經過"))
        self.labelTime.setText(_translate("MainWindow", "12:00 / 12:00"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())
