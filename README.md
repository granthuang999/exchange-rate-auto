# 汇率数据自动更新（美元基准）

**更新时间**：2026-02-17 12:10:46（北京时间）

## Excel 表格（制表符分隔）

Currency	USD	CNY	HKD	EUR	GBP	JPY
USD		6.9032	7.8152	0.8443	0.7348	153.1900
CNY	0.1449		1.1321	0.1223	0.1064	22.1912
HKD	0.1280	0.8833		0.1080	0.0940	19.6015
EUR	1.1844	8.1762	9.2564		0.8703	181.4402
GBP	1.3609	9.3947	10.6358	1.1490		208.4785
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