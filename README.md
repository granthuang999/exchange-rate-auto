# 汇率数据自动更新（美元基准）

**更新时间**：2026-02-03 12:07:05（北京时间）

## Excel 表格（制表符分隔）

Currency	USD	CNY	HKD	EUR	GBP	JPY
USD		6.9381	7.8118	0.8463	0.7306	155.4540
CNY	0.1441		1.1259	0.1220	0.1053	22.4058
HKD	0.1280	0.8882		0.1083	0.0935	19.8999
EUR	1.1816	8.1982	9.2305		0.8633	183.6866
GBP	1.3687	9.4964	10.6923	1.1584		212.7758
JPY	0.0064	0.0446	0.0503	0.0054	0.0047	

## CSV 文件链接

https://raw.githubusercontent.com/granthuang999/exchange-rate-auto/main/exchange_rates.csv

### 数据源说明
- 优先使用 Yahoo Finance 实时汇率
- Yahoo 失败时使用 Wise 汇率
- 最后备选 ExchangeRate-API
- 以美元为基准计算所有交叉汇率

---
*数据仅供参考，交易请以银行报价为准*