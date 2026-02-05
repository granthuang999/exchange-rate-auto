# 汇率数据自动更新（美元基准）

**更新时间**：2026-02-05 12:06:42（北京时间）

## Excel 表格（制表符分隔）

Currency	USD	CNY	HKD	EUR	GBP	JPY
USD		6.9446	7.8074	0.8481	0.7339	156.8260
CNY	0.1440		1.1242	0.1221	0.1057	22.5824
HKD	0.1281	0.8895		0.1086	0.0940	20.0868
EUR	1.1791	8.1884	9.2058		0.8653	184.9145
GBP	1.3626	9.4626	10.6382	1.1556		213.6885
JPY	0.0064	0.0443	0.0498	0.0054	0.0047	

## CSV 文件链接

https://raw.githubusercontent.com/granthuang999/exchange-rate-auto/main/exchange_rates.csv

### 数据源说明
- 优先使用 Yahoo Finance 实时汇率
- Yahoo 失败时使用 Wise 汇率
- 最后备选 ExchangeRate-API
- 以美元为基准计算所有交叉汇率

---
*数据仅供参考，交易请以银行报价为准*