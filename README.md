# 汇率数据自动更新（美元基准）

**更新时间**：2025-10-06 10:56:49（北京时间）

## Excel 表格（制表符分隔）

Currency	USD	CNY	HKD	EUR	GBP	JPY
USD		7.1185	7.7804	0.8524	0.7431	149.8610
CNY	0.1405		1.0930	0.1197	0.1044	21.0523
HKD	0.1285	0.9149		0.1096	0.0955	19.2613
EUR	1.1732	8.3511	9.1276		0.8718	175.8107
GBP	1.3457	9.5795	10.4702	1.1471		201.6700
JPY	0.0067	0.0475	0.0519	0.0057	0.0050	

## CSV 文件链接

https://raw.githubusercontent.com/granthuang999/exchange-rate-auto/main/exchange_rates.csv

### 数据源说明
- 优先使用 Yahoo Finance 实时汇率
- Yahoo 失败时使用 Wise 汇率
- 最后备选 ExchangeRate-API
- 以美元为基准计算所有交叉汇率

---
*数据仅供参考，交易请以银行报价为准*