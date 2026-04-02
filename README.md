# 汇率数据自动更新（美元基准）

**更新时间**：2026-04-02 22:48:17（北京时间）

## Excel 表格（制表符分隔）

Currency	USD	CNY	HKD	EUR	GBP	JPY
USD		6.8886	7.8367	0.8656	0.7556	159.2470
CNY	0.1452		1.1376	0.1257	0.1097	23.1175
HKD	0.1276	0.8790		0.1105	0.0964	20.3207
EUR	1.1553	7.9582	9.0535		0.8729	183.9730
GBP	1.3235	9.1167	10.3715	1.1456		210.7557
JPY	0.0063	0.0433	0.0492	0.0054	0.0047	

## CSV 文件链接

https://raw.githubusercontent.com/granthuang999/exchange-rate-auto/main/exchange_rates.csv

### 数据源说明
- 优先使用 Yahoo Finance 实时汇率
- Yahoo 失败时使用 Wise 汇率
- 最后备选 ExchangeRate-API
- 以美元为基准计算所有交叉汇率

---
*数据仅供参考，交易请以银行报价为准*