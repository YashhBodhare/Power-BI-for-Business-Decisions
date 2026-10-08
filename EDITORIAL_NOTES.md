# 🛡️ Technical review and verification scope

[← Study hub](README.md)

The source is a July 2023 question list. Answers were newly written and version-sensitive claims checked against official Microsoft documentation in October 2026. UI availability, licensing and connector capabilities must still be confirmed for the actual tenant and product version.

## Important clarifications

| Topic | Interpretation in this guide | Official reference |
|---|---|---|
| Power Query folding | Supported transformations may run at the source; folding can be full, partial or absent. | [Folding](https://learn.microsoft.com/en-us/power-query/power-query-folding) |
| M and storage | M transformation/mashup evaluation is different from semantic-model storage. | [M reference](https://learn.microsoft.com/en-us/powerquery-m/), [Folding](https://learn.microsoft.com/en-us/power-query/power-query-folding) |
| CALCULATE / CALCULATETABLE / FILTER | DAX functions, even though one source question places them under Power Query. | [CALCULATE](https://learn.microsoft.com/en-us/dax/calculate-function-dax), [CALCULATETABLE](https://learn.microsoft.com/en-us/dax/calculatetable-function-dax), [FILTER](https://learn.microsoft.com/en-us/dax/filter-function-dax) |
| Model design | Explicit grain, validated keys and intentional relationships matter more than a universal performance claim. | [Star schema](https://learn.microsoft.com/en-us/power-bi/guidance/star-schema) |
| Date roles | USERELATIONSHIP requires a defined relationship; the base fixture uses inactive settlement DueDate. | [USERELATIONSHIP](https://learn.microsoft.com/en-us/dax/userelationship-function-dax) |
| VALUES / DISTINCT | VALUES can include the unknown blank associated with relationship violations. | [VALUES](https://learn.microsoft.com/en-us/dax/values-function-dax) |
| SUMMARIZECOLUMNS | Engine support and context rules evolved; do not repeat old universal prohibitions on use in measures. | [SUMMARIZECOLUMNS](https://learn.microsoft.com/en-us/dax/summarizecolumns-function-dax) |
| Date shifting | Selected-date shifts and complete-period shifts differ in the classic date-column examples. | [DATEADD](https://learn.microsoft.com/en-us/dax/dateadd-function-dax), [PARALLELPERIOD](https://learn.microsoft.com/en-us/dax/parallelperiod-function-dax) |
| RLS | Consumer and editing roles differ. Security tests must use the actual consumer path; visual filters are not access control. | [RLS](https://learn.microsoft.com/en-us/fabric/security/service-admin-row-level-security) |
| Licensing | Separate per-user licences and capacity entitlements; no fixed current prices are assumed. | [Fabric licensing](https://learn.microsoft.com/en-us/fabric/enterprise/licenses) |
| Storage choices | Import, DirectQuery, live connection, composite and Direct Lake concepts are related but distinct. | [DirectQuery](https://learn.microsoft.com/en-us/power-bi/connect-data/desktop-directquery-about), [Direct Lake](https://learn.microsoft.com/en-us/fabric/fundamentals/direct-lake-overview) |
| Incremental refresh | RangeStart/RangeEnd, suitable filtering and supported policies matter; it does not fix every slow visual. | [Incremental refresh](https://learn.microsoft.com/en-us/power-bi/connect-data/incremental-refresh-overview) |
| Alerts | Supported classic tile alerts have limits and differ from newer alerting options. | [Service alerts](https://learn.microsoft.com/en-us/power-bi/create-reports/service-set-data-alerts) |
| Two visuals in a tile | Clarify report layout versus a supported live report-page dashboard tile. | [Pin a page](https://learn.microsoft.com/en-us/power-bi/create-reports/service-dashboard-pin-live-tile-from-report) |
| Performance | Measure visual/model/source timings; no universal fixed speedup is promised. | [Performance Analyzer](https://learn.microsoft.com/en-us/power-bi/create-reports/desktop-performance-analyzer) |

The shared case defines all amounts in INR and business-calendar dates. Fees, success rules, settlement grain, fiscal periods, retry handling and incomplete loads need stakeholder agreement before adapting the patterns to actual payment systems.

## Checks completed

- All **97** source entries mapped to unique curated IDs.
- Every entry contains a clear answer, a PayBridge situation, a BA approach, validation and a decision.
- **Eight independent Python checks** passed for fixture arithmetic, keys, rates, amounts, settlements and entitlement expectations.
- Internal file links, anchors, Markdown fences and expandable-answer structure checked.
- Banner rendered and visually inspected.

## Checks not claimed

No Power BI Desktop/service engine was available for execution here. DAX and M were reviewed but **not executed**. Python reference checks do not validate DAX context transition, M connector/folding behaviour, relationship propagation, service refresh or RLS enforcement. The pack provides a checklist to perform those checks in the actual environment.

No PBIX, published report, live connection, production gateway, actual licence or real payment data is represented as created or verified. All added business scenarios are fictional practice material.
