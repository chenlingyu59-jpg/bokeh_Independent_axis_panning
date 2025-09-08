jscode = """
// console.log("=== Pan Event Triggered ===");
// console.log("Event name:", cb_obj.event_name);
// console.log("Mouse sx:", cb_obj.sx, "sy:", cb_obj.sy);
// 查找所有类名为 bk-LinearAxis 的元素
// 获取LinearAxis元素
// 使用标志确保只执行一次 
// 获取LinearAxis元素

if (cb_obj.event_name === 'panstart') 
{
    window.initialRanges = {};  // 先创建空对象
    // 左轴
    window.initialRanges['y1'] = {start: p.y_range.start, end: p.y_range.end}
    // 右轴
    for (let key in axisNames){
        const val = axisNames[key]
        window.initialRanges[key] = {start: p.extra_y_ranges[val].start, end: p.extra_y_ranges[val].end}
    }
    window.ltend = 0
    const LinearAxisLt = document.querySelectorAll("div.bk-Column")[0]
        .shadowRoot.querySelectorAll("div.bk-Figure")[0]
        .shadowRoot.querySelectorAll("div.bk-Canvas")[0]
        .shadowRoot.querySelectorAll("div.bk-left")[0]
        .shadowRoot.querySelectorAll("div.bk-LinearAxis");

    //console.log(LinearAxislt)
    LinearAxisLt.forEach((axis, index) => 
    {
        if (axis.shadowRoot) 
        {
            // 在shadowRoot中查找包含width的style
            const styles = axis.shadowRoot.querySelectorAll("style");
            let foundWidth = null;
            styles.forEach(style => 
            {
                const match = style.textContent.match(/width:\s*(\d+)px/);
                if (match) foundWidth = match[1];
            });
            window.ltend = +foundWidth
            console.log(`LinearAxis[${index}] 左坐标轴宽度: ${foundWidth}px`);
        }
    });
    window.rtend = []
    const LinearAxisRt = document.querySelectorAll("div.bk-Column")[0]
        .shadowRoot.querySelectorAll("div.bk-Figure")[0]
        .shadowRoot.querySelectorAll("div.bk-Canvas")[0]
        .shadowRoot.querySelectorAll("div.bk-right")[0]
        .shadowRoot.querySelectorAll("div.bk-LinearAxis");
    LinearAxisRt.forEach((axis, index) => 
    {
        if (axis.shadowRoot) 
        {
            // 在shadowRoot中查找包含width的style
            const styles = axis.shadowRoot.querySelectorAll("style");
            let foundWidth = null;
            styles.forEach(style => 
            {
                const match = style.textContent.match(/width:\s*(\d+)px/);
                if (match) foundWidth = match[1];
            });
            window.rtend.push(+foundWidth)
            //console.log(`LinearAxis[${index}] 右第${index}条坐标轴宽度: ${foundWidth}px`);
        }
    });
    //console.log(window.rtend)
    window.rtend.reverse()
    // 初始化结果数组
    window.rightAxisPositions = [];

    // 从右侧开始累计偏移
    let currentEnd = p.width;

    // 遍历每个右轴的宽度（从最右侧开始）
    for (let i = 0; i < window.rtend.length; i++) {
        const axisWidth = window.rtend[i];
        const start = currentEnd - axisWidth;
        const end = currentEnd;

        // 将当前轴的位置信息保存为对象（包含start和end）
        window.rightAxisPositions.push({ start, end });

        // 更新当前结束位置为当前轴的起始位置（为下一个轴做准备）
        currentEnd = start;
    }
    //console.log(window.rightAxisPositions[0]['start'])
    return;
}


const sx = cb_obj.sx;
const delta_y = cb_obj.delta_y;

let range_size, delt;

// 左轴拖动
if (sx >= 0 && sx < window.ltend) {
    range_size = window.initialRanges.y1.end - window.initialRanges.y1.start;
    delt = delta_y / p.inner_height * range_size;
    p.y_range.start = window.initialRanges.y1.start + delt;
    p.y_range.end = window.initialRanges.y1.end + delt;
}

// 右轴拖动

const right_axes = Object.keys(axisNames);
for (let i = 0; i < right_axes.length; i++){
    const start_x = window.rightAxisPositions[right_axes.length - i - 1]['start']
    const end_x   = window.rightAxisPositions[right_axes.length - i - 1]['end']
    // 鼠标x坐标sx是否落在第i个区域
    if (sx >= start_x && sx < end_x){
        const key = right_axes[i];	// 'y2'
        const val = axisNames[key];	// 'y2_axis'
        range_size = window.initialRanges[key].end - window.initialRanges[key].start;
        delt = delta_y / p.inner_height * range_size;
        p.extra_y_ranges[val].start = window.initialRanges[key].start + delt;
        p.extra_y_ranges[val].end = window.initialRanges[key].end + delt;
        break;
    }
}
// 发出变化信号，触发重绘
p.change.emit();
"""

moving_average_js = """
function movingAverage(arr, rate) 
{
    const result = [arr[0]];
    let lastv = arr[0];
    for (let i = 1; i < arr.length; i++) 
    {
        lastv = lastv*(1-rate) + arr[i]*rate;
        result.push(lastv);
    }
    return result;
}
"""

slide_js = """
// 获取当前滑块值
const window_x = slider_x.value;
const window_filter = slider_filter.value;

// 计算新的移动平均
const new_y2_ma = movingAverage(original_data.y2_original, window_x);
const new_y3_ma = movingAverage(original_data.y3_original, window_filter);

// 更新数据源
ma_source.data['y2_ma'] = new_y2_ma;
ma_source.data['y3_ma'] = new_y3_ma;

// 触发更新
ma_source.change.emit();
"""
