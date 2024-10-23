import ctypes
import datetime
import os
import time

import config
from PyQt6.QtCore import QObject, QRunnable, QThreadPool, QTimer, pyqtSignal
from PyQt6.QtWidgets import QApplication, QMainWindow
from ui import Ui_MainWindow


class WorkerSignals(QObject):
    finished = pyqtSignal()
    progress = pyqtSignal(int)


class BackupRunnable(QRunnable):
    def __init__(self, source, destination):
        super().__init__()
        self.source = source
        self.destination = destination
        self.signals = WorkerSignals()

    def run(self):
        # 這裡放置您的備份邏輯
        for i in range(10):
            time.sleep(1)  # 模擬耗時操作
            self.signals.progress.emit((i + 1) * 10)
        self.signals.finished.emit()


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

        # widget setting
        self.startBackupBtn.setEnabled(False)
        self.grounpName.setText(config.BACKUP_GROUP_DEFAULT)
        self.progressBar.hide()
        self.labelTime.hide()
        self.label2.hide()

        # timer
        self.usbeventloop = QTimer()
        self.usbeventloop.timeout.connect(self.update_usb)
        self.usbeventloop.start(1000)

        # widget callback binding
        self.startBackupBtn.clicked.disconnect()
        self.usbDriveList.itemClicked.disconnect()
        self.startBackupBtn.clicked.connect(self.on_startBackupBtn_clicked)
        self.usbDriveList.itemClicked.connect(self.on_usbDriveList_itemClicked)
        self.grounpName.textChanged.connect(self.on_grounpName_textChanged)

    # 開始備份 callback
    def on_startBackupBtn_clicked(self):
        # 取得選擇的 USB Driver
        source = self.usbDriveList.currentItem().text().split(" ")[0]
        # 判斷根目錄是相對路徑還是絕對路徑
        destination = os.getcwd()
        if config.BACKUP_PATH[0] == ".":
            destination = os.path.join(destination, config.BACKUP_PATH[1:])
        destination = os.path.join(destination, config.BACKUP_GROUP_DEFAULT)
        print(source, destination)
        # 驗證兩個路徑都合法
        try:
            os.stat(source)
            os.stat(destination)
        except Exception as e:
            print(e)
            return
        # 儲存路徑不存在則創建
        if not os.path.exists(destination):
            os.makedirs(destination)
        # 創建 BackupRunnable 實例
        backup_task = BackupRunnable(source, destination)
        backup_task.signals.finished.connect(self.on_backup_finished)
        backup_task.signals.progress.connect(self.update_progress)

        # 加入線程池
        self.threadpool.start(backup_task)

        # 禁用按鈕，防止重複點擊
        self.isprogress = True
        self.isBackupBtnEnable()
        self.messageBox.setText(
            "開始備份！ \t" + datetime.datetime.now().strftime("%H:%M:%S %Y-%m-%d")
        )

        self.progressBar.show()
        self.labelTime.show()
        self.label2.show()
        self.progressBar.setValue(0)
        self.labelTime.setText("00:00:00 / 00:00:00")  # 剩餘時間 / 經過時間
        self.startprogresstime = time.time()

    def on_backup_finished(self):
        self.isprogress = False
        self.isBackupBtnEnable()
        # self.messageBox.setText("檔案備份完成！")
        self.messageBox.append(
            "檔案備份完成！ \t" + datetime.datetime.now().strftime("%H:%M:%S %Y-%m-%d")
        )

    def update_progress(self, value):
        self.progressBar.setValue(value)
        # print(f"備份進度: {value}%")
        self.messageBox.append(
            f"備份進度: {value}% \t"
            + datetime.datetime.now().strftime("%H:%M:%S %Y-%m-%d")
        )
        # 計算剩餘時間
        elapsedtime = int(time.time() - self.startprogresstime)
        remainingtime = int((100 - value) * elapsedtime / value)
        # self.labelTime.setText(
        #     f"{datetime.timedelta(seconds=remainingtime)} / {datetime.timedelta(seconds=elapsedtime)}"
        # )
        # format time
        self.labelTime.setText(
            f"{datetime.datetime.fromtimestamp(remainingtime, datetime.timezone.utc).strftime('%H:%M:%S')} / {datetime.datetime.fromtimestamp(elapsedtime, datetime.timezone.utc).strftime('%H:%M:%S')}"
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
            if not os.path.exists(self.usblist[i]):
                # 如果當前選擇的 USB Driver 被移除，則disable 開始備份按鈕
                if (
                    self.usbDriveList.currentItem().text().split(" ")[0]
                    == self.usblist[i]
                ):
                    self.isBackupBtnEnable()
                self.usblist.pop(i)
                self.usbDriveList.takeItem(i)
                break

    # 分類名稱變更事件
    def on_grounpName_textChanged(self):
        self.isBackupBtnEnable()


if __name__ == "__main__":
    import sys

    app = QApplication(sys.argv)
    MainWindow = Main()
    MainWindow.show()
    sys.exit(app.exec())
