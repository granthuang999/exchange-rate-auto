# 汇率数据自动更新（美元基准）

**更新时间**：2025-10-21 11:00:24（北京时间）

## Excel 表格（制表符分隔）

Currency	USD	CNY	HKD	EUR	GBP	JPY
USD		7.1170	7.7668	0.8593	0.7466	151.1080
CNY	0.1405		1.0913	0.1207	0.1049	21.2320
HKD	0.1288	0.9163		0.1106	0.0961	19.4556
EUR	1.1637	8.2823	9.0385		0.8688	175.8501
GBP	1.3394	9.5325	10.4029	1.1510		202.3949
JPY	0.0066	0.0471	0.0514	0.0057	0.0049	

## CSV 文件链接

https://raw.githubusercontent.com/granthuang999/exchange-rate-auto/main/exchange_rates.csv

### 数据源说明
- 优先使用 Yahoo Finance 实时汇率
- Yahoo 失败时使用 Wise 汇率
- 最后备选 ExchangeRate-API
- 以美元为基准计算所有交叉汇率

---
*数据仅供参考，交易请以银行报价为准*