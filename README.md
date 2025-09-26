# 汇率数据自动更新（美元基准）

**更新时间**：2025-09-26 10:54:42（北京时间）

## Excel 表格（制表符分隔）

Currency	USD	CNY	HKD	EUR	GBP	JPY
USD		7.1319	7.7823	0.8560	0.7488	149.7030
CNY	0.1402		1.0912	0.1200	0.1050	20.9906
HKD	0.1285	0.9164		0.1100	0.0962	19.2363
EUR	1.1682	8.3317	9.0915		0.8748	174.8867
GBP	1.3355	9.5244	10.3930	1.1432		199.9239
JPY	0.0067	0.0476	0.0520	0.0057	0.0050	

## CSV 文件链接

https://raw.githubusercontent.com/granthuang999/exchange-rate-auto/main/exchange_rates.csv

### 数据源说明
- 优先使用 Yahoo Finance 实时汇率
- Yahoo 失败时使用 Wise 汇率
- 最后备选 ExchangeRate-API
- 以美元为基准计算所有交叉汇率

---
*数据仅供参考，交易请以银行报价为准*