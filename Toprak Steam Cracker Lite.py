from PySide6.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QLabel, QPushButton, QLineEdit, QFileDialog, QMessageBox, QHBoxLayout, QFrame, QSizePolicy
)
from PySide6.QtCore import Qt, QUrl
from PySide6.QtGui import QFont, QDesktopServices, QIcon
import sys
import os
import subprocess
import zipfile
import shutil
import requests

DARK_BLACK_STYLE = '''
QWidget {
    background: #000000;
    color: #ffffff;
}
QLabel {
    color: #ffffff;
}
QLineEdit {
    border: 2px solid #333333;
    border-radius: 8px;
    padding: 8px 12px;
    font-size: 14px;
    background: #1a1a1a;
    color: #ffffff;
}
QPushButton {
    background: #333333;
    color: #ffffff;
    border-radius: 8px;
    padding: 8px 18px;
    font-size: 14px;
}
QPushButton:hover {
    background: #444444;
}
QMessageBox {
    background-color: #1a1a1a;
}
QMessageBox QLabel {
    color: #ffffff;
    font-size: 14px;
}
QMessageBox QPushButton {
    background: #333333;
    color: #ffffff;
    border-radius: 8px;
    padding: 6px 18px;
    font-size: 13px;
}
QMessageBox QPushButton:hover {
    background: #444444;
}
'''

class DragDropLabel(QLabel):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setText('Oyun dosyasını buraya sürükleyin veya seçin')
        self.setAlignment(Qt.AlignCenter)
        self.setStyleSheet('''
            QLabel {
                border: 3px dashed #333333;
                border-radius: 16px;
                background: #1a1a1a;
                color: #666666;
                font-size: 18px;
                padding: 40px;
                margin-top: 10px;
                margin-bottom: 10px;
            }
            QLabel:hover {
                background: #2a2a2a;
                color: #ffffff;
            }
        ''')
        self.setAcceptDrops(True)

    def dragEnterEvent(self, event):
        if event.mimeData().hasUrls():
            self.setStyleSheet(self.styleSheet() + 'background: #414450;')
            event.acceptProposedAction()
        else:
            event.ignore()

    def dragLeaveEvent(self, event):
        self.setStyleSheet(self.styleSheet().replace('background: #414450;', ''))

    def dropEvent(self, event):
        self.setStyleSheet(self.styleSheet().replace('background: #414450;', ''))
        if event.mimeData().hasUrls():
            for url in event.mimeData().urls():
                if url.toLocalFile().endswith('.zip'):
                    self.parent().process_zip(url.toLocalFile())

    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.parent().select_zip_file()

