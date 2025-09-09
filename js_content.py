jscode = """
// console.log("=== Pan Event Triggered ===");
// console.log("Event name:", cb_obj.event_name);
// console.log("Mouse sx:", cb_obj.sx, "sy:", cb_obj.sy);
// Find all elements with class name 'bk-LinearAxis'
// Get LinearAxis elements
// Use a flag to ensure execution only once
// Get LinearAxis elements

if (cb_obj.event_name === 'panstart') 
{
    // Create empty object first
    window.initialRanges = {};  
    // left axis
    window.initialRanges['y1'] = {start: p.y_range.start, end: p.y_range.end}
    // right axis
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
            // Find style containing 'width' in shadowRoot
            const styles = axis.shadowRoot.querySelectorAll("style");
            let foundWidth = null;
            styles.forEach(style => 
            {
                const match = style.textContent.match(/width:\s*(\d+)px/);
                if (match) foundWidth = match[1];
            });
            window.ltend = +foundWidth
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
            // Find style containing 'width' in shadowRoot
            const styles = axis.shadowRoot.querySelectorAll("style");
            let foundWidth = null;
            styles.forEach(style => 
            {
                const match = style.textContent.match(/width:\s*(\d+)px/);
                if (match) foundWidth = match[1];
            });
            window.rtend.push(+foundWidth)
        }
    });
    //console.log(window.rtend)
    window.rtend.reverse()
    // Initialize result array
    window.rightAxisPositions = [];

    // Start accumulating offset from the right side
    let currentEnd = p.width;

    // Iterate through each right axis width (starting from the rightmost side)
    for (let i = 0; i < window.rtend.length; i++) {
        const axisWidth = window.rtend[i];
        const start = currentEnd - axisWidth;
        const end = currentEnd;

        // Save current axis position info as object (includes start and end)
        window.rightAxisPositions.push({ start, end });

        // Update current end position to current axis start position (prepare for next axis)
        currentEnd = start;
    }
    //console.log(window.rightAxisPositions[0]['start'])
    return;
}


const sx = cb_obj.sx;
const delta_y = cb_obj.delta_y;

let range_size, delt;

// pan left axis
if (sx >= 0 && sx < window.ltend) {
    range_size = window.initialRanges.y1.end - window.initialRanges.y1.start;
    delt = delta_y / p.inner_height * range_size;
    p.y_range.start = window.initialRanges.y1.start + delt;
    p.y_range.end = window.initialRanges.y1.end + delt;
}

// pan right axis

const right_axes = Object.keys(axisNames);
for (let i = 0; i < right_axes.length; i++){
    const start_x = window.rightAxisPositions[right_axes.length - i - 1]['start']
    const end_x   = window.rightAxisPositions[right_axes.length - i - 1]['end']
    // Check if mouse x-coordinate sx falls within the i-th region
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
// Emit change signal to trigger redraw
p.change.emit();
"""
