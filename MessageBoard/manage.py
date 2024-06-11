from app import create_app
import os

# 默认为开发环境，按需求修改
config_name = "default"

app = create_app(config_name)

if __name__ == '__main__':
    app.run()