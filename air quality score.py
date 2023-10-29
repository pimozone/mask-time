#기상 api로부터 받은 온도값 = nowTemp
#기상 api로부터 받은 습도값 = nowHumd
#기상 api로부터 받은 PM-10값 = nowFP (FP = fine particle)
#기상 api로부터 받은 PM-2.5값 = nowUFP (UFP = ultra fine particle)
#기상 api로부터 받은 24시간 PM-10값 = dayFP

########
#api로부터 호출
nowFP = 70 #70은 테스트 용도의 임시값. 실제로는 api로부터 받은 nowFP값임.
########


status = 0 #마스크 전망. 0=default 1=좋음 2=보통 3=나쁨 4=매우나쁨 5=최악

def Tscore(x): #Tscore=시간을 기준으로 한 점수
    x=int(x)
    return (25/16)*x*x

def Pscore(x): #Pscore=입자 농도를 기준으로 한 점수
    x=int(x)
    return x*(1/20)


time = input('착용 시간 입력: ')
Tscore100 = float(Tscore(time))
Pscore100 = float(Pscore(nowFP))
Fscore100 = float(Tscore100 + Pscore100)


if Fscore100 <= 20:
    status = 1

elif Fscore100 <= 40:
    status = 2

elif Fscore100 <= 60:
    status = 3

elif Fscore100 <= 80:
    status = 4

elif Fscore100 > 80:
    status = 5

print(status)
