# 汇率数据自动更新（美元基准）

**更新时间**：2025-10-13 22:12:49（北京时间）

## Excel 表格（制表符分隔）

Currency	USD	CNY	HKD	EUR	GBP	JPY
USD		7.1315	7.7783	0.8642	0.7503	152.2990
CNY	0.1402		1.0907	0.1212	0.1052	21.3558
HKD	0.1286	0.9168		0.1111	0.0965	19.5800
EUR	1.1571	8.2521	9.0006		0.8682	176.2312
GBP	1.3328	9.5049	10.3669	1.1518		202.9841
JPY	0.0066	0.0468	0.0511	0.0057	0.0049	

## CSV 文件链接

https://raw.githubusercontent.com/granthuang999/exchange-rate-auto/main/exchange_rates.csv

### 数据源说明
- 优先使用 Yahoo Finance 实时汇率
- Yahoo 失败时使用 Wise 汇率
- 最后备选 ExchangeRate-API
- 以美元为基准计算所有交叉汇率

---
*数据仅供参考，交易请以银行报价为准*