# 汇率数据自动更新（美元基准）

**更新时间**：2026-03-25 12:11:35（北京时间）

## Excel 表格（制表符分隔）

Currency	USD	CNY	HKD	EUR	GBP	JPY
USD		6.8925	7.8274	0.8619	0.7465	158.8880
CNY	0.1451		1.1356	0.1250	0.1083	23.0523
HKD	0.1278	0.8806		0.1101	0.0954	20.2989
EUR	1.1602	7.9969	9.0816		0.8661	184.3462
GBP	1.3396	9.2331	10.4855	1.1546		212.8439
JPY	0.0063	0.0434	0.0493	0.0054	0.0047	

## CSV 文件链接

https://raw.githubusercontent.com/granthuang999/exchange-rate-auto/main/exchange_rates.csv

### 数据源说明
- 优先使用 Yahoo Finance 实时汇率
- Yahoo 失败时使用 Wise 汇率
- 最后备选 ExchangeRate-API
- 以美元为基准计算所有交叉汇率

---
*数据仅供参考，交易请以银行报价为准*