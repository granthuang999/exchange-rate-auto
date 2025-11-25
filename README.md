# 汇率数据自动更新（美元基准）

**更新时间**：2025-11-25 11:08:48（北京时间）

## Excel 表格（制表符分隔）

Currency	USD	CNY	HKD	EUR	GBP	JPY
USD		7.0937	7.7767	0.8672	0.7626	156.6380
CNY	0.1410		1.0963	0.1222	0.1075	22.0813
HKD	0.1286	0.9122		0.1115	0.0981	20.1420
EUR	1.1531	8.1800	8.9676		0.8794	180.6250
GBP	1.3113	9.3020	10.1976	1.1372		205.3999
JPY	0.0064	0.0453	0.0496	0.0055	0.0049	

## CSV 文件链接

https://raw.githubusercontent.com/granthuang999/exchange-rate-auto/main/exchange_rates.csv

### 数据源说明
- 优先使用 Yahoo Finance 实时汇率
- Yahoo 失败时使用 Wise 汇率
- 最后备选 ExchangeRate-API
- 以美元为基准计算所有交叉汇率

---
*数据仅供参考，交易请以银行报价为准*