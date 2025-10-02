# 汇率数据自动更新（美元基准）

**更新时间**：2025-10-02 10:51:59（北京时间）

## Excel 表格（制表符分隔）

Currency	USD	CNY	HKD	EUR	GBP	JPY
USD		7.1185	7.7800	0.8516	0.7416	147.1490
CNY	0.1405		1.0929	0.1196	0.1042	20.6713
HKD	0.1285	0.9150		0.1095	0.0953	18.9138
EUR	1.1743	8.3590	9.1357		0.8708	172.7912
GBP	1.3484	9.5988	10.4908	1.1483		198.4210
JPY	0.0068	0.0484	0.0529	0.0058	0.0050	

## CSV 文件链接

https://raw.githubusercontent.com/granthuang999/exchange-rate-auto/main/exchange_rates.csv

### 数据源说明
- 优先使用 Yahoo Finance 实时汇率
- Yahoo 失败时使用 Wise 汇率
- 最后备选 ExchangeRate-API
- 以美元为基准计算所有交叉汇率

---
*数据仅供参考，交易请以银行报价为准*