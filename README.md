# KBO_Mock_Draft
A simulated draft in Korea Baseball League in 2018

아이디어 : 2018 KBO 모의 신인 30인 드래프트

## Raw data

* [2017hitter.csv](#sukku04/KBO_Mock_Draft/2017hitter.csv) (규정타석충족 타자)
* [2017pitcher.csv](#sukku04/KBO_Mock_Draft/2017pitcher.csv) (규정이닝충족 투수)
* [2017notqualified_hitter.csv](#sukku04/KBO_Mock_Draft/2017notqualified_hitter.csv) (규정타석미충족 타자)
* [2017notqualified_pitcher.csv](#hitter.ipynb) (규정타석미충족 투수)

** source : Korean highschool baseball league in 2017 on Korea Baseball Softball Association <br>
http://www.korea-baseball.com/record/record/team_record?kind_cd=31&lig_idx=&group_no=&part_no=&season=2018&club_idx=190&player_type=2&group_part_idx=

## Relevant references 

* 고교야구 규정타석 * 이닝 계산
  1) 규정타석 : 팀게임수 * 0.8 * 3(고교야구 시상 기준)<br>
  2) 규정이닝 : 팀게임수 * 0.8 (퓨처스리그 기준)<br>
https://sites.google.com/site/eveningglow17/record/yagu-yong-eo-jeongli

* War(Wins Above Replacement Player)
  1) 투수
http://suxism.com/?p=3467
  2) 타자
http://suxism.com/?p=225

* 2017년 고교야구선수 세부지표
  1) 투수
http://biz.heraldcorp.com/sports/view.php?ud=201710121554026756813_1
  2) 타자
http://biz.heraldcorp.com/sports/view.php?ud=201710181552357377512_1 


* 투수 기록 주요 지표 
  1) cFIP http://suxism.com/?p=1956<br>
  2) FIP http://dontyou.tistory.com/42<br>

* 타자 기록 지표 ( UEQR과 WOBA 차이)<br>
https://blog.naver.com/ianthorpe/220830724053<br>
  1) UEQR<br>
https://namu.wiki/w/UEQR
  2) EQA<br>
https://namu.wiki/w/eqa

* 스카우트 기준 지표<br>
  1) 80 20 Rule(항목별평가) <br>
http://baseballgen.com/78 http://www.mbcsportsplus.com/news/?mode=view&cate=2&b_idx=99977638.000#07D0
https://www.fangraphs.com/blogs/scouting-explained-the-20-80-scouting-scale/
  2) OFP(종합평가)<br>
https://legacy.baseballprospectus.com/glossary/index.php?search=OFP
https://www.baseballamerica.com/draft-history/mlb-draft-database/
  3) 스카우터 인터뷰 글<br>
http://www.gqkorea.co.kr/2016/06/05/%EB%A9%94%EC%9D%B4%EC%A0%80%EB%A6%AC%EA%B7%B8%EB%A5%BC-%EC%95%84%EC%84%B8%EC%9A%94-1/

## etc

* 야구관련 데이터모델링기법들<br>
http://www.baseballdatascience.com/

* 야구 지표 해석<br>
  1) WAR 설명: http://www.yagongso.com/?p=963<br>
  2) MLB와 KBO의 기록차이: http://www.yagongso.com/?p=4405

* MLB 기록 사이트 정리<br>
https://bleacherreport.com/articles/630978-lies-damn-lies-and-statistics-top-baseball-sites-for-the-stats-lover
  1) http://www.retrosheet.org/
  2) http://www.seanlahman.com/baseball-archive/statistics/
  3) https://www.baseball-reference.com/

* MLB 스카우팅 데이터<br>
  1) https://www.baseballamerica.com/statistics/
  2) https://www.sports-reference.com/blog/2018/06/2018-mlb-draft-tools/
  3) https://legacy.baseballprospectus.com/sortable/index.php?cid=1920408

* MLB 스카우팅 리포트<br>
https://collection.baseballhall.org/PASTIME/scouting-reports?f%5B0%5D=mods_originInfo_dateCreated_dt%3A%5B2010-01-01T00%3A00%3A00Z%20TO%202019-01-01T00%3A00%3A00Z%5D

