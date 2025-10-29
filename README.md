# 汇率数据自动更新（美元基准）

**更新时间**：2025-10-29 22:13:23（北京时间）

## Excel 表格（制表符分隔）

Currency	USD	CNY	HKD	EUR	GBP	JPY
USD		7.0985	7.7710	0.8591	0.7570	152.0420
CNY	0.1409		1.0947	0.1210	0.1066	21.4189
HKD	0.1287	0.9135		0.1106	0.0974	19.5653
EUR	1.1640	8.2627	9.0455		0.8812	176.9782
GBP	1.3210	9.3771	10.2655	1.1349		200.8481
JPY	0.0066	0.0467	0.0511	0.0057	0.0050	

## CSV 文件链接

https://raw.githubusercontent.com/granthuang999/exchange-rate-auto/main/exchange_rates.csv

### 数据源说明
- 优先使用 Yahoo Finance 实时汇率
- Yahoo 失败时使用 Wise 汇率
- 最后备选 ExchangeRate-API
- 以美元为基准计算所有交叉汇率

---
*数据仅供参考，交易请以银行报价为准*