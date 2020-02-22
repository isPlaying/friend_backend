# friend_backend



- Python3
- Flask1.1.1
- MySQL5.7
- Docker

项目结构
~~~
├── api
│   ├── app
│   │   ├── __init__.py
│   │   │
│   │   └── friend
│   │       ├── __init__.py
│   │       │ 
│   │       └── friend.py
│   ├── dao
│   │   ├── __init__.py
│   │   │
│   │   ├── db.py              
│   │   └── schema.sql
│   ├── requirements.txt       
│   └── run.py                 
├── deploy                 
│   ├── data
│   │   └── mysql
│   │       └── conf.d
│   │           └── mysql.cnf  # mysql配置文件
│   └── docker-compose.yml     
├── docker                     # docker目录
│   ├── Dockerfile             
│   └── build.sh               # 镜像打包脚本
└── requirements.txt           # 依赖文件

~~~


操作指南

- 基于docker启动

~~~
# 克隆仓库
1. git clone git@github.com:isPlaying/friend_backend.git

# 进入deploy目录
2. cd friend_backend/deploy/

# 启动应用
3. docker-compose up
~~~
