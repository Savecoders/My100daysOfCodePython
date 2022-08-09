

def threeSum(nums: list[int]) -> list[list[int]]:

    if len(nums) <=2:
        return  []

    nums_in_order, count_sums = sorted(nums), []

    # two pointers to arrays
    
    point_one, point_two, point_three = 0, (len(nums_in_order)-1) , 0
    first_count, two_count = 0, 0

    for i in range(len(nums_in_order)-1):

        first_count, two_count = nums_in_order[point_one], nums_in_order[point_two]
        outside = first_count + two_count

        if not outside == 0:

            point_three = 0 - outside

            if point_three in nums_in_order:

                count_sums = [first_count, two_count, point_three]

            elif outside > 0:

                point_two -=1
            
            elif outside < 0:

                point_one+=1
        
        elif 0 in nums_in_order:

            count_sums = [first_count, two_count, point_three]
        
        else:
            point_two -=1
    
    nums.remove(first_count)
    nums.remove(two_count)
    nums.remove(point_three)

    if len(nums) <= 2:
        return [count_sums]
    else:
        return [count_sums, *threeSum(nums)]



print(threeSum([1,-1,0,1,-1,0,2,1,-3]))