# 汇率数据自动更新（美元基准）

**更新时间**：2025-10-02 22:12:12（北京时间）

## Excel 表格（制表符分隔）

Currency	USD	CNY	HKD	EUR	GBP	JPY
USD		7.1185	7.7819	0.8535	0.7449	147.2850
CNY	0.1405		1.0932	0.1199	0.1046	20.6905
HKD	0.1285	0.9148		0.1097	0.0957	18.9266
EUR	1.1716	8.3404	9.1176		0.8728	172.5659
GBP	1.3425	9.5563	10.4469	1.1458		197.7245
JPY	0.0068	0.0483	0.0528	0.0058	0.0051	

## CSV 文件链接

https://raw.githubusercontent.com/granthuang999/exchange-rate-auto/main/exchange_rates.csv

### 数据源说明
- 优先使用 Yahoo Finance 实时汇率
- Yahoo 失败时使用 Wise 汇率
- 最后备选 ExchangeRate-API
- 以美元为基准计算所有交叉汇率

---
*数据仅供参考，交易请以银行报价为准*