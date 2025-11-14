# 汇率数据自动更新（美元基准）

**更新时间**：2025-11-14 22:12:54（北京时间）

## Excel 表格（制表符分隔）

Currency	USD	CNY	HKD	EUR	GBP	JPY
USD		7.0987	7.7709	0.8595	0.7602	154.1440
CNY	0.1409		1.0947	0.1211	0.1071	21.7144
HKD	0.1287	0.9135		0.1106	0.0978	19.8361
EUR	1.1635	8.2591	9.0412		0.8845	179.3415
GBP	1.3154	9.3379	10.2222	1.1306		202.7677
JPY	0.0065	0.0461	0.0504	0.0056	0.0049	

## CSV 文件链接

https://raw.githubusercontent.com/granthuang999/exchange-rate-auto/main/exchange_rates.csv

### 数据源说明
- 优先使用 Yahoo Finance 实时汇率
- Yahoo 失败时使用 Wise 汇率
- 最后备选 ExchangeRate-API
- 以美元为基准计算所有交叉汇率

---
*数据仅供参考，交易请以银行报价为准*