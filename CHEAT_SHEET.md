# 🟨 Power BI cheat sheet: PayBridge

[← Study hub](README.md) · [Case and schema](CASE_STUDY.md) · [DAX definitions](practice/measures.dax)

## 🧭 Start with the business rule

| Question | PayBridge answer |
|---|---|
| What decision? | Which failures and late settlements need investigation? |
| What grain? | One attempt per FactAttempt row; one completed payment settlement per FactSettlement row |
| What currency? | INR reporting amounts already prepared under an approved conversion policy |
| What period? | Attempt date for attempt KPIs; actual settlement date for base settlement KPIs |
| What denominator? | Attempts for attempt rates; logical payments for the separately named logical-payment rate |
| What access? | Country entitlements for consumer identities, enforced and tested through RLS |

## 🛠️ Power Query

| Feature | Use in the case | Check |
|---|---|---|
| Folding | Push supported date filtering to SQL | Inspect query/source behaviour; not every step or connector folds |
| M | Prepare types and approved status mappings | M prepares data; DAX calculates model expressions |
| Append | Combine compatible monthly extracts | Duplicate AttemptID and schema differences |
| Merge | Add unique reference attributes | Keys, join kind and row multiplication |
| Parameter | Configure source/environment/date boundaries | Not automatically a report slicer |
| Function | Reuse a normalisation rule | Unknown inputs and folding/row-by-row costs |
| Types/profile | Convert and inspect incoming fields | Locale, errors, nulls and whole-dataset profiling scope |
| Credentials | Authorised source/service connection | Identity, privacy and gateway mapping; no embedded secrets |

Incremental refresh uses the case-sensitive RangeStart and RangeEnd DateTime parameters in supported policies. Use an inclusive start and exclusive end, verify folding/source handling and account for late updates. Its real-time options and availability depend on platform and licensing.

## 🏗️ Model design

| Choice | Reminder |
|---|---|
| Star schema | Dimensions filter facts through intentional paths |
| One-to-many | Validate a unique one-side key and compatible types |
| Single direction | Default to clear dimension-to-fact filtering |
| Many-to-many | Establish a real business mapping and attribution policy first |
| Calculated column | Row attribute for grouping, filtering or stable classification |
| Measure | Contextual aggregation/KPI that responds to the report's filters |
| Calculated table | Materialised model structure; not recalculated by every slicer click |
| Role-playing dates | State attempt, actual settlement and due-date roles explicitly |
| SCD Type 2 | Preserve versions and map facts to event-time keys upstream |
| Source indexes | SQL tuning concepts; do not create them on Power BI visual fields |

Avoid fact-to-fact joins that multiply attempt and settlement records. Hide technical keys from ordinary report navigation where appropriate without treating hidden fields as a security measure.

## 🧮 Core DAX patterns

```dax
Attempt Count = COUNTROWS(FactAttempt)

Successful Attempts =
CALCULATE([Attempt Count], KEEPFILTERS(FactAttempt[Status] = "Succeeded"))

Success Rate = DIVIDE([Successful Attempts], [Attempt Count])

Successful Amount INR =
CALCULATE(SUM(FactAttempt[AmountINR]), KEEPFILTERS(FactAttempt[Status] = "Succeeded"))
```

These are separate measure definitions. Format Success Rate as percentage. KEEPFILTERS intersects the status condition with existing compatible context; contradictory status selections should not silently redefine the KPI. Configure rate visual scope deliberately.

| Function/concept | What to say | PayBridge use |
|---|---|---|
| SUM | Add a numeric column | Successful reporting amount |
| SUMX | Evaluate and add an expression per row | Amount × fee rate for qualifying attempts |
| CALCULATE | Evaluate a scalar in modified filter context | Status-specific counts and comparison denominators |
| CALCULATETABLE | Evaluate a table in modified context | A virtual failed-attempt population |
| FILTER | Return rows satisfying a row-wise predicate | Actual settlement date later than due date |
| DIVIDE | Handle zero/blank denominator under a chosen policy | Success/failure rates |
| VAR | Name intermediate results at their definition context | Current/prior amount comparison |
| VALUES | Distinct column values, potentially an unknown blank member | Investigating orphan merchant keys |
| DISTINCTCOUNT | Count distinct values under current scope | Logical payments; validate blank IDs first |
| RELATED | Read a value through an appropriate relationship in row context | Current merchant tier enrichment |
| LOOKUPVALUE | Search by explicit conditions | A justified lookup when a suitable relationship is unavailable |
| SUMMARIZE / SUMMARIZECOLUMNS | Group tables/model columns with distinct semantics | Country/channel validation queries |
| ADDCOLUMNS | Extend a table with expressions | Diagnostic per-merchant KPI table |
| REMOVEFILTERS | Remove the specified report filter scope | Country denominator retaining date context |
| ALLSELECTED | Work with the relevant outer/selected scope | Share among selected countries |
| ALLEXCEPT | Remove table filters except specified columns | A carefully defined preserved grouping scope |
| USERELATIONSHIP | Activate a defined relationship for a calculation | Settlement amount analysed by DueDate |

