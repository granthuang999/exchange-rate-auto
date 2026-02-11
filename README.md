# 汇率数据自动更新（美元基准）

**更新时间**：2026-02-11 12:23:11（北京时间）

## Excel 表格（制表符分隔）

Currency	USD	CNY	HKD	EUR	GBP	JPY
USD		6.9102	7.8153	0.8391	0.7316	153.3820
CNY	0.1447		1.1310	0.1214	0.1059	22.1965
HKD	0.1280	0.8842		0.1074	0.0936	19.6259
EUR	1.1918	8.2353	9.3139		0.8719	182.7935
GBP	1.3669	9.4453	10.6825	1.1469		209.6528
JPY	0.0065	0.0451	0.0510	0.0055	0.0048	

## CSV 文件链接

https://raw.githubusercontent.com/granthuang999/exchange-rate-auto/main/exchange_rates.csv

### 数据源说明
- 优先使用 Yahoo Finance 实时汇率
- Yahoo 失败时使用 Wise 汇率
- 最后备选 ExchangeRate-API
- 以美元为基准计算所有交叉汇率

---
*数据仅供参考，交易请以银行报价为准*