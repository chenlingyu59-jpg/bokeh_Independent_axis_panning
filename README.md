# Bokeh 多Y轴独立交互工具

![Bokeh](https://static.bokeh.org/logos/logotype.svg)
![Python](https://img.shields.io/badge/Python-3.13.5-blue.svg)
![Bokeh](https://img.shields.io/badge/Bokeh-3.7.3-orange.svg)

## 🎥 演示动画
![功能演示](example.gif)


## ✨ 项目特色

本项目解决了Bokeh在使用多个Y轴时的一个关键限制：**当拖动一个Y轴时所有数据会同步移动**。通过我们的改进，现在每个Y轴都可以独立拖动和缩放，极大提升了多变量数据可视化的交互体验。

## 🚀 核心功能

- **独立Y轴交互** - 每个Y轴可单独拖动和缩放，互不影响
- **无缝集成** - 基于现有Bokeh工具扩展，保持API一致性
- **灵活配置** - 支持自定义左右Y轴数据系列
- **版本兼容** - 提供版本适配方案，确保长期可用性

## 📦 安装与使用

### 基本配置

```python
# 配置您的数据源和Y轴系列
file_path = r'your_data_source.csv'  # 您的数据文件路径
y1_name = ['primary_metric']        # 左侧Y轴数据列
y2_name = ['extra_metric_1', 'extra_metric_2']  # 右侧额外Y轴数据列
```
### 环境配置
```bash
conda create --name bokeh python=3.13.5
conda activate bokeh
conda install -r requirements.txt
```
详细的包依赖请参考requirement.txt

## 🔧 技术实现

### 核心原理

本项目受Bokeh的 `WheelZoomTool(zoom_together="none")` 启发，通过JavaScript扩展实现了Y轴的独立交互功能。

### 版本适配

```python
# 如果遇到JS定位问题，请修改js_content.py中的
LinearAxisLt = document.querySelectorAll("div.bk-Column")[0]
        .shadowRoot.querySelectorAll("div.bk-Figure")[0]
        .shadowRoot.querySelectorAll("div.bk-Canvas")[0]
        .shadowRoot.querySelectorAll("div.bk-left")[0]
        .shadowRoot.querySelectorAll("div.bk-LinearAxis");
LinearAxisRt = document.querySelectorAll("div.bk-Column")[0]
        .shadowRoot.querySelectorAll("div.bk-Figure")[0]
        .shadowRoot.querySelectorAll("div.bk-Canvas")[0]
        .shadowRoot.querySelectorAll("div.bk-right")[0]
        .shadowRoot.querySelectorAll("div.bk-LinearAxis");
```

## 🌟 高级特性

- **智能轴对齐** - 自动优化多Y轴的布局和间距
- **响应式设计** - 适应不同屏幕尺寸和设备
- **主题支持** - 兼容Bokeh所有内置主题

## ⚠️ 注意事项

1. 确保Bokeh版本 ≥ 3.7.3
2. 大数据集建议启用WebGL加速
3. 多Y轴情况下注意量纲差异对可视化效果的影响
4. 如遇交互问题，请检查浏览器控制台错误信息


## 📄 许可证

本项目采用MIT许可证 - 详见 [LICENSE](LICENSE) 文件

## 🙏 致谢

- 感谢Bokeh开发团队提供的优秀可视化库
- 感谢开源社区的宝贵反馈和建议
---

**享受更加灵活的数据可视化体验！** 🎉

*如有问题或建议，请提交[Issue]或通过Email联系我们*




