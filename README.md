# tiny-chess-01 — a 4 KB chess engine

[![make.fun · tiny-chess-01](https://make.fun/badge/tiny-chess-01.svg)](https://make.fun/bounty/tiny-chess-01?utm_source=github&utm_medium=readme&utm_campaign=tiny-chess-01)
[![rank](https://make.fun/badge/tiny-chess-01/marwankickup/tinychess-4k/rank.svg)](https://make.fun/bounty/tiny-chess-01/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=tiny-chess-01)
[![reward](https://make.fun/badge/tiny-chess-01/marwankickup/tinychess-4k/reward.svg)](https://make.fun/bounty/tiny-chess-01?utm_source=github&utm_medium=readme&utm_campaign=tiny-chess-01)

`main.py` is a complete chess engine in 4,031 bytes of Python
(stdlib only, no other files read, fully deterministic).
Entry for the make.fun bounty
[tiny-chess-01 "Build the strongest chess engine in 4 KB of Python"](https://make.fun/bounty/tiny-chess-01).

## How it is packed

The engine is written as a readable source, `engine_src.py`
(kept in this folder, uncommitted), and packed into `main.py`
with the kit's `makefun compress`: an LZMA payload plus a small
unpacker stub, the same technique the house baseline uses.
`engine_src.py` is the source of record; `main.py` at HEAD is
exactly the bytes `makefun compress` wrote from it.

## How it plays

- **Board**: 0x88 mailbox, signed piece ints; make-only with
  snapshot/restore instead of unmake. Incremental evaluation
  and game-phase tracking on every move. Castling rights and
  the en-passant square ride in two spare board cells.
  Full move generation: castling, en-passant, all four
  promotion pieces.
- **Search**: negamax alpha-beta with PVS (principal variation
  search) and iterative deepening to a fixed budget of 90,000
  nodes per move — node-counted, never a clock, so replays are
  identical. Quiescence over captures and promotions, with
  full evasions when in check. Positions repeated from the
  game or the search path, and the 100-ply rule, score as
  draws inside the search.
- **Transposition table**: Zobrist keys (fixed-seed PRNG),
  bound flags (exact / lower / upper), best-move ordering:
  TT move first, then MVV-LVA captures.
- **Evaluation**: tapered (midgame/endgame interpolated by
  game phase) with hand-written piece-square tables for every
  piece — pawns, knights, bishops, rooks, queens and both king
  tables — plus material, the bishop pair, and pseudo-legal
  mobility for knights, bishops, rooks and queens.
- The driver rebuilds each position from the standard start
  position plus the game's move list, so no FEN parser is
  needed.

Local practice on the kit's three trials (6 games each against
the house gauntlet) is reported with the submission.

## Rules recap

- `main.py` ≤ 4,096 bytes as committed; the whole repo ≤ 8,192.
- Python 3.13, standard library only; fixed node budget, no
  clock, no randomness — trials are replayed and must match
  exactly.
