n = int(input())

for i in range(n):
    m_count = {}
    x = int(input())

    for j in range(x):
        event = input().split(',')
        team_name = ','.join(event[1:-3])
        if event[3] not in m_count:
            m_count[event[3]] = [0, 0]
        if event[2].title() == "Day" and event[-1].lower() == "true":
            m_count[event[3]][0] += 1
        elif event[2].title() == "Night" and event[-1].lower() == "true":
            m_count[event[3]][1] += 1
    for k in sorted(m_count.keys()):
        ans = ""
        ans+=k+","
        for i in range(len(m_count[k])):
            if i == len(m_count[k])-1:
                ans+=str(m_count[k][i])
            else:
                ans+=str(m_count[k][i])+","
        print(ans)