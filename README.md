# 汇率数据自动更新（美元基准）

**更新时间**：2026-02-12 22:42:10（北京时间）

## Excel 表格（制表符分隔）

Currency	USD	CNY	HKD	EUR	GBP	JPY
USD		6.9005	7.8160	0.8412	0.7319	153.0540
CNY	0.1449		1.1327	0.1219	0.1061	22.1801
HKD	0.1279	0.8829		0.1076	0.0936	19.5821
EUR	1.1888	8.2032	9.2915		0.8701	181.9472
GBP	1.3663	9.4282	10.6791	1.1493		209.1187
JPY	0.0065	0.0451	0.0511	0.0055	0.0048	

## CSV 文件链接

https://raw.githubusercontent.com/granthuang999/exchange-rate-auto/main/exchange_rates.csv

### 数据源说明
- 优先使用 Yahoo Finance 实时汇率
- Yahoo 失败时使用 Wise 汇率
- 最后备选 ExchangeRate-API
- 以美元为基准计算所有交叉汇率

---
*数据仅供参考，交易请以银行报价为准*