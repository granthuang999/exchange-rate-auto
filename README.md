# 汇率数据自动更新（美元基准）

**更新时间**：2026-03-02 12:05:48（北京时间）

## Excel 表格（制表符分隔）

Currency	USD	CNY	HKD	EUR	GBP	JPY
USD		6.8683	7.8229	0.8479	0.7435	156.2970
CNY	0.1456		1.1390	0.1235	0.1083	22.7563
HKD	0.1278	0.8780		0.1084	0.0950	19.9794
EUR	1.1794	8.1004	9.2262		0.8769	184.3342
GBP	1.3450	9.2378	10.5217	1.1404		210.2179
JPY	0.0064	0.0439	0.0501	0.0054	0.0048	

## CSV 文件链接

https://raw.githubusercontent.com/granthuang999/exchange-rate-auto/main/exchange_rates.csv

### 数据源说明
- 优先使用 Yahoo Finance 实时汇率
- Yahoo 失败时使用 Wise 汇率
- 最后备选 ExchangeRate-API
- 以美元为基准计算所有交叉汇率

---
*数据仅供参考，交易请以银行报价为准*