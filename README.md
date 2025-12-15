# 汇率数据自动更新（美元基准）

**更新时间**：2025-12-15 11:23:44（北京时间）

## Excel 表格（制表符分隔）

Currency	USD	CNY	HKD	EUR	GBP	JPY
USD		7.0500	7.7824	0.8516	0.7483	155.3960
CNY	0.1418		1.1039	0.1208	0.1061	22.0420
HKD	0.1285	0.9059		0.1094	0.0962	19.9676
EUR	1.1743	8.2785	9.1386		0.8787	182.4753
GBP	1.3364	9.4214	10.4001	1.1380		207.6654
JPY	0.0064	0.0454	0.0501	0.0055	0.0048	

## CSV 文件链接

https://raw.githubusercontent.com/granthuang999/exchange-rate-auto/main/exchange_rates.csv

### 数据源说明
- 优先使用 Yahoo Finance 实时汇率
- Yahoo 失败时使用 Wise 汇率
- 最后备选 ExchangeRate-API
- 以美元为基准计算所有交叉汇率

---
*数据仅供参考，交易请以银行报价为准*