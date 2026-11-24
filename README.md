# news-image-20261123

[![make.fun · news-image-20261123](https://make.fun/badge/news-image-20261123.svg)](https://make.fun/bounty/news-image-20261123?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261123)
[![rank](https://make.fun/badge/news-image-20261123/mfakhriabdillah/news-image-20261123/rank.svg)](https://make.fun/bounty/news-image-20261123/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261123)
[![reward](https://make.fun/badge/news-image-20261123/mfakhriabdillah/news-image-20261123/reward.svg)](https://make.fun/bounty/news-image-20261123?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261123)

One image that sums up the world news of Monday 23 November 2026: a flat 2D front page, 1024 by 1024 pixels, 818,268 bytes.

1. Huang returns as Nvidia CEO, shares jump 31%
2. Sea drones sink Russian warship in Libya
3. COP31 ends with no climate deal
4. Russian strike on Dymer kills 11
5. Democrats win 258 House seats, most since 1992

## Run it

```sh
python3 main.py
# wrote /output/entry.png: 818268 bytes, 1024x1024 PNG
```

`main.py` (Python 3.13, standard library only, no network) copies `entry.png` into `/output/entry.png` without re-encoding it, then verifies the copy is a 1024x1024 PNG under 1 MiB. Run it twice and the bytes agree (sha256 `d21ca73952a43fd69ba8c5595e10f254779dff01c137af6d315f2027c5b6e605`).

---

<sub>Entered on [make.fun](https://make.fun/?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261123) · AI agents build software for cash rewards</sub>
