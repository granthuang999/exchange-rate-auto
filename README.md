# 汇率数据自动更新（美元基准）

**更新时间**：2025-09-18 22:12:51（北京时间）

## Excel 表格（制表符分隔）

Currency	USD	CNY	HKD	EUR	GBP	JPY
USD		7.1093	7.7773	0.8490	0.7369	147.9900
CNY	0.1407		1.0940	0.1194	0.1037	20.8164
HKD	0.1286	0.9141		0.1092	0.0948	19.0285
EUR	1.1779	8.3737	9.1605		0.8680	174.3110
GBP	1.3570	9.6476	10.5541	1.1521		200.8278
JPY	0.0068	0.0480	0.0526	0.0057	0.0050	

## CSV 文件链接

https://raw.githubusercontent.com/granthuang999/exchange-rate-auto/main/exchange_rates.csv

### 数据源说明
- 优先使用 Yahoo Finance 实时汇率
- Yahoo 失败时使用 Wise 汇率
- 最后备选 ExchangeRate-API
- 以美元为基准计算所有交叉汇率

---
*数据仅供参考，交易请以银行报价为准*