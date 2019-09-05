import textwrap

def wrap(string, max_width):
    w = textwrap.TextWrapper(width=max_width)
    result = w.wrap(text = string)
    ans = ""
    for i in result:
        ans += i+'\n'
    return ans

if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)
