# 汇率数据自动更新（美元基准）

**更新时间**：2025-11-13 22:12:44（北京时间）

## Excel 表格（制表符分隔）

Currency	USD	CNY	HKD	EUR	GBP	JPY
USD		7.0966	7.7699	0.8604	0.7589	154.6450
CNY	0.1409		1.0949	0.1212	0.1069	21.7914
HKD	0.1287	0.9133		0.1107	0.0977	19.9031
EUR	1.1623	8.2480	9.0306		0.8820	179.7362
GBP	1.3177	9.3512	10.2384	1.1337		203.7752
JPY	0.0065	0.0459	0.0502	0.0056	0.0049	

## CSV 文件链接

https://raw.githubusercontent.com/granthuang999/exchange-rate-auto/main/exchange_rates.csv

### 数据源说明
- 优先使用 Yahoo Finance 实时汇率
- Yahoo 失败时使用 Wise 汇率
- 最后备选 ExchangeRate-API
- 以美元为基准计算所有交叉汇率

---
*数据仅供参考，交易请以银行报价为准*