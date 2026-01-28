# 汇率数据自动更新（美元基准）

**更新时间**：2026-01-28 22:22:06（北京时间）

## Excel 表格（制表符分隔）

Currency	USD	CNY	HKD	EUR	GBP	JPY
USD		6.9457	7.8014	0.8356	0.7257	152.8220
CNY	0.1440		1.1232	0.1203	0.1045	22.0024
HKD	0.1282	0.8903		0.1071	0.0930	19.5890
EUR	1.1967	8.3122	9.3363		0.8685	182.8889
GBP	1.3780	9.5710	10.7502	1.1514		210.5856
JPY	0.0065	0.0454	0.0510	0.0055	0.0047	

## CSV 文件链接

https://raw.githubusercontent.com/granthuang999/exchange-rate-auto/main/exchange_rates.csv

### 数据源说明
- 优先使用 Yahoo Finance 实时汇率
- Yahoo 失败时使用 Wise 汇率
- 最后备选 ExchangeRate-API
- 以美元为基准计算所有交叉汇率

---
*数据仅供参考，交易请以银行报价为准*