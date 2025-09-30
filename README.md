# 汇率数据自动更新（美元基准）

**更新时间**：2025-09-30 10:53:05（北京时间）

## Excel 表格（制表符分隔）

Currency	USD	CNY	HKD	EUR	GBP	JPY
USD		7.1254	7.7822	0.8529	0.7445	148.6580
CNY	0.1403		1.0922	0.1197	0.1045	20.8631
HKD	0.1285	0.9156		0.1096	0.0957	19.1023
EUR	1.1725	8.3543	9.1244		0.8729	174.2971
GBP	1.3432	9.5707	10.4529	1.1456		199.6749
JPY	0.0067	0.0479	0.0523	0.0057	0.0050	

## CSV 文件链接

https://raw.githubusercontent.com/granthuang999/exchange-rate-auto/main/exchange_rates.csv

### 数据源说明
- 优先使用 Yahoo Finance 实时汇率
- Yahoo 失败时使用 Wise 汇率
- 最后备选 ExchangeRate-API
- 以美元为基准计算所有交叉汇率

---
*数据仅供参考，交易请以银行报价为准*