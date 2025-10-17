# 汇率数据自动更新（美元基准）

**更新时间**：2025-10-17 22:12:17（北京时间）

## Excel 表格（制表符分隔）

Currency	USD	CNY	HKD	EUR	GBP	JPY
USD		7.1256	7.7670	0.8571	0.7459	150.4670
CNY	0.1403		1.0900	0.1203	0.1047	21.1164
HKD	0.1287	0.9174		0.1104	0.0960	19.3726
EUR	1.1667	8.3136	9.0620		0.8703	175.5536
GBP	1.3407	9.5530	10.4129	1.1491		201.7254
JPY	0.0066	0.0474	0.0516	0.0057	0.0050	

## CSV 文件链接

https://raw.githubusercontent.com/granthuang999/exchange-rate-auto/main/exchange_rates.csv

### 数据源说明
- 优先使用 Yahoo Finance 实时汇率
- Yahoo 失败时使用 Wise 汇率
- 最后备选 ExchangeRate-API
- 以美元为基准计算所有交叉汇率

---
*数据仅供参考，交易请以银行报价为准*