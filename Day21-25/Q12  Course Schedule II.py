class Solution(object):
    def findOrder(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: List[int]
        """
        adjacency_list = [[] for i in range(numCourses)]
        in_degrees = [0] * numCourses
        for courses in prerequisites:
            course, prereq = courses
            adjacency_list[prereq].append(course)
            in_degrees[course] += 1
        zero_indegree_courses = [i for i in range(numCourses) if in_degrees[i] == 0]
        for course in zero_indegree_courses:
            for adjacent_course in adjacency_list[course]:
                in_degrees[adjacent_course] -= 1
                if in_degrees[adjacent_course] == 0:
                    zero_indegree_courses.append(adjacent_course)
        return zero_indegree_courses if len(zero_indegree_courses) == numCourses else [] 
