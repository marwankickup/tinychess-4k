# tiny-chess-01 — a 4 KB chess engine

`main.py` is a complete chess engine in 4,079 bytes of Python
(stdlib only, no other files read, fully deterministic).

## How it plays

- **Board**: 0x88 mailbox, signed piece ints; make-only with
  snapshot/restore instead of unmake. Incremental evaluation and
  game-phase tracking on every move.
- **Search**: negamax alpha-beta with iterative deepening to a fixed
  budget of 60,000 nodes per move (node-counted, never a clock, so
  replays are identical). Quiescence over captures and promotions,
  with full evasions when in check.
- **Transposition table**: dict keyed by the raw board bytes plus
  side to move; stores best move, depth and a bound flag, used for
  cutoffs and move ordering (TT move first, then MVV-LVA captures).
- **Evaluation**: tapered — midgame and endgame piece values
  interpolated by game phase, with hand-written piece-square tables
  for pawns, knights and kings in the midgame and kings in the
  endgame (file-mirrored, packed one value per character).
- The driver rebuilds each position from the standard start
  position plus the game's move list, so no FEN parser is needed.

Size trade-offs made to fit 4 KB: the engine never castles and
never captures en passant itself (both are still executed when
the opponent or the opening book plays them), and bishops, rooks
and queens use plain material values without square tables.

## Rules recap

- `main.py` ≤ 4,096 bytes as committed; the whole repo ≤ 8,192.
- Python 3.13, standard library only; fixed node budget, no clock,
  no randomness — trials are replayed and must match exactly.
