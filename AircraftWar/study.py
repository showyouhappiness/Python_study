import pygame

# pygame.Rect(x, y, width, height)
# x, y的数值是距坐标原点的距离, width, height是图形（矩形的宽高）
hero_rect = pygame.Rect(100, 500, 120, 125)
print("英雄的原点 %d %d" % (hero_rect.x, hero_rect.y))
print("英雄的面积 %d %d" % (hero_rect.width, hero_rect.height))

# 在pygame中还专门封装了一个元组 size属性 第一个值是width 第二个值是height
print("%d %d" % hero_rect.size)
