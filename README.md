# 汇率数据自动更新（美元基准）

**更新时间**：2026-07-30 12:49:12（北京时间）

## Excel 表格（制表符分隔）

Currency	USD	CNY	HKD	EUR	GBP	JPY
USD		6.7594	7.8431	0.8729	0.7492	163.4820
CNY	0.1479		1.1603	0.1291	0.1108	24.1859
HKD	0.1275	0.8618		0.1113	0.0955	20.8441
EUR	1.1456	7.7436	8.9851		0.8583	187.2861
GBP	1.3348	9.0222	10.4686	1.1651		218.2088
JPY	0.0061	0.0413	0.0480	0.0053	0.0046	

## CSV 文件链接

https://raw.githubusercontent.com/granthuang999/exchange-rate-auto/main/exchange_rates.csv

### 数据源说明
- 优先使用 Yahoo Finance 实时汇率
- Yahoo 失败时使用 Wise 汇率
- 最后备选 ExchangeRate-API
- 以美元为基准计算所有交叉汇率

---
*数据仅供参考，交易请以银行报价为准*