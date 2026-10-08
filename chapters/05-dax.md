# 🟢 DAX
[← Study hub](../README.md) · [Shared case](../CASE_STUDY.md) · [Cheat sheet](../CHEAT_SHEET.md)

> [!TIP]
> All applications refer to fictional PayBridge. These are proposed approaches, not claims of real employment or completed project work. Expand the answer after attempting the question.

<a id="pbi-051"></a>
## PBI-051 · What DAX does

**Interview question**

Explain what is DAX?

<details>
<summary><strong>💡 Answer + PayBridge business scenario</strong></summary>

### Clear answer

DAX defines measures, calculated columns and calculated tables in supported analytical models. Its results depend on relationships and evaluation context. Use Power Query or upstream processing for data preparation; use DAX for contextual model calculations.

### Applied example

```dax
Attempt Count = COUNTROWS(FactAttempt)

Failed Attempts =
CALCULATE([Attempt Count], KEEPFILTERS(FactAttempt[Status] = "Failed"))

Failure Rate = DIVIDE([Failed Attempts], [Attempt Count])
```

Use the schema and relationships in [CASE_STUDY.md](../CASE_STUDY.md). DAX/M examples are reviewed teaching patterns; they were not executed in a Power BI engine here.

### 🧑‍💼 Same case: PayBridge

**Situation:** Operations needs an attempt-based success rate that changes with country and date selections.

**My BA approach:** Define numerator and denominator as reusable measures over FactAttempt.

**What I validate:** Test overall and sliced rates against independently counted attempts.

**Decision supported:** Provide consistent, interactive payment KPIs.

**Interview-ready response**

> “At fictional PayBridge, I would define numerator and denominator as reusable measures over FactAttempt. I would test overall and sliced rates against independently counted attempts. This would help the team provide consistent, interactive payment KPIs.”

</details>

---

<a id="pbi-052"></a>
## PBI-052 · CALCULATE

**Interview question**

Explain CALCULATE function in DAX.

<details>
<summary><strong>💡 Answer + PayBridge business scenario</strong></summary>

### Clear answer

CALCULATE evaluates a scalar expression in modified filter context. Filter arguments can replace filters on the same columns; KEEPFILTERS can intersect them instead. CALCULATE without explicit filters can perform context transition when row context exists.

### Applied example

```dax
Successful Attempts =
CALCULATE([Attempt Count], KEEPFILTERS(FactAttempt[Status] = "Succeeded"))
```

Use the schema and relationships in [CASE_STUDY.md](../CASE_STUDY.md). DAX/M examples are reviewed teaching patterns; they were not executed in a Power BI engine here.

### 🧑‍💼 Same case: PayBridge

**Situation:** The report needs successful attempts within the user's current scope.

**My BA approach:** Apply the Succeeded condition deliberately, preserving compatible selections with KEEPFILTERS.

**What I validate:** Test selected dates, countries and contradictory status filters.

**Decision supported:** Avoid misleading success counts caused by accidental filter replacement.

**Interview-ready response**

> “At fictional PayBridge, I would apply the Succeeded condition deliberately, preserving compatible selections with KEEPFILTERS. I would test selected dates, countries and contradictory status filters. This would help the team avoid misleading success counts caused by accidental filter replacement.”

</details>

---

<a id="pbi-053"></a>
## PBI-053 · SUM versus SUMX

**Interview question**

Differentiate between Sum() and SUMX()

<details>
<summary><strong>💡 Answer + PayBridge business scenario</strong></summary>

### Clear answer

SUM adds one numeric column. SUMX evaluates an expression for each row of a table and adds the results. Use the iterator when row-level arithmetic is needed; do not add it to a simple column sum without a reason.

### Applied example

```dax
Fee Revenue INR =
SUMX(
    FILTER(FactAttempt, FactAttempt[Status] = "Succeeded"),
    FactAttempt[AmountINR] * FactAttempt[FeeRate]
)
```

Use the schema and relationships in [CASE_STUDY.md](../CASE_STUDY.md). DAX/M examples are reviewed teaching patterns; they were not executed in a Power BI engine here.

### 🧑‍💼 Same case: PayBridge

**Situation:** Finance needs fee revenue calculated from each successful amount and its fee rate.

**My BA approach:** Use SUMX over qualifying attempts when the per-row fee is not already supplied upstream.

**What I validate:** Check rates, rounding and the successful-payment population.

**Decision supported:** Calculate fees at the correct grain.

**Interview-ready response**

> “At fictional PayBridge, I would use SUMX over qualifying attempts when the per-row fee is not already supplied upstream. I would check rates, rounding and the successful-payment population. This would help the team calculate fees at the correct grain.”

</details>

---

