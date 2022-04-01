def alarm_clock(day, vacation):
    if(day >= 1 and day <= 5):
        if(vacation == False):
            return "7:00"
        else: return "10:00"
    elif(day == 0 or day == 6):
        if(vacation == False):
            return "10:00"
        else: return "off"