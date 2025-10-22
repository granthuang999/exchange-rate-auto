# 汇率数据自动更新（美元基准）

**更新时间**：2025-10-22 22:13:45（北京时间）

## Excel 表格（制表符分隔）

Currency	USD	CNY	HKD	EUR	GBP	JPY
USD		7.1270	7.7698	0.8623	0.7491	151.9120
CNY	0.1403		1.0902	0.1210	0.1051	21.3150
HKD	0.1287	0.9173		0.1110	0.0964	19.5516
EUR	1.1597	8.2651	9.0106		0.8687	176.1707
GBP	1.3349	9.5141	10.3722	1.1511		202.7927
JPY	0.0066	0.0469	0.0511	0.0057	0.0049	

## CSV 文件链接

https://raw.githubusercontent.com/granthuang999/exchange-rate-auto/main/exchange_rates.csv

### 数据源说明
- 优先使用 Yahoo Finance 实时汇率
- Yahoo 失败时使用 Wise 汇率
- 最后备选 ExchangeRate-API
- 以美元为基准计算所有交叉汇率

---
*数据仅供参考，交易请以银行报价为准*