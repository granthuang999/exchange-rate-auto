# 汇率数据自动更新（美元基准）

**更新时间**：2025-09-15 22:13:02（北京时间）

## Excel 表格（制表符分隔）

Currency	USD	CNY	HKD	EUR	GBP	JPY
USD		7.1191	7.7782	0.8505	0.7359	147.3890
CNY	0.1405		1.0926	0.1195	0.1034	20.7033
HKD	0.1286	0.9153		0.1093	0.0946	18.9490
EUR	1.1758	8.3705	9.1454		0.8653	173.2969
GBP	1.3589	9.6740	10.5696	1.1557		200.2840
JPY	0.0068	0.0483	0.0528	0.0058	0.0050	

## CSV 文件链接

https://raw.githubusercontent.com/granthuang999/exchange-rate-auto/main/exchange_rates.csv

### 数据源说明
- 优先使用 Yahoo Finance 实时汇率
- Yahoo 失败时使用 Wise 汇率
- 最后备选 ExchangeRate-API
- 以美元为基准计算所有交叉汇率

---
*数据仅供参考，交易请以银行报价为准*