# AI 활용 자유 주제 파이썬 미니 프로젝트
# 이름 또는 학번: 20201 강수인
# 프로젝트 주제: 신제품 바이럴 효과 및 마케팅 점수 계산기
#
# 1. 데이터 준비: 2차원 리스트
# [채널명, 조회수, 좋아요수]
campaign = [
    ["SNS홍보", 5000, 250],
    ["블로그리뷰", 3000, 150],
    ["유튜브숏폼", 12000, 1200]
]

# 2. 함수 정의

def show_intro():
    """프로그램 제목과 안내를 출력한다."""
    print("=" * 40)
    print("★ 신제품 바이럴 효과 및 마케팅 점수 계산기 ★")
    print("=" * 40)


def get_user_input():
    """사용자에게 신제품 이름과 분석할 채널 번호를 입력받는다."""
    product_name = input("가상의 신제품 이름을 입력하세요: ")
    print("\n[분석할 홍보 채널 선택]")
    print("1. SNS홍보")
    print("2. 블로그리뷰")
    print("3. 유튜브숏폼")
    
    # 사용자에게 채널 번호를 정수로 입력받습니다.
    channel_num = int(input("확인하고 싶은 채널 번호를 입력하세요 (1~3): "))
    return product_name, channel_num


def calculate_and_evaluate(data, channel_num):
    """선택한 채널의 데이터를 분석하여 참여율과 등급을 계산한다."""
    # 리스트의 인덱스는 0부터 시작하므로 입력받은 번호에서 1을 뺍니다.
    idx = channel_num - 1 
    
    # 2차원 리스트에서 사용자가 선택한 행의 데이터를 가져옵니다.
    selected_channel = data[idx]
    
    channel_name = selected_channel[0]  # 채널명
    views = selected_channel[1]         # 조회수
    likes = selected_channel[2]         # 좋아요수

    # [스스로 채우기 ①] 참여율 계산 공식: (좋아요수 / 조회수) * 100
    # 아래 빈칸을 올바른 변수명으로 채워보세요!
    engagement_rate = (likes / views) * 100

    # [스스로 채우기 ②] 참여율에 따른 등급 판정 (조건문)
    # 8% 이상: 대박 / 4% 이상: 보통 / 그 외: 노력 필요
    if engagement_rate >= 8:
        grade = "대박 (성공적인 바이럴!)"
    elif engagement_rate >= 4:
        grade = "보통 (안정적인 유지)"
    else:
        grade = "노력 필요 (콘텐츠 개선 필요)"

    return channel_name, views, likes, engagement_rate, grade


def print_result(product, channel, views, likes, rate, grade):
    """최종 마케팅 분석 결과를 화면에 출력한다."""
    print("\n" + "=" * 40)
    print(f"[ 마케팅 분석 결과 보고서 ]")
    print("-" * 40)
    print(f"- 분석 제품명: {product}")
    print(f"- 선택 채널: {channel}")
    print(f"- 누적 조회수: {views}회")
    print(f"- 누적 좋아요수: {likes}개")
    # :.2f는 소수점 둘째 자리까지 출력하라는 뜻입니다.
    print(f"- 계산된 참여율: {rate:.2f}%") 
    print(f"- 최종 성과 등급: {grade}")
    print("=" * 40)


def main():
    # 1. 안내 문구 출력
    show_intro()
    
    # 2. 사용자 입력 받기
    product_name, channel_num = get_user_input()
    
    # 3. 데이터 분석 및 등급 계산
    channel_name, views, likes, rate, grade = calculate_and_evaluate(campaign, channel_num)
    
    # 4. 결과 출력하기
    print_result(product_name, channel_name, views, likes, rate, grade)


# 3. 프로그램 실행
main()