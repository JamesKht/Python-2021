##一、标题
# Heading level 1
## Heading level 2
### Heading level 3
#### Heading level 4
##### Heading level 5
###### Heading level 6
-----------------------------

##二、正文

I really like using Markdown.

换行需要两个回车

##三、加粗，斜体，间隔号


- 要加粗文本，请在单词或短语的前后各添加两个**星号**或__下划线__

- 要用斜体显示文本，请在单词或短语前后添加一个*星号*或_下划线_

- 要同时用粗体和斜体突出显示文本，请在单词或短语的前后各添加三个***星号***或___下划线___

- 由于Markdown 应用程序在处理单词或短语中间添加的下划线上并不一致。为了实现兼容性，使用**星号**将单词或短语的中间部分加粗并以斜体显示，以示重要。

##四、引用

>1、要创建块引用，请在段落前添加一个 > 符号。

>2、块引用可以包含多个段落。
>
>为段落之间的空白行添加一个 > 符号。
>
>3、块引用可以嵌套。
>>在要嵌套的段落前添加一个 >> 符号。
>
>4、可以引用上述的其他块引用

## 五、列表

1. First item
8. Second item
3. Third item
5. Fourth item
1. First item
2. Second item
3. Third item
    3. Indented item
    2. Indented item
4. Fourth item

数字不必按数学顺序排列，但是列表应当以数字 1 起始。

* First item
- Second item
+ Third item
  - Indented item
     - Indented item
+ Fourth item

## 六、代码

要创建代码块，请将代码块的每一行缩进至少四个空格或一个制表符。

	<python>
		print("hello world")
	</python>

At the command prompt, type `nano`.

You also can ``use `code` in your Markdown file.``

围栏代码块

```
据Markdown处理器或编辑器的不同，您将在代码块之前和之后的行上使用三个反引号或三个波浪号。
```

```
{
  "firstName": "John",
  "lastName": "Smith",
  "age": 25
}
```

## 七、分隔线

要创建分隔线，请在单独一行上使用三个或多个星号 (***)、破折号 (---) 或下划线 (___) ，并且不能包含其他内容。

***

为了兼容性，请在分隔线的前后均添加空白行。

---

为了兼容性，请在分隔线的前后均添加空白行。

______

## 八、链接

这是一个链接 [Markdown语法](https://markdown.com.cn)。

这是一个链接 [Markdown语法](https://markdown.com.cn "最好的markdown教程")。

使用尖括号可以很方便地把URL或者email地址变成可点击的链接。

<https://markdown.com.cn>

<fake@example.com>

强调链接, 在链接语法前后增加星号。 要将链接表示为代码，请在方括号中添加反引号。

I love supporting the **[EFF](https://eff.org)**.

This is the *[Markdown Guide](https://www.markdownguide.org)*.

See the section on [`code`](#code).

>- 不同的 Markdown 应用程序处理URL中间的空格方式不一样。为了兼容性，请尽量使用%20代替空格。
>
> [link](https://www.example.com/my%20great%20page)

## 九、图片

![这是图片](baby.jpg "baby")

[![沙漠中的岩石图片](baby.jpg "baby")](https://https://markdown.com.cn/assets/img/shiprock.c3b9a023.jpg)

## 十、转义字符

访问https://markdown.com.cn/basic-syntax/escaping-characters.html获取帮助

## 十一、内嵌HTML标签

This **word** is bold. This <em>word</em> is italic.

区块标签
```
区块元素──比如 <div>、<table>、<pre>、<p> 等标签，必须在前后加上空行，以便于内容区分。而且这些元素的开始与结尾标签，不可以用 tab 或是空白来缩进。Markdown 会自动识别这区块元素，避免在区块标签前后加上没有必要的 <p> 标签。
```
This is a regular paragraph.

<table>
    <tr>
        <td>Foo</td>
    </tr>
</table>

This is another regular paragraph.

在 HTML 块级标签内不能使用 Markdown 语法。

例如 
> <p>italic and **bold**</p> 
> 将不起作用。

