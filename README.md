# 汇率数据自动更新（美元基准）

**更新时间**：2025-12-02 22:14:14（北京时间）

## Excel 表格（制表符分隔）

Currency	USD	CNY	HKD	EUR	GBP	JPY
USD		7.0694	7.7857	0.8605	0.7572	156.0480
CNY	0.1415		1.1013	0.1217	0.1071	22.0737
HKD	0.1284	0.9080		0.1105	0.0973	20.0429
EUR	1.1621	8.2155	9.0479		0.8800	181.3457
GBP	1.3207	9.3362	10.2822	1.1364		206.0856
JPY	0.0064	0.0453	0.0499	0.0055	0.0049	

## CSV 文件链接

https://raw.githubusercontent.com/granthuang999/exchange-rate-auto/main/exchange_rates.csv

### 数据源说明
- 优先使用 Yahoo Finance 实时汇率
- Yahoo 失败时使用 Wise 汇率
- 最后备选 ExchangeRate-API
- 以美元为基准计算所有交叉汇率

---
*数据仅供参考，交易请以银行报价为准*