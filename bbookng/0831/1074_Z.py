N, r, c = map(int, input().split())

result = 0
while N > 0:
    N -= 1                              # 반씩 나눈걸 기준으로 계산할거기 때문에
    if r // (2 ** N):                   # 몫이 1이면 기준보다 밑에 이므로
        result += (2 ** N) ** 2 * 2     # 위에 행 만큼 다 더해줍니다

    if c // (2 ** N):                   # 위에서 행 기준 나누고 열 기준으로
        result += (2 ** N) ** 2         # 몫이 1이면 가운데 기준으로 오른쪽. 그래서 왼쪽만큼 더해줌

    r = r % (2 ** N)                    # 점점 더 잘게 쪼개서 들어가기
    c = c % (2 ** N)

print(result)