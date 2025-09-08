# 汇率数据自动更新（美元基准）

**更新时间**：2025-09-08 22:12:44（北京时间）

## Excel 表格（制表符分隔）

Currency	USD	CNY	HKD	EUR	GBP	JPY
USD		7.1288	7.7937	0.8510	0.7386	147.7300
CNY	0.1403		1.0933	0.1194	0.1036	20.7230
HKD	0.1283	0.9147		0.1092	0.0948	18.9551
EUR	1.1751	8.3770	9.1583		0.8679	173.5958
GBP	1.3539	9.6518	10.5520	1.1522		200.0135
JPY	0.0068	0.0483	0.0528	0.0058	0.0050	

## CSV 文件链接

https://raw.githubusercontent.com/granthuang999/exchange-rate-auto/main/exchange_rates.csv

### 数据源说明
- 优先使用 Yahoo Finance 实时汇率
- Yahoo 失败时使用 Wise 汇率
- 最后备选 ExchangeRate-API
- 以美元为基准计算所有交叉汇率

---
*数据仅供参考，交易请以银行报价为准*