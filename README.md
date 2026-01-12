# 汇率数据自动更新（美元基准）

**更新时间**：2026-01-12 11:41:59（北京时间）

## Excel 表格（制表符分隔）

Currency	USD	CNY	HKD	EUR	GBP	JPY
USD		6.9747	7.7936	0.8577	0.7449	158.0560
CNY	0.1434		1.1174	0.1230	0.1068	22.6613
HKD	0.1283	0.8949		0.1101	0.0956	20.2802
EUR	1.1659	8.1319	9.0866		0.8685	184.2789
GBP	1.3425	9.3633	10.4626	1.1514		212.1842
JPY	0.0063	0.0441	0.0493	0.0054	0.0047	

## CSV 文件链接

https://raw.githubusercontent.com/granthuang999/exchange-rate-auto/main/exchange_rates.csv

### 数据源说明
- 优先使用 Yahoo Finance 实时汇率
- Yahoo 失败时使用 Wise 汇率
- 最后备选 ExchangeRate-API
- 以美元为基准计算所有交叉汇率

---
*数据仅供参考，交易请以银行报价为准*