# 汇率数据自动更新（美元基准）

**更新时间**：2025-11-05 22:12:49（北京时间）

## Excel 表格（制表符分隔）

Currency	USD	CNY	HKD	EUR	GBP	JPY
USD		7.1273	7.7758	0.8711	0.7677	153.9700
CNY	0.1403		1.0910	0.1222	0.1077	21.6029
HKD	0.1286	0.9166		0.1120	0.0987	19.8012
EUR	1.1480	8.1820	8.9264		0.8813	176.7535
GBP	1.3026	9.2840	10.1287	1.1347		200.5601
JPY	0.0065	0.0463	0.0505	0.0057	0.0050	

## CSV 文件链接

https://raw.githubusercontent.com/granthuang999/exchange-rate-auto/main/exchange_rates.csv

### 数据源说明
- 优先使用 Yahoo Finance 实时汇率
- Yahoo 失败时使用 Wise 汇率
- 最后备选 ExchangeRate-API
- 以美元为基准计算所有交叉汇率

---
*数据仅供参考，交易请以银行报价为准*