# 汇率数据自动更新（美元基准）

**更新时间**：2025-08-27 22:12:03（北京时间）

## Excel 表格（制表符分隔）

Currency	USD	CNY	HKD	EUR	GBP	JPY
USD		7.1598	7.7862	0.8622	0.7435	148.0260
CNY	0.1397		1.0875	0.1204	0.1038	20.6746
HKD	0.1284	0.9195		0.1107	0.0955	19.0113
EUR	1.1598	8.3041	9.0306		0.8623	171.6841
GBP	1.3450	9.6299	10.4724	1.1597		199.0935
JPY	0.0068	0.0484	0.0526	0.0058	0.0050	

## CSV 文件链接

https://raw.githubusercontent.com/granthuang999/exchange-rate-auto/main/exchange_rates.csv

### 数据源说明
- 优先使用 Yahoo Finance 实时汇率
- Yahoo 失败时使用 Wise 汇率
- 最后备选 ExchangeRate-API
- 以美元为基准计算所有交叉汇率

---
*数据仅供参考，交易请以银行报价为准*