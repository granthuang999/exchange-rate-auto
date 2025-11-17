# 汇率数据自动更新（美元基准）

**更新时间**：2025-11-17 11:09:44（北京时间）

## Excel 表格（制表符分隔）

Currency	USD	CNY	HKD	EUR	GBP	JPY
USD		7.1040	7.7730	0.8617	0.7606	154.7550
CNY	0.1408		1.0942	0.1213	0.1071	21.7842
HKD	0.1287	0.9139		0.1109	0.0979	19.9093
EUR	1.1605	8.2442	9.0205		0.8827	179.5927
GBP	1.3148	9.3400	10.2196	1.1329		203.4644
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