from flask import Flask, render_template

app = Flask(__name__, static_folder="static_dir")

@app.route('/')
def index():
    return render_template('index.html')
################################################
################################################
@app.route('/smertmir')
def index2():
    return render_template('Smertmir.html')
################################################
################################################
@app.route('/smertrus')
def index3():
    return render_template('Smertru.html')
################################################
################################################
@app.route('/healthmir')
def index4():
    return render_template('healths.html')
################################################
################################################
@app.route('/healthrus')
def index5():
    return render_template('graphicRuSSia.html')
################################################
################################################
@app.route('/testmir')
def index6():
    return render_template('test_World.html')
################################################
################################################
@app.route('/testrus')
def index7():
    return render_template('test_RUS.html')
################################################
################################################
@app.route('/morbiditymir')
def index8():
    return render_template('index (1).html')
################################################
################################################
@app.route('/morbidityrus')
def index9():
    return render_template('index2.html')
################################################
################################################
@app.route('/vacmir')
def index10():
    return render_template('vacmir.html')
################################################
################################################
@app.route('/vacrus')
def index11():
    return render_template('vacrus.html')