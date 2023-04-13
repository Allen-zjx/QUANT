# from datetime import datetime, timedelta
# import pytz
import pandas as pd


def read_data(data_path: str, cols: list = None) -> pd.DataFrame:
    """
    从指定的数据文件中读取数据，并返回一个pandas的DataFrame对象。

    Args:
        data_path (str): 数据文件的路径。
        cols (list): 需要读取的列名列表，如果为None，则读取所有列。默认为None。

    Returns:
        pd.DataFrame: 读取的数据。

    Raises:
        ValueError: 数据文件的格式不支持。

    """
    file_format = data_path.split(".")[-1]

    if file_format == "csv":
        try:
            df = pd.read_csv(data_path, usecols=cols)
        except UnicodeDecodeError:
            try:
                df = pd.read_csv(data_path, usecols=cols, encoding='gbk')
            except UnicodeDecodeError:
                df = pd.read_csv(data_path, usecols=cols, encoding='gb18030')
                try:
                    df = pd.read_csv(data_path, usecols=cols, encoding='ISO-8859-1')
                except UnicodeDecodeError as e:
                    df = pd.read_csv(data_path, usecols=cols, encoding='ANSI')
                    raise ValueError(
                        "The file encoding is not supported. Tried gbk、gb18030、ISO-8859-1、ANSI."
                    ) from e
    elif file_format == "xlsx":
        df = pd.read_excel(data_path, usecols=cols)
    else:
        raise ValueError(
            "Invalid file format. Only csv and xlsx are supported.")

    return df
