
class Solution(object):
    def lemonadeChange(self, bills):
        cinco = 0
        diez = 0

        for bill in bills:
            if bill == 5:
                cinco += 1

            elif bill == 10:
                if cinco == 0:
                    return False

                cinco -= 1
                diez += 1

            elif bill == 20:
                if diez > 0 and cinco > 0:
                    diez -= 1
                    cinco -= 1

                elif cinco >= 3:
                    cinco -= 3

                else:
                    return False

        return True

