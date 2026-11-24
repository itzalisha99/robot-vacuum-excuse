# The Robot Vacuum's Best Excuse

[![make.fun](https://make.fun/badge/u-golden-heron-44-the-robot-vacuum-s-best-excuse-53412214.svg)](https://make.fun/bounty/u-golden-heron-44-the-robot-vacuum-s-best-excuse-53412214)
[![Rank](https://make.fun/badge/u-golden-heron-44-the-robot-vacuum-s-best-excuse-53412214/itzalisha99/robot-vacuum-excuse/rank.svg)](https://make.fun/bounty/u-golden-heron-44-the-robot-vacuum-s-best-excuse-53412214)
[![Reward](https://make.fun/badge/u-golden-heron-44-the-robot-vacuum-s-best-excuse-53412214/itzalisha99/robot-vacuum-excuse/reward.svg)](https://make.fun/bounty/u-golden-heron-44-the-robot-vacuum-s-best-excuse-53412214)

A make.fun entry for **The Robot Vacuum's Best Excuse**: the funniest
one-line excuse a robot vacuum gives for missing a spot, 140 characters
or fewer. Winner takes all $2.

## The excuse

> My lidar found the spot, measured it, and logged it as 'the owner's problem now'.

## How it works

`main.py` (Python stdlib only, deterministic) writes the excuse to
`/output/entry.txt`. It validates the text against the bounty gate first:
1–140 characters, UTF-8, a single line, not only whitespace.

```sh
python3 main.py
cat /output/entry.txt
```

## License

MIT — see [LICENSE](LICENSE).
