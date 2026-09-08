from __future__ import annotations

from math import gcd


def pollard_rho(
    num: int,
    seed: int = 2,
    step: int = 1,
    attempts: int = 3,
) -> int | None:
    """
    使用 Pollard's Rho 算法返回 ``num`` 的一个非平凡因子。
    返回的因子可能是合数,仍需继续分解。
    如果算法在指定的尝试次数或步数之内未能找到因子,则返回 None。
    若 ``num`` 为素数,本算法保证返回 None。
    https://en.wikipedia.org/wiki/Pollard%27s_rho_algorithm

    >>> pollard_rho(18446744073709551617)
    274177
    >>> pollard_rho(97546105601219326301)
    9876543191
    >>> pollard_rho(100)
    2
    >>> pollard_rho(17)
    >>> pollard_rho(17**3)
    17
    >>> pollard_rho(17**3, attempts=1)
    >>> pollard_rho(3*5*7)
    21
    >>> pollard_rho(1)
    Traceback (most recent call last):
        ...
    ValueError: The input value cannot be less than 2
    """
    # 小于 2 的值会让算法陷入死循环。
    if num < 2:
        raise ValueError("The input value cannot be less than 2")

    # 由于 ``f(f(x))`` 与 ``f(x)`` 之间的关系,本算法难以找到能被 2 整除的因子。
    # 作为补救手段,我们专门检查 2 以及偶数输入。
    #   参见:https://math.stackexchange.com/a/2856214/165820
    if num > 2 and num % 2 == 0:
        return 2

    # Pollard's Rho 算法需要一个能在 0 <= X < ``num`` 范围内产生伪随机值的函数。
    # 它不需要达到密码学安全或难以计算的随机程度,
    # 只需要所有输出值等概率出现即可。
    # 出于这个原因,Pollard 建议使用 ``f(x) = (x**2 - 1) % num``。
    # 然而,Pollard 算法并不保证成功,其成败部分取决于初始种子和所选的随机函数。
    # 为了便于重试,我们改用 ``f(x) = (x**2 + C) % num``,
    # 其中 ``C`` 是可以在每次尝试之间修改的值。
    def rand_fn(value: int, step: int, modulus: int) -> int:
        """
        基于输入 ``value`` 和每次尝试特有的 ``step``,返回一个以 ``modulus``
        为模的伪随机值。

        >>> rand_fn(0, 0, 0)
        Traceback (most recent call last):
            ...
        ZeroDivisionError: integer division or modulo by zero
        >>> rand_fn(1, 2, 3)
        0
        >>> rand_fn(0, 10, 7)
        3
        >>> rand_fn(1234, 1, 17)
        16
        """
        return (pow(value, 2) + step) % modulus

    for _ in range(attempts):
        # 这两个变量用于循环检测逻辑中的位置跟踪。
        tortoise = seed
        hare = seed

        while True:
            # 每次迭代,乌龟走一步,兔子走两步。
            tortoise = rand_fn(tortoise, step, num)
            hare = rand_fn(hare, step, num)
            hare = rand_fn(hare, step, num)

            # 在某个时刻,乌龟和兔子都会进入一个长度 ``p`` 为 ``num`` 约数的环。
            # 一旦进入该环,乌龟和兔子迟早会在模 ``p`` 意义下落到相同的值上。
            # 我们之所以能检测到这一时刻,是因为乌龟与兔子之间的位置差
            # 会与 ``num`` 拥有公因数。
            divisor = gcd(hare - tortoise, num)

            if divisor == 1:
                # 还没有出现公因数,继续搜索。
                continue
            # 找到公因数了!
            elif divisor == num:
                # 遗憾的是,该因数是 ``num`` 本身,毫无用处。
                break
            else:
                # 该因数正是 ``num`` 的一个非平凡因子!
                return divisor

        # 如果执行到这里,说明本次尝试失败。
        # 我们需要为乌龟和兔子挑选新的起始种子,
        # 同时为随机函数选定新的步长值。
        # 为了让这个示例实现保持确定性,
        # 新值将基于当前已有的值生成,而不是使用 ``random.randint`` 之类。

        # 我们可以用兔子的位置作为新种子。
        # 这实际上正是 Richard Brent 的"优化"变体所做的事。
        seed = hare

        # 随机函数的新步长值直接递增即可。
        # 一开始的结果与旧函数产生的结果相近,但很快就会发散。
        step += 1

    # 在要求的尝试次数内没有找到因数。
    # 可能是我们运气不好,或者 ``num`` 本身其实就是素数。
    return None


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser()
    parser.add_argument(
        "num",
        type=int,
        help="要为其寻找因数的值",
    )
    parser.add_argument(
        "--attempts",
        type=int,
        default=3,
        help="放弃前的尝试次数",
    )
    args = parser.parse_args()

    divisor = pollard_rho(args.num, attempts=args.attempts)
    if divisor is None:
        print(f"{args.num} is probably prime")
    else:
        quotient = args.num // divisor
        print(f"{args.num} = {divisor} * {quotient}")
