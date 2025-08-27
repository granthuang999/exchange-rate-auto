# 汇率数据自动更新（美元基准）

**更新时间**：2025-08-27 10:57:45（北京时间）

## Excel 表格（制表符分隔）

Currency	USD	CNY	HKD	EUR	GBP	JPY
USD		7.1517	7.7840	0.8595	0.7428	147.7240
CNY	0.1398		1.0884	0.1202	0.1039	20.6558
HKD	0.1285	0.9188		0.1104	0.0954	18.9779
EUR	1.1635	8.3208	9.0564		0.8642	171.8720
GBP	1.3463	9.6280	10.4793	1.1571		198.8745
JPY	0.0068	0.0484	0.0527	0.0058	0.0050	

## CSV 文件链接

https://raw.githubusercontent.com/granthuang999/exchange-rate-auto/main/exchange_rates.csv

### 数据源说明
- 优先使用 Yahoo Finance 实时汇率
- Yahoo 失败时使用 Wise 汇率
- 最后备选 ExchangeRate-API
- 以美元为基准计算所有交叉汇率

---
*数据仅供参考，交易请以银行报价为准*