<a id="pbi-054"></a>
## PBI-054 · DISTINCT versus VALUES

**Interview question**

Difference between DISTINCT() and VALUES()

<details>
<summary><strong>💡 Answer + PayBridge business scenario</strong></summary>

### Clear answer

Both can return distinct column values. VALUES can include an additional blank member associated with invalid relationship keys; DISTINCT does not add that relationship-violation blank. Their table argument behaviour also differs. Investigate unknown members rather than hiding them automatically.

### Applied example

```dax
EVALUATE VALUES(DimMerchant[MerchantKey])
-- Compare in a separate query with:
-- EVALUATE DISTINCT(DimMerchant[MerchantKey])
```

Use the schema and relationships in [CASE_STUDY.md](../CASE_STUDY.md). DAX/M examples are reviewed teaching patterns; they were not executed in a Power BI engine here.

### 🧑‍💼 Same case: PayBridge

**Situation:** The merchant selector includes an unexpected blank.

**My BA approach:** Check orphan MerchantKey values and compare the dimension's values with source keys.

**What I validate:** Trace missing reference records and any real blank values.

**Decision supported:** Repair mapping issues instead of concealing them.

**Interview-ready response**

> “At fictional PayBridge, I would check orphan MerchantKey values and compare the dimension's values with source keys. I would trace missing reference records and any real blank values. This would help the team repair mapping issues instead of concealing them.”

</details>

---

<a id="pbi-055"></a>
## PBI-055 · Basic DAX toolkit

**Interview question**

What are some of the most common, basic DAX Functions you use or have used?

<details>
<summary><strong>💡 Answer + PayBridge business scenario</strong></summary>

### Clear answer

Common tools include SUM, COUNTROWS, DISTINCTCOUNT, CALCULATE, DIVIDE, IF, COALESCE and date functions. Choose functions from the metric definition; for example, attempts and logical payments require different counting rules.

### Applied example

```dax
Attempt Count = COUNTROWS(FactAttempt)

Failed Attempts =
CALCULATE([Attempt Count], KEEPFILTERS(FactAttempt[Status] = "Failed"))

Failure Rate = DIVIDE([Failed Attempts], [Attempt Count])
```

Use the schema and relationships in [CASE_STUDY.md](../CASE_STUDY.md). DAX/M examples are reviewed teaching patterns; they were not executed in a Power BI engine here.

### 🧑‍💼 Same case: PayBridge

**Situation:** Managers need attempts, successful amount and success rate.

**My BA approach:** Define reusable measures and document whether retries belong in each KPI.

**What I validate:** Reconcile counts and test empty selections.

**Decision supported:** Avoid mixing attempt volume with successful-payment value.

**Interview-ready response**

> “At fictional PayBridge, I would define reusable measures and document whether retries belong in each KPI. I would reconcile counts and test empty selections. This would help the team avoid mixing attempt volume with successful-payment value.”

</details>

---

<a id="pbi-056"></a>
## PBI-056 · FILTER

**Interview question**

How is the FILTER function used?

<details>
<summary><strong>💡 Answer + PayBridge business scenario</strong></summary>

### Clear answer

FILTER returns rows of a table for which its row-wise predicate is true. It is useful for conditions involving several columns or a measure evaluated per entity. For a simple supported column condition inside CALCULATE, a direct Boolean filter is often clearer and more efficient.

### Applied example

```dax
Late Settlements =
COUNTROWS(
    FILTER(
        FactSettlement,
        NOT ISBLANK(FactSettlement[SettlementDate])
            && FactSettlement[SettlementDate] > FactSettlement[DueDate]
    )
)
```

Use the schema and relationships in [CASE_STUDY.md](../CASE_STUDY.md). DAX/M examples are reviewed teaching patterns; they were not executed in a Power BI engine here.

### 🧑‍💼 Same case: PayBridge

**Situation:** Finance needs settled payments whose actual date exceeds their contractual due date.

**My BA approach:** Filter FactSettlement with the agreed two-column late rule.

**What I validate:** Test equal dates, early dates and missing actual dates separately.

**Decision supported:** Identify actual late settlements without treating unsettled payments as already late-settled.

**Interview-ready response**

> “At fictional PayBridge, I would filter FactSettlement with the agreed two-column late rule. I would test equal dates, early dates and missing actual dates separately. This would help the team identify actual late settlements without treating unsettled payments as already late-settled.”

</details>

---

<a id="pbi-057"></a>
## PBI-057 · Grouping with DAX

**Interview question**

What is the common table function for grouping data? Describe some examples of GROUP BY like queries via DAX.

<details>
<summary><strong>💡 Answer + PayBridge business scenario</strong></summary>

### Clear answer

