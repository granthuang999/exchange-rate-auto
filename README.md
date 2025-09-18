# 汇率数据自动更新（美元基准）

**更新时间**：2025-09-18 10:52:23（北京时间）

## Excel 表格（制表符分隔）

Currency	USD	CNY	HKD	EUR	GBP	JPY
USD		7.1058	7.7761	0.8458	0.7338	146.9010
CNY	0.1407		1.0943	0.1190	0.1033	20.6734
HKD	0.1286	0.9138		0.1088	0.0944	18.8913
EUR	1.1823	8.4013	9.1938		0.8676	173.6829
GBP	1.3628	9.6836	10.5970	1.1526		200.1922
JPY	0.0068	0.0484	0.0529	0.0058	0.0050	

## CSV 文件链接

https://raw.githubusercontent.com/granthuang999/exchange-rate-auto/main/exchange_rates.csv

### 数据源说明
- 优先使用 Yahoo Finance 实时汇率
- Yahoo 失败时使用 Wise 汇率
- 最后备选 ExchangeRate-API
- 以美元为基准计算所有交叉汇率

---
*数据仅供参考，交易请以银行报价为准*