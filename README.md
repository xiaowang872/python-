# 项目介绍：

<div id="border-example" style="  
  border: 1px solid #333;   
  border-radius: 8px;   
  box-shadow: 2px 2px 5px rgba(0, 0, 0, 0.2);  
  color: red; /* 将文字颜色设置为红色 */  
  text-align: left; /* 水平居中 */  
">  
	 1：python脚本实现自动邮件分发功能。</br>
	 2：支持查看历史qq号功能。</br>
	 3：支持清除历史qq号功能。</br>
</div>



# 如何使用？

## 在send_main.py文件内

![](https://images.cnblogs.com/cnblogs_com/blogs/827070/galleries/2427603/o_241022111714_QQ20241022-191529.png)

输入发件人和接受人的qq号

```python
msg['From'] = '***********@qq.com'   
msg['To'] = '********@qq.com'
```

在此处填入发件人qq号和发件人发件人SMTP授权码

# 如何更改发送邮件内容？

### 默认发送邮件为email.html

发送内容可在email.html修改

## 可以发送txt文本吗？

当然可以

### 你只需要在send_mail.py中

![](https://images.cnblogs.com/cnblogs_com/blogs/827070/galleries/2427603/o_241022112533_QQ20241022-192459.png)

修改为你所要上传的文件即可

```python
textfile = 'email.html'
```
# 一切准备就绪，运行main.py
