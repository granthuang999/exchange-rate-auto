# 汇率数据自动更新（美元基准）

**更新时间**：2026-01-29 12:00:59（北京时间）

## Excel 表格（制表符分隔）

Currency	USD	CNY	HKD	EUR	GBP	JPY
USD		6.9467	7.8024	0.8339	0.7228	152.9030
CNY	0.1440		1.1232	0.1200	0.1040	22.0109
HKD	0.1282	0.8903		0.1069	0.0926	19.5969
EUR	1.1992	8.3304	9.3565		0.8668	183.3589
GBP	1.3835	9.6108	10.7947	1.1537		211.5426
JPY	0.0065	0.0454	0.0510	0.0055	0.0047	

## CSV 文件链接

https://raw.githubusercontent.com/granthuang999/exchange-rate-auto/main/exchange_rates.csv

### 数据源说明
- 优先使用 Yahoo Finance 实时汇率
- Yahoo 失败时使用 Wise 汇率
- 最后备选 ExchangeRate-API
- 以美元为基准计算所有交叉汇率

---
*数据仅供参考，交易请以银行报价为准*