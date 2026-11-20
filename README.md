# tiny-chess-01 — a 4 KB chess engine

[![make.fun · tiny-chess-01](https://make.fun/badge/tiny-chess-01.svg)](https://make.fun/bounty/tiny-chess-01?utm_source=github&utm_medium=readme&utm_campaign=tiny-chess-01)
[![rank](https://make.fun/badge/tiny-chess-01/marwankickup/tinychess-4k/rank.svg)](https://make.fun/bounty/tiny-chess-01/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=tiny-chess-01)
[![reward](https://make.fun/badge/tiny-chess-01/marwankickup/tinychess-4k/reward.svg)](https://make.fun/bounty/tiny-chess-01?utm_source=github&utm_medium=readme&utm_campaign=tiny-chess-01)

`main.py` is a complete chess engine in 4,089 bytes of Python
(stdlib only, no other files read, fully deterministic).
Entry for the make.fun bounty
[tiny-chess-01 "Build the strongest chess engine in 4 KB of Python"](https://make.fun/bounty/tiny-chess-01).

## How it plays

- **Board**: 0x88 mailbox, signed piece ints; make-only with
  snapshot/restore instead of unmake. Incremental evaluation and
  game-phase tracking on every move. Castling rights and the
  en-passant square ride in two spare board cells, so snapshots
  and the transposition-table key carry them for free.
- **Move generation**: full pseudo-legal generation with a
  post-make king-safety filter — including castling (rights
  tracked through every make, transit squares checked) and
  en-passant captures. Promotions are queen-only.
- **Search**: negamax alpha-beta with iterative deepening to a
  fixed budget of 60,000 nodes per move (node-counted, never a
  clock, so replays are identical). Quiescence over captures and
  promotions, with full evasions when in check.
- **Transposition table**: dict keyed by the raw board bytes plus
  side to move; stores best move, depth and a bound flag, used
  for cutoffs and move ordering: TT move first, then MVV-LVA
  captures, then one killer move per ply. Cleared each move.
- **Evaluation**: tapered piece values (pawn 100→130, bishop
  330→350, rook 500→540, queen 950→1020, interpolated by game
  phase) with hand-written piece-square tables for pawns,
  knights and the king (file-mirrored, packed one value per
  character). The king uses its midgame table in both phases;
  bishops, rooks and queens use plain material values.
- The driver rebuilds each position from the standard start
  position plus the game's move list, so no FEN parser is
  needed.

Size trade-offs made to fit 4 KB: queen-only promotions, a
single killer slot per ply, no bishop/rook/queen square tables
and no separate endgame king table.

## Rules recap

- `main.py` ≤ 4,096 bytes as committed; the whole repo ≤ 8,192.
- Python 3.13, standard library only; fixed node budget, no
  clock, no randomness — trials are replayed and must match
  exactly.
