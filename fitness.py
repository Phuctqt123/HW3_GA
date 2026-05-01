def fitness(chromosome):
    penalty = 0

    # =========================
    # 1. Pairwise constraints
    # =========================
    for i in range(len(chromosome)):
        for j in range(i + 1, len(chromosome)):
            a = chromosome[i]
            b = chromosome[j]

            same_time = (a["day"] == b["day"] and a["slot"] == b["slot"])

            # (6) room conflict
            if same_time and a["room"]["id"] == b["room"]["id"]:
                penalty += 20

            # (3) professor conflict
            if same_time and a["prof"] == b["prof"]:
                penalty += 20

            # (5) section conflict
            if same_time and a["section"] == b["section"]:
                penalty += 20

    # =========================
    # 2. Room size constraint
    # =========================
    for gene in chromosome:
        if gene["room"]["size"] == 0 and gene["course"]["size"] == 1:
            penalty += 30

    # =========================
    # 3. Course: 2 sessions / week
    # =========================
    from collections import defaultdict
    course_sessions = defaultdict(list)

    for gene in chromosome:
        course_sessions[gene["course"]["id"]].append(gene)

    for course_id, sessions in course_sessions.items():
        d1 = sessions[0]["day"]
        d2 = sessions[1]["day"]

        # (1) không cùng ngày
        if d1 == d2:
            penalty += 50

        # (1) không ngày liền kề
        if abs(d1 - d2) == 1:
            penalty += 30

    # =========================
    # 4. Professor: max 3 courses
    # =========================
    prof_courses = defaultdict(set)

    for gene in chromosome:
        prof_courses[gene["prof"]].add(gene["course"]["id"])

    for prof, courses in prof_courses.items():
        if len(courses) > 3:
            penalty += 40 * (len(courses) - 3)

    # =========================
    # 5. (4) available rooms
    # =========================
    # (đã đảm bảo vì luôn chọn từ list rooms → bỏ qua)

    return -penalty