class SteamUploader(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Toprak Steam Cracker Lite')
        self.setMinimumSize(600, 530)
        self.setMaximumSize(16777215, 16777215)
        self._min_width = 600
        self._min_height = 530
        self.setStyleSheet(DARK_BLACK_STYLE)
        main_layout = QVBoxLayout()
        main_layout.setAlignment(Qt.AlignTop)
        main_layout.setContentsMargins(30, 30, 30, 30)
        main_layout.setSpacing(18)

        title = QLabel('Toprak Steam Cracker Lite')
        title.setFont(QFont('Segoe UI', 22, QFont.Bold))
        title.setAlignment(Qt.AlignCenter)
        title.setStyleSheet('color: #666666; margin-bottom: 0px;')
        title.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        main_layout.addWidget(title)

        desc = QLabel('Steam yolunu seçin ve ZIP dosyasını sürükleyip bırakın.\nOyun dosyaları steam klasörünüze aktarılır.')
        desc.setFont(QFont('Segoe UI', 11))
        desc.setAlignment(Qt.AlignCenter)
        desc.setStyleSheet('color: #cccccc; margin-bottom: 10px;')
        desc.setWordWrap(True)
        desc.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        desc.setMinimumHeight(50)
        main_layout.addWidget(desc)

        path_layout = QHBoxLayout()
        self.path_edit = QLineEdit()
        self.path_edit.setPlaceholderText('Steam klasörünü seçin...')
        self.path_edit.setMinimumWidth(200)
        self.path_edit.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        path_layout.addWidget(self.path_edit, stretch=3)
        self.browse_btn = QPushButton('Gözat')
        self.browse_btn.setSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        path_layout.addWidget(self.browse_btn, stretch=1)
        self.browse_btn.clicked.connect(self.select_steam_folder)
        main_layout.addLayout(path_layout)

        self.dragdrop_label = DragDropLabel(self)
        self.dragdrop_label.setMinimumHeight(120)
        self.dragdrop_label.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        main_layout.addWidget(self.dragdrop_label, stretch=2)

        self.restart_btn = QPushButton("Steam'i Yeniden Başlat")
        self.restart_btn.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        main_layout.addWidget(self.restart_btn)
        self.restart_btn.clicked.connect(self.restart_steam)

        button_layout = QHBoxLayout()
        discord_btn = QPushButton('Discord')
        discord_btn.setStyleSheet('''
            QPushButton {
                background: #1a1a1a;
                color: #cccccc;
                border-radius: 6px;
                padding: 6px 18px;
                font-size: 13px;
                border: 1px solid #333333;
            }
            QPushButton:hover {
                background: #2a2a2a;
                color: #ffffff;
            }
        ''')
        discord_btn.clicked.connect(lambda: QDesktopServices.openUrl(QUrl('https://discord.gg/DnFnsM8M')))
        button_layout.addWidget(discord_btn)

        github_btn = QPushButton('Github Repo')
        github_btn.setStyleSheet('''
            QPushButton {
                background: #1a1a1a;
                color: #cccccc;
                border-radius: 6px;
                padding: 6px 18px;
                font-size: 13px;
                border: 1px solid #333333;
            }
            QPushButton:hover {
                background: #2a2a2a;
                color: #ffffff;
            }
        ''')
        github_btn.clicked.connect(lambda: QDesktopServices.openUrl(QUrl('https://github.com/toprak1224')))
        button_layout.addWidget(github_btn)

        main_layout.addLayout(button_layout)

        # Version info label (bottom right, above footer)
        self.version_label = QLabel()
        self.version_label.setAlignment(Qt.AlignRight)
        self.version_label.setStyleSheet('color: #cccccc; font-size: 12px; margin-bottom: 2px;')
        self.version_label.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        main_layout.addWidget(self.version_label)

        footer = QLabel('made by Toprak')
        footer.setAlignment(Qt.AlignRight)
        footer.setStyleSheet('color: #888888; font-size: 11px; margin-top: 2px;')
        footer.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        main_layout.addWidget(footer)

        self.setLayout(main_layout)
        self.check_version()

    def check_version(self):
        import requests

        CURRENT_VERSION = "1.0.0"
        VERSION_URL = "https://raw.githubusercontent.com/marcellusdev2/SteamGameDownloader/refs/heads/main/version.txt"

        try:
            response = requests.get(VERSION_URL, timeout=5)
            if response.status_code == 200:
                latest_version = response.text.strip()
                if latest_version != CURRENT_VERSION:
                    self.version_label.setText(f"Yeni sürüm bulundu: v{latest_version}")
                    self.version_label.setStyleSheet('color: #ffb347; font-size: 12px; margin-bottom: 2px;')
                else:
                    self.version_label.setText(f"Güncel sürüm: v{CURRENT_VERSION}")
                    self.version_label.setStyleSheet('color: #cccccc; font-size: 12px; margin-bottom: 2px;')
            else:
                self.version_label.setText("Sürüm kontrolü başarısız")
                self.version_label.setStyleSheet('color: #ff6666; font-size: 12px; margin-bottom: 2px;')
        except Exception as e:
            self.version_label.setText("Sürüm kontrol hatası")
            self.version_label.setStyleSheet('color: #ff6666; font-size: 12px; margin-bottom: 2px;')

    def select_steam_folder(self):
        folder = QFileDialog.getExistingDirectory(self, 'Steam klasörünü seçin')
        if folder:
            self.path_edit.setText(folder)

    def select_zip_file(self):
        file, _ = QFileDialog.getOpenFileName(self, 'ZIP dosyası seçin', '', 'ZIP Dosyası (*.zip)')
        if file:
            self.process_zip(file)

    def show_info(self, title, message):
        msg = QMessageBox(self)
        msg.setWindowTitle(title)
        msg.setText(message)
        msg.setIcon(QMessageBox.Information)
        msg.setStyleSheet(DARK_BLACK_STYLE)
        msg.exec()

    def process_zip(self, zip_path):
        import zipfile
        import shutil
        import requests
        steam_path = self.path_edit.text().strip()
        if not steam_path:
            self.show_info('Hata', 'Lütfen önce Steam klasörünü seçin!')
            return
        stplugin_dir = os.path.join(steam_path, 'config', 'stplug-in')
        depotcache_dir = os.path.join(steam_path, 'config', 'depotcache')
        os.makedirs(stplugin_dir, exist_ok=True)
        os.makedirs(depotcache_dir, exist_ok=True)
        try:
            game_id = os.path.splitext(os.path.basename(zip_path))[0]
            if not game_id.isdigit():
                self.show_info('Hata', 'ZIP dosyasının adı bir AppID (sayı) olmalı!')
                return
            api_url = f'https://store.steampowered.com/api/appdetails?appids={game_id}'
            dlc_ids = []
            try:
                response = requests.get(api_url, timeout=5)
                data = response.json()
                dlc_ids = data.get(game_id, {}).get('data', {}).get('dlc', [])
                if not isinstance(dlc_ids, list):
                    dlc_ids = []
            except Exception as e:
                dlc_ids = []
            with zipfile.ZipFile(zip_path, 'r') as zip_ref:
                lua_count = 0
                manifest_count = 0
                for file in zip_ref.namelist():
                    if file.endswith('.lua'):
                        target = os.path.join(stplugin_dir, os.path.basename(file))
                        with zip_ref.open(file) as src, open(target, 'wb') as dst:
                            shutil.copyfileobj(src, dst)
                        lua_count += 1
                    elif file.endswith('.manifest'):
                        target = os.path.join(depotcache_dir, os.path.basename(file))
                        with zip_ref.open(file) as src, open(target, 'wb') as dst:
                            shutil.copyfileobj(src, dst)
                        manifest_count += 1
            marcellus_path = os.path.join(stplugin_dir, 'marcellus.lua')
            existing_lines = []
            if os.path.exists(marcellus_path):
                with open(marcellus_path, 'r', encoding='utf-8') as f:
                    existing_lines = f.readlines()
            with open(marcellus_path, 'a', encoding='utf-8') as f:
                new_count = 0
                for dlc_id in dlc_ids:
                    add_line = f'addappid({dlc_id}, 1)\n'
                    if add_line not in existing_lines:
                        f.write(add_line)
                        new_count += 1
            self.show_info('Başarılı', f'Oyun dosyaları başarılı bir şekilde steam klasörüne kopyalandı!\nDLC dosyasına {new_count} adet yeni DLC eklendi.')
        except Exception as e:
            self.show_info('Hata', f'Bir hata oluştu:\n{e}')

    def restart_steam(self):
        steam_path = self.path_edit.text().strip()
        if not steam_path:
            self.show_info('Hata', 'Lütfen önce Steam klasörünü seçin!')
            return
        steam_exe = os.path.join(steam_path, 'steam.exe')
        if not os.path.exists(steam_exe):
            self.show_info('Hata', 'steam.exe bulunamadı! Lütfen doğru Steam klasörünü seçtiğinizden emin olun.')
            return
        try:
            subprocess.run(['taskkill', '/F', '/IM', 'steam.exe'], shell=True)
            subprocess.Popen([steam_exe], shell=True)
            self.show_info('Başarılı', 'Steam yeniden başlatıldı!')
        except Exception as e:
            self.show_info('Hata', f'Steam yeniden başlatılamadı:\n{e}')

    def resizeEvent(self, event):
        w = max(self.width(), self._min_width)
        h = max(self.height(), self._min_height)
        if self.width() < self._min_width or self.height() < self._min_height:
            self.resize(w, h)
        super().resizeEvent(event)

def resource_path(relative_path):
    if hasattr(sys, '_MEIPASS'):
        return os.path.join(sys._MEIPASS, relative_path)
    return os.path.join(os.path.abspath("."), relative_path)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    icon_path = resource_path('favicon.png')
    if os.path.exists(icon_path):
        app.setWindowIcon(QIcon(icon_path))
    window = SteamUploader()
    window.show()
    sys.exit(app.exec())