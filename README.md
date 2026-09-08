# 汇率数据自动更新（美元基准）

**更新时间**：2026-09-08 14:45:25（北京时间）

## Excel 表格（制表符分隔）

Currency	USD	CNY	HKD	EUR	GBP	JPY
USD		6.7100	7.8402	0.8599	0.7384	153.7370
CNY	0.1490		1.1684	0.1282	0.1100	22.9116
HKD	0.1275	0.8558		0.1097	0.0942	19.6088
EUR	1.1629	7.8032	9.1176		0.8587	178.7847
GBP	1.3543	9.0872	10.6178	1.1645		208.2029
JPY	0.0065	0.0436	0.0510	0.0056	0.0048	

## CSV 文件链接

https://raw.githubusercontent.com/granthuang999/exchange-rate-auto/main/exchange_rates.csv

### 数据源说明
- 优先使用 Yahoo Finance 实时汇率
- Yahoo 失败时使用 Wise 汇率
- 最后备选 ExchangeRate-API
- 以美元为基准计算所有交叉汇率

---
*数据仅供参考，交易请以银行报价为准*