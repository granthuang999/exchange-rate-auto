# 汇率数据自动更新（美元基准）

**更新时间**：2025-12-31 22:13:04（北京时间）

## Excel 表格（制表符分隔）

Currency	USD	CNY	HKD	EUR	GBP	JPY
USD		6.9926	7.7836	0.8515	0.7433	156.8970
CNY	0.1430		1.1131	0.1218	0.1063	22.4376
HKD	0.1285	0.8984		0.1094	0.0955	20.1574
EUR	1.1744	8.2121	9.1410		0.8729	184.2595
GBP	1.3454	9.4075	10.4717	1.1456		211.0817
JPY	0.0064	0.0446	0.0496	0.0054	0.0047	

## CSV 文件链接

https://raw.githubusercontent.com/granthuang999/exchange-rate-auto/main/exchange_rates.csv

### 数据源说明
- 优先使用 Yahoo Finance 实时汇率
- Yahoo 失败时使用 Wise 汇率
- 最后备选 ExchangeRate-API
- 以美元为基准计算所有交叉汇率

---
*数据仅供参考，交易请以银行报价为准*