# 汇率数据自动更新（美元基准）

**更新时间**：2026-02-03 22:38:15（北京时间）

## Excel 表格（制表符分隔）

Currency	USD	CNY	HKD	EUR	GBP	JPY
USD		6.9369	7.8124	0.8478	0.7315	155.9360
CNY	0.1442		1.1262	0.1222	0.1055	22.4792
HKD	0.1280	0.8879		0.1085	0.0936	19.9601
EUR	1.1795	8.1822	9.2149		0.8628	183.9302
GBP	1.3671	9.4831	10.6800	1.1590		213.1729
JPY	0.0064	0.0445	0.0501	0.0054	0.0047	

## CSV 文件链接

https://raw.githubusercontent.com/granthuang999/exchange-rate-auto/main/exchange_rates.csv

### 数据源说明
- 优先使用 Yahoo Finance 实时汇率
- Yahoo 失败时使用 Wise 汇率
- 最后备选 ExchangeRate-API
- 以美元为基准计算所有交叉汇率

---
*数据仅供参考，交易请以银行报价为准*