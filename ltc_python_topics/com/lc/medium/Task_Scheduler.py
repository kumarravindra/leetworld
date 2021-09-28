"""
https://leetcode.com/problems/task-scheduler/
https://www.youtube.com/watch?v=Z2Plc8o1ld4&ab_channel=SaiAnishMalla
"""

def find_task_schedular(tasks, n):
    freq = {}

    for task in tasks:
        if task not in freq:
            freq[task] = 1
        else:
            freq[task] += 1
    freq = [value for key, value in freq.items()]
    max_freq = max(freq)
    max_freq_tasks = freq.count(max_freq)
    """ in case n = 0 then return whatever is max length or formula value"""
    return max(len(tasks), (max_freq - 1) * (n + 1) + max_freq_tasks)

tsk = ["A","A","A","B","B","B"]
num = 2
print(find_task_schedular(tsk, num))