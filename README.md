# 汇率数据自动更新（美元基准）

**更新时间**：2026-07-28 00:07:51（北京时间）

## Excel 表格（制表符分隔）

Currency	USD	CNY	HKD	EUR	GBP	JPY
USD		6.7524	7.8420	0.8788	0.7518	163.7000
CNY	0.1481		1.1614	0.1301	0.1113	24.2432
HKD	0.1275	0.8611		0.1121	0.0959	20.8748
EUR	1.1379	7.6837	8.9235		0.8555	186.2767
GBP	1.3301	8.9816	10.4310	1.1689		217.7441
JPY	0.0061	0.0412	0.0479	0.0054	0.0046	

## CSV 文件链接

https://raw.githubusercontent.com/granthuang999/exchange-rate-auto/main/exchange_rates.csv

### 数据源说明
- 优先使用 Yahoo Finance 实时汇率
- Yahoo 失败时使用 Wise 汇率
- 最后备选 ExchangeRate-API
- 以美元为基准计算所有交叉汇率

---
*数据仅供参考，交易请以银行报价为准*