# 汇率数据自动更新（美元基准）

**更新时间**：2025-10-15 22:13:16（北京时间）

## Excel 表格（制表符分隔）

Currency	USD	CNY	HKD	EUR	GBP	JPY
USD		7.1257	7.7736	0.8600	0.7487	151.4630
CNY	0.1403		1.0909	0.1207	0.1051	21.2559
HKD	0.1286	0.9167		0.1106	0.0963	19.4843
EUR	1.1628	8.2857	9.0391		0.8706	176.1198
GBP	1.3356	9.5174	10.3828	1.1487		202.3013
JPY	0.0066	0.0470	0.0513	0.0057	0.0049	

## CSV 文件链接

https://raw.githubusercontent.com/granthuang999/exchange-rate-auto/main/exchange_rates.csv

### 数据源说明
- 优先使用 Yahoo Finance 实时汇率
- Yahoo 失败时使用 Wise 汇率
- 最后备选 ExchangeRate-API
- 以美元为基准计算所有交叉汇率

---
*数据仅供参考，交易请以银行报价为准*