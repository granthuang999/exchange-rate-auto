# 汇率数据自动更新（美元基准）

**更新时间**：2026-08-24 10:55:09（北京时间）

## Excel 表格（制表符分隔）

Currency	USD	CNY	HKD	EUR	GBP	JPY
USD		6.7230	7.8380	0.8558	0.7326	158.8670
CNY	0.1487		1.1658	0.1273	0.1090	23.6304
HKD	0.1276	0.8577		0.1092	0.0935	20.2688
EUR	1.1685	7.8558	9.1587		0.8560	185.6357
GBP	1.3650	9.1769	10.6989	1.1682		216.8537
JPY	0.0063	0.0423	0.0493	0.0054	0.0046	

## CSV 文件链接

https://raw.githubusercontent.com/granthuang999/exchange-rate-auto/main/exchange_rates.csv

### 数据源说明
- 优先使用 Yahoo Finance 实时汇率
- Yahoo 失败时使用 Wise 汇率
- 最后备选 ExchangeRate-API
- 以美元为基准计算所有交叉汇率

---
*数据仅供参考，交易请以银行报价为准*