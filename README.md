# 汇率数据自动更新（美元基准）

**更新时间**：2026-08-20 22:25:53（北京时间）

## Excel 表格（制表符分隔）

Currency	USD	CNY	HKD	EUR	GBP	JPY
USD		6.7127	7.8426	0.8560	0.7334	158.7690
CNY	0.1490		1.1683	0.1275	0.1093	23.6520
HKD	0.1275	0.8559		0.1091	0.0935	20.2444
EUR	1.1682	7.8419	9.1619		0.8568	185.4778
GBP	1.3635	9.1528	10.6935	1.1672		216.4835
JPY	0.0063	0.0423	0.0494	0.0054	0.0046	

## CSV 文件链接

https://raw.githubusercontent.com/granthuang999/exchange-rate-auto/main/exchange_rates.csv

### 数据源说明
- 优先使用 Yahoo Finance 实时汇率
- Yahoo 失败时使用 Wise 汇率
- 最后备选 ExchangeRate-API
- 以美元为基准计算所有交叉汇率

---
*数据仅供参考，交易请以银行报价为准*