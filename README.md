# 汇率数据自动更新（美元基准）

**更新时间**：2025-09-25 22:12:38（北京时间）

## Excel 表格（制表符分隔）

Currency	USD	CNY	HKD	EUR	GBP	JPY
USD		7.1313	7.7790	0.8553	0.7474	149.4400
CNY	0.1402		1.0908	0.1199	0.1048	20.9555
HKD	0.1286	0.9167		0.1099	0.0961	19.2107
EUR	1.1692	8.3378	9.0951		0.8738	174.7223
GBP	1.3380	9.5415	10.4081	1.1444		199.9465
JPY	0.0067	0.0477	0.0521	0.0057	0.0050	

## CSV 文件链接

https://raw.githubusercontent.com/granthuang999/exchange-rate-auto/main/exchange_rates.csv

### 数据源说明
- 优先使用 Yahoo Finance 实时汇率
- Yahoo 失败时使用 Wise 汇率
- 最后备选 ExchangeRate-API
- 以美元为基准计算所有交叉汇率

---
*数据仅供参考，交易请以银行报价为准*