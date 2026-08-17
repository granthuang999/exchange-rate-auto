# 汇率数据自动更新（美元基准）

**更新时间**：2026-08-17 22:18:01（北京时间）

## Excel 表格（制表符分隔）

Currency	USD	CNY	HKD	EUR	GBP	JPY
USD		6.7287	7.8450	0.8620	0.7371	159.2130
CNY	0.1486		1.1659	0.1281	0.1095	23.6618
HKD	0.1275	0.8577		0.1099	0.0940	20.2948
EUR	1.1601	7.8059	9.1009		0.8551	184.7019
GBP	1.3567	9.1286	10.6431	1.1694		215.9992
JPY	0.0063	0.0423	0.0493	0.0054	0.0046	

## CSV 文件链接

https://raw.githubusercontent.com/granthuang999/exchange-rate-auto/main/exchange_rates.csv

### 数据源说明
- 优先使用 Yahoo Finance 实时汇率
- Yahoo 失败时使用 Wise 汇率
- 最后备选 ExchangeRate-API
- 以美元为基准计算所有交叉汇率

---
*数据仅供参考，交易请以银行报价为准*