SUMMARIZE, SUMMARIZECOLUMNS and GROUPBY serve different grouping tasks. A DAX query can group by dimensions and evaluate measures, but it is not a literal SQL GROUP BY translation in every context. Use the proper function for the expression and engine version.

### Applied example

```dax
EVALUATE
SUMMARIZECOLUMNS(
    DimCountry[Country],
    "SuccessfulAmountINR", [Successful Amount INR]
)
```

Use the schema and relationships in [CASE_STUDY.md](../CASE_STUDY.md). DAX/M examples are reviewed teaching patterns; they were not executed in a Power BI engine here.

### 🧑‍💼 Same case: PayBridge

**Situation:** A reviewer wants successful amounts by country.

**My BA approach:** Run a grouped DAX query using the model's approved amount measure.

**What I validate:** Compare groups and totals with an independent source aggregation.

**Decision supported:** Validate geographic rollups before publication.

**Interview-ready response**

> “At fictional PayBridge, I would run a grouped DAX query using the model's approved amount measure. I would compare groups and totals with an independent source aggregation. This would help the team validate geographic rollups before publication.”

</details>

---

<a id="pbi-058"></a>
## PBI-058 · Variables in DAX

**Interview question**

What are some benefits and use cases of using variables in DAX?

<details>
<summary><strong>💡 Answer + PayBridge business scenario</strong></summary>

### Clear answer

VAR names an intermediate result evaluated in the context where it is defined. It improves readability and can avoid repeated evaluation. A variable does not automatically recalculate when used inside a later changed filter context, so declare it at the intended scope.

### Applied example

```dax
Successful Amount YoY Growth =
VAR CurrentAmount = [Successful Amount INR]
VAR PriorAmount = CALCULATE([Successful Amount INR], SAMEPERIODLASTYEAR(DimDate[Date]))
RETURN DIVIDE(CurrentAmount - PriorAmount, PriorAmount)
```

Use the schema and relationships in [CASE_STUDY.md](../CASE_STUDY.md). DAX/M examples are reviewed teaching patterns; they were not executed in a Power BI engine here.

### 🧑‍💼 Same case: PayBridge

**Situation:** A growth KPI needs current and prior-year successful amount.

**My BA approach:** Calculate both at explicit scopes and use DIVIDE for the change rate.

**What I validate:** Test prior-year zero, blank and filtered dates.

**Decision supported:** Make the growth definition easier to review.

**Interview-ready response**

> “At fictional PayBridge, I would calculate both at explicit scopes and use DIVIDE for the change rate. I would test prior-year zero, blank and filtered dates. This would help the team make the growth definition easier to review.”

</details>

---

<a id="pbi-059"></a>
## PBI-059 · Bidirectional relationships

**Interview question**

What is bi-directional cross filtering in Power BI?

<details>
<summary><strong>💡 Answer + PayBridge business scenario</strong></summary>

### Clear answer

Bidirectional relationship filtering allows propagation in both directions on a relationship, which can create ambiguity, unexpected populations and extra work. Use it only for a demonstrated requirement and test security paths separately. Visual cross highlighting is a different feature.

### 🧑‍💼 Same case: PayBridge

**Situation:** A proposed bridge should filter attempts by a merchant's multiple business segments.

**My BA approach:** Design a controlled bridge path and compare it with simpler alternatives before enabling both-direction filtering.

**What I validate:** Check multi-segment totals, duplicate attribution and RLS separately.

**Decision supported:** Support segmentation without corrupting counts or access rules.

**Interview-ready response**

> “At fictional PayBridge, I would design a controlled bridge path and compare it with simpler alternatives before enabling both-direction filtering. I would check multi-segment totals, duplicate attribution and RLS separately. This would help the team support segmentation without corrupting counts or access rules.”

</details>

---

<a id="pbi-060"></a>
## PBI-060 · Why CALCULATE matters

**Interview question**

Why do we use CALCULATE?

<details>
<summary><strong>💡 Answer + PayBridge business scenario</strong></summary>

### Clear answer

CALCULATE changes the conditions under which a measure is evaluated. It enables status-specific KPIs, shares of totals and other context-dependent calculations. The useful explanation is the changed business population, not merely the function syntax.

### Applied example

```dax
Attempt Count = COUNTROWS(FactAttempt)

Failed Attempts =
CALCULATE([Attempt Count], KEEPFILTERS(FactAttempt[Status] = "Failed"))

Failure Rate = DIVIDE([Failed Attempts], [Attempt Count])
```

Use the schema and relationships in [CASE_STUDY.md](../CASE_STUDY.md). DAX/M examples are reviewed teaching patterns; they were not executed in a Power BI engine here.

### 🧑‍💼 Same case: PayBridge

**Situation:** Operations compares failed attempts with all eligible attempts.

