# 汇率数据自动更新（美元基准）

**更新时间**：2026-01-07 22:16:53（北京时间）

## Excel 表格（制表符分隔）

Currency	USD	CNY	HKD	EUR	GBP	JPY
USD		7.0038	7.7864	0.8551	0.7413	156.4590
CNY	0.1428		1.1117	0.1221	0.1058	22.3392
HKD	0.1284	0.8995		0.1098	0.0952	20.0939
EUR	1.1695	8.1906	9.1058		0.8669	182.9716
GBP	1.3490	9.4480	10.5037	1.1535		211.0603
JPY	0.0064	0.0448	0.0498	0.0055	0.0047	

## CSV 文件链接

https://raw.githubusercontent.com/granthuang999/exchange-rate-auto/main/exchange_rates.csv

### 数据源说明
- 优先使用 Yahoo Finance 实时汇率
- Yahoo 失败时使用 Wise 汇率
- 最后备选 ExchangeRate-API
- 以美元为基准计算所有交叉汇率

---
*数据仅供参考，交易请以银行报价为准*