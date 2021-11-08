def swap_case(s):
    ns = []
    slist = s.split()
    for w in slist:
        st = ''
        for l in w:
            if l.isupper():
                st += l.lower()
            else:
                st += l.upper()
        ns.append(st)

    return (' '.join(ns))


