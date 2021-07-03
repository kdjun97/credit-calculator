# University Credit Calculator

### 소개
[여기](https://kdjun97.github.io/blog/credit_calculator/)  

### 기능
본인의 전체 학점, 전공학점, 교양학점, pf학점, 총 평점을 알려준다.  
F학점에 대해서는 없다고 생각하고 짰다.(영향미치지 않는다고 가정함)  
~~일단 내가 학점에 영향을 미치는 F가 없어서 짤 필요가 없었음~~  

### Result
![result](/img/result.PNG)

### 사용법

```{.python}
sem_19_summer = [('사회봉사1','교양','P',1)]
sem_20_summer = [('소프트웨어 입문','교양','A0',2)]
sem_21_1 = [('기초전자공학실험', '전공','P',3)]
sem_21_summer =[('현장실습(전산전자)', '전공', 'P', 3), ('시스템 개발 실무특론', '교양','P',2)]

sem_total=[]
sem_total = sem_19_summer + sem_20_summer + sem_21_1 + sem_21_summer
```

위와 같이 본인의 학기에 들었던 과목을 list안에 tuple로 적어주면 된다.  
순서는 ('과목명','이수구분','성적','학점')이다.  

함수 호출은 `sem_cal('19-1',sem_19_1)` 이런식으로 불러주면 된다.  
전체 학기는 `sem_cal('총',sem_total)`로 불러주면 된다.  