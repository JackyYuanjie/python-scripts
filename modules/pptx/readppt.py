#!/usr/bin/env python
# -*- coding:utf-8 -*-

import pptx 
from pptx import Presentation

# Kubernetes技术培训示例
"""
prs = Presentation()
title_slide_layout = prs.slide_layouts[0]
slide = prs.slides.add_slide(title_slide_layout)
title = slide.shapes.title
subtitle = slide.placeholders[1]

title.text = "Kubernetes技术培训"
subtitle.text = "培训日期: 2019.8.8"

prs.save("F:\\PythonProject\\python-scripts\\modules\\pptx\\writepptx\\One.pptx")
"""

# 第二页内容
"""
prs = Presentation()
bullet_slide_layout = prs.slide_layouts[1]

slide = prs.slides.add_slide(bullet_slide_layout)
shapes = slide.shapes

title_shape = shapes.title
body_shape = shapes.placeholders[1]

title_shape.text = "Kubernetes技术概述"

tf = body_shape.text_frame
tf.text = "Kubernetes概述"

p = tf.add_paragraph()
p.text = "Kubernetes特性和概念术语"
p.level = 1

p = tf.add_paragraph()
p.text = "特性是自动装箱,自我修复,水平扩展"
p.level = 2

prs.save("F:\\PythonProject\\python-scripts\\modules\\pptx\\writepptx\\Two.pptx")
"""




# add_textbox()示例
"""
from pptx.util import Inches,Pt

prs = Presentation()
blank_slide_layout = prs.slide_layouts[6]
slide = prs.slides.add_slide(blank_slide_layout)

left = top = width = height = Inches(1)
txBox = slide.shapes.add_textbox(left,top,width,height)
tf = txBox.text_frame

# 小字体的内容
tf.text = "特性是自动装箱"

p = tf.add_paragraph()
p.text = "这是比较大的一张图"
p.font.bold = True 

p = tf.add_paragraph()
p.text = "这是最大的字体"
p.font.size = Pt(40)
prs.save("F:\\PythonProject\\python-scripts\\modules\\pptx\\writepptx\\textbox3.pptx")
"""


# add_picture()示例
"""
from pptx import Presentation
from pptx.util import Inches

img_path = "F:\\PythonProject\\python-scripts\\modules\\pptx\\woman.jpg"

prs = Presentation()
blank_slide_layout = prs.slide_layouts[5]
slide = prs.slides.add_slide(blank_slide_layout)

# left = top = Inches(1)
# pic = slide.shapes.add_picture(img_path,left,top)

left = Inches(3)
top = Inches(1.5)
height = Inches(5.5)
width = Inches(4.5)
pic = slide.shapes.add_picture(img_path,left,top,height=height,width=width)

prs.save("F:\\PythonProject\\python-scripts\\modules\\pptx\\writepptx\\picture4.pptx")
"""




# add_shape() 示例
"""
from pptx.enum.shapes import MSO_SHAPE 
from pptx.util import Inches

prs = Presentation()
title_only_slide_layout = prs.slide_layouts[5]
slide = prs.slides.add_slide(title_only_slide_layout)
shapes = slide.shapes

shapes.title.text = '添加几个步骤'

left = Inches(0.93)
top = Inches(3.0)
width = Inches(1.75)
height = Inches(1.0)

shape = shapes.add_shape(MSO_SHAPE.PENTAGON,left,top,width,height)
shape.text = 'Step 1'

left = left + width - Inches(0.4)
width = Inches(2.0)

for n in range(2,6):
    shape = shapes.add_shape(MSO_SHAPE.CHEVRON, left,top,width,height)
    shape.text = 'Step {}'.format(n)
    left = left + width - Inches(0.4)

prs.save("F:\\PythonProject\\python-scripts\\modules\\pptx\\writepptx\\shapes5.pptx")
"""




# add_table() example
from pptx.util import Inches

prs = Presentation()
title_only_slide_layout = prs.slide_layouts[5]
slide = prs.slides.add_slide(title_only_slide_layout)
shapes = slide.shapes

shapes.title.text = '添加一个表格'

rows = cols = 2
left = top = Inches(2.0)
width = Inches(6.0)
height = Inches(1)

table = shapes.add_table(rows,cols,left,top,width,height).table

# 设置列高度
table.columns[0].width = Inches(2.0)
table.columns[1].width = Inches(4.0)

# 写列头部内容
table.cell(0,0).text = '用户id'
table.cell(0,1).text = '用户问句'

# 写表格内的内容.
table.cell(1,0).text = '45345654'
table.cell(1,1).text = '我要找李某'
prs.save("F:\\PythonProject\\python-scripts\\modules\\pptx\\writepptx\\table6.pptx")




# 从演示文稿中的幻灯片中提取所有文本


# 网址参考: https://python-pptx.readthedocs.io/en/latest/user/quickstart.html