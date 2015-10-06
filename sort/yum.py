root_path = '/spider/dumps/sorted'

from lists.black import subdomains, black_tlds

symbols = [
    '.html', '.php', '@', 'xn--', '<', '>', '?', ' ',
]

all_domains = []
with open(root_path, 'r') as f:
    for line in f:
        all_domains.append(line.strip())

clean_domains = []
for domain in all_domains:
    b = True
    '''
    for symbol in symbols:
        if symbol in domain:
            b = False
            break
    for x in subdomains:
        if x in domain:
            b = False
            break
    '''
    for x in black_tlds:
        if domain[domain.__len__() - x.__len__():] == x:
            b = False
            break

    if b:
        clean_domains.append(domain)

print(clean_domains.__len__())
with open('/spider/dumps/yumyumyumyumyumyumyum.txt', 'w+') as f:
    for x in clean_domains:
        f.write('%s\n' % x)