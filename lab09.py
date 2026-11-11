# Problem-solving practice (LeetCode / ICPC style).
#
# For EACH problem, work out your problem-solving OUTLINE first - restate the problem,
# try a small example by hand, and sketch your approach - BEFORE you write or generate
# any code. You may use an AI assistant to help implement your plan (see the README),
# but do the thinking first.
#
# Do not rename the functions - the tests use these names.


def two_sum(nums, target):
    seen = {}
    for i, num in enumerate(nums):
        diff = target - num
        if diff in seen:
            return [seen[diff], i]
        seen[num] = i


def max_profit(prices):
    min_price = float('inf')
    max_prof = 0
    
    for price in prices:
        if price < min_price:
            min_price = price
        elif price - min_price > max_prof:
            max_prof = price - min_price
            
    return max_prof


def max_subarray(nums):
    max_sum = nums[0]
    current_sum = nums[0]
    
    for num in nums[1:]:
        current_sum = max(num, current_sum + num)
        max_sum = max(max_sum, current_sum)
        
    return max_sum


def is_balanced(s):   # Part 4 - stretch (optional)
    matching_bracket = {')': '(', ']': '[', '}': '{'}
    stack = []
    
    for char in s:
        if char in matching_bracket.values():
            stack.append(char)
        elif char in matching_bracket:
            if not stack or stack[-1] != matching_bracket[char]:
                return False
            stack.pop()
            
    return len(stack) == 0


def main():
    print("two_sum([2, 7, 11, 15], 9) =", two_sum([2, 7, 11, 15], 9)) # Output: [0, 1]
    print("max_profit([7, 1, 5, 3, 6, 4]) =", max_profit([7, 1, 5, 3, 6, 4])) # Output: 5
    print("max_subarray([-2, 1, -3, 4, -1, 2, 1, -5, 4]) =", max_subarray([-2, 1, -3, 4, -1, 2, 1, -5, 4])) # Output: 6
    print("is_balanced('()[]{}') =", is_balanced("()[]{}")) # Output: True
    print("is_balanced('([)]') =", is_balanced("([)]")) # Output: False

if __name__ == "__main__":
    main()
