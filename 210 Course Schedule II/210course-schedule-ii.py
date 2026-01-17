from collections import defaultdict, deque

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        
        graph, dependencies = defaultdict(list), [0] * numCourses

        #build graph
        for course, prereq in prerequisites:
            graph[prereq].append(course)
            dependencies[course] += 1

        #list with course order after completing prereq
        res = []

        #add courses that can be taken immediately
        q = deque([course for course, degree in enumerate(dependencies) if degree == 0])

        while q:
            currCourse = q.popleft()
            #add the queue you can immediately take
            res.append(currCourse)

            #check/ add the courses that can be taken once curr course is cleared
            for dependCourse in graph[currCourse]:
                #reduce the dependencies
                dependencies[dependCourse] -= 1

                #check if its now zero after reducing
                if dependencies[dependCourse] == 0:
                    q.append(dependCourse)

        return res if len(res) == numCourses else []




