# 汇率数据自动更新（美元基准）

**更新时间**：2025-09-26 22:11:42（北京时间）

## Excel 表格（制表符分隔）

Currency	USD	CNY	HKD	EUR	GBP	JPY
USD		7.1345	7.7807	0.8549	0.7467	149.6640
CNY	0.1402		1.0906	0.1198	0.1047	20.9775
HKD	0.1285	0.9169		0.1099	0.0960	19.2353
EUR	1.1697	8.3454	9.1013		0.8734	175.0661
GBP	1.3392	9.5547	10.4201	1.1449		200.4339
JPY	0.0067	0.0477	0.0520	0.0057	0.0050	

## CSV 文件链接

https://raw.githubusercontent.com/granthuang999/exchange-rate-auto/main/exchange_rates.csv

### 数据源说明
- 优先使用 Yahoo Finance 实时汇率
- Yahoo 失败时使用 Wise 汇率
- 最后备选 ExchangeRate-API
- 以美元为基准计算所有交叉汇率

---
*数据仅供参考，交易请以银行报价为准*