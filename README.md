# 汇率数据自动更新（美元基准）

**更新时间**：2025-08-21 22:13:02（北京时间）

## Excel 表格（制表符分隔）

Currency	USD	CNY	HKD	EUR	GBP	JPY
USD		7.1792	7.8131	0.8598	0.7441	147.9100
CNY	0.1393		1.0883	0.1198	0.1036	20.6026
HKD	0.1280	0.9189		0.1100	0.0952	18.9310
EUR	1.1631	8.3498	9.0871		0.8654	172.0284
GBP	1.3439	9.6482	10.5001	1.1555		198.7770
JPY	0.0068	0.0485	0.0528	0.0058	0.0050	

## CSV 文件链接

https://raw.githubusercontent.com/granthuang999/exchange-rate-auto/main/exchange_rates.csv

### 数据源说明
- 优先使用 Yahoo Finance 实时汇率
- Yahoo 失败时使用 Wise 汇率
- 最后备选 ExchangeRate-API
- 以美元为基准计算所有交叉汇率

---
*数据仅供参考，交易请以银行报价为准*