# 汇率数据自动更新（美元基准）

**更新时间**：2025-10-21 22:12:01（北京时间）

## Excel 表格（制表符分隔）

Currency	USD	CNY	HKD	EUR	GBP	JPY
USD		7.1197	7.7701	0.8609	0.7473	151.5170
CNY	0.1405		1.0914	0.1209	0.1050	21.2814
HKD	0.1287	0.9163		0.1108	0.0962	19.5000
EUR	1.1616	8.2701	9.0256		0.8680	175.9984
GBP	1.3382	9.5272	10.3976	1.1520		202.7526
JPY	0.0066	0.0470	0.0513	0.0057	0.0049	

## CSV 文件链接

https://raw.githubusercontent.com/granthuang999/exchange-rate-auto/main/exchange_rates.csv

### 数据源说明
- 优先使用 Yahoo Finance 实时汇率
- Yahoo 失败时使用 Wise 汇率
- 最后备选 ExchangeRate-API
- 以美元为基准计算所有交叉汇率

---
*数据仅供参考，交易请以银行报价为准*