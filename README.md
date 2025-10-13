# 汇率数据自动更新（美元基准）

**更新时间**：2025-10-13 11:04:10（北京时间）

## Excel 表格（制表符分隔）

Currency	USD	CNY	HKD	EUR	GBP	JPY
USD		7.1280	7.7796	0.8602	0.7488	151.9050
CNY	0.1403		1.0914	0.1207	0.1051	21.3110
HKD	0.1285	0.9162		0.1106	0.0963	19.5261
EUR	1.1625	8.2864	9.0439		0.8705	176.5927
GBP	1.3355	9.5192	10.3894	1.1488		202.8646
JPY	0.0066	0.0469	0.0512	0.0057	0.0049	

## CSV 文件链接

https://raw.githubusercontent.com/granthuang999/exchange-rate-auto/main/exchange_rates.csv

### 数据源说明
- 优先使用 Yahoo Finance 实时汇率
- Yahoo 失败时使用 Wise 汇率
- 最后备选 ExchangeRate-API
- 以美元为基准计算所有交叉汇率

---
*数据仅供参考，交易请以银行报价为准*