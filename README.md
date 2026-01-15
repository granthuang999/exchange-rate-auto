# 汇率数据自动更新（美元基准）

**更新时间**：2026-01-15 22:17:44（北京时间）

## Excel 表格（制表符分隔）

Currency	USD	CNY	HKD	EUR	GBP	JPY
USD		6.9666	7.7981	0.8613	0.7474	158.7410
CNY	0.1435		1.1194	0.1236	0.1073	22.7860
HKD	0.1282	0.8934		0.1104	0.0958	20.3564
EUR	1.1610	8.0885	9.0539		0.8678	184.3040
GBP	1.3380	9.3211	10.4336	1.1524		212.3910
JPY	0.0063	0.0439	0.0491	0.0054	0.0047	

## CSV 文件链接

https://raw.githubusercontent.com/granthuang999/exchange-rate-auto/main/exchange_rates.csv

### 数据源说明
- 优先使用 Yahoo Finance 实时汇率
- Yahoo 失败时使用 Wise 汇率
- 最后备选 ExchangeRate-API
- 以美元为基准计算所有交叉汇率

---
*数据仅供参考，交易请以银行报价为准*