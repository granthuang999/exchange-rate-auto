# 汇率数据自动更新（美元基准）

**更新时间**：2025-11-17 22:13:13（北京时间）

## Excel 表格（制表符分隔）

Currency	USD	CNY	HKD	EUR	GBP	JPY
USD		7.1071	7.7733	0.8624	0.7589	154.8920
CNY	0.1407		1.0937	0.1213	0.1068	21.7940
HKD	0.1286	0.9143		0.1109	0.0976	19.9262
EUR	1.1596	8.2411	9.0136		0.8800	179.6058
GBP	1.3177	9.3650	10.2429	1.1364		204.1007
JPY	0.0065	0.0459	0.0502	0.0056	0.0049	

## CSV 文件链接

https://raw.githubusercontent.com/granthuang999/exchange-rate-auto/main/exchange_rates.csv

### 数据源说明
- 优先使用 Yahoo Finance 实时汇率
- Yahoo 失败时使用 Wise 汇率
- 最后备选 ExchangeRate-API
- 以美元为基准计算所有交叉汇率

---
*数据仅供参考，交易请以银行报价为准*