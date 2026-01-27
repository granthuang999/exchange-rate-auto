# 汇率数据自动更新（美元基准）

**更新时间**：2026-01-27 11:41:11（北京时间）

## Excel 表格（制表符分隔）

Currency	USD	CNY	HKD	EUR	GBP	JPY
USD		6.9562	7.7978	0.8409	0.7304	154.2870
CNY	0.1438		1.1210	0.1209	0.1050	22.1798
HKD	0.1282	0.8921		0.1078	0.0937	19.7860
EUR	1.1892	8.2723	9.2732		0.8686	183.4784
GBP	1.3691	9.5238	10.6761	1.1513		211.2363
JPY	0.0065	0.0451	0.0505	0.0055	0.0047	

## CSV 文件链接

https://raw.githubusercontent.com/granthuang999/exchange-rate-auto/main/exchange_rates.csv

### 数据源说明
- 优先使用 Yahoo Finance 实时汇率
- Yahoo 失败时使用 Wise 汇率
- 最后备选 ExchangeRate-API
- 以美元为基准计算所有交叉汇率

---
*数据仅供参考，交易请以银行报价为准*