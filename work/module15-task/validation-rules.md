# README Validation Rules

Use these checks when reviewing README files in the project.

## 1. Required sections
A README should include both of the following sections:
- `## Features` or `## Feature`
- `## Setup`

If either heading is missing, mark the file as incomplete.

## 2. Section naming consistency
Check for a consistent heading style across files.
- Prefer exact headings such as `## Features` and `## Setup`.
- Files using variations like `## Quick start`, `## Configuration`, or `## Getting started` should be reviewed manually to decide whether they satisfy the required intent.

## 3. Content completeness
A valid README should provide enough information for a new developer to understand:
- what the project does
- how to install or configure dependencies
- how to run it locally

A file is weak if it only contains a title and a short description without actionable setup instructions.

## 4. Project readiness signal
A README should not be considered complete if it is only a placeholder.
- Placeholder files with generic text like "This folder is reserved..." should be flagged as missing real project documentation.
- A README should ideally include at least a basic project objective, setup steps, and a short feature summary.

## Review outcome
A README passes when it contains the required sections and enough detail to support a developer starting the project with minimal confusion.
