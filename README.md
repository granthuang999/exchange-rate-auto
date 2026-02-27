# 汇率数据自动更新（美元基准）

**更新时间**：2026-02-27 22:33:42（北京时间）

## Excel 表格（制表符分隔）

Currency	USD	CNY	HKD	EUR	GBP	JPY
USD		6.8574	7.8236	0.8468	0.7427	156.0200
CNY	0.1458		1.1409	0.1235	0.1083	22.7521
HKD	0.1278	0.8765		0.1082	0.0949	19.9422
EUR	1.1809	8.0980	9.2390		0.8771	184.2466
GBP	1.3464	9.2331	10.5340	1.1402		210.0714
JPY	0.0064	0.0440	0.0501	0.0054	0.0048	

## CSV 文件链接

https://raw.githubusercontent.com/granthuang999/exchange-rate-auto/main/exchange_rates.csv

### 数据源说明
- 优先使用 Yahoo Finance 实时汇率
- Yahoo 失败时使用 Wise 汇率
- 最后备选 ExchangeRate-API
- 以美元为基准计算所有交叉汇率

---
*数据仅供参考，交易请以银行报价为准*