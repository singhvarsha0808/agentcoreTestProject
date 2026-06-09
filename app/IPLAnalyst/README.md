# IPL Command Center (IPLAnalyst)

Multi-agent IPL assistant powered by a **Strands Swarm** of five specialists:

| Agent | Role |
| --- | --- |
| `ipl_host` | Fan-facing host — routes questions and delivers final answers |
| `stats_guru` | Player stats, standings, team profiles, comparisons |
| `match_wizard` | Head-to-head, venues, fixtures, match previews |
| `fantasy_coach` | Dream11 XI, captain picks, fantasy ratings |
| `history_buff` | Records, champions, title leaderboard, legendary moments |

## Try it locally

```bash
agentcore dev
```

In another terminal:

```bash
agentcore invoke --dev "Compare Virat Kohli and Travis Head in IPL 2024"
agentcore invoke --dev "Who won IPL 2024 and what was the final scoreline story?"
agentcore invoke --dev "Build a differential fantasy XI for SRH vs KKR"
agentcore invoke --dev "CSK vs MI at Wankhede — who has the edge?"
```

## Data

Stats and records are bundled in `ipl_data/catalogue.py` (2024 season focus). No external API keys required.

## Related agents

- **IPLStatsAgent** — standalone statistics specialist
- **IPLFantasyAgent** — standalone fantasy coach

Invoke them with `agentcore invoke --agent IPLStatsAgent` (after deploy) or run separate dev sessions.
