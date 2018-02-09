def remove_tags(s):
    result = []
    start = s.find('>')
    end = s.find('<',start+1)
    while end<=len(s):
        result.append(s[start+1:end])
        start = s.find('>',end+1)
        end = s.find('<',start+1)
    return result


print(remove_tags('''<h1>Title</h1><p>This is a
                    <a href="http://www.udacity.com">link</a>.<p>'''))