**My BA approach:** Create explicit failed and overall counts and agree how status selections should behave.

**What I validate:** Verify date, channel and country scope stays aligned.

**Decision supported:** Report an interpretable failure rate.

**Interview-ready response**

> “At fictional PayBridge, I would create explicit failed and overall counts and agree how status selections should behave. I would verify date, channel and country scope stays aligned. This would help the team report an interpretable failure rate.”

</details>

---

<a id="pbi-061"></a>
## PBI-061 · CALCULATE and CALCULATETABLE

**Interview question**

What is a CALCULATE & CALCULATE TABLE?

<details>
<summary><strong>💡 Answer + PayBridge business scenario</strong></summary>

### Clear answer

CALCULATE returns a scalar result; CALCULATETABLE returns a table result. Both modify filter context under their filter arguments. A returned virtual table is not automatically a persisted calculated table.

### Applied example

```dax
-- Virtual table in a DAX query; not a slicer-responsive stored calculated table.
EVALUATE
CALCULATETABLE(FactAttempt, KEEPFILTERS(FactAttempt[Status] = "Failed"))
```

Use the schema and relationships in [CASE_STUDY.md](../CASE_STUDY.md). DAX/M examples are reviewed teaching patterns; they were not executed in a Power BI engine here.

### 🧑‍💼 Same case: PayBridge

**Situation:** One task needs a failure count; another needs the failed rows for analysis.

**My BA approach:** Use a scalar measure for the KPI and a table expression for the investigation query.

**What I validate:** Check the rows and count refer to the same population.

**Decision supported:** Keep exception details aligned with their headline KPI.

**Interview-ready response**

> “At fictional PayBridge, I would use a scalar measure for the KPI and a table expression for the investigation query. I would check the rows and count refer to the same population. This would help the team keep exception details aligned with their headline KPI.”

</details>

---

<a id="pbi-062"></a>
## PBI-062 · ALL, ALLEXCEPT and denominator scope

**Interview question**

What are the ALL & ALL EXCEPT DAX functions?

<details>
<summary><strong>💡 Answer + PayBridge business scenario</strong></summary>

### Clear answer

ALL can return unfiltered values or remove filters in appropriate contexts. ALLEXCEPT removes filters from a table except specified columns. REMOVEFILTERS expresses filter removal clearly. Choose the exact scope; broader table removal can discard filters you intended to keep.

### Applied example

```dax
Country Share of All =
DIVIDE(
    [Successful Amount INR],
    CALCULATE([Successful Amount INR], REMOVEFILTERS(DimCountry))
)
-- Date/channel/merchant context and RLS remain.
-- A separate merchant restriction can still restrict the denominator.
-- Use this report layout with DimCountry for geographic slicing.
```

Use the schema and relationships in [CASE_STUDY.md](../CASE_STUDY.md). DAX/M examples are reviewed teaching patterns; they were not executed in a Power BI engine here.

### 🧑‍💼 Same case: PayBridge

**Situation:** A country row needs its share of successful amount within the selected period.

**My BA approach:** Remove country filtering only in the denominator and retain date and other intended context.

**What I validate:** Check shares add to 100 percent for the defined denominator and distinguish selected-total from all-country total.

**Decision supported:** Make share-of-total comparisons explicit.

**Interview-ready response**

> “At fictional PayBridge, I would remove country filtering only in the denominator and retain date and other intended context. I would check shares add to 100 percent for the defined denominator and distinguish selected-total from all-country total. This would help the team make share-of-total comparisons explicit.”

</details>

---

<a id="pbi-063"></a>
## PBI-063 · TOTALYTD

**Interview question**

What is TOTALYTD?

<details>
<summary><strong>💡 Answer + PayBridge business scenario</strong></summary>

### Clear answer

TOTALYTD evaluates an expression over the year-to-date period in the current date context. For the classic date-column pattern, use a properly configured complete date table and an agreed year-end convention. YTD is not an automatic financial-year definition.

### Applied example

```dax
Successful Amount YTD = TOTALYTD([Successful Amount INR], DimDate[Date])
```

Use the schema and relationships in [CASE_STUDY.md](../CASE_STUDY.md). DAX/M examples are reviewed teaching patterns; they were not executed in a Power BI engine here.

### 🧑‍💼 Same case: PayBridge

**Situation:** Finance monitors successful payment value accumulated this calendar year.

**My BA approach:** Use the active attempt-date relationship and document that the metric refers to successful attempt dates.

**What I validate:** Check January reset, partial-year periods and prior-year dates.

**Decision supported:** Provide an agreed cumulative view.

**Interview-ready response**

> “At fictional PayBridge, I would use the active attempt-date relationship and document that the metric refers to successful attempt dates. I would check January reset, partial-year periods and prior-year dates. This would help the team provide an agreed cumulative view.”

