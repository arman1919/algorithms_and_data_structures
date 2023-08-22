def majorityElement(list0: list[int]) -> int:
        counts = {}
        max_count = 0
        major = list0.value
        while list0.next != None:
            
            if list0.value in counts:
                
                counts[list0.value] += 1
                if counts[list0.value] > max_count:
                    max_count = counts[list0.value]
                    major = list0
                    list0 = list0.next
                
            else:
                counts[list0.value] = 1
                list0 = list0.next
                        

        return major