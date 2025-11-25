# 汇率数据自动更新（美元基准）

**更新时间**：2025-11-25 22:13:08（北京时间）

## Excel 表格（制表符分隔）

Currency	USD	CNY	HKD	EUR	GBP	JPY
USD		7.0847	7.7766	0.8644	0.7597	156.1410
CNY	0.1411		1.0977	0.1220	0.1072	22.0392
HKD	0.1286	0.9110		0.1112	0.0977	20.0783
EUR	1.1569	8.1961	8.9965		0.8789	180.6351
GBP	1.3163	9.3257	10.2364	1.1378		205.5298
JPY	0.0064	0.0454	0.0498	0.0055	0.0049	

## CSV 文件链接

https://raw.githubusercontent.com/granthuang999/exchange-rate-auto/main/exchange_rates.csv

### 数据源说明
- 优先使用 Yahoo Finance 实时汇率
- Yahoo 失败时使用 Wise 汇率
- 最后备选 ExchangeRate-API
- 以美元为基准计算所有交叉汇率

---
*数据仅供参考，交易请以银行报价为准*