</details>

---

<a id="pbi-064"></a>
## PBI-064 · Time-intelligence tools

**Interview question**

In time intelligence functions which are all DAX functions you have used?

<details>
<summary><strong>💡 Answer + PayBridge business scenario</strong></summary>

### Clear answer

DATEADD, SAMEPERIODLASTYEAR, DATESYTD and DATESINPERIOD support common comparisons and windows, subject to date-table and function requirements. Distinguish a selected date set from a complete calendar period. Mention only functions you actually used when describing experience.

### Applied example

```dax
Previous Month Successful Amount =
CALCULATE([Successful Amount INR], DATEADD(DimDate[Date], -1, MONTH))
```

Use the schema and relationships in [CASE_STUDY.md](../CASE_STUDY.md). DAX/M examples are reviewed teaching patterns; they were not executed in a Power BI engine here.

### 🧑‍💼 Same case: PayBridge

**Situation:** Operations compares this month's failures with the prior month.

**My BA approach:** Choose a shift or complete-period comparison matching the stakeholder's question.

**What I validate:** Test partial-month selections, empty periods and the reporting cut-off.

**Decision supported:** Avoid comparing incompatible periods.

**Interview-ready response**

> “At fictional PayBridge, I would choose a shift or complete-period comparison matching the stakeholder's question. I would test partial-month selections, empty periods and the reporting cut-off. This would help the team avoid comparing incompatible periods.”

</details>

---

<a id="pbi-065"></a>
## PBI-065 · Previous-year YTD

**Interview question**

How can you calculate the previous year's YTD?

<details>
<summary><strong>💡 Answer + PayBridge business scenario</strong></summary>

### Clear answer

Evaluate the YTD measure in a prior-year shifted date context, using a valid calendar and matching cutoff. The result is prior-year YTD for the corresponding selected endpoint, not necessarily the full previous year. Calendar and fiscal policies must align.

### Applied example

```dax
Successful Amount PY YTD =
CALCULATE([Successful Amount YTD], SAMEPERIODLASTYEAR(DimDate[Date]))
```

Use the schema and relationships in [CASE_STUDY.md](../CASE_STUDY.md). DAX/M examples are reviewed teaching patterns; they were not executed in a Power BI engine here.

### 🧑‍💼 Same case: PayBridge

**Situation:** The finance lead wants like-for-like growth through the selected day.

**My BA approach:** Compare current YTD with the prior-year YTD up to the equivalent period.

**What I validate:** Check the endpoint and confirm leap-day and incomplete-year expectations.

**Decision supported:** Support a fair annual comparison.

**Interview-ready response**

> “At fictional PayBridge, I would compare current YTD with the prior-year YTD up to the equivalent period. I would check the endpoint and confirm leap-day and incomplete-year expectations. This would help the team support a fair annual comparison.”

</details>

---

<a id="pbi-066"></a>
## PBI-066 · LOOKUPVALUE and relationships

**Interview question**

When will you use the LOOKUP function?

<details>
<summary><strong>💡 Answer + PayBridge business scenario</strong></summary>

### Clear answer

The intended DAX function is usually LOOKUPVALUE. It searches for a result matching specified conditions; ambiguous matches require a defined policy. When a suitable relationship exists, RELATED is often clearer in row context. Prefer sound modelling over repeated lookups.

### Applied example

```dax
-- Calculated column; this is current-tier enrichment, not an SCD2 lookup.
MerchantRiskTier = RELATED(DimMerchant[RiskTier])
```

Use the schema and relationships in [CASE_STUDY.md](../CASE_STUDY.md). DAX/M examples are reviewed teaching patterns; they were not executed in a Power BI engine here.

### 🧑‍💼 Same case: PayBridge

**Situation:** An attempt needs its merchant risk tier for a row-level classification.

**My BA approach:** Use a validated merchant relationship and RELATED for the current-tier example.

**What I validate:** Check unique keys and decide whether current or historical tier is required.

**Decision supported:** Avoid ambiguous or historically incorrect enrichment.

**Interview-ready response**

> “At fictional PayBridge, I would use a validated merchant relationship and RELATED for the current-tier example. I would check unique keys and decide whether current or historical tier is required. This would help the team avoid ambiguous or historically incorrect enrichment.”

</details>

---

<a id="pbi-067"></a>
## PBI-067 · Other table functions

**Interview question**

What are other functions used other than SUMMARIZE?

<details>
<summary><strong>💡 Answer + PayBridge business scenario</strong></summary>

### Clear answer

