# 汇率数据自动更新（美元基准）

**更新时间**：2026-03-23 12:20:51（北京时间）

## Excel 表格（制表符分隔）

Currency	USD	CNY	HKD	EUR	GBP	JPY
USD		6.9090	7.8305	0.8655	0.7506	159.3940
CNY	0.1447		1.1334	0.1253	0.1086	23.0705
HKD	0.1277	0.8823		0.1105	0.0959	20.3555
EUR	1.1554	7.9827	9.0474		0.8672	184.1641
GBP	1.3323	9.2046	10.4323	1.1531		212.3554
JPY	0.0063	0.0433	0.0491	0.0054	0.0047	

## CSV 文件链接

https://raw.githubusercontent.com/granthuang999/exchange-rate-auto/main/exchange_rates.csv

### 数据源说明
- 优先使用 Yahoo Finance 实时汇率
- Yahoo 失败时使用 Wise 汇率
- 最后备选 ExchangeRate-API
- 以美元为基准计算所有交叉汇率

---
*数据仅供参考，交易请以银行报价为准*