A total measure is recalculated in total context. The overall success rate is total successes ÷ total attempts, not the average of country rates.

## 📅 Time intelligence

```dax
Successful Amount YTD = TOTALYTD([Successful Amount INR], DimDate[Date])

Successful Amount PY YTD =
CALCULATE([Successful Amount YTD], SAMEPERIODLASTYEAR(DimDate[Date]))
```

For the classic patterns used here, configure a complete marked date table and the intended active relationship. DATEADD shifts a selected date set; PARALLELPERIOD returns complete periods at the requested granularity for the classic date-column overload. Date selection and newer calendar-based variants can change behaviour; test the exact pattern.

A fixed April metric needs an explicit year. A rolling 24-month visual needs an agreed anchor, exact displayed month set and a visible policy for incomplete or missing periods. The tiny fixture is not evidence of 24 months of production history.

## 🎛️ Report interactions

| Feature | PayBridge example | Main distinction |
|---|---|---|
| Filters | Date/page investigation scope | Report, page and visual levels |
| Slicer | User chooses country | Visible interaction, not security |
| Edit interactions | Preserve a global benchmark beside local detail | Does not erase other filters or RLS |
| Sync slicers | Country selection follows navigation | Hidden synced selections can still filter |
| Bookmark | Switch summary/detail panels | Data-state capture can reset selections |
| Field parameter | Choose count or rate | Titles and units must change consistently |
| Drillthrough | Open a merchant investigation page | Not the same as drilldown within a hierarchy |
| Page navigation | Home button | Does not need a bookmark for simple navigation |
| Conditional formatting | Flag an approved high-failure condition | Threshold, minimum volume and accessible label |
| Top N | Prioritise largest failure workloads | Measure, ties and denominator scope |

A dashboard is a service tile canvas; a report is a multi-page analytical experience. If two visuals must appear in one service tile, evaluate a supported live-page pin instead of assuming an ordinary tile can combine independent visuals.

## ☁️ Service and connectivity

| Area | Reminder |
|---|---|
| Import | Stored model data and refresh; often strong interactive performance |
| DirectQuery | Source queries at report time; source load, latency and caching matter |
| Live connection | Reuse an existing semantic model/Analysis Services model |
| Composite / Dual | Supported combinations; inspect restrictions and relationship behaviour |
| Direct Lake | Fabric-specific storage option; not simply a synonym for DirectQuery |
| Gateway | Choose the supported network/connectivity option for the source |
| Licensing | Distinguish per-user licences from capacity; verify current viewer/author requirements |
| RLS | Enforce row access for consumer identities and test actual service roles |
| Alerts | Supported dashboard tiles or separately configured newer alerting options; evaluation is not every transaction |
| Refresh | Gate on completed source loads; monitor credentials, mappings, history and freshness |
| Embedding | Authenticated architecture and effective identity; publish-to-web exposes public data |

Do not use Publish to web for payment data. Do not infer RLS protection from a country slicer or a hidden page. Report filters and REMOVEFILTERS do not override model RLS.

## ✅ Analyst validation

1. Agree metric definitions and compare attempt-based vs payment-based counts.
2. Validate keys, orphan records, types and the approved status mapping.
3. Reconcile counts and amounts by period and entity, not only a grand total.
4. Test relationship paths, denominators, blank selections and date boundaries.
5. Test allowed, denied and unmapped access with consumer identities.
6. Measure refresh and response targets; expose incomplete data and stale sources.
7. Regression-test approved changes through QA/UAT before release.

DAX/M patterns are reviewed examples. The independent fixture checks validate expected arithmetic, not execution in Power BI. See the [Desktop and service checklist](practice/README.md).
