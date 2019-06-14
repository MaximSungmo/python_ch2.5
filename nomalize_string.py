# 문자열 데이터를 분석 하기 전에 처리함수 만들기
# 1. 공백제거
# 2. 필요 없는 문자 부호 제거
# 3. 대소문자 정리(Capitalize)
import re

states = ['Alabama', ' Georgia!', 'Georgia ', 'georgia', 'FlOrIda', 'south carolina   ', 'West virginia?']

def clean_strings(strings):
    result  = []
    for s in strings:
        # 공백 제거
        s = s.strip()
        # 정규표현식 (해당하는 표현에 대하여 , 변환, 참조변수)
        s = re.sub('[!#?]', '', s)
        s = s.title()
        result.append(s)

    return result
result = clean_strings(states)
print(result)

# ----------------------------------------------------------------
states = ['Alabama', ' Georgia!', 'Georgia ', 'georgia', 'FlOrIda', 'south carolina   ', 'West virginia?']

def clean_strings(strings, *funcs):
    results = []
    for string in strings:
        for func in funcs:
            string = func(string)
        results.append(string)
    return results
# 일반적으로 스트링 처리해주는 함수는 다음과 같이 사용했었다.
# "abc   ".strip()
# 하지만 str.string("abc   ") 으로도 사용이 가능하다.
# 따라서 본 함수에서는 위와 같이 구현을 하였다.

def remove_special(string):
    return re.sub('[!#?]', '', string)

states = clean_strings(states, str.strip, str.title, remove_special)
print(states)

# 람다로 변경
# s라는 변수가 들어 올 것인데, s가 들어오면 : 이하 내용을 처리한다.
states = clean_strings(states, str.strip, str.title, (lambda s: re.sub('[!#?]', '', s)))
print(states)



