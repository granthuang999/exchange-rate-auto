# 汇率数据自动更新（美元基准）

**更新时间**：2026-09-07 14:49:22（北京时间）

## Excel 表格（制表符分隔）

Currency	USD	CNY	HKD	EUR	GBP	JPY
USD		6.6989	7.8392	0.8606	0.7392	155.7790
CNY	0.1493		1.1702	0.1285	0.1103	23.2544
HKD	0.1276	0.8545		0.1098	0.0943	19.8718
EUR	1.1620	7.7840	9.1090		0.8589	181.0121
GBP	1.3528	9.0624	10.6050	1.1642		210.7400
JPY	0.0064	0.0430	0.0503	0.0055	0.0047	

## CSV 文件链接

https://raw.githubusercontent.com/granthuang999/exchange-rate-auto/main/exchange_rates.csv

### 数据源说明
- 优先使用 Yahoo Finance 实时汇率
- Yahoo 失败时使用 Wise 汇率
- 最后备选 ExchangeRate-API
- 以美元为基准计算所有交叉汇率

---
*数据仅供参考，交易请以银行报价为准*