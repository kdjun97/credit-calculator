## 학점 계산기 Ver 1.0.0
## Made By 김동준
## 2021-07-03 수정

# 학기 평점 계산기
def sem_cal(name,input):
  this_sem_total=0.0 # 이번학기 총 들은 학점
  this_sem=0.0 # 실적용 이번학기 총 들은 학점 (P/F 제외)
  my_score=0.0
  major=0.0
  major_total=0.0
  major_pf_total=0.0
  no_major=0.0
  no_major_total=0.0
  no_major_pf_total=0.0
  temp=0.0

  for i in range(len(input)):
    temp = switch(input[i][2])
    if (not temp == -1): # F 아니면
      this_sem_total += input[i][3]
      
      if (input[i][1] == '교양'): no_major_pf_total += input[i][3]
      else: major_pf_total += input[i][3]

      if (not temp == 0): # P나 PD가 아니면
        this_sem += input[i][3]
        my_score += (temp * input[i][3])
        if (input[i][1] == '교양'):
          no_major_total += input[i][3]
          no_major += (temp * input[i][3])
        else:
          major_total += input[i][3]
          major += (temp * input[i][3])
  
  print('******************************************************************')
  print('{}학기 전공학점은 {}점(P/F 제외) {}점(P/F 포함) 들으셨습니다.'.format(name, major_total,major_pf_total))
  print('{}학기 교양학점은 {}점(P/F 제외) {}점(P/F 포함) 들으셨습니다.'.format(name, no_major_total,no_major_pf_total))
  print('{}학기 pf학점 :{}'.format(name,(major_pf_total-major_total)+(no_major_pf_total-no_major_total)))

  print('{}학기 들은학점 :{}'.format(name,this_sem_total))
  
  try: 
    print('{}학기 전공평점 :{}'.format(name,major/major_total))
  except: 
    ZeroDivisionError: print('{}학기 전공평점 :{}'.format(name,0.0))
  try: 
    print('{}학기 교양평점 :{}'.format(name,no_major/no_major_total))
  except: 
    ZeroDivisionError: print('{}학기 교양평점 :{}'.format(name,0.0))
  try:
    print('{}학기 총평점   :{}'.format(name,my_score/this_sem))
  except ZeroDivisionError:
    print('{}학기 총평점   :{}'.format(name,0.0))
  print('******************************************************************')

def switch(temp):
  return {'A+': 4.5, 'A0': 4.0, 'B+': 3.5, 'B0': 3.0, 'C+': 2.5, 'C0': 2.0, 'D+': 1.5, 'D0': 1.0, 'P': 0, 'PD':0}.get(temp, -1)

# '과목명', '이수구분', '성적', '학점'
sem_19_summer = [('사회봉사1','교양','P',1)]
sem_20_summer = [('소프트웨어 입문','교양','A0',2)]
sem_21_1 = [('기초전자공학실험', '전공','P',3), ('모바일 앱 개발','전공','A+',3), ('데이타베이스','전공','A0',3), ('하이브리드 웹 설계','교양','A+',2), ('모두를 위한 인공지능의 활용','교양','A+',3), ('신앙특론', '교양', 'P', 3)]
sem_21_summer =[('현장실습(전산전자)', '전공', 'P', 3), ('시스템 개발 실무특론', '교양','P',2)]

sem_total=[]
#sem_total = sem_16_1 + sem_16_2 + sem_19_1 + sem_19_summer + sem_19_2 + sem_20_1 + sem_20_summer + sem_20_2 + sem_21_1 + sem_21_summer
sem_total = sem_19_summer + sem_20_summer + sem_21_1 + sem_21_summer

sem_cal("21-1", sem_21_1)
sem_cal("총", sem_total)