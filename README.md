# 汇率数据自动更新（美元基准）

**更新时间**：2025-12-16 11:18:23（北京时间）

## Excel 表格（制表符分隔）

Currency	USD	CNY	HKD	EUR	GBP	JPY
USD		7.0422	7.7800	0.8504	0.7480	154.7520
CNY	0.1420		1.1048	0.1208	0.1062	21.9750
HKD	0.1285	0.9052		0.1093	0.0961	19.8910
EUR	1.1759	8.2810	9.1486		0.8796	181.9755
GBP	1.3369	9.4147	10.4011	1.1369		206.8877
JPY	0.0065	0.0455	0.0503	0.0055	0.0048	

## CSV 文件链接

https://raw.githubusercontent.com/granthuang999/exchange-rate-auto/main/exchange_rates.csv

### 数据源说明
- 优先使用 Yahoo Finance 实时汇率
- Yahoo 失败时使用 Wise 汇率
- 最后备选 ExchangeRate-API
- 以美元为基准计算所有交叉汇率

---
*数据仅供参考，交易请以银行报价为准*