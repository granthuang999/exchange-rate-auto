# 汇率数据自动更新（美元基准）

**更新时间**：2025-10-27 22:13:06（北京时间）

## Excel 表格（制表符分隔）

Currency	USD	CNY	HKD	EUR	GBP	JPY
USD		7.1076	7.7672	0.8590	0.7502	153.0870
CNY	0.1407		1.0928	0.1209	0.1055	21.5385
HKD	0.1287	0.9151		0.1106	0.0966	19.7094
EUR	1.1641	8.2743	9.0421		0.8733	178.2154
GBP	1.3330	9.4743	10.3535	1.1450		204.0616
JPY	0.0065	0.0464	0.0507	0.0056	0.0049	

## CSV 文件链接

https://raw.githubusercontent.com/granthuang999/exchange-rate-auto/main/exchange_rates.csv

### 数据源说明
- 优先使用 Yahoo Finance 实时汇率
- Yahoo 失败时使用 Wise 汇率
- 最后备选 ExchangeRate-API
- 以美元为基准计算所有交叉汇率

---
*数据仅供参考，交易请以银行报价为准*