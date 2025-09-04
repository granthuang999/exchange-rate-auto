# 汇率数据自动更新（美元基准）

**更新时间**：2025-09-04 22:12:06（北京时间）

## Excel 表格（制表符分隔）

Currency	USD	CNY	HKD	EUR	GBP	JPY
USD		7.1396	7.8006	0.8582	0.7442	148.4030
CNY	0.1401		1.0926	0.1202	0.1042	20.7859
HKD	0.1282	0.9153		0.1100	0.0954	19.0246
EUR	1.1652	8.3193	9.0895		0.8672	172.9236
GBP	1.3437	9.5937	10.4819	1.1532		199.4128
JPY	0.0067	0.0481	0.0526	0.0058	0.0050	

## CSV 文件链接

https://raw.githubusercontent.com/granthuang999/exchange-rate-auto/main/exchange_rates.csv

### 数据源说明
- 优先使用 Yahoo Finance 实时汇率
- Yahoo 失败时使用 Wise 汇率
- 最后备选 ExchangeRate-API
- 以美元为基准计算所有交叉汇率

---
*数据仅供参考，交易请以银行报价为准*