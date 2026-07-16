# Compact Homepage Design

## Goal

Shorten the public homepage by removing the visible per-report archive rows between the date selector and paper search.

## Scope

- Keep the separate year, month, and day selectors.
- Keep the paper-distribution dialog and complete-report link.
- Keep title and author search across all eligible reports.
- Keep all report metadata and archived report HTML files available to the selector and search index.
- Remove the generated report-row list, its rendering helper, and its dedicated CSS.
- Let the search area follow the date controls with restrained spacing and a divider.

## Behavior

The newest report remains selected by default. A reader can choose another date and open its distribution dialog, then enter the complete report. No individual report rows appear on the homepage.

## Verification

- Unit tests assert that date controls and search remain present while archive-row markup is absent.
- Browser checks assert zero report rows, correct default date, a working distribution dialog, working author/title search, and no horizontal overflow on desktop or mobile.
- The rebuilt public site is visually inspected before publication.

## Non-goals

- No report files or metadata are deleted.
- No changes are made to report content, inclusion rules, sorting, or the daily publishing workflow.
