# 汇率数据自动更新（美元基准）

**更新时间**：2025-10-22 11:05:17（北京时间）

## Excel 表格（制表符分隔）

Currency	USD	CNY	HKD	EUR	GBP	JPY
USD		7.1232	7.7714	0.8612	0.7476	151.6520
CNY	0.1404		1.0910	0.1209	0.1050	21.2899
HKD	0.1287	0.9166		0.1108	0.0962	19.5141
EUR	1.1612	8.2712	9.0239		0.8681	176.0938
GBP	1.3376	9.5281	10.3951	1.1520		202.8518
JPY	0.0066	0.0470	0.0512	0.0057	0.0049	

## CSV 文件链接

https://raw.githubusercontent.com/granthuang999/exchange-rate-auto/main/exchange_rates.csv

### 数据源说明
- 优先使用 Yahoo Finance 实时汇率
- Yahoo 失败时使用 Wise 汇率
- 最后备选 ExchangeRate-API
- 以美元为基准计算所有交叉汇率

---
*数据仅供参考，交易请以银行报价为准*