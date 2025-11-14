# 汇率数据自动更新（美元基准）

**更新时间**：2025-11-14 11:07:02（北京时间）

## Excel 表格（制表符分隔）

Currency	USD	CNY	HKD	EUR	GBP	JPY
USD		7.0940	7.7693	0.8590	0.7605	154.4160
CNY	0.1410		1.0952	0.1211	0.1072	21.7671
HKD	0.1287	0.9131		0.1106	0.0979	19.8751
EUR	1.1641	8.2584	9.0446		0.8853	179.7625
GBP	1.3149	9.3281	10.2160	1.1295		203.0454
JPY	0.0065	0.0459	0.0503	0.0056	0.0049	

## CSV 文件链接

https://raw.githubusercontent.com/granthuang999/exchange-rate-auto/main/exchange_rates.csv

### 数据源说明
- 优先使用 Yahoo Finance 实时汇率
- Yahoo 失败时使用 Wise 汇率
- 最后备选 ExchangeRate-API
- 以美元为基准计算所有交叉汇率

---
*数据仅供参考，交易请以银行报价为准*