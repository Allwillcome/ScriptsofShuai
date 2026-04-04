# microGPT 学习资源汇总

## 1. Karpathy 官方文章
- 链接: https://karpathy.github.io/2026/02/12/microgpt/
- 源码: https://gist.github.com/karpathy/8627fe009c40f57531cb18360106ce95

## 2. 微信文章（需要手动打开）
- 200 行代码教程: https://mp.weixin.qq.com/s/_T97yI9WmhUY-GSbXcGWaQ
- 金融原理讲解: https://mp.weixin.qq.com/s/883sHlZLG9sp0bDkEe-Alg

---

## 学习路径建议

### 第一阶段：理解核心概念
1. 阅读 Karpathy 官方博客
2. 运行 microgpt.py 观察输出

### 第二阶段：深入代码
1. `Value` 类 - 自定义 autograd 引擎
2. `LayerNorm` / `RMSNorm` - 归一化
3. `Linear` + `Softmax` - 线性层和注意力
4. `Attention` - 多头注意力机制
5. `Transformer` - 整体架构

### 第三阶段：动手实验
- 修改超参数观察效果
- 尝试不同的数据集