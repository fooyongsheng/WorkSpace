##### 使用清华源安装

> pip install tensorflow-gpu==2.0.0 -i https://pypi.tuna.tsinghua.edu.cn/simple
>
> 把conda源设置为清华源：conda config --add channels https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/free/         conda config --set show_channel_urls yes

##### Ubuntu常用压缩和解压

> .tar 打包，并无压缩
>
> 解包： tar -xvf filename.tar
>
> 打包：tar -cvf filename.tar filename
>
> .gz
>
> 解压：gunzip filename.gz  或 gzip -d filename.gz
>
> 压缩：gzip filename
>
> .tar.gz,  .tgz  压缩
>
> 解压：tar -zxvf filename.tar.gz
>
> 压缩： tar -zcvf filename.tar.gz filename
>
> 解压到指定路径：tar -c path/filename -zxvf filename.tar.gz
>
> .zip
>
> 解压：unzip filename.zip
>
> 压缩：zip filename.zip filename
>
> 将目录下的所有文件和子目录一起压缩：zip -r filename.zip filename
>
> .rar
>
> 解压：rar x filename.rar
>
> 压缩：rar a filename.rar filename
>
> 

##### 导入自定义文件夹里面的py文件时

> import sys, os
> sys.path.append(os.path.join(os.getcwd(),'directory_name/'))

##### Ubuntu一个界面多命令行窗口

> ctrl+shift+T

##### ubuntu文件隐藏于显示

> ctrl+h

##### conda使用

> conda创建env环境：conda create -n env_name python=X.X(2.7, 3.5, 3.6)
> conda查看env列表: conda env list
> conda激活环境：conda activate env_name
> conda关闭环境：conda deactivate
> conda查看安装的包：conda list
> codna删除环境：conda remove -n env_name --all

##### virtualenv使用，jupyter notebook

> 创建虚拟环境：mkvirtualenv env_name -p /usr/bin/python3.5
> 激活环境：workon env_name  或 source activate env_name
> 关闭环境：deactivate
> 查看列表：lsvirtualenv
>
> 复制环境：cpvirtualenv source_env dst_env
>
> 删除环境：rmvirtualenv env_name
>
> 指定jupyter notebook使用虚拟环境： ipython kernel install --user --name=my_venv
>
> jupyter notebook运行：Ctrl+Enter   或 Shift+Enter 运行并跳到下一行
>
> 查看所有jupyter中的核心： jupyter kernelspec list
>
> 删除指定核心：jupyter kernelspec remove kernel_name
>
> cd到当前环境的site-packages目录：cdsitepackages
>
> 列出当前环境中site-packages内容：lssigepackages
>
> 绑定现存的项目和环境：setvirtualenvproject
>
> 清除环境内所有第三方包：wipeenv

##### 软链接的创建与删除：保持每一处链接文件的同步性

> 软链接ln -s src dst,生成镜像，不会占用空间
> 硬链接ln src dst，占用磁盘空间
> 创建：sudo ln -s /origianl_path/directory_name   /save_path/symbolic_name
> 删除：rm -rf symbolic_name
> 修改：ln -s /new_link_path/directory_name  /save_path/symbolic_name
> 覆盖：-b
> 强制执行：-f

##### 修改Ubuntu下Python软链接

> 查看Python对应指向：ls -l /usr/bin | grep python
> 删除原有Python软链接：rm /usr/bin/python
> 建立新的Python软链接：ln -s /usr/bin/python3.5 /usr/bin/python 
> 下载Python3版本的pip：apt-get insatll python3-pip
> 建立pip到pip3的软链接：ls -s /usr/bin/pip3 /usr/bin/pip

##### docker的使用

