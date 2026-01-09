# mcp-servers
A collection of mcp servers created by me.

## Setup with uv
1. Install dependencies:
   ```sh
   uv pip install -r pyproject.toml
   ```
   Or, if you have a uv.lock file:
   ```sh
   uv sync
   ```
2. Run the server:
   ```sh
   uvicorn <your_module>:<app_instance>
   ```

## Setup MCP server with agent
1. Configure your MCP server as needed (see mcp.json or relevant config).
2. Register or connect your agent according to your agent's documentation or configuration steps.
