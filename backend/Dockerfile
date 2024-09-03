# 使用轻量级Python镜像作为基础镜像
FROM python:3.12-slim

# 设置工作目录
WORKDIR /app

# 将 Poetry 安装到镜像中
RUN pip install poetry

# 复制 Poetry 项目文件
COPY pyproject.toml poetry.lock ./

# 安装依赖（不创建虚拟环境，直接在Docker容器的环境中安装）
RUN poetry config virtualenvs.create false && poetry install --no-interaction --no-ansi

# 复制应用代码
COPY . .

# 暴露服务端口
EXPOSE 5000

# 启动应用
CMD ["poetry", "run", "python", "main.py"]

