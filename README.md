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
在bokeh中有参数zoom_together在zoom_together = 'none'时，每一个y轴数据都可以使用滚轮独立缩放。但是在bokeh的没有一个类似的参数pan_together来控制每一条y轴的独立拖动。本项目支持了所有y轴的独立拖动。  
运行main.py后会在浏览器输出example.html. 样例[example.html](https://chenlingyu59-jpg.github.io/bokeh_Independent_axis_panning/example.html)了解功能  
将鼠标移动至任意y轴区域内进行拖动，对应的y轴图像跟随移动，使用滚轮时，对应y轴图像缩放  

指导教师 bookaa













































