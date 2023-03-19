import random
import math


class MathsExpressionGenerator:
    # These methods should return an answer
    # Ideally, a tuple with the snd being the answer to that expression
    # There are quite a bit of overlap in these methods, maybe use helper functions?
    @staticmethod
    def addition():
        fst_no = random.randint(1, 999)
        snd_no = random.randint(1, 999)

        answer = fst_no + snd_no
        expressions = [
            f"{fst_no} plus {snd_no}",
            f"Add {fst_no} to {snd_no}",
            f"Sum of {fst_no} and {snd_no}",
            f"Increase {fst_no} by {snd_no}"
        ]
        return random.choice(expressions), answer

    @staticmethod
    def subtraction():
        fst_no = random.randint(1, 999)
        snd_no = random.randint(1, fst_no)

        answer = fst_no - snd_no

        expressions = [
            f"{fst_no} minus {snd_no}",
            f"Subtract {snd_no} from {fst_no}",
            f"Take away {snd_no} from {fst_no}",
            f"Difference between {fst_no} and {snd_no}",
            f"Difference between {snd_no} and {fst_no}",
            f"Decrease {fst_no} by {snd_no}",
            f"Reduce {fst_no} by {snd_no}"
        ]

        return random.choice(expressions), answer

    @staticmethod
    def multiplication():
        multiplication_types = [
            MathsExpressionGenerator.multiplication1xn,
            MathsExpressionGenerator.multiplication2x2
        ]

        (fst_no, snd_no) = random.choice(multiplication_types)()

        answer = fst_no * snd_no

        expressions = [
            f"{fst_no} times {snd_no}",
            f"Multiply {fst_no} by {snd_no}",
            f"Product of {fst_no} and {snd_no}"
        ]

        return random.choice(expressions), answer

    @staticmethod
    def multiplication2x2():
        fst_no = random.randint(10, 20)
        snd_no = random.randint(10, 20)

        return fst_no, snd_no

    @staticmethod
    def multiplication1xn():
        # Should I do reverse sometimes (It is always 1xn instead of nx1)
        fst_no = random.randint(1, 9)
        snd_no = random.randint(10, 999)

        return fst_no, snd_no

    @staticmethod
    def division():
        dividend, divisor = MathsExpressionGenerator.division_hard()

        answer = math.round(dividend / divisor)

        expressions = [
            f"Divide {dividend} by {divisor}",
            f"{dividend} divided by {divisor}"
        ]

        return random.choice(expressions), answer

    @staticmethod
    def divisionNats():
        # Increase difficulty of the number range?
        divisor = random.randint(1, 20)
        dividend = divisor * random.randint(1, 20)

        answer = int(dividend / divisor)

        expressions = [
            f"Divide {dividend} by {divisor}",
            f"{dividend} divided by {divisor}"
        ]
        return random.choice(expressions), answer

    @staticmethod
    def division_hard():
        dividend = random.randint(2, 999)
        # Fix this
        divisor = random.randint(1, math.ceil(dividend/2))

        return dividend, divisor


    @staticmethod
    def large_no_generator(self):
        large_no = random.randint(1000, 99999)
        return f"{large_no}"