ADDCOLUMNS, SELECTCOLUMNS, FILTER, VALUES, DISTINCT, GROUPBY and SUMMARIZECOLUMNS serve different table-shaping tasks. ADDCOLUMNS extends rows; SELECTCOLUMNS projects columns. GROUPBY uses CURRENTGROUP for supported aggregations and does not imply the same context behaviour as every grouping function.

### Applied example

```dax
EVALUATE
ADDCOLUMNS(
    VALUES(DimMerchant[MerchantKey]),
    "MerchantAttempts", CALCULATE(COUNTROWS(FactAttempt))
)
```

Use the schema and relationships in [CASE_STUDY.md](../CASE_STUDY.md). DAX/M examples are reviewed teaching patterns; they were not executed in a Power BI engine here.

### 🧑‍💼 Same case: PayBridge

**Situation:** A model review needs a virtual merchant table with an approved KPI beside each merchant.

**My BA approach:** Choose table shaping that preserves the intended entity grain and measure context.

**What I validate:** Check one row per merchant and compare results with the report.

**Decision supported:** Make diagnostic tables useful without creating duplicate entities.

**Interview-ready response**

> “At fictional PayBridge, I would choose table shaping that preserves the intended entity grain and measure context. I would check one row per merchant and compare results with the report. This would help the team make diagnostic tables useful without creating duplicate entities.”

</details>

---

<a id="pbi-068"></a>
## PBI-068 · SUMMARIZE versus SUMMARIZECOLUMNS

**Interview question**

Difference between SUMMARIZE & SUMMARIZE COLUMNS?

<details>
<summary><strong>💡 Answer + PayBridge business scenario</strong></summary>

### Clear answer

SUMMARIZE groups a supplied table expression; SUMMARIZECOLUMNS groups model columns and evaluates expressions with its own filter and blank-row rules. Recent engine versions support broader context-transition scenarios, so avoid outdated universal claims that it cannot be used in measures. Function behaviour and model properties still matter.

### Applied example

```dax
EVALUATE
SUMMARIZECOLUMNS(
    DimCountry[Country],
    "SuccessfulAmountINR", [Successful Amount INR]
)
```

Use the schema and relationships in [CASE_STUDY.md](../CASE_STUDY.md). DAX/M examples are reviewed teaching patterns; they were not executed in a Power BI engine here.

### 🧑‍💼 Same case: PayBridge

**Situation:** A DAX query validates successful amounts by country and channel.

**My BA approach:** Use an appropriate grouping query and inspect missing or blank-valued combinations.

**What I validate:** Compare returned groups, totals and current engine behaviour.

**Decision supported:** Validate the query without relying on obsolete restrictions.

**Interview-ready response**

> “At fictional PayBridge, I would use an appropriate grouping query and inspect missing or blank-valued combinations. I would compare returned groups, totals and current engine behaviour. This would help the team validate the query without relying on obsolete restrictions.”

</details>

---

<a id="pbi-069"></a>
## PBI-069 · Dynamic RLS identity functions

**Interview question**

What DAX function have you used other than USERPRINCIPALNAME for dynamic RLS?

<details>
<summary><strong>💡 Answer + PayBridge business scenario</strong></summary>

### Clear answer

USERNAME and USERPRINCIPALNAME provide identity-related values whose format depends on environment and connection scenario. They are not interchangeable everywhere. Use a validated entitlement model and test the actual service identity; do not hard-code undocumented identity assumptions.

### Applied example

```dax
-- RLS rule on DimCountry; UserCountryAccess is a disconnected entitlement table.
-- Create one consumer role; also add the DimMerchant and UserCountryAccess
-- rules documented in CASE_STUDY.md, then test actual Viewer access.
DimCountry[CountryKey] IN
SELECTCOLUMNS(
    FILTER(UserCountryAccess, UserCountryAccess[UPN] = USERPRINCIPALNAME()),
    "AllowedCountryKey", UserCountryAccess[CountryKey]
)
```

Use the schema and relationships in [CASE_STUDY.md](../CASE_STUDY.md). DAX/M examples are reviewed teaching patterns; they were not executed in a Power BI engine here.

### 🧑‍💼 Same case: PayBridge

**Situation:** A manager is authorised for India and Singapore.

**My BA approach:** Map the service identity to both permitted CountryKey values and filter through a tested security path.

**What I validate:** Test multi-country access and an unmapped identity with no entitlement.

**Decision supported:** Apply the intended access rule reliably.

**Interview-ready response**

> “At fictional PayBridge, I would map the service identity to both permitted CountryKey values and filter through a tested security path. I would test multi-country access and an unmapped identity with no entitlement. This would help the team apply the intended access rule reliably.”

</details>

---

<a id="pbi-070"></a>
## PBI-070 · Quick measures

**Interview question**

Difference between Measures & Quick Measures.

