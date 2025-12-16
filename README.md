# 汇率数据自动更新（美元基准）

**更新时间**：2025-12-16 22:16:50（北京时间）

## Excel 表格（制表符分隔）

Currency	USD	CNY	HKD	EUR	GBP	JPY
USD		7.0412	7.7790	0.8491	0.7452	154.9170
CNY	0.1420		1.1048	0.1206	0.1058	22.0015
HKD	0.1286	0.9052		0.1092	0.0958	19.9148
EUR	1.1777	8.2925	9.1615		0.8776	182.4485
GBP	1.3419	9.4487	10.4388	1.1394		207.8865
JPY	0.0065	0.0455	0.0502	0.0055	0.0048	

## CSV 文件链接

https://raw.githubusercontent.com/granthuang999/exchange-rate-auto/main/exchange_rates.csv

### 数据源说明
- 优先使用 Yahoo Finance 实时汇率
- Yahoo 失败时使用 Wise 汇率
- 最后备选 ExchangeRate-API
- 以美元为基准计算所有交叉汇率

---
*数据仅供参考，交易请以银行报价为准*