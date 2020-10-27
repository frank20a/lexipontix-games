while True:
    cmd = ''

    while not cmd.isdigit() or 6 < int(cmd) < 1:
        cmd = input('1)Κο-02_Παιχνίδι_Βελάκι\n2)Κο-03_Ποντικός_Εναντίων_Κέντρου_Ελέγχου\n3)Κο-05_Σενάρια_'
                    'Ανησυχόμετρου\n4)Κι-01_ Συναγερμός_στη_Μηχανή_Λέξεων\n5)Κο-11_Αλλόκοτα_γυαλιά\n6)Κο-12_Βρες_τα_'
                    'Αλλοκοτα_Γυαλιά\n')
    cmd = int(cmd)

    if cmd == 1:
        import ko02
    elif cmd == 2:
        import ko03
    elif cmd == 3:
        import ko05
    elif cmd == 4:
        import ki01
    elif cmd == 5:
        import ko11
    elif cmd == 6:
        import ko12