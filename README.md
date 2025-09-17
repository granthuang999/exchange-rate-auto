# 汇率数据自动更新（美元基准）

**更新时间**：2025-09-17 22:12:10（北京时间）

## Excel 表格（制表符分隔）

Currency	USD	CNY	HKD	EUR	GBP	JPY
USD		7.1030	7.7760	0.8435	0.7319	146.2740
CNY	0.1408		1.0947	0.1188	0.1030	20.5933
HKD	0.1286	0.9135		0.1085	0.0941	18.8110
EUR	1.1855	8.4209	9.2187		0.8677	173.4132
GBP	1.3663	9.7049	10.6244	1.1525		199.8552
JPY	0.0068	0.0486	0.0532	0.0058	0.0050	

## CSV 文件链接

https://raw.githubusercontent.com/granthuang999/exchange-rate-auto/main/exchange_rates.csv

### 数据源说明
- 优先使用 Yahoo Finance 实时汇率
- Yahoo 失败时使用 Wise 汇率
- 最后备选 ExchangeRate-API
- 以美元为基准计算所有交叉汇率

---
*数据仅供参考，交易请以银行报价为准*