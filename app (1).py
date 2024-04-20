from flask import Flask, jsonify, request, render_template

app = Flask (__name__)

@app.route('/')
def index ():
    return render_template('index.html')

@app.route('/google-charts/curve-chart')
def google_curve_chart():
    data = {'Task' : 'Hours per Day', 'Work' : 11, 'Eat' : 2, 'Commute' : 2, 'Watching TV' : 2, 'Sleeping' : 7}
    return render_template('curve-chart.html', data=data)

if __name__=="__main__":
    app.run()


