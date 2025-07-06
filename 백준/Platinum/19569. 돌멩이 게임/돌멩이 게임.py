import sys

# ----- 보조 함수 -----

def step_mod(k: int) -> int:

    """k(=직전에 상대가 가져간 개수)가 주어졌을 때

    '패배 위치'가 되는 간격 M(k) 를 계산한다."""

    if k == 1:          # k == 1 은 따로 처리하므로 의미 없음

        return 5

    m, upper = 5, 3     # 첫 구간: k ∈ [2,3], M = 5

    while k > upper:    # 구간을 넘어가면 M 과 upper 를 두 배씩 늘린다

        m *= 2

        upper += m // 2

    return m            # k 가 속한 구간의 간격

def choose_move(n: int, k: int) -> int:

    """현재 남은 돌 n, 직전에 상대가 가져간 수 k 가 주어질 때

    승리를 보장하는 우리 측 한 수를 돌려준다."""

    limit = min(n, k + 1)          # 이번에 가져갈 수 있는 최대치

    if k == 1:                     # 특수 : 남은 돌 ≡ 0 or 3 (mod 5) 로 만든다

        for t in range(1, limit + 1):

            r = (n - t) % 5

            if r == 0 or r == 3:

                return t

    else:

        mod = step_mod(k)          # 일반 : 남은 돌을 mod 의 배수로 만든다

        for t in range(1, limit + 1):

            if (n - t) % mod == 0:

                return t

    return 1                       # 이론상 도달하지 않음 (안전장치)

# ----- 메인 -----

def main() -> None:

    input = sys.stdin.readline

    N = int(input().strip())

    # 1) 처음 판단

    if N % 5 not in (1, 4):        # 이길 수 없는 경우

        print("NO")

        sys.stdout.flush()

        return

    # 2) 이길 수 있는 경우 – 게임 진행

    print("YES")

    sys.stdout.flush()

    remain = N

    first = 1                      # 규칙상 첫 수는 무조건 1

    print(first)

    sys.stdout.flush()

    remain -= first

    prev = first                   # 직전에 가져간 돌 개수

    if remain == 0:                # 이미 끝난 경우( N == 1 은 없지만 안전)

        return

    while True:

        # 3) muse 의 수 입력

        line = input()

        if not line:               # 입력이 없으면 채점 종료

            return

        muse = int(line.strip())

        remain -= muse

        prev = muse

        if remain == 0:            # 우리가 졌다

            return

        # 4) 우리의 다음 수 계산 후 출력

        me = choose_move(remain, prev)

        print(me)

        sys.stdout.flush()

        remain -= me

        prev = me

        if remain == 0:            # 마지막 돌을 가져가서 승리

            return

if __name__ == "__main__":

    main()