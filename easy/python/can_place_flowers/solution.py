class Solution:
    """Return whether n flowers can be planted in flowerbed while
    maintaining empty plots between each flower in O(n) time and O(1) space."""
    def canPlaceFlowers(self, flowerbed, n):
        buffer = False
        just_planted = False
        new_flowers = 0
        for flower in flowerbed:
            if not flower:
                if buffer:
                    buffer = False
                    just_planted = False
                else:
                    new_flowers += 1
                    just_planted = True
                    buffer = True
            elif flower:
                buffer = True
                if just_planted:
                    just_planted = False
                    new_flowers -= 1
        return n <= new_flowers
