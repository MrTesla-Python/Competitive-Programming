import re
def sorted_1( l ): 
    convert = lambda text: int(text) if text.isdigit() else text 
    alphanum_key = lambda key: [ convert(c) for c in re.split('([0-9]+)', key) ] 
    return sorted(l, key = alphanum_key)
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
    counts = [str(i) for i in m_count.keys()]
    for k in sorted_1(counts):
        if m_count[k][0] == 0 and m_count[k][1] == 0:
          continue
        else:
          ans = ""
          ans+=k+","
          ans+=str(m_count[k][0])+","+str(m_count[k][1])
          print(ans)