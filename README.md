# 汇率数据自动更新（美元基准）

**更新时间**：2026-01-26 22:20:53（北京时间）

## Excel 表格（制表符分隔）

Currency	USD	CNY	HKD	EUR	GBP	JPY
USD		6.9537	7.7972	0.8427	0.7313	153.9050
CNY	0.1438		1.1213	0.1212	0.1052	22.1328
HKD	0.1283	0.8918		0.1081	0.0938	19.7385
EUR	1.1867	8.2517	9.2526		0.8678	182.6332
GBP	1.3674	9.5087	10.6621	1.1523		210.4540
JPY	0.0065	0.0452	0.0507	0.0055	0.0048	

## CSV 文件链接

https://raw.githubusercontent.com/granthuang999/exchange-rate-auto/main/exchange_rates.csv

### 数据源说明
- 优先使用 Yahoo Finance 实时汇率
- Yahoo 失败时使用 Wise 汇率
- 最后备选 ExchangeRate-API
- 以美元为基准计算所有交叉汇率

---
*数据仅供参考，交易请以银行报价为准*