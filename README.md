# 汇率数据自动更新（美元基准）

**更新时间**：2026-04-09 12:26:35（北京时间）

## Excel 表格（制表符分隔）

Currency	USD	CNY	HKD	EUR	GBP	JPY
USD		6.8323	7.8345	0.8567	0.7461	158.6510
CNY	0.1464		1.1467	0.1254	0.1092	23.2207
HKD	0.1276	0.8721		0.1093	0.0952	20.2503
EUR	1.1673	7.9751	9.1450		0.8709	185.1885
GBP	1.3403	9.1574	10.5006	1.1482		212.6404
JPY	0.0063	0.0431	0.0494	0.0054	0.0047	

## CSV 文件链接

https://raw.githubusercontent.com/granthuang999/exchange-rate-auto/main/exchange_rates.csv

### 数据源说明
- 优先使用 Yahoo Finance 实时汇率
- Yahoo 失败时使用 Wise 汇率
- 最后备选 ExchangeRate-API
- 以美元为基准计算所有交叉汇率

---
*数据仅供参考，交易请以银行报价为准*