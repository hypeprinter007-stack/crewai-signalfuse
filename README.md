# crewai-signalfuse

CrewAI tools for [SignalFuse](https://signalfuse.co) — fused crypto trading signals.

## Install

```bash
pip install crewai httpx
```

## Usage

```python
from signalfuse_tool import SignalFuseTool, MacroRegimeTool, SentimentTool

tools = [
    SignalFuseTool(credit_token="your-token"),
    MacroRegimeTool(credit_token="your-token"),
    SentimentTool(credit_token="your-token"),
]

# Use in any CrewAI agent
from crewai import Agent

analyst = Agent(
    role="Crypto Market Analyst",
    goal="Analyze current market conditions and provide trading insights",
    tools=tools,
)
```

## Tools

- **SignalFuseTool** — fused directional signal (long/short/neutral) with strength and confidence
- **MacroRegimeTool** — current macro risk regime (risk_on / risk_off / neutral)
- **SentimentTool** — aggregated social sentiment score

## Assets

BTC, ETH, SOL, DOGE, PEPE, WIF, BONK, ARB, OP, AVAX

## Credits

Get 25 free calls at [signalfuse.co](https://signalfuse.co) — no signup.

## Disclaimer

SignalFuse provides a data fusion API, not financial advice. Signals are mathematical composites that can be wrong. Trade at your own risk.
