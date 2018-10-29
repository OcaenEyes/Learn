from lxml import etree
text ='''
<div>
    <ui>
        <li class='item-0'><a href='link1.html'>first item</a></li>
        <li class='item-1'><a href='link2.html'>first item</a></li>
        <li class='item-2'><a href='link3.html'>first item</a></li>
        <li class='item-3'><a href='link4.html'>first item</a></li>
        <li class='item-4'><a href='link5.html'>first item</a></li>
    </ui>
</div>
'''

html = etree.HTML(text)
result = etree.tostring(html)
print(result.decode('utf-8'))
