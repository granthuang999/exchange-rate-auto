# 汇率数据自动更新（美元基准）

**更新时间**：2025-10-23 22:13:04（北京时间）

## Excel 表格（制表符分隔）

Currency	USD	CNY	HKD	EUR	GBP	JPY
USD		7.1219	7.7712	0.8609	0.7501	152.6690
CNY	0.1404		1.0912	0.1209	0.1053	21.4366
HKD	0.1287	0.9164		0.1108	0.0965	19.6455
EUR	1.1616	8.2726	9.0268		0.8713	177.3365
GBP	1.3332	9.4946	10.3602	1.1477		203.5315
JPY	0.0066	0.0466	0.0509	0.0056	0.0049	

## CSV 文件链接

https://raw.githubusercontent.com/granthuang999/exchange-rate-auto/main/exchange_rates.csv

### 数据源说明
- 优先使用 Yahoo Finance 实时汇率
- Yahoo 失败时使用 Wise 汇率
- 最后备选 ExchangeRate-API
- 以美元为基准计算所有交叉汇率

---
*数据仅供参考，交易请以银行报价为准*