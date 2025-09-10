## 语言

- [English](README.md)
- [中文](README_zh.md)

# Bokeh 多Y轴独立交互
![Bokeh](https://static.bokeh.org/logos/logotype.svg) 
![Python](https://img.shields.io/badge/Python-3.13.5-blue.svg)  
![Bokeh](https://img.shields.io/badge/Bokeh-3.7.3-orange.svg) 
```bash
version
bokeh = 3.7.3
```
# 项目特色  
**本项目解决了Bokeh在使用多个Y轴时，无法支持仅对单个Y轴进行拖动**  
在bokeh中设置参数 `zoom_together = none`，每一个y轴数据都可以使用滚轮独立缩放。但是，没有一个类似的参数`pan_together`来控制每一条y轴的独立拖动。本项目支持了所有y轴的独立拖动。  
   
运行 `main.py`后会输出`example.html`.   
   
在线样例[example.html](https://chenlingyu59-jpg.github.io/bokeh_Independent_axis_panning/example.html)  
   
打开`example.html`将鼠标移动至任意y轴区域内进行拖动，对应的y轴图像跟随移动。  


指导教师 bookaa

