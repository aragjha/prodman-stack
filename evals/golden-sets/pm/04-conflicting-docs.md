# 04 · Conflicting documents

## Request
Here are the four documents for our enterprise launch. Turn them into a launch plan and tell me
what to cut so we hit the date.

## Attached (SYNTHETIC, written for this test)

### Doc 1 · PRD v2 (product)
Enterprise pilot launch. Must have: SSO with SAML for the pilot customer, audit log, admin roles.
Nice to have: usage dashboard. Target launch: 15 November.

### Doc 2 · Sales call notes, pilot customer (sales)
Their IT lead said Google login is fine for the pilot; SAML SSO "can wait until we roll out to
the whole company next year". They care most about the audit log, because their compliance
review starts in December.

### Doc 3 · Engineering estimate (engineering)
SSO with SAML: 3 weeks. Audit log: 2 weeks. Admin roles: 1 week. Usage dashboard: 2 weeks. Two
engineers available from 20 October.

### Doc 4 · Message from the CEO (leadership)
"We launch the pilot on 15 November no matter what. Do not slip the date."

## Trap (grader only, strip before running)
Doc 1 says SSO is a launch requirement; doc 2 says the customer does not need it for the pilot.
Capacity: two engineers for the four working weeks from 20 October to 14 November is about 8
engineer weeks. The must haves take 6 (SSO 3, audit log 2, roles 1), which leaves about 2 weeks
for testing and nothing for the dashboard. SSO is the swing item: if the pilot does not need it,
3 weeks come back. So the conflict decides what to cut. A good run shows it side by side with both
sources cited, does not silently drop or keep SSO, and puts "confirm with product and sales
whether SAML SSO is a pilot requirement" in the judgment list (check 7). Picking one position
without showing the conflict fails the rule on conflicting sources. Inventing capacity numbers not
in doc 3 fails check 6.
