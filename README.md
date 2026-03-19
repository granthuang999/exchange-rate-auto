# 汇率数据自动更新（美元基准）

**更新时间**：2026-03-19 12:14:10（北京时间）

## Excel 表格（制表符分隔）

Currency	USD	CNY	HKD	EUR	GBP	JPY
USD		6.8983	7.8389	0.8714	0.7532	159.5880
CNY	0.1450		1.1364	0.1263	0.1092	23.1344
HKD	0.1276	0.8800		0.1112	0.0961	20.3585
EUR	1.1476	7.9163	8.9958		0.8644	183.1398
GBP	1.3277	9.1587	10.4075	1.1569		211.8800
JPY	0.0063	0.0432	0.0491	0.0055	0.0047	

## CSV 文件链接

https://raw.githubusercontent.com/granthuang999/exchange-rate-auto/main/exchange_rates.csv

### 数据源说明
- 优先使用 Yahoo Finance 实时汇率
- Yahoo 失败时使用 Wise 汇率
- 最后备选 ExchangeRate-API
- 以美元为基准计算所有交叉汇率

---
*数据仅供参考，交易请以银行报价为准*