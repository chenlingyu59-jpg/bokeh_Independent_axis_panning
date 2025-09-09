# Bokeh 多Y轴独立交互

![Bokeh](https://static.bokeh.org/logos/logotype.svg)
![Python](https://img.shields.io/badge/Python-3.13.5-blue.svg)  
![Bokeh](https://img.shields.io/badge/Bokeh-3.7.3-orange.svg)
```bash
version
bokeh >= 3.7.3
```
# ✨ 项目特色

**本项目解决了Bokeh在使用多个Y轴时，Bokeh无法支持仅对单个Y轴进行拖动**  
在bokeh的WheelZoomTool中有一个参数zoom_together，该参数设置为'none'时，每一个y轴数据都可以使用滚轮独立缩放。但当我们拖动数据时所有数据都和同步移动，在PanTool中没有一个参数pan_togrther来控制每一条y轴的独立拖动。本项目的实现方法如下，先通过bokeh的pyhon代码生成对应的网页代码，根据bokeh文档我们能够很快的得到鼠标pan的移动距cb_obj.delta_y由这一数据就能够生成新的y轴范围，实现独立拖动。同时为了自适应y轴宽度，我们在网页抓取了每一个y轴宽度来更新我们的pan判定范围，以上两点结合实现了对任意y轴进行的独立拖动。

# 🚀 核心功能

- **独立Y轴交互** - 每个Y轴可单独拖动和缩放，互不影响
- **灵活配置** - 支持自定义左右Y轴数据系列
- **点击图例隐藏曲线** - 每条数据线独立显示隐藏
- **滚轮缩放对应坐标轴** - 每条数据线独立缩放

# 打开样例[example.html](https://chenlingyu59-jpg.github.io/bokeh_Independent_axis_panning/example.html)了解功能
- **使用pan工具**-在pan工具激活的情况下我们能够直接对图形进行拖动，此时所有的数据同步更新
- **使用pan（x-axis）工具**-在此工具激活的情况下只能够对x轴进行全局拖动，将鼠标移动至对应的y轴进行拖动能够实现每一个y轴的独立拖动
- **独立拖动y轴**-取消pan工具的选中将鼠标移动至对应的y轴区域能偶独立拖动y轴
- **独立缩放y轴**-点击工具栏的wheelzoom，将鼠标移至对应的y轴使用滚轮进行独立缩放
- **刷新**-点击工具栏刷新按钮实现图形恢复初始状态

# ⚠️ 注意事项

1. 确保Bokeh版本 ≥ 3.7.3
2. 大数据集可能造成卡顿
3. 多Y轴情况下注意量纲差异对可视化效果的影响
4. 如遇交互问题，请检查浏览器控制台错误信息

指导教师 bookaa




























