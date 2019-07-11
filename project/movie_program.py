class theater:
    def __init__(self, name, time1, time2, time3, time4, money, allseat): # 각 상영관에서 상영하는 영화의 이름, 시간, 수익을 저장
        self.name = name
        self.time = [time1, time2, time3, time4]
        self.money = money
        self.allseat = allseat

    def earnmoney(self, profit): # 이익 계산
        self.money += profit

class Seat:
    def __init__(self, seat): # 각 영화마다 좌석을 입력받음
        self.seat = seat

    def showseat(self): # 현재 좌석 예매 상황을 알려줌
        for i in range(5):
            for j in range(5):
                if self.seat[i][j] == 0: # 좌석이 비어있으면
                    if(i == 0):
                        if(j == 4):
                            print("A" + str(5))
                        else:
                            print("A" + str(j + 1), end = " ")
                    if(i == 1):
                        if (j == 4):
                            print("B" + str(5))
                        else:
                            print("B" + str(j + 1), end = " ")
                    if(i == 2):
                        if (j == 4):
                            print("C" + str(5))
                        else:
                            print("C" + str(j + 1), end = " ")
                    if(i == 3):
                        if (j == 4):
                            print("D" + str(5))
                        else:
                            print("D" + str(j + 1), end = " ")
                    if(i == 4):
                        if (j == 4):
                            print("E" + str(5))
                        else:
                            print("E" + str(j + 1), end = " ")
                else: # 좌석이 비어있지 않다면
                    if (j == 4):
                        print("XX")
                    else:
                        print("XX", end = " ")
        print("")

movie_price = [-3000, -1000, 8000] # 영화표 가격 어린이(어른-3000), 청소년(어른-1000), 어른

movie1_time1 = Seat([[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]])
movie1_time2 = Seat([[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]])
movie1_time3 = Seat([[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]])
movie1_time4 = Seat([[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]])
all_time1 = [movie1_time1, movie1_time2, movie1_time3, movie1_time4]
movie1 = theater("1편", "09:00", "11:00", "13:00", "15:00", 0, all_time1)

movie2_time1 = Seat([[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]])
movie2_time2 = Seat([[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]])
movie2_time3 = Seat([[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]])
movie2_time4 = Seat([[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]])
all_time2 = [movie2_time1, movie2_time2, movie2_time3, movie2_time4]
movie2 = theater("2편", "10:00", "12:30", "15:00", "17:30", 0, all_time2)


movie3_time1 = Seat([[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]])
movie3_time2 = Seat([[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]])
movie3_time3 = Seat([[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]])
movie3_time4 = Seat([[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]])
all_time3 = [movie3_time1, movie3_time2, movie3_time3, movie3_time4]
movie3 = theater("3편", "08:00", "11:00", "14:00", "17:00", 0, all_time3)

all_movie = [movie1, movie2, movie3]

#--------------------------------영화 예매-----------------------------------------
def selectseat(movie_select, time_select, people_num): # 좌석 선택 함수
    print("선택하신 시간의 좌석 상황은 다음과 같습니다.\n영화 : {}\n상영 시간 : {}\n".format(all_movie[movie_select - 1].name, all_movie[movie_select - 1].time[time_select - 1]))
    all_movie[movie_select - 1].allseat[time_select - 1].showseat()
    for i in range(people_num):
        print("좌석을 선택해 주세요.\n1. A\n2. B\n3. C\n4. D\n5. E\n")
        try:
            seat1_select = int(input())
            if (seat1_select != 1 and seat1_select != 2 and seat1_select != 3 and seat1_select != 4 and seat1_select != 5):
                print("잘못 입력하셨습니다. 다시 입력해주세요.\n")
                selectseat(movie_select, time_select, people_num)
            else:
                print("좌석을 선택해 주세요.\n1. 1\n2. 2\n3. 3\n4. 4\n5. 5\n")
                try:
                    seat2_select = int(input())
                    if(seat2_select != 1 and seat2_select != 2 and seat2_select != 3 and seat2_select != 4 and seat2_select != 5):
                        print("잘못 입력하셨습니다. 처음부터 다시 입력해주세요.\n")
                        selectseat(movie_select, time_select, people_num)
                    else:
                        if(all_movie[movie_select-1].allseat[time_select-1].seat[seat1_select-1][seat2_select-1] == 1):
                            print("이미 예매된 좌석입니다. 다른 좌석을 선택해주세요.\n")
                            selectseat(movie_select, time_select, people_num)
                        else:
                            all_movie[movie_select-1].allseat[time_select-1].seat[seat1_select-1][seat2_select-1] = 1 # 선택한 좌석 구매
                            print("선택하신 시간의 좌석 상황은 다음과 같습니다.\n영화 : {}\n상영 시간 : {}\n".format(all_movie[movie_select - 1].name, all_movie[movie_select - 1].time[time_select - 1]))
                            all_movie[movie_select - 1].allseat[time_select - 1].showseat()
                            people_num -= 1
                except ValueError:
                    print("처음부터 다시 숫자만 입력해주세요\n")
                    selectseat(movie_select, time_select, people_num)
        except ValueError:
            print("숫자만 입력해주세요\n")
            selectseat(movie_select, time_select, people_num)

