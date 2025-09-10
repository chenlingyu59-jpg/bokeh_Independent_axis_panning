from bokeh import events
from bokeh.plotting import figure, show,output_file,save
from bokeh.models import LinearAxis, Range1d, WheelZoomTool, PanTool, CustomJS, Slider
from bokeh.layouts import column
import numpy as np
from js_content import jscode


# -------------------------- 1. GenData --------------------------
# this is a example
x = np.linspace(0.1, 50, 1000)
y2 = [np.sin(x),np.cos(x)]
n2 = len(y2)
y1 = np.log(x) 
colors = ["blue","red","green","orange","purple"] #add color which you like

# -------------------------- 2. create figure --------------------------
p = figure(
    title="example",
    width=1300,
    height=500,
    tools="pan,reset,save", # We remain some tools
    toolbar_location="above"    # Toolbar layout on top
)
# left LinearAxis
p.line(x, y1, color=colors[0], line_width=2, legend_label='y1')
p.y_range = Range1d(start=min(y1)*0.9, end=max(y1)*1.1)
# -------------------------- 3. add extra axis --------------------------
p.extra_y_ranges = {
    f"y{i+2}_axis": Range1d(start=min(y2[i])-1, end=max(y2[i])+1) for i in range(n2)
}
# Add corresponding Y-axes to the chart, position them on the right side, remove axis labels, in the order [y2, y3, y4, y5]
axis_names = list(p.extra_y_ranges.keys())
for axis_name in axis_names:
    p.add_layout(LinearAxis(y_range_name=axis_name, axis_label=" "), "right")

# draw right axis
for i in range(n2):
    p.line(x, y2[i], color=colors[i+1], line_width=2, y_range_name=axis_names[i], legend_label=f"y{i+2}")

# setting legend to hide/show every line
p.legend.click_policy = "hide"

# -------------------------- 4. Adaptive Drag-and-Drop Interaction --------------------------
rightstart = p.width
axisnames2 = {f'y{i+2}':axis_names[i] for i in range(n2)}
# create pan_callback listeing panning
pan_callback = CustomJS(args=dict(
    p=p,
    axisNames = axisnames2
), code=jscode)
# Add event listeners for pan actions (start, move, and end)
p.js_on_event(events.PanStart, pan_callback)
p.js_on_event(events.Pan, pan_callback)

# -------------------------- 5. Tool Configuration (Keep your original code logic) --------------------------
pan = PanTool(dimensions="width")  # Horizontal panning
p.add_tools(pan)
p.toolbar.active_drag = pan  # Activate pan tool

# Zoom with mouse wheel
wheel_zoom = WheelZoomTool(zoom_together="none")   # Zoom on individual Y-axis with mouse wheel
p.add_tools(wheel_zoom)
p.toolbar.active_scroll = wheel_zoom  # Activate wheel zoom tool

# -------------------------- 6. Display Chart --------------------------
layout = column(p)
output_file("example.html")
save(layout)
