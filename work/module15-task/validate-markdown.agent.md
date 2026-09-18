# Validate Markdown Files

Use this checklist when reviewing Markdown files such as README documents or project notes.

## Goal
Confirm the document is clear, complete, and suitable for onboarding or project review.

## Validation steps

### 1. Required sections
Check whether the document includes the required headings.
- `## Features` or `## Feature`
- `## Setup`

If one is missing, record it as an issue.

### 2. Section quality
Verify the headings are meaningful and consistent.
- Prefer standard section names such as `## Features` and `## Setup`.
- If the file uses `Quick start`, `Configuration`, or `Getting started`, decide whether these satisfy the same intent.
- Record any naming inconsistency as a review issue.

### 3. Content completeness
Review the Markdown for enough information to help a new developer.
- What the project does
- How to install dependencies
- How to run the project locally
- Any required environment variables or setup notes

If content is vague or missing, flag it as incomplete.

### 4. Placeholder detection
Identify placeholder content.
- Generic statements such as "This folder is reserved..." should be treated as incomplete.
- A file should not be considered valid if it lacks a real project objective or actionable setup steps.

### 5. Final pass/fail decision
The file passes if it:
- includes the required headings,
- uses clear and consistent section names,
- contains enough information for setup and onboarding,
- is not just a placeholder.

If any of the above fail, record the issue and recommend the needed update.

## Example review output
- PASS: README includes both Features and Setup and includes actionable instructions.
- FAIL: README missing Setup section or only contains a generic placeholder.
