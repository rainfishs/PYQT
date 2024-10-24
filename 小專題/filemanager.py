import datetime
import os
import re
import shutil

import config
from PyQt6.QtCore import QObject, QRunnable, pyqtSignal


def are_files_equal(file1, file2):
    stat1 = os.stat(file1)
    stat2 = os.stat(file2)
    return stat1.st_size == stat2.st_size and stat1.st_mtime == stat2.st_mtime


class WorkerSignals(QObject):
    finished = pyqtSignal()
    progress = pyqtSignal(float)
    other = pyqtSignal(str)


class BackupRunnable(QRunnable):
    def __init__(self, source, destination):
        super().__init__()
        self.source = source
        self.destination = destination
        self.signals = WorkerSignals()

    def run(self):
        # 先統計檔案數量
        file_count = 0
        for root, dirs, files in os.walk(self.source):
            file_count += len(files)
        self.signals.other.emit(f"檔案總數: {file_count}")
        # 開始備份
        i = 0
        target_folder = config.BACKUP_DIR_FORMAT.format(
            DATE=datetime.datetime.now().strftime(config.BACKUP_DATE_FORMAT)
        )
        target_folder = os.path.join(self.destination, target_folder)
        # 如果同日備份要建立新的資料夾
        if config.SAME_DAY_NEW_FOLDER and os.path.exists(target_folder):
            # 找出最後一個數字
            last_num = 0
            for folder in os.listdir(self.destination):
                if re.match(r"\d+$", folder):
                    num = int(folder)
                    if num > last_num:
                        last_num = num
            target_folder = f"{target_folder}_{last_num + 1}"

        for root, dirs, files in os.walk(self.source):
            for f in files:
                source_path = os.path.join(root, f)
                self.signals.other.emit(
                    f"正在備份:( {i+1} / {file_count} ) {source_path}"
                )
                # 目標資料夾 = config.BACKUP_DIR_FORMAT.format(DATE=datetime.datetime.now().strftime(config.BACKUP_DATE_FORMAT))
                # 目標位置 = self.destination(目標跟目錄) + 目標資料夾 + 相對路徑(含檔名)

                target_path = os.path.join(
                    target_folder,
                    os.path.relpath(source_path, self.source),
                )

                if not os.path.exists(os.path.dirname(target_path)):
                    os.makedirs(os.path.dirname(target_path))

                # if os.path.exists(target_path):
                #     if config.OVERWRITE_MODE:
                #         if config.OVERWRITE_SIMPLE_CHECK:
                #             source_stat = os.stat(source_path)
                #             target_stat = os.stat(target_path)
                #             if (
                #                 source_stat.st_size == target_stat.st_size
                #                 and source_stat.st_mtime == target_stat.st_mtime
                #             ):
                #                 # 檔案相同，不用備份
                #                 pass
                #             else:
                #                 # 覆蓋模式
                #                 shutil.copy2(source_path, target_path)
                #         else:
                #             # 覆蓋模式
                #             shutil.copy2(source_path, target_path)
                #     else:
                #         # 略過同名檔案
                #         pass
                # else:
                #     # 複製檔案
                #     shutil.copy2(source_path, target_path)
                a = os.path.exists(target_path)
                b = config.OVERWRITE_MODE
                c = config.OVERWRITE_SIMPLE_CHECK
                sp, tp = source_path, target_path
                # 不存在目標檔案
                if not a:
                    shutil.copy2(sp, tp)
                # 存在目標檔案 且 我要覆蓋 我不想檢查更多
                elif a and b and not c:
                    shutil.copy2(sp, tp)
                # 存在目標檔案 且 我要覆蓋 但 我想檢查如果檔案大小與修改時間相同就不覆蓋
                elif a and b and c and not are_files_equal(sp, tp):
                    shutil.copy2(sp, tp)
                i += 1
                print(i, file_count, i / file_count * 100)
                self.signals.progress.emit(i / file_count * 100)
        self.signals.finished.emit()

        # # 這裡放置您的備份邏輯
        # for i in range(10):
        #     time.sleep(1)  # 模擬耗時操作
        #     self.signals.progress.emit((i + 1) * 10)
        # self.signals.finished.emit()