* NFL Draft project<br>
https://seanjtaylor.github.io/learning-the-draft/


### 타자 기록 지표 선정 (UEQR)
* **선정이유**<br>
    UEQR 혹은 Eqa 는 타자 지표중 안타 이외에도 볼넷, 장타 등의 보정이 포함된 지표임.<br>
    이러한 factor들로 인해 타율과 비슷하여 타율 보정 지표라고도 불림.<br>
    현재 KBO 리그 에서도 대표적으로 쓰이는 지표이며, 상대값에 대한 보정이<br>
    KBO 리그 특징중에 하나인 상대성을 보정하여 시즌별 값의 신빙성이 높음 <br>

    고교 타자의 지표의 경우 3학년 총 타석수가 기록되어 상대적 보정이 필요함 <br>
    이로인해 시즌별 타격이 보정된 지표인 <br>
    UEQR 이 적합. <br>

    References <br>
    http://kini.kr/230 <br>
    https://xe.rigvedawiki.net/w/%EC%95%BC%EA%B5%AC%EC%9D%98%20%EA%B8%B0%EB%A1%9D%20%EA%B3%84%EC%82%B0%EB%B2%95 <br>
    http://birdsnest.tistory.com/73 <br>


### 타자 기록 지표 선정 변경 (UEQR -> wOBA) 09.Aug.2018 Update
* **변경이유**<br>
    현재 고교야구의 데이터 상으로 UEQR 공식의 변수가 부족한 상황.<br>
    UEQR이 KBO 지표에 가장 통용되는 변수이기는 하나, <br>
    현재 보유한 데이터 로는 고교야구의 UEQR을 구할수 없음.<br>

    따라서 현상황에 고려한 지표 변경이 필요.<br>
    지표 wOBA로 변경. <br>

    지표 변경으로 인한 개선 사항으로 WAR을 이용한 타자 투수 지표 일체화 결정.<br>
   
   ** WAR 참고 ** <br>
   https://namu.wiki/w/WAR <br>
   https://www.reddit.com/r/baseball/comments/3tdpvf/is_it_fair_to_compare_a_pitchers_war_vs_a/ <br>
   https://www.fangraphs.com/blogs/a-discussion-about-improving-war/ <br>



### 투수 기록 지표 선정 (cFIP)
 * **선정이유**<br>
  
   대형신인의 경우 즉시 전력으로 1군 데뷔가 가능하지만<br>
   현재 투수 드래프트 시장의 경우, 구단 내 육성후 데뷔 의 경우가 대다수.<br>
  
   타자의 경우 현재 이정후, 강백호 등 1-2년차 신인의 주전의 경우가 있음<br>

   투수 드래프트의 경우 향후 발전 가능성 및 장기적 계획의 경우가 높음<br>

   cFIP 의 경우 FIP 와 동일 하지만 구장, 상대 타자의 성적,<br>
   포수의 능력 등의 다양한 변수가 보정되어 경기수가 적은<br>
   드래프트 선수들의 경우에 적합함.<br>


   따라서 현재 기준 예측성 (FIP) 가 아닌, 장기적 예측이 가능한<br>
   **cFIP** 지표가 타당<br>

   References<br>

   KBO 신인 투수 상황<br>
   http://www.sportsseoul.com/news/read/652127
   MLB 드래프트 신인 상황<br>
   http://www.mbcsportsplus.com/news/?mode=view&cate=2&b_idx=99939077.000
   KBO 투수 연봉 영향 요인<br>
   http://dx.doi.org/10.7465/jkdi.2017.28.2.317
   cFIP 와 FIP 의 비교<br>
   https://www.fangraphs.com/tht/fip-in-context/