<details>
<summary><strong>💡 Answer + PayBridge business scenario</strong></summary>

### Clear answer

Quick measures generate DAX from a guided template; the output is still a measure. Inspect and adapt the generated expression to the business calendar, denominator and model. A template does not validate the requirement for you.

### 🧑‍💼 Same case: PayBridge

**Situation:** A new analyst prototypes a rolling payment KPI.

**My BA approach:** Use generated DAX as a starting point and review it with the metric dictionary.

**What I validate:** Check windows, totals and filter context against a hand-worked fixture.

**Decision supported:** Accelerate authoring without surrendering correctness.

**Interview-ready response**

> “At fictional PayBridge, I would use generated DAX as a starting point and review it with the metric dictionary. I would check windows, totals and filter context against a hand-worked fixture. This would help the team accelerate authoring without surrendering correctness.”

</details>

---

<a id="pbi-071"></a>
## PBI-071 · Complex business logic

**Interview question**

Have you worked with calculated columns and measures that involve complex logic in DAX? Can you provide an example?

<details>
<summary><strong>💡 Answer + PayBridge business scenario</strong></summary>

### Clear answer

Break complex measures into reviewed base measures and variables. Define rule priority, missing values and zero denominators before coding. Separate row classifications from contextual calculations, and explain hypothetical examples as proposals rather than past work.

### Applied example

```dax
Failure Review Flag =
VAR MinimumAttempts = 100
VAR FailureThreshold = 0.05
RETURN
    IF(
        [Attempt Count] < MinimumAttempts,
        "Insufficient volume",
        IF([Failure Rate] > FailureThreshold, "Investigate", "Within threshold")
    )
-- Illustrative policy only; both thresholds require stakeholder approval.
```

Use the schema and relationships in [CASE_STUDY.md](../CASE_STUDY.md). DAX/M examples are reviewed teaching patterns; they were not executed in a Power BI engine here.

### 🧑‍💼 Same case: PayBridge

**Situation:** A failure KPI should ignore channels below a minimum attempt threshold when flagging risk.

**My BA approach:** Build the base counts and rate, then add the approved minimum-volume rule.

**What I validate:** Test threshold boundaries, zero attempts and country slices.

**Decision supported:** Prevent noisy low-volume channels from dominating escalation.

**Interview-ready response**

> “At fictional PayBridge, I would build the base counts and rate, then add the approved minimum-volume rule. I would test threshold boundaries, zero attempts and country slices. This would help the team prevent noisy low-volume channels from dominating escalation.”

</details>

---

<a id="pbi-072"></a>
## PBI-072 · DAX performance

**Interview question**

How do you optimize DAX calculations to improve query performance in Power BI?

<details>
<summary><strong>💡 Answer + PayBridge business scenario</strong></summary>

### Clear answer

Measure slow queries with Performance Analyzer and, where authorised, suitable model/query tools. Improve the model first, simplify unnecessary iterators and filter scope, and reuse clear base measures. No rewrite is guaranteed faster without testing.

### 🧑‍💼 Same case: PayBridge

**Situation:** A country failure-rate visual loads slowly.

**My BA approach:** Capture timings, isolate its measure and compare a revised expression on representative filters.

**What I validate:** Check result equivalence, cold/warm behaviour and peak usage.

**Decision supported:** Improve the experience with measurable evidence.

**Interview-ready response**

> “At fictional PayBridge, I would capture timings, isolate its measure and compare a revised expression on representative filters. I would check result equivalence, cold/warm behaviour and peak usage. This would help the team improve the experience with measurable evidence.”

</details>

---

<a id="pbi-073"></a>
## PBI-073 · Context transition

**Interview question**

Can you explain the concept of context transition in DAX and its implications?

<details>
<summary><strong>💡 Answer + PayBridge business scenario</strong></summary>

### Clear answer

Context transition converts an existing row context into filter context, commonly through CALCULATE or a measure reference evaluated in row context. It matters in iterators and calculated columns. A plain aggregate expression is not automatically filtered by the current row.

### Applied example

```dax
EVALUATE
ADDCOLUMNS(
    VALUES(DimMerchant[MerchantKey]),
    "MerchantAttempts", CALCULATE(COUNTROWS(FactAttempt))
)
```

Use the schema and relationships in [CASE_STUDY.md](../CASE_STUDY.md). DAX/M examples are reviewed teaching patterns; they were not executed in a Power BI engine here.

### 🧑‍💼 Same case: PayBridge

**Situation:** A diagnostic merchant table needs each merchant's own attempt count.

**My BA approach:** Use a measure reference or explicit CALCULATE at the intended row scope.

**What I validate:** Compare per-merchant results with a grouped visual and total counts.

