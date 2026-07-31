# 汇率数据自动更新（美元基准）

**更新时间**：2026-07-31 13:27:10（北京时间）

## Excel 表格（制表符分隔）

Currency	USD	CNY	HKD	EUR	GBP	JPY
USD		6.7364	7.8424	0.8689	0.7438	160.6880
CNY	0.1484		1.1642	0.1290	0.1104	23.8537
HKD	0.1275	0.8590		0.1108	0.0948	20.4896
EUR	1.1509	7.7528	9.0257		0.8560	184.9327
GBP	1.3444	9.0567	10.5437	1.1682		216.0366
JPY	0.0062	0.0419	0.0488	0.0054	0.0046	

## CSV 文件链接

https://raw.githubusercontent.com/granthuang999/exchange-rate-auto/main/exchange_rates.csv

### 数据源说明
- 优先使用 Yahoo Finance 实时汇率
- Yahoo 失败时使用 Wise 汇率
- 最后备选 ExchangeRate-API
- 以美元为基准计算所有交叉汇率

---
*数据仅供参考，交易请以银行报价为准*