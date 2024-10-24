import ctypes
import datetime
import os
import sys
import time
from turtle import back

import config
from filemanager import BackupRunnable, UsbDeviceClear
from PyQt6.QtCore import QThreadPool, QTimer, pyqtSignal
from PyQt6.QtWidgets import QApplication, QMainWindow
from ui import Ui_MainWindow


class Main(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.initialize()

    def initialize(self):
        # memory data
        self.usblist = []
        self.threadpool = QThreadPool()
        self.isprogress = False
        self.startprogresstime = 0
        self.progressvalue = 0

        # widget setting
        self.startBackupBtn.setEnabled(False)
        self.grounpName.setText(config.BACKUP_GROUP_DEFAULT)
        self.progressBar.hide()
        self.labelTime.hide()
        self.label2.hide()
        self.clearUsbBtn.hide()

        # timer
        self.usbeventloop = QTimer()
        self.usbeventloop.timeout.connect(self.update_usb)
        self.usbeventloop.start(1000)
        self.nowtimeloop = QTimer()
        self.nowtimeloop.timeout.connect(self.update_time)

        # widget callback binding
        self.startBackupBtn.clicked.disconnect()
        self.usbDriveList.itemClicked.disconnect()
        self.clearUsbBtn.clicked.disconnect()
        self.startBackupBtn.clicked.connect(self.on_startBackupBtn_clicked)
        self.usbDriveList.itemClicked.connect(self.on_usbDriveList_itemClicked)
        self.grounpName.textChanged.connect(self.on_grounpName_textChanged)
        self.clearUsbBtn.clicked.connect(self.on_clearUsbBtn_clicked)

    # 開始備份 callback
    def on_startBackupBtn_clicked(self):
        # 取得選擇的 USB Driver
        source = self.usbDriveList.currentItem().text().split(" ")[0]
        # 判斷根目錄是相對路徑還是絕對路徑
        destination = os.getcwd()
        if config.BACKUP_PATH[0] == ".":
            destination = os.path.join(destination, config.BACKUP_PATH[1:])
        destination = os.path.join(destination, self.grounpName.toPlainText())
        print(source, destination)
        # 儲存路徑不存在則創建
        if not os.path.exists(destination):
            os.makedirs(destination)

        # 創建 BackupRunnable 實例
        backup_task = BackupRunnable(source, destination)
        backup_task.signals.finished.connect(self.on_backup_finished)
        backup_task.signals.progress.connect(self.update_progress)
        backup_task.signals.other.connect(self.statusBar().showMessage)
        # backup_task.signals.other.connect(self.messageBox.append)

        # 加入線程池
        self.threadpool.start(backup_task)

        # 禁用按鈕，防止重複點擊
        self.isprogress = True
        self.isBackupBtnEnable()
        self.messageBox.append(
            "開始備份！ \t" + datetime.datetime.now().strftime("%H:%M:%S %Y-%m-%d")
        )

        self.nowtimeloop.start(1000)

        self.progressBar.show()
        self.labelTime.show()
        self.label2.show()
        self.progressBar.setValue(0)
        self.labelTime.setText("00:00:00 / 00:00:00")  # 剩餘時間 / 經過時間
        self.startprogresstime = time.time()
        self.progressvalue = 0

    def on_backup_finished(self):
        self.isprogress = False
        self.isBackupBtnEnable()
        self.nowtimeloop.stop()
        # self.messageBox.setText("檔案備份完成！")
        self.messageBox.append(
            "備份完成！ \t" + datetime.datetime.now().strftime("%H:%M:%S %Y-%m-%d")
        )
        self.statusBar().showMessage("")
        self.clearUsbBtn.show()

    def update_progress(self, value):
        self.progressvalue = value
        self.progressBar.setValue(int(value))
        # print(f"備份進度: {value}%")
        # self.messageBox.append(
        #     f"備份進度: {value}% \t"
        #     + datetime.datetime.now().strftime("%H:%M:%S %Y-%m-%d")
        # )
        # 計算剩餘時間
        # elapsedtime = int(time.time() - self.startprogresstime)
        # remainingtime = int((100 - value) * elapsedtime / value)
        # self.labelTime.setText(
        #     f"{datetime.timedelta(seconds=remainingtime)} / {datetime.timedelta(seconds=elapsedtime)}"
        # )
        # format time
        # self.labelTime.setText(
        #     f"{datetime.datetime.fromtimestamp(remainingtime, datetime.timezone.utc).strftime('%H:%M:%S')} / {datetime.datetime.fromtimestamp(elapsedtime, datetime.timezone.utc).strftime('%H:%M:%S')}"
        # )

    def update_time(self):
        # 計算剩餘時間
        elapsedtime = int(time.time() - self.startprogresstime)
        remainingtime = int(
            (100 - self.progressvalue) * elapsedtime / self.progressvalue
        )
        self.labelTime.setText(
            f"{datetime.timedelta(seconds=remainingtime)} / {datetime.timedelta(seconds=elapsedtime)}"
        )

    # BackupBtn Enable 判斷
    def isBackupBtnEnable(self):
        condition = (
            self.usbDriveList.currentItem() is not None
            and self.grounpName.toPlainText() != ""
            and not self.isprogress
        )
        self.startBackupBtn.setEnabled(condition)

    # 選擇 USB Drive callback
    def on_usbDriveList_itemClicked(self, item):
        self.isBackupBtnEnable()
        self.messageBox.append(
            "已選擇 " + item.text() + "\n 請設定分類名稱，按下開始備份"
        )
        print(item.text())

    def update_usb(self):
        drives = ctypes.windll.kernel32.GetLogicalDrives()
        for i in range(26):
            mask = 1 << i
            if drives & mask:
                drive = chr(65 + i) + ":/"
                dtype = ctypes.windll.kernel32.GetDriveTypeW(drive)
                dname = ctypes.create_unicode_buffer(1024)
                ctypes.windll.kernel32.GetVolumeInformationW(
                    ctypes.c_wchar_p(drive),
                    dname,
                    ctypes.sizeof(dname),
                    None,
                    None,
                    None,
                    None,
                    0,
                )
                # print(dtype, drive, dname.value)
                if dtype == 2 and (drive not in self.usblist):
                    self.usblist.append(drive)
                    self.usbDriveList.addItem(drive + " " + dname.value)

        # 偵測移除 USB Driver
        for i in range(len(self.usblist)):
            ci = self.usbDriveList.currentItem()
            if not os.path.exists(self.usblist[i]) and ci is not None:
                # 如果當前選擇的 USB Driver 被移除，則disable 開始備份按鈕
                if ci.text().split(" ")[0] == self.usblist[i]:
                    self.startBackupBtn.setEnabled(False)
                self.usblist.pop(i)
                self.usbDriveList.takeItem(i)
                break

    # 分類名稱變更事件
    def on_grounpName_textChanged(self):
        self.isBackupBtnEnable()

    # 清除 USB 內容
    def on_clearUsbBtn_clicked(self):
        # 取得選擇的 USB Driver
        source = self.usbDriveList.currentItem().text().split(" ")[0]
        backtask = UsbDeviceClear(source)
        backtask.signals.finished.connect(self.on_clearUsb_finished)
        backtask.signals.other.connect(self.statusBar().showMessage)
        self.threadpool.start(backtask)
        self.clearUsbBtn.setEnabled(False)
        self.messageBox.append(
            "開始清除 USB 內容！ \t"
            + datetime.datetime.now().strftime("%H:%M:%S %Y-%m-%d")
        )

    def on_clearUsb_finished(self):
        self.clearUsbBtn.hide()
        self.messageBox.append(
            "清除 USB 內容完成！ \t"
            + datetime.datetime.now().strftime("%H:%M:%S %Y-%m-%d")
        )


import logging
import traceback

appdata = os.getenv("LOCALAPPDATA")
assert appdata is not None
log_dir = os.path.join(appdata, "Rainfish_USB_Backup")
os.makedirs(log_dir, exist_ok=True)
logging.basicConfig(
    filename=os.path.join(log_dir, "error.log"),
    level=logging.ERROR,
    filemode="a",
    encoding="utf-8",
    format="%(asctime)s - %(levelname)s - %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",  # 指定日期時間格式
)

erra = []


def exception_hook(exctype: type, value: BaseException, tb):
    exc = "".join(traceback.format_exception(exctype, value, tb))
    logging.error(f"未捕獲例外: {exc}")
    erra.append("發生未預期錯誤，請聯繫開發者")
    # traceback.print_exception(exctype, value, tb)


if __name__ == "__main__":
    sys.excepthook = exception_hook
    app = QApplication(sys.argv)
    MainWindow = Main()
    erra = MainWindow.messageBox
    MainWindow.show()
    sys.exit(app.exec())
