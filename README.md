# 汇率数据自动更新（美元基准）

**更新时间**：2025-12-24 11:17:29（北京时间）

## Excel 表格（制表符分隔）

Currency	USD	CNY	HKD	EUR	GBP	JPY
USD		7.0253	7.7748	0.8477	0.7395	155.7920
CNY	0.1423		1.1067	0.1207	0.1053	22.1759
HKD	0.1286	0.9036		0.1090	0.0951	20.0381
EUR	1.1797	8.2875	9.1716		0.8724	183.7820
GBP	1.3523	9.5001	10.5136	1.1463		210.6721
JPY	0.0064	0.0451	0.0499	0.0054	0.0047	

## CSV 文件链接

https://raw.githubusercontent.com/granthuang999/exchange-rate-auto/main/exchange_rates.csv

### 数据源说明
- 优先使用 Yahoo Finance 实时汇率
- Yahoo 失败时使用 Wise 汇率
- 最后备选 ExchangeRate-API
- 以美元为基准计算所有交叉汇率

---
*数据仅供参考，交易请以银行报价为准*