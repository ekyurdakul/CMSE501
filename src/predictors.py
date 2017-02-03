import numpy as np

#Same as last week
def pred1(attendance):
    ln = len(attendance)
    if ln == 0:
        return 0
    else:
        return attendance[ln-1]
#Same as two weeks ago
def pred2(attendance):
    ln = len(attendance)
    if ln >= 2:
        return attendance[ln-2]
    else:
        return 0
#Same as three weeks ago
def pred13(attendance):
    ln = len(attendance)
    if ln >= 3:
        return attendance[ln-3]
    else:
        return 0
#Same as four weeks ago
def pred14(attendance):
    ln = len(attendance)
    if ln >= 4:
        return attendance[ln-4]
    else:
        return 0
#Same as five weeks ago
def pred7(attendance):
    ln = len(attendance)
    if ln >= 5:
        return attendance[ln-5]
    else:
        return 0
#Same as six weeks ago
def pred15(attendance):
    ln = len(attendance)
    if ln >= 6:
        return attendance[ln-6]
    else:
        return 0
#Same as seven weeks ago
def pred16(attendance):
    ln = len(attendance)
    if ln >= 7:
        return attendance[ln-7]
    else:
        return 0
#Same as eight weeks ago
def pred17(attendance):
    ln = len(attendance)
    if ln >= 8:
        return attendance[ln-8]
    else:
        return 0
#Same as nine weeks ago
def pred18(attendance):
    ln = len(attendance)
    if ln >= 9:
        return attendance[ln-9]
    else:
        return 0
#Same as ten weeks ago
def pred19(attendance):
    ln = len(attendance)
    if ln >= 10:
        return attendance[ln-10]
    else:
        return 0
#Average of the last two weeks
def pred3(attendance):
    ln = len(attendance)
    if ln == 0:
        return 0
    elif ln == 1:
        return int(attendance[0]/2)
    else:
        return int((attendance[ln-1] + attendance[ln-2]) / 2)
#Constant value
def pred4(attendance):
    return 67
#Mirror image around 50 of last week's
def pred5(attendance):
    ln = len(attendance)
    if ln == 0:
        return 0
    else:
        return abs(attendance[ln-1]-50) + attendance[ln-1]
#Average of the last four weeks
def pred6(attendance):
    ln = len(attendance)
    if ln >= 4:
        return np.mean([attendance[ln-1],attendance[ln-2],attendance[ln-3],attendance[ln-4]])
    else:
        return 0
#Trend in the last 8 weeks
def pred8(attendance):
    ln = len(attendance)
    if ln >= 8:
        p = np.polyfit(range(8),attendance[-8:],1)
        pred = int(p[0]*8+p[1])
        if pred > 100:
            pred = 100
        elif pred < 0:
            pred = 0
        return pred
    else:
        return 0
#Same as the first week
def pred9(attendance):
    ln = len(attendance)
    if ln == 0:
        return 0
    else:
        return attendance[0]
#Average of the first two weeks
def pred10(attendance):
    ln = len(attendance)
    if ln == 0:
        return 0
    elif ln == 1:
        return int(attendance[0]/2)
    else:
        return int((attendance[0] + attendance[1]) / 2)
#Constant value
def pred11(attendance):
    return 59
#Trend in the last 2 weeks
def pred12(attendance):
    ln = len(attendance)
    if ln >= 2:
        p = np.polyfit(range(2),attendance[-2:],1)
        pred = int(p[0]*2+p[1])
        if pred > 100:
            pred = 100
        elif pred < 0:
            pred = 0
        return pred
    else:
        return 0
#Same as fifteen weeks ago
def pred20(attendance):
    ln = len(attendance)
    if ln >= 15:
        return attendance[ln-15]
    else:
        return 0
#Same as twenty weeks ago
def pred21(attendance):
    ln = len(attendance)
    if ln >= 20:
        return attendance[ln-20]
    else:
        return 0
#Same as twenty five weeks ago
def pred22(attendance):
    ln = len(attendance)
    if ln >= 25:
        return attendance[ln-25]
    else:
        return 0
#Same as fifty weeks ago
def pred23(attendance):
    ln = len(attendance)
    if ln >= 50:
        return attendance[ln-50]
    else:
        return 0
#Same as seventy five weeks ago
def pred24(attendance):
    ln = len(attendance)
    if ln >= 75:
        return attendance[ln-75]
    else:
        return 0
        
#Keep a list of all predictors
predictors = [pred1,pred2,pred3,pred4,pred5,pred6,pred7,pred8,pred9,pred10,pred11,pred12,pred13,pred14,pred15,pred16,pred17,pred18,pred19,pred20,pred21,pred22,pred23,pred24]