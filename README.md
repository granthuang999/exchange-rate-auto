# 汇率数据自动更新（美元基准）

**更新时间**：2025-12-18 22:15:40（北京时间）

## Excel 表格（制表符分隔）

Currency	USD	CNY	HKD	EUR	GBP	JPY
USD		7.0400	7.7814	0.8514	0.7447	155.3940
CNY	0.1420		1.1053	0.1209	0.1058	22.0730
HKD	0.1285	0.9047		0.1094	0.0957	19.9699
EUR	1.1745	8.2687	9.1395		0.8747	182.5159
GBP	1.3428	9.4535	10.4490	1.1433		208.6666
JPY	0.0064	0.0453	0.0501	0.0055	0.0048	

## CSV 文件链接

https://raw.githubusercontent.com/granthuang999/exchange-rate-auto/main/exchange_rates.csv

### 数据源说明
- 优先使用 Yahoo Finance 实时汇率
- Yahoo 失败时使用 Wise 汇率
- 最后备选 ExchangeRate-API
- 以美元为基准计算所有交叉汇率

---
*数据仅供参考，交易请以银行报价为准*