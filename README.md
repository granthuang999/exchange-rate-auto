# 汇率数据自动更新（美元基准）

**更新时间**：2025-10-23 10:58:30（北京时间）

## Excel 表格（制表符分隔）

Currency	USD	CNY	HKD	EUR	GBP	JPY
USD		7.1229	7.7709	0.8620	0.7498	152.4440
CNY	0.1404		1.0910	0.1210	0.1053	21.4020
HKD	0.1287	0.9166		0.1109	0.0965	19.6173
EUR	1.1601	8.2632	9.0150		0.8698	176.8492
GBP	1.3337	9.4997	10.3640	1.1496		203.3129
JPY	0.0066	0.0467	0.0510	0.0057	0.0049	

## CSV 文件链接

https://raw.githubusercontent.com/granthuang999/exchange-rate-auto/main/exchange_rates.csv

### 数据源说明
- 优先使用 Yahoo Finance 实时汇率
- Yahoo 失败时使用 Wise 汇率
- 最后备选 ExchangeRate-API
- 以美元为基准计算所有交叉汇率

---
*数据仅供参考，交易请以银行报价为准*