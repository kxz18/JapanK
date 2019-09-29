## JapanK - 日语课背单词

### 使用方式

#### create

创建新词条

```
create <entry type> entry [word info]
```

##### entry type

- word - 单词
- character - 字符
- sentence - 句子

##### word info

此为选择项，可以不加，如果不加的话可以按提示输入新加项的内容；如果加的话需按照词条所需项一个个输入信息

- 建议不加

#### show

展示现有的表

```
show <table name>
```

##### table name

- 详情可以看data目录下的structure.py
- 常用：
  - vocabulary/words - 所有单词
  - fifty/character - 五十音
  - sentence - 所有句子

#### search

搜索词条

```
search <parameter1, parameter2, ...> (from <table1, table2, ...>)
```

#####  parameter

可以有**多个**搜索目标，结果会返回所有符合要求的结果集合

- 搜索参数可以见data目录下structure.py中的`search_index`项
- 常用搜索参数
  - 平假名
  - 片假名
  - 汉字

##### table

可选参数，如果填了，就从指定的表格中搜索结果

#### update

更新已有的词条

```
update <table_name> SET <column1=value1, column2=value2, ...> where <column=value>
```

- 与sql标准语句格式相同，`set`后为需要改变的选项，`where`后为改变的对象。
- 如果成功就会输出`successfully updated`

#### recite

随机背诵功能

```
recite <type> [options]
```

##### type

背诵的种类

- word(s) - 背诵单词
- character - 字符
- sentence - 句子

##### options

可选选项，默认背诵时显示平假名（如果是外来词会显示片假名）

- hiragana - 背诵时显示平假名
- katakana - 背诵时显示片假名

##### 交互

1. 首先会显示背诵对象的平假名，并提示按**Enter**可以查看释义
2. 出现释义后会提示是否继续，可以：
   - 按**Enter**继续下一个
   - 按**d**将该单词从需要背诵的词汇表中删除
   - 按**0**退出背诵模式

#### delete

删除

```
delete <word> from <table>
```

##### word

需要删除的词条的某个信息，该信息需要在该词条所在表的`search_index`列中，否则搜索不到

##### table

指定从哪个表格中删除

#### quit（exit）

退出

#### /

该命令会重复执行上一轮指令