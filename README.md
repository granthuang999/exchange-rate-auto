# 汇率数据自动更新（美元基准）

**更新时间**：2025-09-16 10:51:21（北京时间）

## Excel 表格（制表符分隔）

Currency	USD	CNY	HKD	EUR	GBP	JPY
USD		7.1166	7.7773	0.8489	0.7346	147.1360
CNY	0.1405		1.0928	0.1193	0.1032	20.6750
HKD	0.1286	0.9150		0.1092	0.0945	18.9186
EUR	1.1780	8.3833	9.1616		0.8654	173.3255
GBP	1.3613	9.6877	10.5871	1.1556		200.2940
JPY	0.0068	0.0484	0.0529	0.0058	0.0050	

## CSV 文件链接

https://raw.githubusercontent.com/granthuang999/exchange-rate-auto/main/exchange_rates.csv

### 数据源说明
- 优先使用 Yahoo Finance 实时汇率
- Yahoo 失败时使用 Wise 汇率
- 最后备选 ExchangeRate-API
- 以美元为基准计算所有交叉汇率

---
*数据仅供参考，交易请以银行报价为准*