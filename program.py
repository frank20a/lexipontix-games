while True:
    cmd = ''

    while not cmd.isdigit() or 6 < int(cmd) < 1:
        cmd = input('1)Ko-03\n2)Ko-05\n3)Ki-01\n4)Ko-11\n5)Ko-12\n6)Ko-02\n')
    cmd = int(cmd)

    if cmd == 1:
        import ko03
    elif cmd == 2:
        import ko05
    elif cmd == 3:
        import ki01
    elif cmd == 4:
        import ko11
    elif cmd == 5:
        import ko12
    elif cmd == 6:
        import ko02