# Bokeh 多Y轴独立交互

![Bokeh](https://static.bokeh.org/logos/logotype.svg)
![Python](https://img.shields.io/badge/Python-3.13.5-blue.svg)  
![Bokeh](https://img.shields.io/badge/Bokeh-3.7.3-orange.svg)
```bash
bokeh >= 3.7.3
```
# ✨ 项目特色

本项目解决了Bokeh在使用多个Y轴时，Bokeh无法支持仅对单个Y轴进行拖动。  
受到WheelZoomTool(zoom_together="none")启发，既然能够对任一Y轴进行缩放，应该可以对任一Y轴进行单独的拖动，但在bokeh中并没有相对应的功能。在bokeh中拖动一个Y轴时所有数据会同步移动。通过我们的改进，现在每个Y轴都可以独立拖动和缩放，极大提升了多变量数据可视化的交互体验。

# 🚀 核心功能

- **独立Y轴交互** - 每个Y轴可单独拖动和缩放，互不影响
- **灵活配置** - 支持自定义左右Y轴数据系列
- **点击图例隐藏曲线** - 每条数据线独立显示隐藏
- **滚轮缩放对应坐标轴** - 每条数据线独立缩放

# 打开样例example.html了解功能

# 对于其他版本的bokeh需要修改以下代码
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
# ⚠️ 注意事项

1. 确保Bokeh版本 ≥ 3.7.3
2. 大数据集可能造成卡顿
3. 多Y轴情况下注意量纲差异对可视化效果的影响
4. 如遇交互问题，请检查浏览器控制台错误信息

# 指导教师 *Bookaa*






















