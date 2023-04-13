import pandas as pd
# from sqlalchemy import create_engine
# from db_config import engine


class Db():
    def __init__(self, engine):

        self.engine = engine

    def save_df_to_db(self, df, table_name):
        df.to_sql(con=self.engine,
                  name=table_name,
                  if_exists='replace',
                  index=False)

        print(
            f"{table_name} is successfully stored in the database: {self.engine_params['database']}"
        )

    def select_table_names_from_database(self):
        conn = self.engine.connect()

        # 查询数据库中的所有表名
        query = """
            SELECT TABLE_NAME
            FROM INFORMATION_SCHEMA.TABLES
            WHERE TABLE_TYPE = 'BASE TABLE' AND TABLE_CATALOG = %s
        """
        tables = conn.execute(query,
                              (self.engine_params['database'], )).fetchall()
        table_list = [table[0] for table in tables]
        print("成功获取到{}数据库中{}张表的表名".format(self.engine_params['database'],
                                          len(table_list)))
        # 关闭连接
        conn.close()
        return table_list

    def select_table_from_database(self, table):
        sql = f"SELECT * FROM {table}"
        df = pd.read_sql(sql=sql, con=self.engine)
        return df
