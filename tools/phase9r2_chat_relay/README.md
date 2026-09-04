# Phase9R2 Encrypted Chat Relay

Temporary read-only request/response transport for authoritative dashboard and runtime reads while the Desktop Commander remote provider is unavailable.

- Requests and responses are AES-256-GCM encrypted.
- The relay executes only a fixed read-only command allowlist.
- No order, AutoTrading, EA, dashboard, Overdrive, or MT4 mutation is permitted.
- Payload files contain ciphertext only.
