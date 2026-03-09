# 汇率数据自动更新（美元基准）

**更新时间**：2026-03-09 22:42:27（北京时间）

## Excel 表格（制表符分隔）

Currency	USD	CNY	HKD	EUR	GBP	JPY
USD		6.9140	7.8169	0.8645	0.7481	158.3800
CNY	0.1446		1.1306	0.1250	0.1082	22.9071
HKD	0.1279	0.8845		0.1106	0.0957	20.2612
EUR	1.1567	7.9977	9.0421		0.8654	183.2042
GBP	1.3367	9.2421	10.4490	1.1556		211.7097
JPY	0.0063	0.0437	0.0494	0.0055	0.0047	

## CSV 文件链接

https://raw.githubusercontent.com/granthuang999/exchange-rate-auto/main/exchange_rates.csv

### 数据源说明
- 优先使用 Yahoo Finance 实时汇率
- Yahoo 失败时使用 Wise 汇率
- 最后备选 ExchangeRate-API
- 以美元为基准计算所有交叉汇率

---
*数据仅供参考，交易请以银行报价为准*