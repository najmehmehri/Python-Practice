"""
Tower of Hanoi - Recursive Solution
Move n disks from source peg to target peg using a helper peg.
"""
def hanoi(n, source, helper, target):
    if n == 1:
        print(f"move disk 1 from peg {source} to peg {target}")
        return
    hanoi(n-1, source, target, helper)
    print(f"move disk {n} from peg {source} to peg {target}")
    hanoi(n-1, helper, source, target)


hanoi(3, "A", "B", "C")
