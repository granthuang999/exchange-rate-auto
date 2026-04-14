# 汇率数据自动更新（美元基准）

**更新时间**：2026-04-14 23:06:44（北京时间）

## Excel 表格（制表符分隔）

Currency	USD	CNY	HKD	EUR	GBP	JPY
USD		6.8151	7.8324	0.8472	0.7366	158.8000
CNY	0.1467		1.1493	0.1243	0.1081	23.3012
HKD	0.1277	0.8701		0.1082	0.0940	20.2748
EUR	1.1804	8.0443	9.2450		0.8695	187.4410
GBP	1.3576	9.2521	10.6332	1.1501		215.5851
JPY	0.0063	0.0429	0.0493	0.0053	0.0046	

## CSV 文件链接

https://raw.githubusercontent.com/granthuang999/exchange-rate-auto/main/exchange_rates.csv

### 数据源说明
- 优先使用 Yahoo Finance 实时汇率
- Yahoo 失败时使用 Wise 汇率
- 最后备选 ExchangeRate-API
- 以美元为基准计算所有交叉汇率

---
*数据仅供参考，交易请以银行报价为准*