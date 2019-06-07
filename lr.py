import math
import numpy as np
import pymysql
import pandas as pd
from sklearn import preprocessing, model_selection
from sklearn.linear_model import LinearRegression

def pre(state_code):
    con = pymysql.connect(host='127.0.0.1', user='root', passwd='123456', db='stock', charset='utf8')
    sql = "SELECT * FROM stock_all a where stock_code = '%s' order by state_dt asc " %(state_code)
    df = pd.read_sql(sql, index_col='state_dt',
                     parse_dates=True, con=con)
    # 定义预测列变量，它存放研究对象的标签名
    forecast_col = 'close'
    # 定义预测天数
    # forecast_out = int(math.ceil(0.01*len(df)))
    forecast_out = 7
    # 只用到df中下面的几个字段
    df = df[['open', 'high', 'low', 'close', 'vol']]

    # 构造两个新的列
    # HL_PCT为股票最高价与最低价的变化百分比
    df['HL_PCT'] = (df['high'] - df['close']) / df['close'] * 100.0
    # HL_PCT为股票收盘价与开盘价的变化百分比
    df['PCT_change'] = (df['close'] - df['open']) / df['open'] * 100.0
    # 下面为真正用到的特征字段
    df = df[['close', 'HL_PCT', 'PCT_change', 'vol']]
    # 因为scikit-learn并不会处理空数据，需要把为空的数据都设置为一个比较难出现的值，这里取-9999，
    df.fillna(-99999, inplace=True)
    # 用label代表该字段，是预测结果
    # 通过让与Adj. Close列的数据往前移动1%行来表示
    df['label'] = df[forecast_col].shift(-forecast_out)

    X = np.array(df.drop(['label'], 1))
    X = preprocessing.scale(X)
    X_lately = X[-forecast_out:]
    X = X[:-forecast_out]
    # 抛弃label列中为空的那些行
    df.dropna(inplace=True)
    y = np.array(df['label'])

    X_train, X_test, y_train, y_test = model_selection.train_test_split(X, y, test_size=0.2)

    clf = LinearRegression(n_jobs=-1)
    clf.fit(X_train, y_train)  # Here, start training
    accuracy = clf.score(X_test, y_test)  # Test an get a score for the classfier
    forecast_set = clf.predict(X_lately)
    return forecast_set