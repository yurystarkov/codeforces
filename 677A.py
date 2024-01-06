friends_num, fence_height = map(int, input().split())
friends_heights = [int(height) for height in input().split()]

road_width = sum(
    1 if height <= fence_height else 2
    for height in friends_heights
)

print(road_width)
