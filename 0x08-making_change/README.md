# 0x08. Making Change

### Tasks

### [0. Change comes from within](./0-making_change.py)

Given a pile of coins of different values, determine the fewest number of coins needed to meet a given amount `total`.

- [x] Prototype: def makeChange(coins, `total`)
- [x] Return: fewest number of coins needed to meet `total`
  - [x] If `total` is `0` or less, return `0`
  - [x] If `total` cannot be met by any number of coins you have, return `-1`
- [x] `coins` is a list of the values of the coins in your possession
- [x] The value of a coin will always be an integer greater than `0`
- [x] You can assume you have an infinite number of each denomination of coin in the list
- [x] Your solution’s runtime will be evaluated in this task

```sh
carrie@ubuntu:~/0x08-making_change$ cat 0-main.py
#!/usr/bin/python3
"""
Main file for testing
"""

makeChange = __import__('0-making_change').makeChange

print(makeChange([1, 2, 25], 37))

print(makeChange([1256, 54, 48, 16, 102], 1453))

carrie@ubuntu:~/0x08-making_change$
```

```sh
carrie@ubuntu:~/0x08-making_change$ ./0-main.py
7
-1
carrie@ubuntu:~/0x08-making_change$
```
