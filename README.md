# 汇率数据自动更新（美元基准）

**更新时间**：2026-02-02 22:36:03（北京时间）

## Excel 表格（制表符分隔）

Currency	USD	CNY	HKD	EUR	GBP	JPY
USD		6.9437	7.8098	0.8459	0.7326	154.7800
CNY	0.1440		1.1247	0.1218	0.1055	22.2907
HKD	0.1280	0.8891		0.1083	0.0938	19.8187
EUR	1.1822	8.2087	9.2325		0.8661	182.9767
GBP	1.3650	9.4782	10.6604	1.1547		211.2749
JPY	0.0065	0.0449	0.0505	0.0055	0.0047	

## CSV 文件链接

https://raw.githubusercontent.com/granthuang999/exchange-rate-auto/main/exchange_rates.csv

### 数据源说明
- 优先使用 Yahoo Finance 实时汇率
- Yahoo 失败时使用 Wise 汇率
- 最后备选 ExchangeRate-API
- 以美元为基准计算所有交叉汇率

---
*数据仅供参考，交易请以银行报价为准*