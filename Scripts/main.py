import sys
from PyQt5.QtWidgets import QApplication
from .bian_api import BinanceAPI
from ui_main import MainWindow

# 填入你的API KEY
api_key = 'YOUR_API_KEY'
api_secret = 'YOUR_API_SECRET'

def main():
    app = QApplication(sys.argv)
    api = BinanceAPI(api_key, api_secret)
    window = MainWindow(api)
    window.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()