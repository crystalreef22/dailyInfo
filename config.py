# calender studf
cdDay=int(input("?cday"))
#idk later
SCHEDULE=["🎻","💻","🧭","➗","📜","🧪","📝","🔲","📵"]
LATELUNCH=[1,1,1,0,1,0,0,2,1] # 1 is early lunch, 2 is two free at lunch, 0 is late lunch
# 🎻💻🧭📜late lunch

TODAYSCHEDOVERRIDE = None


PERIODS=[
        [0,1,2,3,4,5],
        [6,3,4,7,0,1],
        [5,5,0,2,6,3],
        [1,2,6,4,5,7],
        [3,4,5,0,1,2],
        [7,0,1,6,3,4],
        [2,6,3,5,5,0],
        [4,5,8,1,2,6]
        ]

nextDayTime = None
