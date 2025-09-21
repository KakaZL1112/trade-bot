import numpy as np

class AlphaStrategy:
    def __init__(self, short_window=5, long_window=20, debug=False):
        """
        初始化策略参数
        :param short_window: 短期均线窗口
        :param long_window: 长期均线窗口
        :param debug: 是否打印调试信息
        """
        self.short_window = short_window
        self.long_window = long_window
        self.debug = debug

    def should_trade(self, market_data):
        """
        根据市场数据判断是否交易
        :param market_data: list或array，收盘价序列，最新价在最后一个元素
        :return: (是否交易, 'BUY'/'SELL'/None, 原因)
        """
        if len(market_data) < self.long_window:
            if self.debug:
                print("数据长度不足")
            return False, None, "数据长度不足"

        prices = np.array(market_data)
        short_ma = prices[-self.short_window:].mean()
        long_ma = prices[-self.long_window:].mean()

        if self.debug:
            print(f"短期均线: {short_ma}, 长期均线: {long_ma}")

        # 策略逻辑：短期均线上穿长期均线买入，下穿卖出
        if short_ma > long_ma:
            return True, 'BUY', "短期均线上穿长期均线"
        elif short_ma < long_ma:
            return True, 'SELL', "短期均线下穿长期均线"
        else:
            return False, None, "无交易信号"