## JapanK - 日语课背单词

### 使用方式

---

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

---

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

---

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

---

#### update

更新已有的词条

```
update <table_name> SET <column1=value1, column2=value2, ...> where <column=value>
```

- 与sql标准语句格式相同，`set`后为需要改变的选项，`where`后为改变的对象。
- 如果成功就会输出`successfully updated`

---

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

```
//demo
recite character katakana
//此时通过显示片假名来背诵五十音图
```

##### 交互

1. 首先会显示背诵对象的平假名，并提示按**Enter**可以查看释义
2. 出现释义后会提示是否继续，可以：
   - 按**Enter**继续下一个
   - 按**d**将该单词从需要背诵的词汇表中删除
   - 按**0**退出背诵模式

---

#### delete

删除

```
delete <word> from <table>
```

##### word

需要删除的词条的某个信息，该信息需要在该词条所在表的`search_index`列中，否则搜索不到

##### table

指定从哪个表格中删除

---

#### quit（exit）

退出

---

#### /

该命令会重复执行上一轮指令

例如，想进行一系列单词添加，可以在第一次`create`指令后以`/`重复这条指令，方便连续添加

```
//demo
japanK> create character entry
hiragana: あ
katakana: ア
roman: a
japanK> /		//继续添加
hiragana: 
```

---

### 表格详情和创建

`data/structure.py`中存储了所有表格信息

#### 创建

想自行创建表格，只需按照一下步骤：

1. 在`data/structure.py`中创建新表格的字典，格式之后细说

2. 在表格汇总字典`TABLES`中添加表格名字和表格信息字典的对应关系

3. 在`data/structure.py`的函数`toTable(_type)`中新增 if 分支，规定哪些关键词是指向这个表格

#### structure.py 表格字典项目解释

- name - 表格名称

- columns - 以sql表格的格式书写表格的各字段名，其中注意第一项需要为“ID”，ID项之后会要求设置为自增，只是用来找到这个词条的唯一标识符，不会在show指令等展示词条的指令中输出ID。

- col_types - sql方式按顺序说明表格各字段的数据类型，其中第一项（ID）需要设置为`INTEGER AUTOINCREMENT`，是否设置为`PRIMARY KEY`并不要紧

- searchIndex - 此处输入的字段名是在search、delete等搜索操作中会被列入搜索列表的字段，例如`VOCABULARY`的此项为‘hiragana’，‘katakana’，‘kanji’，则搜索某关键词时会对每个词条检索这三项，如果有匹配到即把此词条加入搜索结果

- formats - 为各字段输出时的宽度，可自行设置以调节适合自己眼球的输出宽度，其中不要忘了第一项是ID，不会输出，所有有效设置从第二位开始

- has_active - 是否有active附属，若为True，则会在新建此表时自动添加名为active_tableName的附属表格，用于存储需要背诵的词条。例如vocabulary背诵时只会从active_vocabulary中随机抽词显示。此项只需给需要背诵的表格设置True。

---



   

