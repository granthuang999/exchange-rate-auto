# 汇率数据自动更新（美元基准）

**更新时间**：2026-03-02 22:37:31（北京时间）

## Excel 表格（制表符分隔）

Currency	USD	CNY	HKD	EUR	GBP	JPY
USD		6.8816	7.8218	0.8532	0.7459	157.4370
CNY	0.1453		1.1366	0.1240	0.1084	22.8780
HKD	0.1278	0.8798		0.1091	0.0954	20.1280
EUR	1.1721	8.0656	9.1676		0.8742	184.5253
GBP	1.3407	9.2259	10.4864	1.1439		211.0698
JPY	0.0064	0.0437	0.0497	0.0054	0.0047	

## CSV 文件链接

https://raw.githubusercontent.com/granthuang999/exchange-rate-auto/main/exchange_rates.csv

### 数据源说明
- 优先使用 Yahoo Finance 实时汇率
- Yahoo 失败时使用 Wise 汇率
- 最后备选 ExchangeRate-API
- 以美元为基准计算所有交叉汇率

---
*数据仅供参考，交易请以银行报价为准*