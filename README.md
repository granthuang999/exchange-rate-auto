# 汇率数据自动更新（美元基准）

**更新时间**：2026-04-07 12:26:27（北京时间）

## Excel 表格（制表符分隔）

Currency	USD	CNY	HKD	EUR	GBP	JPY
USD		6.8758	7.8374	0.8667	0.7560	159.7830
CNY	0.1454		1.1399	0.1261	0.1100	23.2385
HKD	0.1276	0.8773		0.1106	0.0965	20.3872
EUR	1.1538	7.9333	9.0428		0.8723	184.3579
GBP	1.3228	9.0950	10.3669	1.1464		211.3532
JPY	0.0063	0.0430	0.0491	0.0054	0.0047	

## CSV 文件链接

https://raw.githubusercontent.com/granthuang999/exchange-rate-auto/main/exchange_rates.csv

### 数据源说明
- 优先使用 Yahoo Finance 实时汇率
- Yahoo 失败时使用 Wise 汇率
- 最后备选 ExchangeRate-API
- 以美元为基准计算所有交叉汇率

---
*数据仅供参考，交易请以银行报价为准*