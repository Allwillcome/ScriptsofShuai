import os
import markdownify
import re
import datetime
from bs4 import BeautifulSoup

os.chdir("/Users/wangshuaibo/Downloads/flomo@阿帅-20240219")

with open("阿帅的笔记.html") as f:
	html = f.read()
	soup = BeautifulSoup(html, 'html.parser')

	memos = soup.find_all('div', class_='memo')

	for memo in memos:
	    time = memo.find('div', class_='time').text
	    content = memo.find('div', class_='content')

	    # print(content)

	    #清理内容
	    markdown_text = markdownify.markdownify(str(content))  
	    print(markdown_text)  
	    # 输出Markdown
	    dt = datetime.datetime.strptime(time, '%Y-%m-%d %H:%M:%S')
	    date = dt.date()

	    file_name = str(date) + '.md'
	    print(file_name)
	    # 需要先创建 flomo目录，最终按照文件日期创建相关导出文件
	    file_path = "flomo/" + file_name
	    with open(file_path, 'a') as f:
	        f.write(f'{markdown_text}\n[{time}]\n\n')