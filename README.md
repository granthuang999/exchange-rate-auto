# 汇率数据自动更新（美元基准）

**更新时间**：2026-02-02 12:14:52（北京时间）

## Excel 表格（制表符分隔）

Currency	USD	CNY	HKD	EUR	GBP	JPY
USD		6.9535	7.8076	0.8410	0.7289	154.7300
CNY	0.1438		1.1228	0.1209	0.1048	22.2521
HKD	0.1281	0.8906		0.1077	0.0934	19.8179
EUR	1.1891	8.2681	9.2837		0.8667	183.9834
GBP	1.3719	9.5397	10.7115	1.1538		212.2788
JPY	0.0065	0.0449	0.0505	0.0054	0.0047	

## CSV 文件链接

https://raw.githubusercontent.com/granthuang999/exchange-rate-auto/main/exchange_rates.csv

### 数据源说明
- 优先使用 Yahoo Finance 实时汇率
- Yahoo 失败时使用 Wise 汇率
- 最后备选 ExchangeRate-API
- 以美元为基准计算所有交叉汇率

---
*数据仅供参考，交易请以银行报价为准*