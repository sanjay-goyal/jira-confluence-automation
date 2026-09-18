# Module 13 Completion Report

## MCP Configuration
```json
{
  "servers": {
    "echo-windows": {
      "command": "powershell",
      "args": [
        "-ExecutionPolicy",
        "Bypass",
        "-File",
        "${workspaceFolder}/work/module13-task/scripts/mcp-echo.ps1"
      ]
    },
    "epamJira": {
      "type": "http",
      "url": "https://mcp.epam.com/mcp/jira",
      "headers": {
        "Authorization": "Bearer [REDACTED]"
      }
    }
  },
  "inputs": [
    {
      "id": "epam-jira-token",
      "type": "promptString",
      "description": "EPAM Jira MCP bearer token",
      "password": true
    }
  }
}
```

## Configured Servers
- echo-windows
- epamJira

## MCP Tool Test
- Tool used: echo
- Output:
```text
Echo: Hello MCP!
```