def youth(movie_select, people_num): # 청소년의 수 확인 함수
    try:
        print("청소년 수를 입력해 주세요")
        youth_num = int(input())
        if(youth_num > people_num):
            print("입력 인원이 어린이를 제외한 전체 인원보다 많습니다. 다시 입력해주세요\n")
            youth(movie_select, people_num)
        else:
            all_movie[movie_select - 1].earnmoney(youth_num * movie_price[1])  # 청소년 수만큼의 이익을 해당 영화에서 제외
    except ValueError:
        print("숫자만 입력해주세요\n")
        youth(movie_select, people_num)


def child(movie_select, people_num): # 어린이의 수 확인 함수
    try:
        print("어린이 수를 입력해 주세요")
        child_num = int(input())
        if(child_num > people_num):
            print("입력 인원이 전체 인원보다 많습니다. 다시 입력해주세요\n")
            child(movie_select, people_num)
        else:
            all_movie[movie_select - 1].earnmoney(child_num * movie_price[0])  # 어린이 수만큼의 이익을 해당 영화에서 제외
            people_num -= child_num
            if(people_num != 0):
                youth(movie_select, people_num)
    except ValueError:
        print("숫자만 입력해주세요\n")
        child(movie_select, people_num)


def people(movie_select, time_select): # 인원 확인 함수
    try:
        print("인원 수를 입력해 주세요")
        people_num = int(input())
    except ValueError:
        print("숫자만 입력해주세요\n")
        people(movie_select, time_select)

    all_movie[movie_select - 1].earnmoney(people_num * movie_price[2])  # 인원 수만큼의 이익을 해당 영화에 저장

    child(movie_select, people_num)

    selectseat(movie_select, time_select, people_num)



def viewseat(movie_select, time_select): # 좌석 현황 확인 함수
    print("선택하신 시간의 좌석 상황은 다음과 같습니다.\n영화 : {}\n상영 시간 : {}\n".format(all_movie[movie_select - 1].name, all_movie[movie_select - 1].time[time_select - 1]))
    all_movie[movie_select - 1].allseat[time_select - 1].showseat()

    people(movie_select, time_select)


def viewtime(movie_select): #상영 시간 선택 함수
    print("상영 시간을 선택해 주세요.\n1. {}\n2. {}\n3. {}\n4. {}\n".format(all_movie[movie_select - 1].time[0], all_movie[movie_select - 1].time[1], all_movie[movie_select - 1].time[2], all_movie[movie_select - 1].time[3],))
    try:
        time_select = int(input())
        if(time_select != 1 and time_select != 2 and time_select != 3 and time_select != 4):
            print("잘못 입력하셨습니다. 다시 입력해주세요\n")
            viewtime(movie_select)
        else:
            viewseat(movie_select, time_select)
    except ValueError:
        print("숫자만 입력해주세요\n")
        viewtime(movie_select)


def moviebuy(): #영화 선택 함수
    print("예매하실 영화를 선택해 주세요.\n1. {}\n2. {}\n3. {}\n".format(movie1.name, movie2.name, movie3.name))
    try:
        movie_select = int(input())

        if(movie_select != 1 and movie_select != 2 and movie_select != 3):
            print("잘못 입력하셨습니다. 다시 입력해주세요\n")
            moviebuy()
        else:
            viewtime(movie_select)
    except ValueError:
        print("숫자만 입력해주세요\n")
        moviebuy()

#------------------------------------상영 시간 확인----------------------------------------------

def movietime():
    print("상영 시간을 확인하고 싶은 영화를 선택해 주세요\n1. {}\n2. {}\n3. {}\n".format(movie1.name, movie2.name, movie3.name))
    try:
        movietime_select = int(input())
        if(movietime_select != 1 and movietime_select != 2 and movietime_select != 3):
            print("잘못 입력하셨습니다. 다시 입력해주세요\n")
            movietime()
        else:
            print("선택하신 영화의 상영 시간은 다음과 같습니다.\n영화 : {}\n상영 시간\n{}\n{}\n{}\n{}\n".format(all_movie[movietime_select-1].name, all_movie[movietime_select-1].time[0], all_movie[movietime_select-1].time[1], all_movie[movietime_select-1].time[2], all_movie[movietime_select-1].time[3]))
    except ValueError:
        print("숫자만 입력해주세요\n")
        movietime()

#---------------------------------------수입 확인 함수-----------------------------------------------------

def viewprofit():
    profit = all_movie[0].money + all_movie[1].money + all_movie[2].money #모든 영화의 수입을 더함
    print("현재 총 수입 : {}원\n".format(profit))

#------------------------------------메인 시스템 함수-------------------------------------------------------------------

def systemstart():
    while(True):
        print("원하는 기능을 선택해 주세요.\n1. 영화 예매\n2. 영화 상영 시간 확인\n3. 총 수입 확인\n4. 프로그램 종료\n") # 원하는 기능을 선택
        try:
            menu_select = int(input())

            if(menu_select == 1):
                moviebuy()
            elif(menu_select == 2):
                movietime()
            elif(menu_select == 3):
                viewprofit()
            elif(menu_select == 4):
                print("프로그램을 종료합니다.\n")
                exit()
            else:
                print("잘못 입력하셨습니다. 다시 입력해주세요\n")
                systemstart()
        except ValueError:
            print("숫자만 입력해주세요\n")
            systemstart()

#-----------------------------------------------------프로그램 시작---------------------------------------------------------

systemstart()