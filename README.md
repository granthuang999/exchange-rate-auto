# 汇率数据自动更新（美元基准）

**更新时间**：2026-08-26 10:56:35（北京时间）

## Excel 表格（制表符分隔）

Currency	USD	CNY	HKD	EUR	GBP	JPY
USD		6.7202	7.8401	0.8568	0.7331	159.0320
CNY	0.1488		1.1666	0.1275	0.1091	23.6648
HKD	0.1275	0.8572		0.1093	0.0935	20.2844
EUR	1.1671	7.8434	9.1504		0.8556	185.6116
GBP	1.3641	9.1668	10.6944	1.1687		216.9308
JPY	0.0063	0.0423	0.0493	0.0054	0.0046	

## CSV 文件链接

https://raw.githubusercontent.com/granthuang999/exchange-rate-auto/main/exchange_rates.csv

### 数据源说明
- 优先使用 Yahoo Finance 实时汇率
- Yahoo 失败时使用 Wise 汇率
- 最后备选 ExchangeRate-API
- 以美元为基准计算所有交叉汇率

---
*数据仅供参考，交易请以银行报价为准*