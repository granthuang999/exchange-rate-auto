# 汇率数据自动更新（美元基准）

**更新时间**：2025-10-08 10:52:46（北京时间）

## Excel 表格（制表符分隔）

Currency	USD	CNY	HKD	EUR	GBP	JPY
USD		7.1185	7.7831	0.8599	0.7462	152.3930
CNY	0.1405		1.0934	0.1208	0.1048	21.4080
HKD	0.1285	0.9146		0.1105	0.0959	19.5800
EUR	1.1629	8.2783	9.0512		0.8678	177.2218
GBP	1.3401	9.5397	10.4303	1.1524		204.2254
JPY	0.0066	0.0467	0.0511	0.0056	0.0049	

## CSV 文件链接

https://raw.githubusercontent.com/granthuang999/exchange-rate-auto/main/exchange_rates.csv

### 数据源说明
- 优先使用 Yahoo Finance 实时汇率
- Yahoo 失败时使用 Wise 汇率
- 最后备选 ExchangeRate-API
- 以美元为基准计算所有交叉汇率

---
*数据仅供参考，交易请以银行报价为准*