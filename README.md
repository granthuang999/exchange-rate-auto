# 汇率数据自动更新（美元基准）

**更新时间**：2025-09-09 10:56:54（北京时间）

## Excel 表格（制表符分隔）

Currency	USD	CNY	HKD	EUR	GBP	JPY
USD		7.1229	7.7878	0.8495	0.7372	147.3210
CNY	0.1404		1.0933	0.1193	0.1035	20.6827
HKD	0.1284	0.9146		0.1091	0.0947	18.9169
EUR	1.1772	8.3848	9.1675		0.8678	173.4208
GBP	1.3565	9.6621	10.5640	1.1523		199.8386
JPY	0.0068	0.0483	0.0529	0.0058	0.0050	

## CSV 文件链接

https://raw.githubusercontent.com/granthuang999/exchange-rate-auto/main/exchange_rates.csv

### 数据源说明
- 优先使用 Yahoo Finance 实时汇率
- Yahoo 失败时使用 Wise 汇率
- 最后备选 ExchangeRate-API
- 以美元为基准计算所有交叉汇率

---
*数据仅供参考，交易请以银行报价为准*