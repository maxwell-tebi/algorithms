#I showed up on day 4 and struggled to understand Trionic Subarray II but I tried

def max_sum_trionic(nums):
    n = len(nums)
    if n < 5:
        return -1

    # Step 1: best increasing sums and lengths from the left
    incL_sum = nums[:]
    incL_len = [1] * n
    for i in range(1, n):
        if nums[i] > nums[i - 1]:
            incL_sum[i] = incL_sum[i - 1] + nums[i]
            incL_len[i] = incL_len[i - 1] + 1

    # Step 2: best increasing sums and lengths from the right
    incR_sum = nums[:]
    incR_len = [1] * n
    for i in range(n - 2, -1, -1):
        if nums[i] < nums[i + 1]:
            incR_sum[i] = incR_sum[i + 1] + nums[i]
            incR_len[i] = incR_len[i + 1] + 1

    ans = float('-inf')
    i = 1

    # Step 3: scan decreasing middle segments
    while i < n - 1:
        if nums[i - 1] > nums[i]:
            dec_sum = nums[i]
            dec_len = 1
            j = i

            while j + 1 < n and nums[j] > nums[j + 1]:
                j += 1
                dec_sum += nums[j]
                dec_len += 1

                # enforce all three parts have length >= 2
                if (
                    incL_len[i - 1] >= 2 and
                    dec_len >= 2 and
                    incR_len[j + 1] >= 2
                ):
                    ans = max(
                        ans,
                        incL_sum[i - 1] +
                        dec_sum +
                        incR_sum[j + 1]
                    )

            i = j
        i += 1

    return ans if ans != float('-inf') else -1
