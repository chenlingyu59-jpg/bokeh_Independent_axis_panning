import pandas as pd
from bokeh import events
from bokeh.plotting import figure, show,output_file,save
from bokeh.models import LinearAxis, Range1d, WheelZoomTool, PanTool, CustomJS, Slider
from bokeh.layouts import column
import numpy as np
from js_content import jscode,moving_average_js,slide_js

output_file("example.html")
# -------------------------- 1. 生成数据 --------------------------
file_path = r'yourdata.csv' #最好是csv文件
df = pd.read_csv(file_path, encoding="utf-8-sig")
y1_name = ['y1']	# 左边放一个
y2_name = ['y2','y3']
n1,n2 = len(y1_name),len(y2_name)
df.columns = df.columns.str.strip()

x = df.index.values
y1 = df[y1_name[0]].values	# 左轴
y2 = []	# 右轴
for name in y2_name:
    y2.append(df[name].values)
colors = ["blue","red","green","orange","purple"]

# -------------------------- 2. 创建图表 --------------------------
p = figure(
    title="CSV图表",
    width=1300,
    height=500,
    tools="pan,reset,save", # 只保留全局pan，重置，保存
    toolbar_location="above"    # 将工具栏调整至顶部
)

# 左轴
p.line(x, y1, color=colors[0], line_width=2, legend_label=y1_name[0])
p.y_range = Range1d(start=min(y1)*0.9, end=max(y1)*1.1)
# -------------------------- 3. 添加右边多个轴 --------------------------
p.extra_y_ranges = {
    f"y{i+2}_axis": Range1d(start=min(y2[i])-1, end=max(y2[i])+1) for i in range(n2)
}
# 添加对应的Y轴到图中，并指定它的位置在右侧，去掉轴标签，顺序是[y2,y3,y4,y5]
axis_names = list(p.extra_y_ranges.keys())
for axis_name in axis_names:
    p.add_layout(LinearAxis(y_range_name=axis_name, axis_label=" "), "right")

# 绘制右轴曲线
for i in range(n2):
    p.line(x, y2[i], color=colors[i+1], line_width=2, y_range_name=axis_names[i], legend_label=y2_name[i])

# 设置legend为可点击状态以隐藏/显示线条
p.legend.click_policy = "hide"

# 创建移动平均函数
def moving_average(data, window):
    return pd.Series(data).rolling(window=window, center=True, min_periods=1).mean().to_numpy()

# 初始窗口大小
initial_window_x = 10
initial_window_filter = 10

# 计算初始移动平均
y2_ma = moving_average(y2[0], initial_window_x)
y3_ma = moving_average(y2[1], initial_window_filter)

# 创建移动平均线的数据源
from bokeh.models import ColumnDataSource
ma_source = ColumnDataSource(data={
    'x': x,
    'y2_ma': y2_ma,
    'y3_ma': y3_ma
})

# 绘制移动平均线
y2_ma_line = p.line('x', 'y2_ma', source=ma_source, color=[255,100,0], line_width=2,
                   y_range_name="y2_axis", legend_label=f"{y2_name[0]} (移动平均)")
y3_ma_line = p.line('x', 'y3_ma', source=ma_source, color=[0,255,100], line_width=2,
                   y_range_name="y3_axis", legend_label=f"{y2_name[1]} (移动平均)")

# 存储原始数据以便更新
original_data = {
    'y2_original': y2[0],
    'y3_original': y2[1]
}

# -------------------------- 4. 自适应拖拽交互 --------------------------
# 定义轴区域边界
left_axis_boundary = 55
axis_width = 50
rightstart = p.width
right_axis_boundaries = []
for i in range(n2):
    start = (p.width-20) - axis_width*(i+1)
    end   = (p.width-20) - axis_width*i
    right_axis_boundaries.insert(0,[start, end])

axisnames2 = {f'y{i+2}':axis_names[i] for i in range(n2)}
# 改进的平移事件回调 - 更平滑的拖动
pan_callback = CustomJS(args=dict(
    p=p,
    right_axis_boundaries = right_axis_boundaries,
    rightstart = rightstart,
    axisNames = axisnames2
), code=jscode)

# 添加平移事件监听（开始、移动和结束）
p.js_on_event(events.PanStart, pan_callback)
p.js_on_event(events.Pan, pan_callback)

# -------------------------- 5. 工具配置（保持你原始代码的逻辑） --------------------------
pan = PanTool(dimensions="width")  # 水平平移
p.add_tools(pan)
p.toolbar.active_drag = pan  # 激活平移工具

# 滚轮缩放
wheel_zoom = WheelZoomTool(zoom_together="none")    # 对单独y轴滚轮缩放
p.add_tools(wheel_zoom)
p.toolbar.active_scroll = wheel_zoom  # 激活滚轮工具

# -------------------------- 6. 添加滑块控件 --------------------------
# 圆心X移动平均窗口滑块
slider_x = Slider(start=0, end=1, value=1, step=0.01, 
                  title=f"{y2_name[0]} EMA的rate大小")

# 滤波移动平均窗口滑块
slider_filter = Slider(start=0, end=1, value=1, step=0.01, 
                       title=f"{y2_name[1]} EMA的rate大小")

# 滑块更新的JavaScript回调
slider_js_callback = CustomJS(args=dict(
    ma_source=ma_source,
    original_data=original_data,
    slider_x=slider_x,
    slider_filter=slider_filter
), code=moving_average_js + slide_js)

# 为滑块添加JavaScript回调（实时更新）
slider_x.js_on_change('value', slider_js_callback)
slider_filter.js_on_change('value', slider_js_callback)


# -------------------------- 7. 显示图表 --------------------------
layout = column(p, slider_x, slider_filter)

show(layout)
