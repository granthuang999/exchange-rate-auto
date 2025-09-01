# 汇率数据自动更新（美元基准）

**更新时间**：2025-09-01 11:15:27（北京时间）

## Excel 表格（制表符分隔）

Currency	USD	CNY	HKD	EUR	GBP	JPY
USD		7.1300	7.7930	0.8535	0.7393	146.9290
CNY	0.1403		1.0930	0.1197	0.1037	20.6072
HKD	0.1283	0.9149		0.1095	0.0949	18.8540
EUR	1.1716	8.3538	9.1306		0.8662	172.1488
GBP	1.3526	9.6443	10.5411	1.1545		198.7407
JPY	0.0068	0.0485	0.0530	0.0058	0.0050	

## CSV 文件链接

https://raw.githubusercontent.com/granthuang999/exchange-rate-auto/main/exchange_rates.csv

### 数据源说明
- 优先使用 Yahoo Finance 实时汇率
- Yahoo 失败时使用 Wise 汇率
- 最后备选 ExchangeRate-API
- 以美元为基准计算所有交叉汇率

---
*数据仅供参考，交易请以银行报价为准*