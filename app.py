from flask import Flask, render_template

app = Flask(__name__)

from pymongo import MongoClient
client = MongoClient('mongodb+srv://sparta:test@cluster0.rsr8xyc.mongodb.net/?retryWrites=true&w=majority')
db = client.dbsparta

# 개별 페이지 출력
@app.route('/')
def home():
    return render_template('index.html')

@app.route('/sub1')
def sub1():
    return render_template('sub1.html')


@app.route('/sub2')
def sub2():
    return render_template('sub2.html')


@app.route('/sub3')
def sub3():
    return render_template('sub3.html')

@app.route('/sub4')
def sub4():
    return render_template('sub4.html')

@app.route('/input')
def input():
    return render_template('input.html')


# 관람평 데이터1 -----------------------------
# A : 데이터 받기
@app.route("/subA1", methods=["post"])
def subA1():
   id_receive = request.form['id_give']
   comment_receive = request.form['comment_give']
   sum = id_receive + comment_receive
   doc = {
       'id': id_receive,
       'comment' : comment_receive,
       'sum' : sum
   }
   db.vision5_comment1.insert_one(doc)
   return jsonify({'msg': '저장완료'})

#  B : 데이터 보내기
@app.route("/subB1", methods=["GET"])
def subB1():
    comment_data = list(db.vision5_comment1.find({},{'_id':False}))
    return jsonify({'result': comment_data})

#삭제기능
@app.route("/subC1", methods=["post"])
def subC1():
    id_receive = request.form['id_del']
    db.vision5_comment1.delete_one({'sum':id_receive})
    return jsonify({'del': '삭제 성공'})

# 관람평 데이터2 -----------------------------
# A : 데이터 받기
@app.route("/subA2", methods=["post"])
def subA2():
   id_receive = request.form['id_give']
   comment_receive = request.form['comment_give']
   sum = id_receive + comment_receive
   doc = {
       'id': id_receive,
       'comment' : comment_receive,
       'sum' : sum
   }
   db.vision5_comment2.insert_one(doc)
   return jsonify({'msg': '저장완료'})

#  B : 데이터 보내기
@app.route("/subB2", methods=["GET"])
def subB2():
    comment_data = list(db.vision5_comment2.find({},{'_id':False}))
    return jsonify({'result': comment_data})

#삭제기능
@app.route("/subC2", methods=["post"])
def subC2():
    id_receive = request.form['id_del']
    db.vision5_comment2.delete_one({'sum':id_receive})
    return jsonify({'del': '삭제 성공'})

# 관람평 데이터3 -----------------------------
# A : 데이터 받기
@app.route("/subA3", methods=["post"])
def subA3():
   id_receive = request.form['id_give']
   comment_receive = request.form['comment_give']
   sum = id_receive + comment_receive
   doc = {
       'id': id_receive,
       'comment' : comment_receive,
       'sum' : sum
   }
   db.vision5_comment3.insert_one(doc)
   return jsonify({'msg': '저장완료'})

#  B : 데이터 보내기
@app.route("/subB3", methods=["GET"])
def subB3():
    comment_data = list(db.vision5_comment3.find({},{'_id':False}))
    return jsonify({'result': comment_data})

#삭제기능
@app.route("/subC3", methods=["post"])
def subC3():
    id_receive = request.form['id_del']
    db.vision5_comment3.delete_one({'sum':id_receive})
    return jsonify({'del': '삭제 성공'})

# 관람평 데이터4 -----------------------------
# A : 데이터 받기
@app.route("/subA4", methods=["post"])
def subA4():
   id_receive = request.form['id_give']
   comment_receive = request.form['comment_give']
   sum = id_receive + comment_receive
   doc = {
       'id': id_receive,
       'comment' : comment_receive,
       'sum' : sum
   }
   db.vision5_comment4.insert_one(doc)
   return jsonify({'msg': '저장완료'})

#  B : 데이터 보내기
@app.route("/subB4", methods=["GET"])
def subB4():
    comment_data = list(db.vision5_comment4.find({},{'_id':False}))
    return jsonify({'result': comment_data})

#삭제기능
@app.route("/subC4", methods=["post"])
def subC4():
    id_receive = request.form['id_del']
    db.vision5_comment4.delete_one({'sum':id_receive})
    return jsonify({'del': '삭제 성공'})


# 웹 스크롤링 --------------------------------------------
# 웹 스크롤링 데이터 mongoDB에 저장
import requests
from bs4 import BeautifulSoup

