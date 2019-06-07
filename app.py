from flask import Flask,render_template,request,g
import pandas as pd
import pymysql
import lr
import time
import datetime



app = Flask(__name__)
# app.config.from_object(fundconfig)



@app.route('/',methods=["POST","GET"])
def hello_world():
    if request.method=="GET":
        # 打开数据库连接
        db = pymysql.connect(host='127.0.0.1', user='root', passwd='123456', db='stock', charset='utf8')
        cursor = db.cursor()
        sql_done_set1 = "SELECT * FROM stock_all a where stock_code = '603912.SH' order by state_dt desc "
        sql_done_set2 = "SELECT * FROM stock_all a where stock_code = '300666.SZ' order by state_dt desc "
        sql_done_set3 = "SELECT * FROM stock_all a where stock_code = '300618.SZ' order by state_dt desc "
        sql_done_set4 = "SELECT * FROM stock_all a where stock_code = '002049.SZ' order by state_dt desc "
        sql_done_set5 = "SELECT * FROM stock_all a where stock_code = '300672.SZ' order by state_dt desc "
        cursor.execute(sql_done_set1)
        g.done_set1 = cursor.fetchone()
        cursor.execute(sql_done_set2)
        g.done_set2 = cursor.fetchone()
        cursor.execute(sql_done_set3)
        g.done_set3 = cursor.fetchone()
        cursor.execute(sql_done_set4)
        g.done_set4 = cursor.fetchone()
        cursor.execute(sql_done_set5)
        g.done_set5 = cursor.fetchone()
        return render_template("index.html")
    else:
        db = pymysql.connect(host='127.0.0.1', user='root', passwd='123456', db='stock', charset='utf8')
        cursor = db.cursor()
        stock_code=request.form.get("stock_code")
        # print(stock_code)
        sql_done_set1 = "SELECT * FROM stock_all a where stock_code = '%s' order by state_dt desc " %(stock_code)
        cursor.execute(sql_done_set1)
        g.done_set1 = cursor.fetchone()
        g.stock_code=stock_code
        return render_template("result.html")
#603912.SH
@app.route("/his1/",methods=["POST","GET"],endpoint="his1")
def his1():
    if request.method=="GET":
        # 打开数据库连接
        db = pymysql.connect(host='127.0.0.1', user='root', passwd='123456', db='stock', charset='utf8')
        cursor = db.cursor()
        sql_done_set1 = "SELECT * FROM stock_all a where stock_code = '603912.SH' order by state_dt asc "
        cursor.execute(sql_done_set1)
        g.done_set1 = cursor.fetchall()
        date = []
        re = []
        d = "["
        for i in g.done_set1:
            date1 = str(i[0])
            date.append(format(date1))
            re2 = int(i[10])
            re.append(re2)
        date = date[-30:]
        date = str(date).replace("'", "")
        date = date.replace("2019-", "")
        g.date = date.replace("-", "")
        g.re = re[-30:]
        l=[]
        for i in range(1,31,1):
            l.append(i)
        g.l=l
        return render_template("his1.html")
    else:
        con = pymysql.connect(host='127.0.0.1', user='root', passwd='123456', db='stock', charset='utf8')
        sql = "SELECT * FROM stock_all a where stock_code = '603912.SH' order by state_dt asc "
        df = pd.read_sql(sql, con=con)
        df=df[['state_dt', 'pct_change']].tail(30)
        df.to_csv("603912.SH_his.csv", encoding='utf-8', index=False)
        return "数据导出成功"

@app.route("/his4/",endpoint="his4",methods=["POST","GET"])
def his4():
    if request.method == "GET":
        # 打开数据库连接
        db = pymysql.connect(host='127.0.0.1', user='root', passwd='123456', db='stock', charset='utf8')
        cursor = db.cursor()
        sql_done_set1 = "SELECT * FROM stock_all a where stock_code = '002049.SZ' order by state_dt asc "
        cursor.execute(sql_done_set1)
        g.done_set1 = cursor.fetchall()
        date = []
        re = []
        d = "["
        for i in g.done_set1:
            date1 = str(i[0])
            date.append(format(date1))
            re2 = int(i[10])
            re.append(re2)
        date = date[-30:]
        date = str(date).replace("'", "")
        date = date.replace("2019-", "")
        g.date = date.replace("-", "")
        g.re = re[-30:]
        l = []
        for i in range(1, 31, 1):
            l.append(i)
        g.l = l
        return render_template("his4.html")
    else:
        con = pymysql.connect(host='127.0.0.1', user='root', passwd='123456', db='stock', charset='utf8')
        sql = "SELECT * FROM stock_all a where stock_code = '002049.SZ' order by state_dt asc "
        df = pd.read_sql(sql, con=con)
        df = df[['state_dt', 'pct_change']].tail(30)
        df.to_csv("002049.SZ_his.csv", encoding='utf-8', index=False)
        return "数据导出成功"
