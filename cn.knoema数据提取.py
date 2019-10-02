import re
data_re=r'<td class="\s+(.*?)\s+">\s+(.*?)\s+<\/td>'
#第一组匹配标签信息，第二组匹配数值
data_compile=re.compile(data_re)
output=open('output.txt',mode='w', encoding='utf-8')
with open('file.txt',encoding='utf-8') as file:
    data=data_compile.findall(file.read())
    #返回一个列表，因为只匹配一组所以没有嵌套元祖
    i=0
    for item in data:
        output.write(item[1])
        output.write('\t')
        i+=1
        if(i%56==0):
            #1961-2016共56年
            output.write('\n')
            i=0
print('end')
