class Solution:
		def maxProbability(self, n, edges, succProb, start, end) :

			graph = [[] for _ in range(n)]
			for i,(u,v) in enumerate(edges):
				graph[u].append([v,succProb[i]])
				graph[v].append([u,succProb[i]])

			pq = [[-1,start]]

			dist = collections.defaultdict(int)
			dist[start] = -1

			while pq:
				d,node = heapq.heappop(pq)            
				for nei,w in graph[node]:
					d2 = d*w
					if d2 < dist[nei]:
						heapq.heappush(pq,[d2,nei])
						dist[nei] = d2

			return -dist[end]
