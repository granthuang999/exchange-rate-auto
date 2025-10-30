# 汇率数据自动更新（美元基准）

**更新时间**：2025-10-30 11:05:31（北京时间）

## Excel 表格（制表符分隔）

Currency	USD	CNY	HKD	EUR	GBP	JPY
USD		7.0960	7.7695	0.8605	0.7572	152.2380
CNY	0.1409		1.0949	0.1213	0.1067	21.4541
HKD	0.1287	0.9133		0.1108	0.0975	19.5943
EUR	1.1621	8.2464	9.0291		0.8800	176.9181
GBP	1.3207	9.3714	10.2608	1.1364		201.0539
JPY	0.0066	0.0466	0.0510	0.0057	0.0050	

## CSV 文件链接

https://raw.githubusercontent.com/granthuang999/exchange-rate-auto/main/exchange_rates.csv

### 数据源说明
- 优先使用 Yahoo Finance 实时汇率
- Yahoo 失败时使用 Wise 汇率
- 最后备选 ExchangeRate-API
- 以美元为基准计算所有交叉汇率

---
*数据仅供参考，交易请以银行报价为准*