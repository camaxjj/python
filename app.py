from flask import Flask, render_template, request
import pandas as pd
from pyecharts import options as opts
from pyecharts.charts import Map, EffectScatter
from pyecharts.faker import Faker
from pyecharts.globals import SymbolType
from pyecharts.charts import Pie, Bar

app = Flask(__name__)

@app.route('/')
def map() -> 'Map':
    df = pd.read_csv('data3.csv')
    a = (
        Map()
        .add("数量", list(zip(df.省, df.数量)), "china")
        .set_global_opts(
         title_opts=opts.TitleOpts(title=""),
         visualmap_opts=opts.VisualMapOpts(min_=2, max_=4924),
        )
    )
    a.render("./templates/map.html")
    with open("./templates/map.html", encoding="utf8", mode="r") as f:
        map = "".join(f.readlines())
        data_str = df.to_html()
        the_select_province = {'北京': '4924',
                               '上海': '3114',
                               '广东': '3164',
                               '浙江': '1244',
                               '南京': '701',
                               '湖北': '412',
                               '江苏': '450',
                               '福建': '359',
                               '四川': '985',
                               '辽宁': '227',
                               '安徽': '236',
                               '湖南': '239',
                               '山东': '360',
                               '吉林': '88',
                               '江西': '60',
                               '天津': '355',
                               '山西': '417',
                               '陕西': '60',
                               '重庆': '179',
                               '黑龙江': '60',
                               '河南': '477',
                               '贵州': '60',
                               '河北': '60', }
    return render_template('python_map.html',
                           the_map=map,
                           the_province=the_select_province,
                           the_res=data_str
                           )


@app.route('/effectscatter_symbol/')
def effectscatter_symbol() -> EffectScatter:
    df = pd.read_csv('data4.csv', encoding='utf8', index_col="名称")
    省 = list(df.loc["省"].values)[-24:]
    平均月薪 = list(df.loc["平均月薪"].values)[-24:]
    c = (
        EffectScatter()
        .add_xaxis(省)
        .add_yaxis("平均月薪", 平均月薪, symbol=SymbolType.ARROW)
    ).set_global_opts(title_opts=opts.TitleOpts(title=""))
    c.render("./templates/symbol.html")
    with open("./templates/symbol.html", encoding="utf8", mode="r") as f:
        sym = "".join(f.readlines())
        return render_template('python_effectscatter_symbol.html',
                               the_sym=sym,
                               )


@app.route('/pie_base/')
def pie_base() -> Pie:
    df = pd.read_csv('data1.csv', encoding='utf8')
    c = (
        Pie()
        .add("饼图", [list(z) for z in zip(df.最低学历, df.学历百分比)])
        .set_global_opts(title_opts=opts.TitleOpts(title=""))
        .set_series_opts(label_opts=opts.LabelOpts(formatter="{b}: {c}"))
    )
    c.render("./templates/pie_base.html")
    with open("./templates/pie_base.html", encoding="utf8", mode="r") as f:
        pie_base = "".join(f.readlines())
        return render_template('python_pie_base.html',
                               the_pie_base=pie_base,
                               )


@app.route('/pie_rosetype/')
def pie_rosetype() -> Pie:
    df = pd.read_csv('data1.csv', encoding='utf8')
    v = Faker.choose()
    c = (
        Pie()
        .add(
            "经验",
            [list(z) for z in zip(df.工作经验, df.经验百分比)],
            radius=["45%", "85%"],
            center=["50%", "50%"],
            rosetype="area",
        )
        .set_global_opts(title_opts=opts.TitleOpts(title=""))
    )
    c.render("./templates/pie_rosetype.html")
    with open("./templates/pie_rosetype.html", encoding="utf8", mode="r") as f:
        pie_rosetype = "".join(f.readlines())
        return render_template('python_pie_rosetype.html',
                               the_pie_rosetype=pie_rosetype,
                               )


@app.route('/Bar/')
def bar_base() -> Bar:
    df = pd.read_csv('data2.csv', encoding='utf8', index_col="学历")
    最低学历 = list(df.loc["最低学历"].values)[-6:]
    无经验 = list(df.loc["无经验"].values)[-6:]
    一年以下 = list(df.loc["一年以下"].values)[-6:]
    不限 = list(df.loc["不限"].values)[-24:]
    一至三年 = list(df.loc["一至三年"].values)[-24:]
    三至五年 = list(df.loc["三至五年"].values)[-24:]
    五至十年 = list(df.loc["五至十年"].values)[-24:]
    十年以上 = list(df.loc["十年以上"].values)[-24:]
    c = (
        Bar()
        .add_xaxis(最低学历)
        .add_yaxis("无经验", 无经验)
        .add_yaxis("一年以下", 一年以下)
        .add_yaxis("不限", 不限)
        .add_yaxis("一至三年", 一至三年)
        .add_yaxis("三至五年", 三至五年)
        .add_yaxis("五至十年", 五至十年)
        .add_yaxis("十年以上", 十年以上)
        .set_global_opts(title_opts=opts.TitleOpts(title="",
                                                   subtitle="平均月薪(元)"))
    )
    c.render("./templates/Bar.html")
    with open("./templates/Bar.html", encoding="utf8", mode="r") as f:
        bar_base = "".join(f.readlines())
        return render_template('python_bar.html',
                               the_bar_base=bar_base,
                               )


if __name__ == '__main__':
    app.run(debug=True)
