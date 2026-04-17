# 汇率数据自动更新（美元基准）

**更新时间**：2026-04-17 12:42:58（北京时间）

## Excel 表格（制表符分隔）

Currency	USD	CNY	HKD	EUR	GBP	JPY
USD		6.8241	7.8285	0.8484	0.7394	159.4210
CNY	0.1465		1.1472	0.1243	0.1084	23.3615
HKD	0.1277	0.8717		0.1084	0.0944	20.3642
EUR	1.1787	8.0435	9.2274		0.8715	187.9078
GBP	1.3524	9.2292	10.5876	1.1474		215.6086
JPY	0.0063	0.0428	0.0491	0.0053	0.0046	

## CSV 文件链接

https://raw.githubusercontent.com/granthuang999/exchange-rate-auto/main/exchange_rates.csv

### 数据源说明
- 优先使用 Yahoo Finance 实时汇率
- Yahoo 失败时使用 Wise 汇率
- 最后备选 ExchangeRate-API
- 以美元为基准计算所有交叉汇率

---
*数据仅供参考，交易请以银行报价为准*