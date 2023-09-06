from lxml import etree

# XPath解析
tree = etree.parse('XPath解析示例.html')

# XPath解析
tree = etree.parse('XPath解析示例.html')
# //子孙节点    /子节点
li_list = tree.xpath('//ul/li')
# 标签内容
li_list = tree.xpath('//ul/li/text()')
# 查找有id属性的
li_list = tree.xpath('//ul/li[@id]')
# 查找id属性值为l1的
li_list = tree.xpath('//ul/li[@id="l1"]')
# 查找有id属性的class属性值
li_list = tree.xpath('//ul/li[@id]/@class')
# 逻辑运算
li_list = tree.xpath('//ul/li[@id="l2" and @class="addr"]')
# contains()模糊     starts-with()
li_list = tree.xpath('//ul/li[contains(@id,"l")]')
li_list = tree.xpath('//ul/li[starts-with(@id,"c")]')

print(li_list)
