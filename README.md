# 汇率数据自动更新（美元基准）

**更新时间**：2025-09-17 10:50:01（北京时间）

## Excel 表格（制表符分隔）

Currency	USD	CNY	HKD	EUR	GBP	JPY
USD		7.1067	7.7780	0.8433	0.7329	146.5350
CNY	0.1407		1.0945	0.1187	0.1031	20.6193
HKD	0.1286	0.9137		0.1084	0.0942	18.8397
EUR	1.1858	8.4273	9.2233		0.8691	173.7638
GBP	1.3644	9.6967	10.6126	1.1506		199.9386
JPY	0.0068	0.0485	0.0531	0.0058	0.0050	

## CSV 文件链接

https://raw.githubusercontent.com/granthuang999/exchange-rate-auto/main/exchange_rates.csv

### 数据源说明
- 优先使用 Yahoo Finance 实时汇率
- Yahoo 失败时使用 Wise 汇率
- 最后备选 ExchangeRate-API
- 以美元为基准计算所有交叉汇率

---
*数据仅供参考，交易请以银行报价为准*