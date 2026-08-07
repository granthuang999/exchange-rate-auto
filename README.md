# 汇率数据自动更新（美元基准）

**更新时间**：2026-08-07 12:19:17（北京时间）

## Excel 表格（制表符分隔）

Currency	USD	CNY	HKD	EUR	GBP	JPY
USD		6.7462	7.8438	0.8676	0.7433	158.3960
CNY	0.1482		1.1627	0.1286	0.1102	23.4793
HKD	0.1275	0.8601		0.1106	0.0948	20.1938
EUR	1.1526	7.7757	9.0408		0.8567	182.5680
GBP	1.3454	9.0760	10.5527	1.1672		213.0983
JPY	0.0063	0.0426	0.0495	0.0055	0.0047	

## CSV 文件链接

https://raw.githubusercontent.com/granthuang999/exchange-rate-auto/main/exchange_rates.csv

### 数据源说明
- 优先使用 Yahoo Finance 实时汇率
- Yahoo 失败时使用 Wise 汇率
- 最后备选 ExchangeRate-API
- 以美元为基准计算所有交叉汇率

---
*数据仅供参考，交易请以银行报价为准*