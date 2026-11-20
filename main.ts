// gta6-meme-x-01 — "My 2013 pre-order finally arrived" (Node 22, stdlib only).
// The entry is the X post itself: a GTA VI pre-order receipt paid in full
// on 17 Sep 2013, stamped DELIVERED 19 Nov 2026 after a 13-year wait, with
// the make.fun ghost as the cashier who is still there too. This program
// only hands the post's address to the gate: it copies POST.json from the
// repository root to /output/POST.json. Nothing it writes is judged — the
// house reads the post from X and builds the dossier itself.
//
// Local run:
//   mkdir -p out && MAKEFUN_BOT_DIR=. MAKEFUN_OUTPUT_DIR=out node main.ts

import { copyFileSync, mkdirSync, readFileSync } from 'node:fs';
import { join } from 'node:path';

const BOT_DIR = process.env.MAKEFUN_BOT_DIR ?? '/bot';
const OUTPUT_DIR = process.env.MAKEFUN_OUTPUT_DIR ?? '/output';

mkdirSync(OUTPUT_DIR, { recursive: true });
try {
  // Fail loudly (instead of copying a broken file) if POST.json is not
  // a JSON object with a url string — the gate refuses anything else.
  const parsed: unknown = JSON.parse(
    readFileSync(join(BOT_DIR, 'POST.json'), 'utf8'),
  );
  if (typeof parsed !== 'object' || parsed === null || !('url' in parsed)
    || typeof (parsed as { url: unknown }).url !== 'string') {
    throw new Error('POST.json must be a JSON object with a string "url"');
  }
  copyFileSync(join(BOT_DIR, 'POST.json'), join(OUTPUT_DIR, 'POST.json'));
} catch (err) {
  console.error(`POST.json could not be copied from ${BOT_DIR}: ${(err as Error).message}`);
  process.exit(1);
}
