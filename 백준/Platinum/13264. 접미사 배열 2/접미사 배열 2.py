def build_suffix_array(s):

    n = len(s)

    k = 1

    # 각 접미사에 대한 초기 랭크 설정: 아스키값 사용

    rank = [ord(c) for c in s] + [-1]  # rank[n]은 -1 (범위 밖 처리용)

    tmp = [0] * n

    sa = list(range(n))  # 접미사 시작 인덱스 리스트

    while True:

        # (현재 랭크, k칸 뒤 랭크)를 기준으로 정렬

        sa.sort(key=lambda x: (rank[x], rank[x + k] if x + k < n else -1))

        # 새 랭크 계산

        tmp[sa[0]] = 0

        for i in range(1, n):

            prev = sa[i - 1]

            curr = sa[i]

            prev_rank = (rank[prev], rank[prev + k] if prev + k < n else -1)

            curr_rank = (rank[curr], rank[curr + k] if curr + k < n else -1)

            if prev_rank == curr_rank:

                tmp[curr] = tmp[prev]

            else:

                tmp[curr] = tmp[prev] + 1

        # 새 랭크로 업데이트

        rank = tmp[:]

        # 모든 접미사가 고유한 순위를 가지면 종료

        if rank[sa[-1]] == n - 1:

            break

        # 비교 거리 2배 증가

        k *= 2

    return sa

# ✅ 입력 및 출력 처리

def main():

    import sys

    input = sys.stdin.readline

    S = input().strip()

    sa = build_suffix_array(S)

    for i in sa:

        print(i)

if __name__ == "__main__":

    main()