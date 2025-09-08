# Bokeh能够单独移动任意y轴
# PanTools，WheelZoomTool，zoom_together
## Bokeh版本3.7.3
## python版本3.13.5

1.本项目解决了bokeh在使用多个y轴时，当我们拖动一个y轴会时所有的数据进行移动，这个特性使得使用bokeh画图难以直观的观察数据，本次改动使所有的y轴能够单独拖动。  
2.本次改动主要由bokeh的WheelZoomTool(zoom_together="none")启发。通过js代码实现的多轴互相独立  
3.使用时请修改
file_path = r'yourdatasource'  
y1_name = ['yourrigthaxis']	# 左边放一个  
y2_name = ['extra_axis','extra_axis']  
4.由于版本问题造成的js定位不准确请修改js_content.py文件  
5.使用样例  
<video src="example.mp4" width="640" controls>
</video>
