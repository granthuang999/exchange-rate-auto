# 汇率数据自动更新（美元基准）

**更新时间**：2025-09-24 10:54:01（北京时间）

## Excel 表格（制表符分隔）

Currency	USD	CNY	HKD	EUR	GBP	JPY
USD		7.1157	7.7743	0.8474	0.7401	147.7790
CNY	0.1405		1.0926	0.1191	0.1040	20.7680
HKD	0.1286	0.9153		0.1090	0.0952	19.0087
EUR	1.1801	8.3971	9.1743		0.8734	174.3911
GBP	1.3512	9.6145	10.5044	1.1450		199.6744
JPY	0.0068	0.0482	0.0526	0.0057	0.0050	

## CSV 文件链接

https://raw.githubusercontent.com/granthuang999/exchange-rate-auto/main/exchange_rates.csv

### 数据源说明
- 优先使用 Yahoo Finance 实时汇率
- Yahoo 失败时使用 Wise 汇率
- 最后备选 ExchangeRate-API
- 以美元为基准计算所有交叉汇率

---
*数据仅供参考，交易请以银行报价为准*