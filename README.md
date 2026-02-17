# 汇率数据自动更新（美元基准）

**更新时间**：2026-02-17 22:39:32（北京时间）

## Excel 表格（制表符分隔）

Currency	USD	CNY	HKD	EUR	GBP	JPY
USD		6.9075	7.8145	0.8456	0.7394	153.4860
CNY	0.1448		1.1313	0.1224	0.1070	22.2202
HKD	0.1280	0.8839		0.1082	0.0946	19.6412
EUR	1.1826	8.1688	9.2414		0.8744	181.5114
GBP	1.3524	9.3420	10.5687	1.1436		207.5818
JPY	0.0065	0.0450	0.0509	0.0055	0.0048	

## CSV 文件链接

https://raw.githubusercontent.com/granthuang999/exchange-rate-auto/main/exchange_rates.csv

### 数据源说明
- 优先使用 Yahoo Finance 实时汇率
- Yahoo 失败时使用 Wise 汇率
- 最后备选 ExchangeRate-API
- 以美元为基准计算所有交叉汇率

---
*数据仅供参考，交易请以银行报价为准*