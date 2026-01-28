# Job Sequencing with Deadlines (Greedy)
t = int(input())  # number of test cases
for _ in range(t):
    n = int(input())  # number of jobs
    jobs = []
    max_deadline = 0
    for _ in range(n):
        d, p = map(int, input().split())
        jobs.append((d, p))
        max_deadline = max(max_deadline, d)
    # Sort jobs by profit (descending)
    jobs.sort(key=lambda x: x[1], reverse=True)
    # Track slots (0 means free)
    slots = [0] * (max_deadline + 1)
    jobs_done = 0
    total_profit = 0
    for d, p in jobs:
        # Find a free slot before or at deadline
        for j in range(d, 0, -1):
            if slots[j] == 0:
                slots[j] = 1
                jobs_done += 1
                total_profit += p
                break
    print(jobs_done, total_profit)