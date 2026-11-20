# gta6-meme-x-01 — agent notes

Entry: one GTA 6 meme posted on X, handed in via `POST.json`.

- Meme: `gta6-meme.png`, built by `build_meme.py` (PIL, code-drawn text so
  spelling is exact). A 2013 GTA VI pre-order receipt, paid in full,
  delivered 13 years later; the make.fun ghost is the cashier, holding
  its magenta star coin. `make.fun` is also written large in the bottom
  banner, so the picture passes the judge's first criterion even at
  480×480 px.
- Post (Rika's step, never the agent's): public X account, meme as first
  picture, text with a make.fun link and/or `@makefunai`, one play code,
  and the earn-money pitch. Then fill in `POST.json` with the real URL.
- Program: `main.ts` copies `POST.json` to `/output/POST.json`, stdlib
  only, no network, deterministic. Test locally with
  `mkdir -p out && MAKEFUN_BOT_DIR=. MAKEFUN_OUTPUT_DIR=out node main.ts`
  and confirm `out/POST.json` matches.
- Submit from the kit directory with the kit CLI `check` then `submit`
  (see the kit's RULES.txt); repo `RockyGoon/gta6-meme-x-01`, created
  after the bounty opened 2026-11-19T14:00:00Z, deadline
  2026-11-23T14:00:00Z (23 Nov 21:00 WIB).
