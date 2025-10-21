from flask import Flask, render_template
import datetime

app = Flask(__name__)

@app.route('/')
def hello_world():
    """Hello World 主页"""
    current_time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    return render_template('index.html', 
                         message='Hello, World!',
                         current_time=current_time,
                         student_info={
                             'student_id': '20231201020',
                             'name': '彭方冠'
                         })

@app.route('/api/hello')
def api_hello():
    """API接口 - 返回JSON格式的Hello World"""
    return {
        'message': 'Hello, World!',
        'timestamp': datetime.datetime.now().isoformat(),
        'student': {
            'id': '20231201020',
            'name': '彭方冠'
        }
    }

@app.route('/hello/<name>')
def hello_name(name):
    """个性化问候页面"""
    return f'<h1>Hello, {name}!</h1><p>Welcome to our Hello World app!</p>'

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)