**Decision supported:** Avoid repeating the overall count for every merchant.

**Interview-ready response**

> “At fictional PayBridge, I would use a measure reference or explicit CALCULATE at the intended row scope. I would compare per-merchant results with a grouped visual and total counts. This would help the team avoid repeating the overall count for every merchant.”

</details>

---

<a id="pbi-074"></a>
## PBI-074 · Blank and error handling

**Interview question**

How do you handle error handling and exception scenarios in DAX calculations?

<details>
<summary><strong>💡 Answer + PayBridge business scenario</strong></summary>

### Clear answer

Use DIVIDE for a defined zero/blank-denominator result and IF, ISBLANK or COALESCE according to the metric policy. IFERROR can mask problems if used broadly. Fix source/model errors at their origin and distinguish no data from a true zero.

### Applied example

```dax
Success Rate = DIVIDE([Successful Attempts], [Attempt Count])
-- Format as percentage. BLANK means no eligible denominator here.
-- At the total level it uses total successes / total attempts, not AVG(country rates).
```

Use the schema and relationships in [CASE_STUDY.md](../CASE_STUDY.md). DAX/M examples are reviewed teaching patterns; they were not executed in a Power BI engine here.

### 🧑‍💼 Same case: PayBridge

**Situation:** A new channel has no attempts in the selected month.

**My BA approach:** Return a blank rate with a clear no-data label rather than inventing a zero success rate.

**What I validate:** Test no rows, zero denominator and actual zero successes.

**Decision supported:** Prevent missing data being interpreted as bad performance.

**Interview-ready response**

> “At fictional PayBridge, I would return a blank rate with a clear no-data label rather than inventing a zero success rate. I would test no rows, zero denominator and actual zero successes. This would help the team prevent missing data being interpreted as bad performance.”

</details>

---

<a id="pbi-075"></a>
## PBI-075 · Evaluation context

**Interview question**

Can you explain the concept of evaluation context in DAX and how it impacts calculation results?

<details>
<summary><strong>💡 Answer + PayBridge business scenario</strong></summary>

### Clear answer

Row context identifies the current row in an iterator or calculated column. Filter context describes restrictions from visuals, slicers, filters, relationships and expressions. Measures use their evaluation context; a total is recalculated in total context, not always the sum of visible row results.

### Applied example

```dax
Success Rate = DIVIDE([Successful Attempts], [Attempt Count])
-- Format as percentage. BLANK means no eligible denominator here.
-- At the total level it uses total successes / total attempts, not AVG(country rates).
```

Use the schema and relationships in [CASE_STUDY.md](../CASE_STUDY.md). DAX/M examples are reviewed teaching patterns; they were not executed in a Power BI engine here.

### 🧑‍💼 Same case: PayBridge

**Situation:** Country success rates must have a correct overall total.

**My BA approach:** Calculate the total from overall successful and total attempts rather than averaging country percentages.

**What I validate:** Use countries with unequal attempt counts to expose the difference.

**Decision supported:** Report a properly weighted company-wide rate.

**Interview-ready response**

> “At fictional PayBridge, I would calculate the total from overall successful and total attempts rather than averaging country percentages. I would use countries with unequal attempt counts to expose the difference. This would help the team report a properly weighted company-wide rate.”

</details>

---

<a id="pbi-076"></a>
## PBI-076 · Time-intelligence example

**Interview question**

Have you utilized DAX functions for time intelligence calculations like YEAR-TO-DATE, PREVIOUSYEAR, or SAMEPERIODLASTYEAR? Can you provide an example?

<details>
<summary><strong>💡 Answer + PayBridge business scenario</strong></summary>

### Clear answer

YTD, full prior-year and same-period-prior-year calculations answer different questions. Choose the required period and date role explicitly. A marked complete date table supports the classic patterns used here; future calendar-based options have their own rules.

### Applied example

```dax
Successful Amount YTD = TOTALYTD([Successful Amount INR], DimDate[Date])
```

Use the schema and relationships in [CASE_STUDY.md](../CASE_STUDY.md). DAX/M examples are reviewed teaching patterns; they were not executed in a Power BI engine here.

### 🧑‍💼 Same case: PayBridge

**Situation:** Finance wants both YTD payment value and the corresponding prior-year period.

**My BA approach:** Label the comparison window and use the same successful-amount base measure.

**What I validate:** Check date endpoints and ensure settlement-date measures are not mixed into attempt-date comparisons.

**Decision supported:** Keep time-based conclusions comparable.

**Interview-ready response**

> “At fictional PayBridge, I would label the comparison window and use the same successful-amount base measure. I would check date endpoints and ensure settlement-date measures are not mixed into attempt-date comparisons. This would help the team keep time-based conclusions comparable.”

</details>

---
