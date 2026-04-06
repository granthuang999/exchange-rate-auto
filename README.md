# 汇率数据自动更新（美元基准）

**更新时间**：2026-04-06 12:37:36（北京时间）

## Excel 表格（制表符分隔）

Currency	USD	CNY	HKD	EUR	GBP	JPY
USD		6.8816	7.8370	0.8676	0.7569	159.5440
CNY	0.1453		1.1388	0.1261	0.1100	23.1841
HKD	0.1276	0.8781		0.1107	0.0966	20.3578
EUR	1.1526	7.9318	9.0330		0.8724	183.8912
GBP	1.3212	9.0918	10.3541	1.1463		210.7861
JPY	0.0063	0.0431	0.0491	0.0054	0.0047	

## CSV 文件链接

https://raw.githubusercontent.com/granthuang999/exchange-rate-auto/main/exchange_rates.csv

### 数据源说明
- 优先使用 Yahoo Finance 实时汇率
- Yahoo 失败时使用 Wise 汇率
- 最后备选 ExchangeRate-API
- 以美元为基准计算所有交叉汇率

---
*数据仅供参考，交易请以银行报价为准*