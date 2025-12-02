# 汇率数据自动更新（美元基准）

**更新时间**：2025-12-02 11:12:16（北京时间）

## Excel 表格（制表符分隔）

Currency	USD	CNY	HKD	EUR	GBP	JPY
USD		7.0753	7.7877	0.8611	0.7567	155.6650
CNY	0.1413		1.1007	0.1217	0.1069	22.0012
HKD	0.1284	0.9085		0.1106	0.0972	19.9886
EUR	1.1613	8.2166	9.0439		0.8788	180.7746
GBP	1.3215	9.3502	10.2917	1.1380		205.7156
JPY	0.0064	0.0455	0.0500	0.0055	0.0049	

## CSV 文件链接

https://raw.githubusercontent.com/granthuang999/exchange-rate-auto/main/exchange_rates.csv

### 数据源说明
- 优先使用 Yahoo Finance 实时汇率
- Yahoo 失败时使用 Wise 汇率
- 最后备选 ExchangeRate-API
- 以美元为基准计算所有交叉汇率

---
*数据仅供参考，交易请以银行报价为准*