param(
    [string]$Command = "echo",
    [string]$Message = "hello from mcp echo",
    [string]$Operation = "+",
    [double]$A = 0,
    [double]$B = 0
)

function Invoke-Echo {
    param([string]$Text)
    return "Echo: $Text"
}

function Get-CurrentTimestamp {
    return (Get-Date).ToString("o")
}

function Invoke-Calculation {
    param(
        [string]$Op,
        [double]$Left,
        [double]$Right
    )

    switch ($Op) {
        "+" { return [string]($Left + $Right) }
        "-" { return [string]($Left - $Right) }
        "*" { return [string]($Left * $Right) }
        "/" {
            if ($Right -eq 0) {
                throw "Division by zero is not allowed."
            }
            return [string]($Left / $Right)
        }
        default {
            throw "Unsupported operation. Use one of: +, -, *, /."
        }
    }
}

try {
    switch ($Command.ToLowerInvariant()) {
        "echo" {
            Write-Output (Invoke-Echo -Text $Message)
        }
        "get_time" {
            Write-Output (Get-CurrentTimestamp)
        }
        "calculate" {
            Write-Output (Invoke-Calculation -Op $Operation -Left $A -Right $B)
        }
        default {
            Write-Output "Unknown command: $Command"
            exit 1
        }
    }
} catch {
    Write-Error $_.Exception.Message
    exit 1
}
