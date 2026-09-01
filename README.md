# 汇率数据自动更新（美元基准）

**更新时间**：2026-09-01 15:00:42（北京时间）

## Excel 表格（制表符分隔）

Currency	USD	CNY	HKD	EUR	GBP	JPY
USD		6.7199	7.8384	0.8615	0.7385	159.9520
CNY	0.1488		1.1664	0.1282	0.1099	23.8027
HKD	0.1276	0.8573		0.1099	0.0942	20.4062
EUR	1.1608	7.8002	9.0985		0.8572	185.6669
GBP	1.3541	9.0994	10.6139	1.1666		216.5904
JPY	0.0063	0.0420	0.0490	0.0054	0.0046	

## CSV 文件链接

https://raw.githubusercontent.com/granthuang999/exchange-rate-auto/main/exchange_rates.csv

### 数据源说明
- 优先使用 Yahoo Finance 实时汇率
- Yahoo 失败时使用 Wise 汇率
- 最后备选 ExchangeRate-API
- 以美元为基准计算所有交叉汇率

---
*数据仅供参考，交易请以银行报价为准*