level = 1
day = 1

daily_mission = ['먹이주기', '배설물치우기', '샤워시키기']
growth_level = ['알', '영유아', '어린이', '청소년', '성인']
growth_mission = ['잠재우기', '쓰다듬기', '놀아주기', '학교 보내기']

daily_mission_status = [False, False, False]
growth_daily_status = False
growth_mission_status = False

def print_current_status():
    '''
    현재 성장 단계 이미지를 출력하는 함수
    '''

    if level == 1:
        print("        ⬛⬛⬛⬛")
        print("     ⬛⬜⬜⬜⬜⬛")
        print("    ⬛⬜⬜⬜⬜⬜⬛")
        print("    ⬛⬜⬜⬜⬜⬜⬛")
        print("      ⬛⬛⬛⬛⬛")
    
    elif level == 2:
        print("        ⬛⬛⬛⬛⬛")
        print("     ⬛⬜⬜⬜⬜⬜⬛")
        print("    ⬛⬜⬜⬜⬜⬜⬜⬛")
        print("    ⬛⬜⬛⬜⬜⬛⬜⬛")
        print("    ⬛⬜⬜⬜⬜⬜⬜⬛")
        print("       ⬛⬛⬛⬛⬛⬛")
    
    elif level == 3:
        print("        ⬛⬛⬛⬛⬛")
        print("     ⬛⬜⬜⬜⬜⬜⬛")
        print("    ⬛⬜⬜⬜⬜⬜⬜⬛")
        print("    ⬛⬜⬛⬜⬜⬛⬜⬛")
        print("    ⬛⬜⬜⬜⬜⬜⬜⬛")
        print("       ⬛⬛⬛⬛⬛⬛")
        print("          ⬛     ⬛")
    
    elif level == 4:
        print("              ⬛   ")
        print("           ⬛⬛⬛⬛⬛")
        print("        ⬛⬜⬛⬜⬜⬜⬛")
        print("       ⬛⬜⬜⬜⬜⬜⬜⬛")
        print("    ⬛⬛⬜⬛⬜⬜⬛⬜⬛⬛")
        print("       ⬛⬜⬜⬜⬜⬜⬜⬛")
        print("          ⬛⬛⬛⬛⬛⬛")
        print("             ⬛     ⬛")
        print("             ⬛     ⬛")
    
    elif level == 5:
        print("              ⬛   ⬛")
        print("           ⬛⬛⬛⬛⬛")
        print("        ⬛⬜⬛⬛⬛⬜⬛")
        print("       ⬛⬜⬜⬜⬜⬜⬜⬛")
        print("    ⬛⬛⬜⬛⬜⬜⬛⬜⬛⬛")
        print("       ⬛⬜⬜⬜⬜⬜⬜⬛")
        print("       ⬛⬜⬜⬜⬜⬜⬜⬛")
        print("          ⬛⬛⬛⬛⬛⬛")
        print("             ⬛     ⬛")
        print("             ⬛     ⬛")
        print("             ⬛     ⬛")
        print("          ⬛⬛   ⬛⬛")

    else:
        print('ERROR: 잘못된 성장 단계입니다.')

def is_daily_complete():
    '''
    세 가지 데일리 미션을 모두 수행하였는지 여부를 확인하는 함수
    '''
    return daily_mission_status[0] and daily_mission_status[1] and daily_mission_status[2]

def is_growth_right():
    '''
    입력 받은 성장 미션이 현재 성장 단계에 알맞은 성장 미션인지 확인하는 함수
    '''

def next_growth_status():
    '''
    성장 단계를 다음 단계로 변경하는 함수
    '''

def display():
    '''
    게임 디스플레이
    '''
    print('========================================')
    print(f'[{level}일차] - 성장단계: {growth_level[level-1]}')
    print(f'오늘 진행된 데일리 미션: 먹이주기({'O' if daily_mission_status[0] else 'X'}), 배설물치우기({'O' if daily_mission_status[1] else 'X'}), 샤워시키기({'O' if daily_mission_status[2] else 'X'})')
    print_current_status()
    print(f'({growth_level[level-1]})단계 데일리 미션: {'O' if growth_daily_status else 'X'}')
    print(f'({growth_level[level-1]})단계 성장 미션: {'O' if growth_mission_status else 'X'}')
    print('========================================')

def logic():
    '''
    각 미션 입력 단계별 로직
    '''
    display()
    mission = input('미션 입력: ')

    if mission in daily_mission:
        if mission == daily_mission[0]:
            daily_mission_status[0] = True
        elif mission == daily_mission[1]:
            daily_mission_status[1] = True
        elif mission == daily_mission[2]:
            daily_mission_status[2] = True
        if is_daily_complete():
            print('========================================')
            print('다음날이 되었습니다!')
            day += 1
    
    elif mission in growth_mission:
        if is_growth_right():
            growth_mission_status = True
        else:
            print('ERROR: 성장 미션을 수행할 수 없습니다.')
    
    else:
        print('ERROR: 잘못된 미션입니다.')