#300672.SZ
@app.route("/his5/",endpoint="his5",methods=["POST","GET"])
def his5():
    if request.method == "GET":
        # 打开数据库连接
        db = pymysql.connect(host='127.0.0.1', user='root', passwd='123456', db='stock', charset='utf8')
        cursor = db.cursor()
        sql_done_set1 = "SELECT * FROM stock_all a where stock_code = '300672.SZ' order by state_dt asc "
        cursor.execute(sql_done_set1)
        g.done_set1 = cursor.fetchall()
        date = []
        re = []
        d = "["
        for i in g.done_set1:
            date1 = str(i[0])
            date.append(format(date1))
            re2 = int(i[10])
            re.append(re2)
        date = date[-30:]
        date = str(date).replace("'", "")
        date = date.replace("2019-", "")
        g.date = date.replace("-", "")
        g.re = re[-30:]
        # print(g.date, g.re)
        l = []
        for i in range(1, 31, 1):
            l.append(i)
        g.l = l
        return render_template("his5.html")
    else:
        con = pymysql.connect(host='127.0.0.1', user='root', passwd='123456', db='stock', charset='utf8')
        sql = "SELECT * FROM stock_all a where stock_code = '300672.SZ' order by state_dt asc "
        df = pd.read_sql(sql, con=con)
        df = df[['state_dt', 'pct_change']].tail(30)
        df.to_csv("300672.SZ_his.csv", encoding='utf-8', index=False)
        return "数据导出成功"
#300666.SZ
@app.route("/his2/",endpoint="his2",methods=["POST","GET"])
def his2():
    if request.method == "GET":
        # 打开数据库连接
        db = pymysql.connect(host='127.0.0.1', user='root', passwd='123456', db='stock', charset='utf8')
        cursor = db.cursor()
        sql_done_set1 = "SELECT * FROM stock_all a where stock_code = '300666.SZ' order by state_dt asc "
        cursor.execute(sql_done_set1)
        g.done_set1 = cursor.fetchall()
        date = []
        re = []
        d = "["
        for i in g.done_set1:
            date1 = str(i[0])
            date.append(format(date1))
            re2 = int(i[10])
            re.append(re2)
        date = date[-30:]
        date = str(date).replace("'", "")
        date = date.replace("2019-", "")
        g.date = date.replace("-", "")
        g.re = re[-30:]
        l = []
        for i in range(1, 31, 1):
            l.append(i)
        g.l = l
        # print(g.date, g.re)
        return render_template("his2.html")
    else:
        con = pymysql.connect(host='127.0.0.1', user='root', passwd='123456', db='stock', charset='utf8')
        sql = "SELECT * FROM stock_all a where stock_code = '300666.SZ' order by state_dt asc "
        df = pd.read_sql(sql, con=con)
        df = df[['state_dt', 'pct_change']].tail(30)
        df.to_csv("300666.SZ_his.csv", encoding='utf-8', index=False)
        return "数据导出成功"
@app.route("/his3/",endpoint="his3",methods=["POST","GET"])
def his3():
    if request.method == "GET":
        # 打开数据库连接
        db = pymysql.connect(host='127.0.0.1', user='root', passwd='123456', db='stock', charset='utf8')
        cursor = db.cursor()
        sql_done_set1 = "SELECT * FROM stock_all a where stock_code = '300618.SZ' order by state_dt asc "
        cursor.execute(sql_done_set1)
        g.done_set1 = cursor.fetchall()
        pre = cursor.fetchall()
        date = []
        re = []
        d = "["
        for i in g.done_set1:
            date1 = str(i[0])
            date.append(format(date1))
            re2 = int(i[10])
            re.append(re2)
        date = date[-30:]
        date = str(date).replace("'", "")
        date = date.replace("2019-", "")
        g.date = date.replace("-", "")
        g.re = re[-30:]
        # print(g.date, g.re)
        l = []
        for i in range(1, 31, 1):
            l.append(i)
        g.l = l
        return render_template("his3.html")
    else:
        con = pymysql.connect(host='127.0.0.1', user='root', passwd='123456', db='stock', charset='utf8')
        sql = "SELECT * FROM stock_all a where stock_code = '300618.SZ' order by state_dt asc "
        df = pd.read_sql(sql, con=con)
        df = df[['state_dt', 'pct_change']].tail(30)
        df.to_csv("300618.SZ_his.csv", encoding='utf-8', index=False)
        return "数据导出成功"

