# Bokeh 多Y轴独立交互

![Bokeh](https://static.bokeh.org/logos/logotype.svg)
![Python](https://img.shields.io/badge/Python-3.13.5-blue.svg)  
![Bokeh](https://img.shields.io/badge/Bokeh-3.7.3-orange.svg)
```bash
version
bokeh >= 3.7.3
```
# 项目特色

**本项目解决了Bokeh在使用多个Y轴时，无法支持仅对单个Y轴进行拖动**  
在bokeh的WheelZoomTool中有一个参数zoom_together，该参数设置为'none'时，每一个y轴数据都可以使用滚轮独立缩放。而在bokeh的PanTool中没有一个参数pan_togrther来控制每一条y轴的独立拖动。本项目支持了所有y轴的独立拖动。
# 功能
- **独立Y轴交互** - 每个Y轴可单独拖动和缩放，互不影响

# 打开样例[example.html](https://chenlingyu59-jpg.github.io/bokeh_Independent_axis_panning/example.html)了解功能

- 点击example跳转至图像，将鼠标移动至任意y轴区域内进行拖动，对应的y轴图像跟随移动，使用滚轮时，对应y轴图像缩放

指导教师 bookaa









































