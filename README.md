# 汇率数据自动更新（美元基准）

**更新时间**：2025-10-14 10:55:58（北京时间）

## Excel 表格（制表符分隔）

Currency	USD	CNY	HKD	EUR	GBP	JPY
USD		7.1346	7.7770	0.8636	0.7493	152.3650
CNY	0.1402		1.0900	0.1210	0.1050	21.3558
HKD	0.1286	0.9174		0.1110	0.0963	19.5917
EUR	1.1579	8.2615	9.0053		0.8676	176.4301
GBP	1.3346	9.5217	10.3790	1.1525		203.3431
JPY	0.0066	0.0468	0.0510	0.0057	0.0049	

## CSV 文件链接

https://raw.githubusercontent.com/granthuang999/exchange-rate-auto/main/exchange_rates.csv

### 数据源说明
- 优先使用 Yahoo Finance 实时汇率
- Yahoo 失败时使用 Wise 汇率
- 最后备选 ExchangeRate-API
- 以美元为基准计算所有交叉汇率

---
*数据仅供参考，交易请以银行报价为准*