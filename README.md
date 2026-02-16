# 汇率数据自动更新（美元基准）

**更新时间**：2026-02-16 22:36:24（北京时间）

## Excel 表格（制表符分隔）

Currency	USD	CNY	HKD	EUR	GBP	JPY
USD		6.9075	7.8148	0.8428	0.7333	153.2840
CNY	0.1448		1.1313	0.1220	0.1062	22.1910
HKD	0.1280	0.8839		0.1078	0.0938	19.6146
EUR	1.1865	8.1959	9.2724		0.8701	181.8747
GBP	1.3637	9.4197	10.6570	1.1493		209.0331
JPY	0.0065	0.0451	0.0510	0.0055	0.0048	

## CSV 文件链接

https://raw.githubusercontent.com/granthuang999/exchange-rate-auto/main/exchange_rates.csv

### 数据源说明
- 优先使用 Yahoo Finance 实时汇率
- Yahoo 失败时使用 Wise 汇率
- 最后备选 ExchangeRate-API
- 以美元为基准计算所有交叉汇率

---
*数据仅供参考，交易请以银行报价为准*