# 汇率数据自动更新（美元基准）

**更新时间**：2026-03-03 22:38:00（北京时间）

## Excel 表格（制表符分隔）

Currency	USD	CNY	HKD	EUR	GBP	JPY
USD		6.8991	7.8020	0.8634	0.7515	157.9010
CNY	0.1449		1.1309	0.1251	0.1089	22.8872
HKD	0.1282	0.8843		0.1107	0.0963	20.2385
EUR	1.1582	7.9906	9.0364		0.8704	182.8828
GBP	1.3307	9.1804	10.3819	1.1489		210.1144
JPY	0.0063	0.0437	0.0494	0.0055	0.0048	

## CSV 文件链接

https://raw.githubusercontent.com/granthuang999/exchange-rate-auto/main/exchange_rates.csv

### 数据源说明
- 优先使用 Yahoo Finance 实时汇率
- Yahoo 失败时使用 Wise 汇率
- 最后备选 ExchangeRate-API
- 以美元为基准计算所有交叉汇率

---
*数据仅供参考，交易请以银行报价为准*