# 汇率数据自动更新（美元基准）

**更新时间**：2026-09-02 14:38:50（北京时间）

## Excel 表格（制表符分隔）

Currency	USD	CNY	HKD	EUR	GBP	JPY
USD		6.7223	7.8411	0.8637	0.7406	159.6110
CNY	0.1488		1.1664	0.1285	0.1102	23.7435
HKD	0.1275	0.8573		0.1102	0.0945	20.3557
EUR	1.1578	7.7831	9.0785		0.8575	184.7991
GBP	1.3503	9.0768	10.5875	1.1662		215.5158
JPY	0.0063	0.0421	0.0491	0.0054	0.0046	

## CSV 文件链接

https://raw.githubusercontent.com/granthuang999/exchange-rate-auto/main/exchange_rates.csv

### 数据源说明
- 优先使用 Yahoo Finance 实时汇率
- Yahoo 失败时使用 Wise 汇率
- 最后备选 ExchangeRate-API
- 以美元为基准计算所有交叉汇率

---
*数据仅供参考，交易请以银行报价为准*