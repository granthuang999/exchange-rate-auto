# 汇率数据自动更新（美元基准）

**更新时间**：2026-01-30 22:28:34（北京时间）

## Excel 表格（制表符分隔）

Currency	USD	CNY	HKD	EUR	GBP	JPY
USD		6.9500	7.8074	0.8396	0.7274	154.3880
CNY	0.1439		1.1234	0.1208	0.1047	22.2141
HKD	0.1281	0.8902		0.1075	0.0932	19.7746
EUR	1.1910	8.2778	9.2990		0.8664	183.8828
GBP	1.3748	9.5546	10.7333	1.1542		212.2464
JPY	0.0065	0.0450	0.0506	0.0054	0.0047	

## CSV 文件链接

https://raw.githubusercontent.com/granthuang999/exchange-rate-auto/main/exchange_rates.csv

### 数据源说明
- 优先使用 Yahoo Finance 实时汇率
- Yahoo 失败时使用 Wise 汇率
- 最后备选 ExchangeRate-API
- 以美元为基准计算所有交叉汇率

---
*数据仅供参考，交易请以银行报价为准*