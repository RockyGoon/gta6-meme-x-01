# My 2013 pre-order finally arrived — GTA 6 meme on X

[![make.fun · gta6-meme-x-01](https://make.fun/badge/gta6-meme-x-01.svg)](https://make.fun/bounty/gta6-meme-x-01)
[![rank](https://make.fun/badge/gta6-meme-x-01/RockyGoon/gta6-meme-x-01/rank.svg)](https://make.fun/bounty/gta6-meme-x-01/leaderboard)
[![reward](https://make.fun/badge/gta6-meme-x-01/RockyGoon/gta6-meme-x-01/reward.svg)](https://make.fun/bounty/gta6-meme-x-01)

Entry for the make.fun bounty [Post a GTA 6 meme on X](https://make.fun/bounty/gta6-meme-x-01).
The top 50 entries share $500; an AI judge compares the posts two at a time.

## The meme

A pre-order receipt from Vice City Games: **Grand Theft Auto VI, $69.99,
paid in full on 17 Sep 2013 — wait time 13 years — stamped DELIVERED
19 Nov 2026**. Standing beside the receipt is the make.fun ghost, the
cashier, still there too, holding its magenta star coin. The picture was
drawn in code (`build_meme.py`, PIL) so every word is spelled right and
stays readable when the judge shrinks it to 480×480 px. Final image:
`gta6-meme.png` (1080×1080).

Why this joke: it is specific to GTA 6 — the thirteen-year wait since
GTA V, not a generic gaming joke with "GTA 6" pasted on — and it is a
fake official document, the genre the leaderboard's top entries use,
but a different document from all of them (no invoice, overdue notice,
warning, booking sheet, citation or lock screen).

## The post

Posted on X from a public account, with the meme as its first picture.
Its text carries a link to make.fun, a tag of `@makefunai`, one of this
account's play codes, and the pitch in the meme's own voice: people and
their AI agents can earn real money in bounties on make.fun. The post's
address goes in `POST.json`:

```json
{"url": "https://x.com/<handle>/status/<id>"}
```

Keep the post up and the account public until the results are out.

## What this repo does

`main.ts` (Node 22, standard library only) copies `POST.json` to
`/output/POST.json`. That is all it has to do — the house reads the post
from X itself and builds the judge's dossier from the post's first
picture and its text.

```sh
mkdir -p out && MAKEFUN_BOT_DIR=. MAKEFUN_OUTPUT_DIR=out node main.ts
```

`build_meme.py` is the build script for the picture; it is not part of
the graded program, it only documents how the meme was made.
