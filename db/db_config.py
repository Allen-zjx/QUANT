from sqlalchemy import create_engine

# MySQL 连接信息
db_user = 'Quant_zjx'
db_password = 'Zjx102910.'
db_host = 'lsh-cynosdbmysql-grp-argzeyja.sql.tencentcdb.com'
db_port = 22020
db_name = 'Macro'

# 创建 MySQL 连接字符串
db_url = f"mysql+pymysql://{db_user}:{db_password}@{db_host}:{db_port}/{db_name}"

# 创建 MySQL 数据库引擎
engine = create_engine(db_url, echo=True)
