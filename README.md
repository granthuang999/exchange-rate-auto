# 汇率数据自动更新（美元基准）

**更新时间**：2026-08-27 20:10:44（北京时间）

## Excel 表格（制表符分隔）

Currency	USD	CNY	HKD	EUR	GBP	JPY
USD		6.7093	7.8384	0.8585	0.7363	159.3860
CNY	0.1490		1.1683	0.1280	0.1097	23.7560
HKD	0.1276	0.8560		0.1095	0.0939	20.3340
EUR	1.1648	7.8151	9.1303		0.8577	185.6564
GBP	1.3581	9.1122	10.6457	1.1660		216.4688
JPY	0.0063	0.0421	0.0492	0.0054	0.0046	

## CSV 文件链接

https://raw.githubusercontent.com/granthuang999/exchange-rate-auto/main/exchange_rates.csv

### 数据源说明
- 优先使用 Yahoo Finance 实时汇率
- Yahoo 失败时使用 Wise 汇率
- 最后备选 ExchangeRate-API
- 以美元为基准计算所有交叉汇率

---
*数据仅供参考，交易请以银行报价为准*