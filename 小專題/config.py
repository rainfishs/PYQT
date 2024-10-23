"""
使用者設定
"""

BACKUP_PATH = ".Backup"
""" 備份根路徑 """

BACKUP_GROUP_DEFAULT = "記憶卡"  # ***常用設定***
""" 子資料夾預設名稱 """

BACKUP_DATE_FORMAT = "%Y_%m_%d"
""" 資料夾日期格式 """

BACKUP_DIR_FORMAT = "{DATE}"
""" 資料夾名稱格式 ex: backup_{DATE} """

SAME_DAY_NEW_FOLDER = True
"""同日備份是否要建立新的資料夾, 例如: .Backup/2021-01-01_1"""

OVERWRITE_MODE = False
"""覆蓋模式，和上面設定關聯。 True: 同名檔案覆蓋, False: 略過同名檔案"""

OVERWRITE_SIMPLE = True
"""覆蓋時是否簡易判斷檔案大小與修改時間，若檔案大小與修改時間相同則不覆蓋"""