### 투수 기록 지표 선정 변겅 (cFIP -> FIP) 09.Aug.2018 Update
 * **변경이유**<br>
   cFIP의 경우 FIP 에서 context 가 추가된 상황, 하지만 현재 <br>
   고교야구의 경우 각 구장별 상황, 상대 타자의 지표 등 cFIP에 필요한<br> 
   다양한 환경 Variable 들의 기록이 부재한 상황<br>

   따라서, FIP로 지표 변경.<br>

   이로 인한 해결책으로 WAR의 중요성을 높여 투수와 타자 지표를 <br>
   일체화 시켜 비교 하는 것으로 결정. <br> 

## Regression source
https://www.geeksforgeeks.org/linear-regression-python-implementation/ <br>
https://towardsdatascience.com/simple-and-multiple-linear-regression-in-python-c928425168f9 <br>

## Assumptions
 * **가정 항목** <br>
   **선수**<br>
   드래프트의 경우 고교 신인, 대학 신인, 해외 드래프트 신청 선수로 이루어 지나, <br>
   현재 데이터의 경우, 대학 리그 선수의 데이터가 없음. <br>
   따라서 TOP30 의 선수는 고교 졸업 선수 한정으로 제한 한다.<br>
   <br>
   **드래프트**<br>
   드래프트 방식의 경우, 각 구단이 전년도 성적순으로 지명을 하며, <br>
   1차 연고지 지명 후, 2차 라운드 지명으로 이어서 진행한다. <br>
   2017년 드래프트 부터, 기존의 스네이크 방식(혹은 ㄹ자 방식)이 아닌 <br>
   모든 라운드를 전 시즌 순위의 역순으로 지명하는 Z형 방식으로 변경되었다. <br>
   현재 보유한 데이터는, 각 구단의 포지션 선호도, 투타 선호도를 나타낼수 없다. <br>
   따라서 실제 2018 드래프트의 자료를 비교하여 계산된 WAR에 대입한 결과로 대채한다. <br>
   <br>
   **WAR**<br>
   WAR의 경우 fWAR (fangraph WAR)를 기준으로 하며 타자는 Statiz 를 기준으로 하여 각 WAR을 통합하여 비교한다. <br>
   허나 실제 WAR의 값의 경우, 투수의 이닝 으로 인해 타자의 WAR이 상대적으로 투수에 비해 높다<br>
   또한 타자의 경우 포지션별 보정또한 존재 하며 투수 또한 상대타자, 수비보정이 존재 한다.<br>
   허나, 현재 데이터 상으로 보정이 불가능 하며, 파크 팩터의 경우또한 KBO의 경우, <br> 
   잠실 구장을 제외한 나머지 구장은 크게 관여 하지 않아 대부분 1로 대체한다. <br>
   또한 고교 야구의 경우, 파크 팩터의 간섭의 더욱 적어 위와 같이 1로 대체한다. <br>
   *관련 자료* <br> 
   http://old.statiz.co.kr/glossary.php?opt=1&sopt=2<br>
   https://frhyme.github.io/baseball/baseball-parkfactor/<br>
   <br>

## 리포트 섹션
 * **비교 방법**<br>
   1) For matching 이용<br>
     For 문을 이용하여 실제 데이터(드래프트 결과)의 이름, 구해진 데이터(Project 결과)의 이름을 매칭<br>
     카운트 후 퍼센트로 전개<br>
     Accuracy 측정 가능, 그후, 기준 지표비교 가능<br>
     ex)fWAR 혹은 wOBA 와 같이 비교가능.<br>
   2) Boolean 값 매칭 graph
     각각의 데이터 매칭후 True or False 혹은 0 or 1 으로 <br>
     나타내어 visualise 함.<br>
     **update 필요**<br>
     파이 그래프 매칭 그래프화 후 % 계산<br>
     ![graph](https://user-images.githubusercontent.com/37870412/44184786-33476d80-a143-11e8-8595-fcdbcd18e220.JPG)
   3) 매칭 그래프
     각각의 데이터 매칭후 매칭 구분 <br>
     ex) 완벽일치<br>
         불일치 (순서 불일치, 실제 데이터 없음)
     따라서 총 3개의 데이터 구분 생성.<br>
     조금더 구체적인 비교 가능.<br>
     ![Graph Example][graph2.jpg]













  


