#테스트를 위한 별 의미없는 주석이다. 
import openpyxl
import turtle
ex = openpyxl.load_workbook('Susi_2014.xlsx')
data = ex.active

checklist = []
costlist = []
for aline in data.rows:
    name = aline[0].value
    card = aline[1].value
    check = aline[2].value
    year = aline[3].value
    time = aline[4].value
    cost = aline[7].value


#각 카드사 별로 묶어보기
def makeDict() :
    check_cost_dict = {}
    cardlist = []
    costlist_Sin= []
    costlist_B = []
    costlist_W= []
    costlist_K=[]
    costlist_Sam = []
    costlist_N = []
    costlist_H = []
    costlist_L = []
    
    for aline in data.rows:
        
        name = aline[0].value
        card = aline[1].value
        check = aline[2].value
        year = aline[3].value
        time = aline[4].value
        cost = aline[7].value

        if '신한' in card :
            costlist_Sin.append(cost)
        elif '비씨' in card:
            costlist_B.append(cost)
        elif '외환' in card:
            costlist_W.append(cost)
        elif '국민' in card:
            costlist_K.append(cost)
        elif '삼성' in card:
            costlist_Sam.append(cost)
        elif '농협' in card:
            costlist_N.append(cost)
        elif '현대' in card:
            costlist_H.append(cost)
        elif '롯데' in card:
            costlist_L.append(cost)
    costlist = [costlist_Sin,costlist_B,costlist_W,costlist_K,costlist_Sam]
    
    check_cost_dict['신한카드']=costlist_Sin
    check_cost_dict['비씨카드']=costlist_B
    check_cost_dict['외환카드']=costlist_W
    check_cost_dict['국민카드']=costlist_K
    check_cost_dict['삼성카드']=costlist_Sam
    check_cost_dict['농협카드']=costlist_N
    check_cost_dict['현대카드']=costlist_H
    check_cost_dict['롯데카드']=costlist_L
    
    return check_cost_dict


def mode(alist):
    countdict= {}
    for item in alist:
        if item in countdict:
            countdict[item] += 1
        else:
            countdict[item] = 1

    itemlist = list(countdict.keys())
    itemlist.sort()
    cost = 20000
    summing = 0
    total = 0
    maxsum = 0
    for i in itemlist:
        
        if  i <= cost:
            
            summing += countdict[i]
            total += countdict[i]  #18~20만원대가 1개 있고 그다음이 20만원 이상이면 else를 안거치고 바로 빠짐

        elif cost == 200000:   #다음과 같이 보안
            print(cost - 20000 ,'원 초과',cost,'원 이하의 거래수',summing)
            cost += 0.1
            summing = countdict[i]
            total += countdict[i]
            maxsum = countdict[i]
            continue;
            
        elif cost > 200000:
            summing += countdict[i]
            total += countdict[i]
            maxsum += countdict[i]

        elif (i - cost)>20000:
            bcost = cost -20000
            print(bcost ,'원 초과',cost,'원 이하의 거래수',0 )
            cost += 20000
            summing +=countdict[i]
            total += countdict[i]

            continue;


        else :
            print(cost - 20000 ,'원 초과',cost,'원 이하의 거래수',summing)
            cost += 20000
            summing = countdict[i]
            total += countdict[i]
            continue;
    print('20만원 초과 거래수:', maxsum)
           
    print('총 거래수:',total)



#####################
cardlist = ['신한카드','비씨카드','외환카드','국민카드','삼성카드','농협카드','현대카드','롯데카드']
data = makeDict()
for i in cardlist:
    print('-'*20)
    print(i)
    mode(data[i])
