import pandas as pd
import backtrader as bt
import backtrader.feeds as btfeeds


class TestStrategy(bt.Strategy):
    
    params = (
        (),
    )
    
    def log(self, txt, dt=None):
        
        dt = dt or self.datas[0].datetime.date(0)
        print("%s, %s" % (dt.isoformat(), txt))
        
    def __init__(self):
        
        pass
    
    def notify_order(self, order):
        return super().notify_order(order)
    
    def notify_trade(self, trade):
        return super().notify_trade(trade)
    
    def next(self):
        
        pass
    
cerebro = bt.Cerebro()

data = btfeeds.BacktraderCSVData()

cerebro.adddata(data)

cerebro.broker.setcash()

cerebro.broker.setcommission()

cerebro.broker.set_slippage_perc(prec=0.001)

cerebro.addsizer()

cerebro.addanalyzer()

cerebro.addobserver()

cerebro.run()

cerebro.plot()


