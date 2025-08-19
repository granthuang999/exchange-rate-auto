# 汇率数据自动更新（美元基准）

**更新时间**：2025-08-19 11:05:14（北京时间）

## Excel 表格（制表符分隔）

Currency	USD	CNY	HKD	EUR	GBP	JPY
USD		7.1846	7.8036	0.8579	0.7407	147.8210
CNY	0.1392		1.0862	0.1194	0.1031	20.5747
HKD	0.1281	0.9207		0.1099	0.0949	18.9427
EUR	1.1656	8.3746	9.0962		0.8634	172.3056
GBP	1.3501	9.6997	10.5354	1.1582		199.5693
JPY	0.0068	0.0486	0.0528	0.0058	0.0050	

## CSV 文件链接

https://raw.githubusercontent.com/granthuang999/exchange-rate-auto/main/exchange_rates.csv

### 数据源说明
- 优先使用 Yahoo Finance 实时汇率
- Yahoo 失败时使用 Wise 汇率
- 最后备选 ExchangeRate-API
- 以美元为基准计算所有交叉汇率

---
*数据仅供参考，交易请以银行报价为准*