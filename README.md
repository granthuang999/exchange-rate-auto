# 汇率数据自动更新（美元基准）

**更新时间**：2026-07-29 23:44:03（北京时间）

## Excel 表格（制表符分隔）

Currency	USD	CNY	HKD	EUR	GBP	JPY
USD		6.7574	7.8431	0.8784	0.7526	163.8600
CNY	0.1480		1.1607	0.1300	0.1114	24.2490
HKD	0.1275	0.8616		0.1120	0.0960	20.8922
EUR	1.1384	7.6929	8.9288		0.8568	186.5437
GBP	1.3287	8.9787	10.4213	1.1672		217.7252
JPY	0.0061	0.0412	0.0479	0.0054	0.0046	

## CSV 文件链接

https://raw.githubusercontent.com/granthuang999/exchange-rate-auto/main/exchange_rates.csv

### 数据源说明
- 优先使用 Yahoo Finance 实时汇率
- Yahoo 失败时使用 Wise 汇率
- 最后备选 ExchangeRate-API
- 以美元为基准计算所有交叉汇率

---
*数据仅供参考，交易请以银行报价为准*