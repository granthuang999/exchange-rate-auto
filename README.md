# 汇率数据自动更新（美元基准）

**更新时间**：2026-01-26 11:49:44（北京时间）

## Excel 表格（制表符分隔）

Currency	USD	CNY	HKD	EUR	GBP	JPY
USD		6.9549	7.7935	0.8426	0.7319	154.2140
CNY	0.1438		1.1206	0.1212	0.1052	22.1734
HKD	0.1283	0.8924		0.1081	0.0939	19.7875
EUR	1.1868	8.2541	9.2493		0.8686	183.0216
GBP	1.3663	9.5025	10.6483	1.1513		210.7036
JPY	0.0065	0.0451	0.0505	0.0055	0.0047	

## CSV 文件链接

https://raw.githubusercontent.com/granthuang999/exchange-rate-auto/main/exchange_rates.csv

### 数据源说明
- 优先使用 Yahoo Finance 实时汇率
- Yahoo 失败时使用 Wise 汇率
- 最后备选 ExchangeRate-API
- 以美元为基准计算所有交叉汇率

---
*数据仅供参考，交易请以银行报价为准*