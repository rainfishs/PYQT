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
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.messageBox = QtWidgets.QTextEdit(parent=self.centralwidget)
        self.messageBox.setEnabled(True)
        self.messageBox.setGeometry(QtCore.QRect(30, 20, 391, 201))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.messageBox.sizePolicy().hasHeightForWidth())
        self.messageBox.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("等距更紗黑體 TC Xlight")
        font.setPointSize(20)
        self.messageBox.setFont(font)
        self.messageBox.setAutoFillBackground(False)
        self.messageBox.setLineWrapMode(QtWidgets.QTextEdit.LineWrapMode.NoWrap)
        self.messageBox.setReadOnly(True)
        self.messageBox.setObjectName("messageBox")
        self.usbDriveList = QtWidgets.QListWidget(parent=self.centralwidget)
        self.usbDriveList.setGeometry(QtCore.QRect(30, 240, 391, 192))
        font = QtGui.QFont()
        font.setPointSize(22)
        self.usbDriveList.setFont(font)
        self.usbDriveList.setObjectName("usbDriveList")
        self.layoutWidget = QtWidgets.QWidget(parent=self.centralwidget)
        self.layoutWidget.setGeometry(QtCore.QRect(490, 60, 256, 288))
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout()
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.label1 = QtWidgets.QLabel(parent=self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("等距更紗黑體 TC Xlight")
        font.setPointSize(26)
        self.label1.setFont(font)
        self.label1.setObjectName("label1")
        self.verticalLayout_5.addWidget(self.label1)
        self.grounpName = QtWidgets.QTextEdit(parent=self.layoutWidget)
        self.grounpName.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.grounpName.sizePolicy().hasHeightForWidth())
        self.grounpName.setSizePolicy(sizePolicy)
        self.grounpName.setMaximumSize(QtCore.QSize(250, 60))
        font = QtGui.QFont()
        font.setFamily("等距更紗黑體 TC Xlight")
        font.setPointSize(26)
        self.grounpName.setFont(font)
        self.grounpName.setAutoFillBackground(False)
        self.grounpName.setLineWrapMode(QtWidgets.QTextEdit.LineWrapMode.NoWrap)
        self.grounpName.setReadOnly(False)
        self.grounpName.setObjectName("grounpName")
        self.verticalLayout_5.addWidget(self.grounpName)
        self.verticalLayout_6.addLayout(self.verticalLayout_5)
        spacerItem = QtWidgets.QSpacerItem(28, 108, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.verticalLayout_6.addItem(spacerItem)
        self.startBackupBtn = QtWidgets.QPushButton(parent=self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("等距更紗黑體 TC Xlight")
        font.setPointSize(28)
        self.startBackupBtn.setFont(font)
        self.startBackupBtn.setObjectName("startBackupBtn")
        self.verticalLayout_6.addWidget(self.startBackupBtn)
        self.widget = QtWidgets.QWidget(parent=self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(430, 370, 361, 62))
        self.widget.setObjectName("widget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.widget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.label2 = QtWidgets.QLabel(parent=self.widget)
        font = QtGui.QFont()
        font.setFamily("等距更紗黑體 TC Xlight")
        font.setPointSize(16)
        self.label2.setFont(font)
        self.label2.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label2.setObjectName("label2")
        self.verticalLayout.addWidget(self.label2)
        self.labelTime = QtWidgets.QLabel(parent=self.widget)
        font = QtGui.QFont()
        font.setFamily("等距更紗黑體 TC Xlight")
        font.setPointSize(16)
        self.labelTime.setFont(font)
        self.labelTime.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.labelTime.setObjectName("labelTime")
        self.verticalLayout.addWidget(self.labelTime)
        self.horizontalLayout.addLayout(self.verticalLayout)
        self.progressBar = QtWidgets.QProgressBar(parent=self.widget)
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
        self.progressBar.setObjectName("progressBar")
        self.horizontalLayout.addWidget(self.progressBar)
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
