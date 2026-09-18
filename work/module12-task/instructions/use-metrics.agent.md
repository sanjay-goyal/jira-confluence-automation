# Use Sprint Metrics Tool

- Use this instruction when a task requires sprint summary metrics from a list of issue records.
- Use `./tools/Metrics.py` to compute committed points, completed points, remaining points, completion percentage, created/resolved/active/blocked counts, and trend direction.
- Run the script with either a JSON file or a raw JSON array.
- Command examples:
  + `python ./tools/Metrics.py --issues-file ./sample_issues.json`
  + `python ./tools/Metrics.py --issues-json "[{\"status\":\"Done\",\"story_points\":8}]"`
- Input requirements:
  + The JSON payload must be a list of issue objects.
  + Each issue should include at least: `status` and `story_points`.
  + Missing or invalid story points are treated as 0.0 to keep the analysis stable.
  + Only issue records from the active sprint should be passed into the script.
- Processing behavior:
  + Filter to the active sprint before calculating metrics.
  + Sum story points for committed and completed work.
  + Compute remaining points as committed minus completed.
  + Compute completion percentage as completed / committed, capped safely between 0 and 100.
  + Count issues in created, resolved, active, and blocked states.
  + Report a trend direction of `ahead`, `behind`, or `neutral` based on the relative completion level.
- Output rules:
  + Print the results as JSON.
  + Keep the output concise and structured for dashboard or reporting use.
  + Use the returned values directly in UI or status reporting tasks.
- Constraints:
  + Do not infer unsupported values.
  + Do not pass non-array data to the script.
  + Do not include narrative text in the output if the goal is machine-readable metrics.
  + If no valid issues are supplied, return zeroed metrics rather than crashing.
