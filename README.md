# 汇率数据自动更新（美元基准）

**更新时间**：2025-11-19 11:05:55（北京时间）

## Excel 表格（制表符分隔）

Currency	USD	CNY	HKD	EUR	GBP	JPY
USD		7.1088	7.7910	0.8634	0.7610	155.3320
CNY	0.1407		1.0960	0.1215	0.1071	21.8507
HKD	0.1284	0.9124		0.1108	0.0977	19.9374
EUR	1.1582	8.2335	9.0236		0.8814	179.9073
GBP	1.3141	9.3414	10.2378	1.1346		204.1156
JPY	0.0064	0.0458	0.0502	0.0056	0.0049	

## CSV 文件链接

https://raw.githubusercontent.com/granthuang999/exchange-rate-auto/main/exchange_rates.csv

### 数据源说明
- 优先使用 Yahoo Finance 实时汇率
- Yahoo 失败时使用 Wise 汇率
- 最后备选 ExchangeRate-API
- 以美元为基准计算所有交叉汇率

---
*数据仅供参考，交易请以银行报价为准*