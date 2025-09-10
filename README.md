## Language

- [English](README.md)
- [中文](README_zh.md)

# Bokeh Multiple Y-Axes Independent Interaction  
![Bokeh](https://static.bokeh.org/logos/logotype.svg)  
![Python](https://img.shields.io/badge/Python-3.13.5-blue.svg)  
![Bokeh](https://img.shields.io/badge/Bokeh-3.7.3-orange.svg)  
```bash
version  
bokeh = 3.7.3  
```
# Project Highlights  
**This project addresses the issue in Bokeh where dragging cannot be performed independently for a single Y-axis when using multiple Y-axes.**  
In Bokeh, when the parameter `zoom_together = none` is set, each Y-axis data can be independently zoomed using the scroll wheel. However, there is no similar parameter like `pan_together` to control independent dragging for each Y-axis. This project enables independent dragging for all Y-axes.  

Running `main.py` will generate `example.html`.  

Online example: [example.html](https://chenlingyu59-jpg.github.io/bokeh_Independent_axis_panning/example.html)  

Open `example.html` and drag within the area of any Y-axis to move the corresponding Y-axis plot.  

Instructor: bookaa