@app.route('/input', methods=["POST"])
def movie_post():
    url_receive = request.form['url_give']
    # 입력한 url 저장
    comment_receive = request.form['comment_give']
    # 입력한 comment 저장
    star_receive = request.form['star_give']
    # 입력한 별점 저장

    headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
    data = requests.get(url_receive,headers=headers)
    soup = BeautifulSoup(data.text, 'html.parser')

    ogtitle = soup.select_one('meta[property="og:title"]')['content']
    ogimage = soup.select_one('meta[property="og:image"]')['content']
    # ogdesc = soup.select_one('meta[property="og:description"]')['content'] # cgv에는 og:description 태그 부분이 없기에 주석처리
    # meta tag에서 제목, 이미지, 간단 설명 스크랩하는 코드

    director = soup.select_one('#select_main > div.sect-base-movie > div.box-contents > div.spec > dl > dd:nth-child(2) > a').text
    # 감독 정보 selector 복사
    character = soup.select_one('#select_main > div.sect-base-movie > div.box-contents > div.spec > dl > dd:nth-child(5) > a:nth-child(1)').text
    # 출연진 정보 selector 복사
    character_2 = soup.select_one('#select_main > div.sect-base-movie > div.box-contents > div.spec > dl > dd:nth-child(5) > a:nth-child(2)').text
    # 출연진이 따로 따로 저장되어 있어 두번째 등장인물 저장
    character_3 = soup.select_one('#select_main > div.sect-base-movie > div.box-contents > div.spec > dl > dd:nth-child(5) > a:nth-child(3)').text
    # 세 명까지 저장
    desc = soup.select_one('#menu > div.col-detail > div.sect-story-movie').text.strip()
    # meta tag에 없던 세부 설명을 가져오기 위해 selector 따로 복사

    doc = {
        'title' : ogtitle.replace(' | 영화 그 이상의 감동. CGV',''),
        # 'desc' : ogdesc,
        'desc' : desc,
        'image' : ogimage,
        'comment' : comment_receive,
        'star' : star_receive,
        'director' : director,
        'character1' : character,
        'character2' : character_2,
        'character3' : character_3
    }
    db.movies.insert_one(doc)
    # main이라는 콜렉션 생성, 데이터들 가져와서 저장하기

    return jsonify({'msg':'등록 완료!'}) # 위 코드가 정상 작동 시 등록 완료라는 메시지 반환

# DB 데이터 -> 메인에 출력--------------------------------------------------------------------------
@app.route("/movies", methods=["GET"]) # 메인화면에서 목록을 불러오기 위한 get
def movies():
    all_movies = list(db.movies.find({},{'_id':False})) 
    # 코멘트, 감독, 등장인물은 메인화면에서 표시하지 않을 것이기 때문에 제외
    # db에서 main 콜렉션에 있는 데이터들을 리스트화 해서 저장
    return jsonify({'result': all_movies}) # 저장한 값 반환

# DB 데이터 -> 상세 페이지에 출력*****************************************************************************
# DB 데이터 -> 가디언즈 오브 갤럭시-Volume 3의 상세 페이지에 출력-----------------------------------------------
@app.route("/movies1", methods=["GET"]) # 메인화면에서 목록을 불러오기 위한 get
def movies1():
    all_movies1 = list(db.recommend_movies.find({'title':"가디언즈 오브 갤럭시-Volume 3"},{'_id':False})) 
    # 코멘트, 감독, 등장인물은 메인화면에서 표시하지 않을 것이기 때문에 제외
    # db에서 main 콜렉션에 있는 데이터들을 리스트화 해서 저장
    return jsonify({'result1': all_movies1}) # 저장한 값 반환

# DB 데이터 -> 분노의 질주-라이드 오어 다이의 상세 페이지에 출력-------------------------------------------------
@app.route("/movies2", methods=["GET"]) # 메인화면에서 목록을 불러오기 위한 get
def movies2():
    all_movies2 = list(db.recommend_movies.find({'title':"분노의 질주-라이드 오어 다이"},{'_id':False})) 
    # 코멘트, 감독, 등장인물은 메인화면에서 표시하지 않을 것이기 때문에 제외
    # db에서 main 콜렉션에 있는 데이터들을 리스트화 해서 저장
    return jsonify({'result2': all_movies2}) # 저장한 값 반환

# DB 데이터 -> 롱디의 상세 페이지에 출력------------------------------------------------------------------------
@app.route("/movies3", methods=["GET"]) # 메인화면에서 목록을 불러오기 위한 get
def movies3():
    all_movies3 = list(db.recommend_movies.find({'title':"롱디"},{'_id':False})) 
    # 코멘트, 감독, 등장인물은 메인화면에서 표시하지 않을 것이기 때문에 제외
    # db에서 main 콜렉션에 있는 데이터들을 리스트화 해서 저장
    return jsonify({'result3': all_movies3}) # 저장한 값 반환

# DB 데이터 -> 메리 마이 데드 바디------------------------------------------------------------------------------
@app.route("/movies4", methods=["GET"]) # 메인화면에서 목록을 불러오기 위한 get
def movies4():
    all_movies4 = list(db.recommend_movies.find({'title':"메리 마이 데드 바디"},{'_id':False})) 
    # 코멘트, 감독, 등장인물은 메인화면에서 표시하지 않을 것이기 때문에 제외
    # db에서 main 콜렉션에 있는 데이터들을 리스트화 해서 저장
    return jsonify({'result4': all_movies4}) # 저장한 값 반환


@app.route("/")
def index():
    return render_template('./index.html')