@app.route("/pre1/",endpoint="pre1",methods=["POST","GET"])
def predict1():
    if request.method == "GET":
        l = []
        for i in range(1, 8, 1):
            l.append(i)
        g.pre_date = l
        pre_data = lr.pre(state_code="603912.SH")
        li = []
        for i in pre_data:
            li.append(int(i))
        g.pre_data = li
        return render_template("pre1.html")
    else:
        pre_date=[]
        time1=datetime.datetime.now()
        for i in range(1,8,1):
            time2=time1+datetime.timedelta(days=i)
            time2=time2.strftime("%Y-%m-%d")
            pre_date.append(time2)
        pre_data = lr.pre(state_code="603912.SH")
        pre_date1={"state_dt":pre_date,"close":pre_data}
        df=pd.DataFrame(pre_date1,columns=['state_dt', 'close'])
        df.to_csv("603912.SH_predict.csv", encoding='utf-8', index=False)
        return "数据导出成功"
@app.route("/pre2/",endpoint="pre2",methods=["POST","GET"])
def predict2():
    if request.method == "GET":
        l = []
        for i in range(1, 8, 1):
            l.append(i)
        g.pre_date = l
        pre_data = lr.pre(state_code="300666.SZ")
        li = []
        for i in pre_data:
            li.append(int(i))
        g.pre_data = li
        return render_template("pre2.html")
    else:
        pre_date = []
        time1 = datetime.datetime.now()
        for i in range(1, 8, 1):
            time2 = time1 + datetime.timedelta(days=i)
            time2 = time2.strftime("%Y-%m-%d")
            pre_date.append(time2)
        pre_data = lr.pre(state_code="300666.SZ")
        pre_date1 = {"state_dt": pre_date, "close": pre_data}
        df = pd.DataFrame(pre_date1, columns=['state_dt', 'close'])
        df.to_csv("300666.SZ_predict.csv", encoding='utf-8', index=False)
        return "数据导出成功"
@app.route("/pre3/",endpoint="pre3",methods=["POST","GET"])
def predict3():
    if request.method == "GET":
        l = []
        for i in range(1, 8, 1):
            l.append(i)
        g.pre_date = l
        pre_data = lr.pre(state_code="300618.SZ")
        li = []
        for i in pre_data:
            li.append(int(i))
        g.pre_data = li
        return render_template("pre3.html")
    else:
        pre_date = []
        time1 = datetime.datetime.now()
        for i in range(1, 8, 1):
            time2 = time1 + datetime.timedelta(days=i)
            time2 = time2.strftime("%Y-%m-%d")
            pre_date.append(time2)
        pre_data = lr.pre(state_code="300618.SZ")
        pre_date1 = {"state_dt": pre_date, "close": pre_data}
        df = pd.DataFrame(pre_date1, columns=['state_dt', 'close'])
        df.to_csv("300618.SZ_predict.csv", encoding='utf-8', index=False)
        return "数据导出成功"
@app.route("/pre4/",endpoint="pre4",methods=["POST","GET"])
def predict4():
    if request.method == "GET":
        l = []
        for i in range(1, 8, 1):
            l.append(i)
        g.pre_date = l
        pre_data=lr.pre(state_code="002049.SZ")
        li = []
        for i in pre_data:
            li.append(int(i))
        g.pre_data = li
        return render_template("pre4.html")
    else:
        pre_date = []
        time1 = datetime.datetime.now()
        for i in range(1, 8, 1):
            time2 = time1 + datetime.timedelta(days=i)
            time2 = time2.strftime("%Y-%m-%d")
            pre_date.append(time2)
        pre_data = lr.pre(state_code="002049.SZ")
        pre_date1 = {"state_dt": pre_date, "close": pre_data}
        df = pd.DataFrame(pre_date1, columns=['state_dt', 'close'])
        df.to_csv("002049.SZ_predict.csv", encoding='utf-8', index=False)
        return "数据导出成功"
@app.route("/pre5/",endpoint="pre5",methods=["POST","GET"])
def predict5():
    if request.method == "GET":
        l = []
        for i in range(1, 8, 1):
            l.append(i)
        g.pre_date = l
        pre_data=lr.pre(state_code="300672.SZ")
        li = []
        for i in pre_data:
            li.append(int(i))
        g.pre_data = li
        return render_template("pre1.html")
    else:
        pre_date = []
        time1 = datetime.datetime.now()
        for i in range(1, 8, 1):
            time2 = time1 + datetime.timedelta(days=i)
            time2 = time2.strftime("%Y-%m-%d")
            pre_date.append(time2)
        pre_data = lr.pre(state_code="300672.SZ")
        pre_date1 = {"state_dt": pre_date, "close": pre_data}
        df = pd.DataFrame(pre_date1, columns=['state_dt', 'close'])
        df.to_csv("300672.SZ_predict.csv", encoding='utf-8', index=False)
        return "数据导出成功"
if __name__ == '__main__':
    app.run(debug=True)
