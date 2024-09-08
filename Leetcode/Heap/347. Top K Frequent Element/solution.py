#solution1
#Counter
class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        from collections import Counter
        c = Counter(nums)
        com = c.most_common(k)
        list = []
        for i in range(len(com)):
            list.append(com[i][0])
        return list

#solution2
#heapq
import heapq
from collections import defaultdict
class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        dict = defaultdict(int)
        for i in nums:
            dict[i] += 1
        
        #定義一個min_heap，大小为k
        pri_que = [] 
        
        #用固定大小為k的min_heap，掃描所有频率的數值
        for key, freq in dict.items():
            heapq.heappush(pri_que, (freq, key))
            if len(pri_que) > k: #如果堆的大小大於K，则隊列弹出，保證堆的大小一直為k
                heapq.heappop(pri_que)
        #找出前K个高频元素，因为min_heap先弹出的是最小的，所以倒序来输出到数组
        result = [0] * k
        for i in range(k-1, -1, -1):
            result[i] = heapq.heappop(pri_que)[1]
        return result

#solution3
from collections import defaultdict
class Solution:
    def topKFrequent(self,nums, k):
        time_dict = defaultdict(int)
        for num in nums:
            time_dict[num] += 1
        #更改字典，key為頻率，value為相應的數字
        index_dict = defaultdict(list)
        for key in time_dict:
            index_dict[time_dict[key]].append(key)

        #排序
        key = list(index_dict.keys()) 
        key.sort()
        result = []
        cnt = 0
        while key and cnt != k:
            result += index_dict[key[-1]]
            cnt += len(index_dict[key[-1]])
            key.pop()
        
        return result[0:k]



nums=[1,1,1,2,2,3]
k=2
obj = Solution()
print(obj.topKFrequent(nums,k))