> 服务器上已经安装上docker，现在是在一个docker用户组下面配置自己的环境
> docker查看镜像列表：docker images 或 docker image ls
> docker查找镜像：docker search image_name(tensorflow, pytorch, ubuntu16.04)
> docker查看容器列表: docker ps -a
> docker删除镜像：
> 		1).先退出容器：exit or ctrl+d
> 		2).先删除对应的container： docker rm container_ID
> 		3).再删除对应的image: docker rmi image_ID/repository_name
> 		4).如果镜像存在子镜像，需要先删除子镜像
> docker创建镜像
> 		1). 从镜像库中拉取： docker pull image_name(通过search寻找)
> 		2). 从Dockerfile文件创建：docker run -i -t image_name /bin/bash
> 镜像重命名：docker tag image_ID repository_name:tag_name
> 容器重命名：docker rename old_container_name new_container_name
> 启动镜像：docker run -it image_name /bin/bash    #-it交互运行，-d后台运行
> 将主机目录挂在到镜像：docker run -it -v local_path:in_image_path --name container_name image_name /bin/bash，(比如将服务器的根目录挂载到pytorch-yxq镜像下的root目录：nvidia-docker run -it -v /:/root --name home-yxq pytorch-yxq /bin/bash)
>
> 在docker中使用apt-get install之前：apt-get update
>
> 查找nvidia的docker环境：[docker hub](https://hub.docker.com/r/nvidia/cuda/)
>
> 启动容器：docker start container_ID
>
> 启动镜像：docker  start container_name  & docker attach container_name
>
> 停止容器：docker stop name/contrainer_ID
>
> 强制停止容器：docker kill name/container_ID

##### Latex

> 一. 安装Textlive+Texstudio
>
> 下载Texlive：[官网](https://tug.org/texlive/)或[清华镜像](https://mirrors.tuna.tsinghua.edu.cn/CTAN/systems/texlive/Images/)
>
> 网页版：[overleaf](https://www.overleaf.com/)
>
> 二. ubuntu安装texlive+texstudio
>
> 1). 下载texlive2019: [官网](https://tug.org/texlive/)或[清华镜像](https://mirrors.tuna.tsinghua.edu.cn/CTAN/systems/texlive/Images/)
>
> 2). 安装texlive2019.iso文件
>
> 安装图形化用户界面(似乎可有可无)：sudo apt-get install perl-tk
>
> 加载.iso镜像文件：sudo mount -o loop texlive2019.iso /mnt
>
> 启动图形化安装配置：cd /mnt/
>
> ​									  sudo ./install-tl -gui 				
>
> 安装完成后，卸载镜像文件： cd /;  sudo umount /mnt					
>
> 字体配置：	sudo cp /usr/local/texlive/2019/texmf-var/fonts/conf/texlive-fontconfig.conf /etc/fonts/conf.d/09-texlive.conf 
>
> ​						sudo fc-cache -fsv 
>
> 在~/.bashrc中添加环境变量：
>
> ​								export MANPATH=${MANPATH}:/usr/local/texlive/2019/texmf-dist/doc/man
> ​								export INFOPATH=${INFOPATH}:/usr/local/texlive/2019/texmf-dist/doc/info
> ​								export PATH=${PATH}:/usr/local/texlive/2019/bin/x86_64-linux
> 安装成功测试：  tex --version
>
> 3). 安装texstudio
>
> 下载texstudio: 官网下载的源码安装不上，使用ppa方式也安装不上，因此使用 [texstudio AppImage](https://sourceforge.net/projects/texstudio/)，不用安装可直接运行
>
> 如何运行AppImage文件：文件右键->属性->权限->运行作为程序执行文件，然后双击可运行
>
> texstudio配置texlive环境：options->configure texstudio->commands，找到latex, pdflatex, xelatex, lualatex, bibtex, biber对应的路径，在/usr/local/texlive/2019/bin/x86_64-linux/xxx
>
> 测试：新建.tex文件，运行
>
> 三. latex使用技巧
>
> 使用中文，在`\documentclass`之前加一行： % !TeX program=xelatex
>
> ​															使用包：	\usepackage{xeCJK}  或 \usepackage{ctex}

##### 绘图工具

> 绘制各种流程图
>
> [draw.io](https://www.draw.io/)
>
> [ProcessOn](https://processon.com/)

##### Markdown使用

> 编辑.md文件，推荐：typora

##### 记事本

> 快捷美观记事本：oneNote
>
> 列表记事本：Trello

##### 论文管理工具

> 快捷管理论文，导出参考文献：mendeley

##### 播放器

> 可直接通过在线视频链接播放：[VLC](https://www.videolan.org/vlc/)
>
> 可按帧播放，快捷键提取帧画面：PotPlayer

##### 远程服务器

> 客户端：VNC Viewer
>
> 服务器端：VNC Server
>
> windows数据传输：WinSCP
>
> ubuntu数据传输：FileZilla

##### 编辑本

> Sublime Text
>
> VSCode

##### 编译器

> python，可远程编译：PyCharm Professional
>
> C/C++：Clion, Visual Studio, dev C++轻便

##### ubuntu安装软件包

> .deb安装包：sudo dpkg -i xxxx.deb
>
> .sh安装：bash xxxx.sh

##### 查看系统版本

> 查看系统是哪个Linux的发行版本
>
> lsb_release -a

##### Ubuntu卸载软件

> 查看软件安装位置：whereis xxx，比如卸载vscode, whereis code
>
> 通过apt-get 方式安装的，删除时会有提示确认
>
> ​				卸载，保留配置：sudo apt-get remove code
>
> ​				彻底清除，包括配置：sudo apt-get --purge remove code 或 sudo apt-get purge code
>
> 通过dpkg方式安装的，删除时没有确认提示
>
> ​				只是卸载，保留配置：sudo dpkg -r code 或 sudo  dpkg --remove code
>
> ​				彻底清除，包括配置：sudo dpkg -purge code

##### git使用

> 查看系统是否安装git: git
>
> 安装git: sudo apt-get install git
>
> 设置机器：git config --global user.name 'Yxiaoqian'
>
> ​					git config --global user.email '18373152076@163.com'
>
> 把目录变成git可以管理的仓库：git init
>
> 把文件添加到仓库: git add filename   或 git add *  添加目录下所有文件
>
> 把文件提交到仓库: git commit -m 'some statement'
>
> 查看仓库状态：git status
>
> 查看仓库文件具体修改内容： git diff filename
>
> 提交后查看工作区和版本库里面最新版本的区别：git diff HEAD -- filename
>
> 还原工作区的修改：git checkout -- filename
>
> 查看文件属性：cat filename
>
> 删除文件：git rm filename
>
> 远程仓库创建SSH Key: ssh-keygen -t rsa -C 'email@xxx.com'
>
> 远程仓库添加SSH Key: 添加/home/yxq/.ssh/id_rsa.pub文件的内容
>
> 本地仓库关联远程仓库： git remote add origin git@github.com:Yxiaoqian/Read-Papers.git
>
> 本地仓库的内容推送到远程仓库：git push -u origin master(第一次) 或  git push origin master
>
> 推送其他分支： git push origin dev
>
> 从远程仓库克隆: git clone git@github.com:Yxiaoqian/Read-Papers.git
>
> 修改克隆下来的文件: git catch readme.md
>
> 创建dev分支，并切换到dev分支：git checkout -b dev 或git switch -c dev（更科学） 等同于下面两条命令
>
> 创建分支：git branch dev  
>
> 切换分支： git checkout dev    或 git switch dev（更科学）
>
> 查看当前分支: git branch
>
> 合并某分支到当前分支：git merge dev
>
> 删除分支： git branch -d dev
>
> 查看分支合并图：git log --graph
>
> 查看远程仓库信息：git remote  或 更详细 git remote -v
>
> 抓取远程最新的内容: git pull
>
> 取消本地关联的远程仓库：git remote remove origin
>
> 删除远程仓库的文件夹或文件：先预览  git rm -r -n --cached  dir_name/file_name
>
> ​										确认无误后删除  git rm -r --cached  dir_name/file_name
>
> ​										提交本地到远程服务器 git commit -m 'statement'
>
> ​																				git push origin master

##### pytorch

> 1. 查看函数文档： torch.func_name?   或 torch.func_name??

##### IPython

> %，魔术命令：
>
> （1）%hist 查看在当前IPython下的输入历史
>
> （2）%timeit a.sum()  检测某条语句的执行时间
>
> （3）%paste 执行粘贴板中的代码
>
> （4）%cat a.py  查看某一个文件的内容
>
> （5）%run -i a.py 执行文件，-i表示在当前命令空间中执行
>
> （6）% command? 或 %command?? 查看使用说明
>
> （7）%quickref 显示快速参考
>
> （8）%who显示当前命名空间中的变量
>
> （9）%debug进入调试模式，按q退出
>
> （10）%magic查看所有魔术命令
>
> （11）%env查看系统环境变量
>
> （12）%xdel 删除变量并删除其在IPython上的一切引用