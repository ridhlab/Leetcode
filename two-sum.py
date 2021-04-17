class Solution:   
    def twoSum(self, nums, target):
        self.List_ = nums
        self.target = target
        self.banyak_sample = len(self.List_)
        for i in range(self.banyak_sample):
            self.a = False
            self.list_result = []
            for x in range(i+1, self.banyak_sample):
                if self.List_[i] + self.List_[x] == self.target:
                    self.sum_ = self.List_[i] + self.List_[x]
                    self.list_result.append(i)
                    self.list_result.append(x)
                    self.a = True
                    break
                else:
                    pass
            if self.a == True:
                break
        return self.list_result
input_sample = [2, 7, 11, 15]  
input_target = 9
p1 = Solution()
result = p1.twoSum(input_sample, input_target)
print(result)

   