# 使用官方的 Python 运行环境作为基础镜像
FROM python:3.8

# 设置工作目录
WORKDIR /app

# 复制项目文件到容器中
COPY . /app

# 安装项目依赖
RUN pip install -r requirements.txt

# 暴露应用程序所使用的端口
EXPOSE 5000

# 启动应用程序
CMD ["python", "aggregate/server.py"]
