## git learning

### 概述
- 版本库(Repository): git初始化后,在当前目录会生成一个.git目录.
- Workspace工作区: .git所在的目录是工作区,一般是项目根目录.
- Index索引: 介于工作区和版本库之间,暂存修改的.
- remote远程版本库: 网络上的版本库,可以和本地库交互.

### 使用
- 本地初始化一个版本库: `git init`
- 新建文件.
  - 单个文件添加:`git add filename`, 把文件的当前变化增加到索引中,以后这个文件需要版本库来跟踪管理. 
  - 批量添加:`git add .` 将递归添加当前目录及其子目录所有文件.
- 查看状态:`git status`,短格式输出: `git status -s`
- 提交代码: `git commit --help`
  - `git commit -m "update"`,commit提交更改到版本库,-m 填写本次日志消息.

### git提交
提交分为2个步骤:
- 暂存变更: add作用是把新文件或者文件新的改动添加到一个暂存区stage,加入到Index中.
- 提交变更: commit提交的是暂存区中的改动. 提交到当前分支,默认是master分支.

批量提交文件:
- `git commit -a -m "message"`, -a把所有跟踪的文件的改动自动暂存,然后commit.


查看版本库里提交的历史记录: `git log`

### 检出和重置
checkout用于切换分支,或恢复工作区文件.
| 命令  | 说明  |
| ---: | ---: |
| `git checkout` | 列出暂存区可以被检出的文件 |
| `git checkout file` | 从暂存区检出文件到工作区,覆盖工作区文件,可指定检出的文件,不清除stage. |
| `git checkout commit file` | 检出某个commit的指定文件到暂存区和工作区 |
| `git checkout .` | 检出暂存区的所有文件到工作区. |


| 命令  | 说明  |
| ---: | ---: |
| `git reset` | 列出将被reset的文件 |
| `git reset file` | 重置文件的暂存区,工作区不影响 |
| `git reset --hard` | 重置暂存区和工作区 |
| `git reflog` | 显示commit信息,HEAD变化,就可以看到 |
| `git reset commit` | 重置当前分支的HEAD为指定commit,重置暂存区,工作区不变 |
| `git reset --hard [commit]` | 重置当前分支的HEAD为指定commit,重置暂存区和工作区 |
| `git reset --keep [commit]` | 重置当前HEAD为指定commit,但保持暂存区和工作区不变. |

### 移动和删除
- 改名,把改名的改动放入暂存区:`git mv src dest`
- 真删除,同时在版本库和工作目录删除文件:`git rm file`
- 
将文件从暂存转成未暂存,从版本库中删除,但不删除工作目录的该文件,即文件恢复成不追踪的状态:`git rm --cached file`

**注意: commit以后算是真的改动了.**

### push推送

- 配置本地用户名和邮箱:
  ```
  git config --global user.name "firstoney"
  git config --global user.email "devops_yj@163.com"
  ```

- 关联远程版本库
  - 列出所有远程仓库:`git remote`
  - 详细列出所有远程仓库: `git remote -v`
  - 指定一个名称指向远程仓库:`git remote add [shortname] [url]`,远程版本库名origin,是习惯用法,将建立origin和url的映射,这些信息保存在.git/config文件的`[remote "origin"]`中.
    ```
    git config --system 在/etc/gitconfig文件中读写配置.
    git config --global 在~/.gitconfig文件中读写配置.
    ```
    `.git/config`这个文件是版本库级别设置文件.

- 推送数据
  - 指定推送到的远程主机和分支:`git push origin master`
  - 指定当前分支推送到的主机和对应分支:`git push origin`
  - 指定远程默认主机和分支:`git push -u origin master`
  - 默认只推送当前分支到默认关联的远程仓库.

