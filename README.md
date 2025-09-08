# Bokeh 多Y轴独立交互工具

![Bokeh](https://static.bokeh.org/logos/logotype.svg)
![Python](https://img.shields.io/badge/Python-3.13.5-blue.svg)
![Bokeh](https://img.shields.io/badge/Bokeh-3.7.3-orange.svg)

## ✨ 项目特色

本项目解决了Bokeh在使用多个Y轴时的一个关键限制：**当拖动一个Y轴时所有数据会同步移动**。通过我们的改进，现在每个Y轴都可以独立拖动和缩放，极大提升了多变量数据可视化的交互体验。

## 🚀 核心功能

- **独立Y轴交互** - 每个Y轴可单独拖动和缩放，互不影响
- **无缝集成** - 基于现有Bokeh工具扩展，保持API一致性
- **灵活配置** - 支持自定义左右Y轴数据系列
- **版本兼容** - 提供版本适配方案，确保长期可用性
- **点击图例隐藏曲线** - 能够更加直观的对比对应曲线数据
- **滚轮缩放对应坐标轴** - 能够将两条曲线缩放至较为接近的比例尺进行比较

### 版本适配

```python
# 如果遇到JS定位问题，请修改js_content.py中的
LinearAxisLt = document.querySelectorAll("div.bk-Column")[0]
        .shadowRoot.querySelectorAll("div.bk-Figure")[0]
        .shadowRoot.querySelectorAll("div.bk-Canvas")[0]
        .shadowRoot.querySelectorAll("div.bk-left")[0]
        .shadowRoot.querySelectorAll("div.bk-LinearAxis");
LinearAxisRt = document.querySelectorAll("div.bk-Column")[0]
        .shadowRoot.querySelectorAll("div.bk-Figure")[0]
        .shadowRoot.querySelectorAll("div.bk-Canvas")[0]
        .shadowRoot.querySelectorAll("div.bk-right")[0]
        .shadowRoot.querySelectorAll("div.bk-LinearAxis");
```

## 🌟 高级特性

- **智能轴对齐** - 自动优化多Y轴的布局和间距
- **响应式设计** - 适应不同屏幕尺寸和设备
- **主题支持** - 兼容Bokeh所用tools工具

## ⚠️ 注意事项

1. 确保Bokeh版本 ≥ 3.7.3
2. 大数据集可能造成卡顿
3. 多Y轴情况下注意量纲差异对可视化效果的影响
4. 如遇交互问题，请检查浏览器控制台错误信息









