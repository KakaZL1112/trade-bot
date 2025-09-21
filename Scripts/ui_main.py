from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QPushButton, QLineEdit, QComboBox

class MainWindow(QWidget):
    def __init__(self, api):
        super().__init__()
        self.api = api
        self.init_ui()
    
    def init_ui(self):
        self.setWindowTitle('Binance Alpha Bot')
        layout = QVBoxLayout()

        self.symbol_input = QLineEdit(self)
        self.symbol_input.setPlaceholderText('交易对 (如 BTCUSDT)')
        layout.addWidget(self.symbol_input)

        self.qty_input = QLineEdit(self)
        self.qty_input.setPlaceholderText('交易量')
        layout.addWidget(self.qty_input)

        self.side_combo = QComboBox(self)
        self.side_combo.addItems(['BUY', 'SELL'])
        layout.addWidget(self.side_combo)

        self.status_label = QLabel('状态: 等待开始')
        layout.addWidget(self.status_label)

        self.trade_btn = QPushButton('手动下单', self)
        self.trade_btn.clicked.connect(self.place_order)
        layout.addWidget(self.trade_btn)

        self.setLayout(layout)
    
    def place_order(self):
        symbol = self.symbol_input.text()
        qty = float(self.qty_input.text())
        side = self.side_combo.currentText()
        try:
            order = self.api.place_order(symbol, side, qty)
            self.status_label.setText(f'下单成功: {order}')
        except Exception as e:
            self.status_label.setText(f'下单失败: {e}')