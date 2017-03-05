# kickstart
kickstart(google code jam)比赛环境, 方便快速进行比赛

## 指令们

1. 开始比赛, 准备模板: `./easy_go.py -c`
2. 做题, 比如说A题:
    1. 用C++来做: 直接编辑`src/A.cpp`
    2. 用python来做: `./easy_go.py A -p`, 就有`src/A.py`文件啦
3. 运行各数据(A题为例):
    1. 样例(比复制样例到文件`data/A/sample.in`, 然后`./easy_go.py A -r1`
    2. 运行small规模数据: `./easy_go.py A -r2`
    3. 运行large规模数据: `./easy_go.py A -r3`
    4. 一起运行各数据: `./easy_go.py A -r123`
    5. 用的python的话, `./easy_go.py A -rp123`
4. 备份当前代码(比如A题有个版本可以过小数据, 但不能过大数据, 先备份这个版本再说): `./easy_go.py A -b`

## 关于模板

cpp模板, py模板放在`template`里面了(`test.cpp`, `test.py`). 修改模板就修改这个.


## 其它说明

咦, 应该要有data, backup, src文件夹的, 到github怎么不见了~~

window可用, 要安装g++