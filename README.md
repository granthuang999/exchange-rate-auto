# 汇率数据自动更新（美元基准）

**更新时间**：2025-12-03 22:13:49（北京时间）

## Excel 表格（制表符分隔）

Currency	USD	CNY	HKD	EUR	GBP	JPY
USD		7.0632	7.7849	0.8571	0.7519	155.3360
CNY	0.1416		1.1022	0.1213	0.1065	21.9923
HKD	0.1285	0.9073		0.1101	0.0966	19.9535
EUR	1.1667	8.2408	9.0828		0.8773	181.2344
GBP	1.3300	9.3938	10.3536	1.1399		206.5913
JPY	0.0064	0.0455	0.0501	0.0055	0.0048	

## CSV 文件链接

https://raw.githubusercontent.com/granthuang999/exchange-rate-auto/main/exchange_rates.csv

### 数据源说明
- 优先使用 Yahoo Finance 实时汇率
- Yahoo 失败时使用 Wise 汇率
- 最后备选 ExchangeRate-API
- 以美元为基准计算所有交叉汇率

---
*数据仅供参考，交易请以银行报价为准*