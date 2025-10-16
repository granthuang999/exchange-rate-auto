# 汇率数据自动更新（美元基准）

**更新时间**：2025-10-16 22:13:17（北京时间）

## Excel 表格（制表符分隔）

Currency	USD	CNY	HKD	EUR	GBP	JPY
USD		7.1253	7.7712	0.8571	0.7451	150.9120
CNY	0.1403		1.0906	0.1203	0.1046	21.1797
HKD	0.1287	0.9169		0.1103	0.0959	19.4194
EUR	1.1667	8.3133	9.0669		0.8693	176.0728
GBP	1.3421	9.5629	10.4297	1.1503		202.5393
JPY	0.0066	0.0472	0.0515	0.0057	0.0049	

## CSV 文件链接

https://raw.githubusercontent.com/granthuang999/exchange-rate-auto/main/exchange_rates.csv

### 数据源说明
- 优先使用 Yahoo Finance 实时汇率
- Yahoo 失败时使用 Wise 汇率
- 最后备选 ExchangeRate-API
- 以美元为基准计算所有交叉汇率

---
*数据仅供参考，交易请以银行报价为准*