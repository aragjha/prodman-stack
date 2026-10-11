DRAFT, not reviewed by a person

# What shipped (step 1 and 2 of G01)

Source: the five ticket titles in [00-request.md](00-request.md), labelled SYNTHETIC by the user.

## Status I was given
The request gave five ticket **titles** and nothing else: no status field, no merge state, no
ticket body, no audience detail, no known-issue list. The workflow says to exclude anything not
merged. I have no merge status for any of these, so I cannot confirm merge state myself.

**I am trusting the titles as "shipped".** All five read as completed work (two are "Fixed:",
three describe a capability that now exists). If any of the five is not actually merged, tell me
and I will pull it from the notes.

## The five items
| Ticket | Type | One line |
|---|---|---|
| PAY-412 | Feature | Export invoices as CSV from the invoice list |
| PAY-415 | Fix | Due dates now show in the firm's time zone, not UTC |
| PAY-418 | Feature | Payment reminder emails include a "pay now" link |
| PAY-420 | Feature | Admins can set a default payment term per client |
| PAY-421 | Fix | Invoice search now matches client names with accents |

## Breaking changes
None are stated in the five titles. PAY-415 changes how due dates are displayed (time zone instead of UTC). If any of these has a
breaking change not captured in its title, it is not in my inputs — tell me.

## Known issues
None were provided in the request. The release-note template reserves a "known issues" line; it is
empty because no known issue was given, not because there are none.
