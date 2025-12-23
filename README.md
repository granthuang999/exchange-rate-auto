# 汇率数据自动更新（美元基准）

**更新时间**：2025-12-23 11:20:04（北京时间）

## Excel 表格（制表符分隔）

Currency	USD	CNY	HKD	EUR	GBP	JPY
USD		7.0291	7.7774	0.8490	0.7417	156.2980
CNY	0.1423		1.1065	0.1208	0.1055	22.2358
HKD	0.1286	0.9038		0.1092	0.0954	20.0964
EUR	1.1779	8.2793	9.1607		0.8736	184.0966
GBP	1.3483	9.4770	10.4859	1.1447		210.7294
JPY	0.0064	0.0450	0.0498	0.0054	0.0047	

## CSV 文件链接

https://raw.githubusercontent.com/granthuang999/exchange-rate-auto/main/exchange_rates.csv

### 数据源说明
- 优先使用 Yahoo Finance 实时汇率
- Yahoo 失败时使用 Wise 汇率
- 最后备选 ExchangeRate-API
- 以美元为基准计算所有交叉汇率

---
*数据仅供参考，交易请以银行报价为准*