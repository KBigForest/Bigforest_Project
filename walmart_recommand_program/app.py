from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/search', methods=['POST'])
def search():
    search_query = request.form['search']
    # 검색어를 이용하여 데이터베이스에서 검색결과를 찾는 로직 구현
    # 검색결과를 리스트로 받아옴
    search_result = [
        {'항목 1': '결과 1-1', '항목 2': '결과 1-2', '항목 3': '결과 1-3'},
        {'항목 1': '결과 2-1', '항목 2': '결과 2-2', '항목 3': '결과 2-3'}
    ]
    return render_template('index.html', search_query=search_query, search_result=search_result)

if __name__ == '__main__':
    app.run()