# web_scraping
+1. web_scraper클래스 구성
+2. 클래스 객체 생성 시 url 입력 요구
+3. __init__함수 구현(크롬 기본드라이버 설정)
+4. naver() 전체 데이터 크롤링
+4-1. naver_finish_novel()
    - 페이지를 돌아가며 크롤링(naver_basic_info/naver_page_info)을 하면서 반복하되, 마지막 페이지이면 나감
    - sleep으로 크롤링간의 시간차는 주어야 함
+4-2. naver_basic_info() 기본정보 저장 함수
    - 정적 방식으로 아래 사항 저장
    - result table구조
    - 제목 [title]
    - 작가 [writer]
    - 장르 [genre]     
    - 해당 작품 링크[link] 
    - 연재화수 [status_num]: 완결 화수 혹은 마지막 연재화
    - 연재상태 [status]: 완결
+4-3. naver_page_info()
    - 정적방식으로도 해당 작품 링크[link]로 받아와서 들어가는 방식이면 충분히 가능할거 같음 
      + 물론 SLEEP으로 크롤링할 시간주고
    - 연재기간 [period] 
    - 플랫폼[platform]
    - 상세설명[detailed_description]
    - 번역상태 [translation]: default = O
    - 태그[tag] = Null
+4-4. naver_serialized_info()
    - 해당 크롤링은 Url에서 요일별로 변화를 주면서 추가
    - 연재중의 경우 여러 날짜에 연재하는 경우 중복되는 데이터가 발생함. set로 중복제거 필요
    - naver_basic_info 실행
    - 간단하게도 2페이지 이상은 없음
    - 앞에서와 마찬가지로 naver_page_info 수집

+5-1. 얻은 데이터를 merge시킴
+6. savedata(): result to_json으로 json 형태로 만들어주고 저장
+7. novelupdate사이트