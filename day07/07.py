import sys
from collections import defaultdict
from copy import deepcopy
from pprint import pprint


class Task:
    def __init__(self, name, prerequisites=None, is_assigned=False):
        self.name = name
        self.time_remaining = self.time_required
        self.prerequisites = set(prerequisites) if prerequisites else set()
        self.is_assigned = is_assigned

    @property
    def time_required(self):
        return 60 + ord(self.name) - 64

    @property
    def is_done(self):
        return self.time_remaining <= 0

    def do_work(self):
        self.time_remaining -= 1
        
    def __str__(self):
        return f'<Task name={self.name}, t_req={self.time_required}, t_left={self.time_remaining}, done={self.is_done}, prereq={"".join(sorted(t.name for t in self.prerequisites))}>'
    
    def __repr__(self):
        return self.__str__()


INPUT = "input.txt" if len(sys.argv) == 1 else sys.argv[1]
print(f'Using input file "{INPUT}"')


parent_steps = {}
child_steps = {}

SECONDS = 60
WORKERS = 5

with open(INPUT) as f:
    # "Step C must be finished before step A can begin."

    for line in f:
        words = line.split() # ["Step", "C", ...]
        parent = words[1]
        child = words[-3]

        if child in parent_steps:
            parent_steps[child].append(parent)
        else: # KeyError
            parent_steps[child] = [parent]

        if parent in child_steps:
            child_steps[parent].append(child)
        else:
            child_steps[parent] = [child]

        if parent not in parent_steps:
            parent_steps[parent] = []

print('PARENT STEPS', parent_steps)
print("----------")
print('CHILD STEPS', child_steps)

# setup for pt 2
tasks_names = set(parent_steps.keys()).union(set(child_steps.keys()))
tasks = set(Task(name) for name in tasks_names)

for task in tasks:
    if task.name in parent_steps:
        task.prerequisites = [t for t in tasks if t.name in parent_steps[task.name]]

# pt 1
order = []

try:
    while True:
        for step in sorted(parent_steps.keys()):
            if not parent_steps[step]:
                order.append(step)
                del parent_steps[step]
                for child in child_steps[step]:
                    parent_steps[child].remove(step)
                del child_steps[step]
                break
except KeyError:
    pass

output = "".join(order)
print(output)


# pt.2

ts = 0

# pprint(tasks)

# dict { worker_number: task }
workers = {i: None for i in range(WORKERS)}
work_queue = []
work_done = []

while len(work_done) < len(tasks):
    # print(f'------ Time: {ts} -----')
    # pprint(f'work queue: {work_queue}')

    # add to the work queue all tasks that are not already done
    # and are currently not blocked by a requirement 
    work_queue.extend(
        task for task in tasks
        if
            not task.is_done
            and not task.is_assigned
            and all(prereq.is_done for prereq in task.prerequisites)
            and not task in work_queue
    )
    work_queue.sort(key=lambda task: task.name)

    for w in workers:
        if not workers[w] and work_queue:
            task = work_queue.pop(0)
            print(f'Assigning task {task} to worker {w}')
            workers[w] = task
            task.is_assigned = True

    ts += 1

    for w in workers:
        task = workers[w]
        if task:
            task.do_work()
            if task.is_done:
                print(f'Task {task} done.')
                work_done.append(task)
                workers[w] = None

print(f'Time elapsed: {ts} seconds.')
# pprint(tasks)
# pprint(sorted(work_done, key=lambda t: t.name))