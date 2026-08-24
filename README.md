# 汇率数据自动更新（美元基准）

**更新时间**：2026-08-24 22:32:10（北京时间）

## Excel 表格（制表符分隔）

Currency	USD	CNY	HKD	EUR	GBP	JPY
USD		6.7217	7.8363	0.8566	0.7331	159.1190
CNY	0.1488		1.1658	0.1274	0.1091	23.6724
HKD	0.1276	0.8578		0.1093	0.0936	20.3054
EUR	1.1674	7.8470	9.1481		0.8558	185.7565
GBP	1.3641	9.1689	10.6893	1.1685		217.0495
JPY	0.0063	0.0422	0.0492	0.0054	0.0046	

## CSV 文件链接

https://raw.githubusercontent.com/granthuang999/exchange-rate-auto/main/exchange_rates.csv

### 数据源说明
- 优先使用 Yahoo Finance 实时汇率
- Yahoo 失败时使用 Wise 汇率
- 最后备选 ExchangeRate-API
- 以美元为基准计算所有交叉汇率

---
*数据仅供参考，交易请以银行报价为准*