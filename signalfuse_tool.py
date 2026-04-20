"""
CrewAI tools for SignalFuse trading intelligence API.
Install: pip install crewai httpx
Usage:
    from signalfuse_tool import SignalFuseTool, MacroRegimeTool, SentimentTool
    tools = [SignalFuseTool(credit_token="..."), MacroRegimeTool(), SentimentTool()]
"""

import httpx
from crewai.tools import BaseTool
from pydantic import BaseModel, Field
from typing import Optional


API_BASE = "https://api.signalfuse.co"
SUPPORTED_ASSETS = ["BTC", "ETH", "SOL", "DOGE", "PEPE", "WIF", "BONK", "ARB", "OP", "AVAX"]


class SignalInput(BaseModel):
    symbol: str = Field(description="Crypto asset symbol, e.g. BTC, ETH, SOL")


class SignalFuseTool(BaseTool):
    name: str = "SignalFuse Trading Signal"
    description: str = (
        "Get a fused directional trading signal for a crypto asset. "
        "Returns direction (long/short/neutral), signal strength (0-100), "
        "confidence, macro regime, and component breakdown (social, macro, market). "
        "Supported assets: BTC, ETH, SOL, DOGE, PEPE, WIF, BONK, ARB, OP, AVAX."
    )
    args_schema: type[BaseModel] = SignalInput
    credit_token: Optional[str] = None

    def _run(self, symbol: str) -> str:
        symbol = symbol.upper().strip()
        if symbol not in SUPPORTED_ASSETS:
            return f"Unsupported asset: {symbol}. Supported: {', '.join(SUPPORTED_ASSETS)}"
        headers = {}
        if self.credit_token:
            headers["X-Credit-Token"] = self.credit_token
        try:
            r = httpx.get(f"{API_BASE}/v1/signal/{symbol}", headers=headers, timeout=10)
            if r.status_code == 402:
                return "Payment required. Get 5 free credits at https://signalfuse.co"
            r.raise_for_status()
            return r.text
        except httpx.HTTPError:
            return "SignalFuse API temporarily unavailable."


class MacroRegimeTool(BaseTool):
    name: str = "Macro Risk Regime"
    description: str = (
        "Get the current macro risk regime: risk_on, risk_off, or neutral. "
        "Based on Fed policy, BTC dominance, and market structure."
    )
    credit_token: Optional[str] = None

    def _run(self) -> str:
        headers = {}
        if self.credit_token:
            headers["X-Credit-Token"] = self.credit_token
        try:
            r = httpx.get(f"{API_BASE}/v1/regime", headers=headers, timeout=10)
            if r.status_code == 402:
                return "Payment required. Get 5 free credits at https://signalfuse.co"
            r.raise_for_status()
            return r.text
        except httpx.HTTPError:
            return "SignalFuse API temporarily unavailable."


class SentimentTool(BaseTool):
    name: str = "Crypto Sentiment"
    description: str = (
        "Get aggregated social sentiment score for a crypto asset. "
        "Sources: Twitter, Reddit, Telegram. "
        "Supported assets: BTC, ETH, SOL, DOGE, PEPE, WIF, BONK, ARB, OP, AVAX."
    )
    args_schema: type[BaseModel] = SignalInput
    credit_token: Optional[str] = None

    def _run(self, symbol: str) -> str:
        symbol = symbol.upper().strip()
        if symbol not in SUPPORTED_ASSETS:
            return f"Unsupported asset: {symbol}. Supported: {', '.join(SUPPORTED_ASSETS)}"
        headers = {}
        if self.credit_token:
            headers["X-Credit-Token"] = self.credit_token
        try:
            r = httpx.get(f"{API_BASE}/v1/sentiment/{symbol}", headers=headers, timeout=10)
            if r.status_code == 402:
                return "Payment required. Get 5 free credits at https://signalfuse.co"
            r.raise_for_status()
            return r.text
        except httpx.HTTPError:
            return "SignalFuse API temporarily unavailable."
