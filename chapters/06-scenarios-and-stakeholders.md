# 🔴 Scenario practice and stakeholder decisions
[← Study hub](../README.md) · [Shared case](../CASE_STUDY.md) · [Cheat sheet](../CHEAT_SHEET.md)

> [!TIP]
> All applications refer to fictional PayBridge. These are proposed approaches, not claims of real employment or completed project work. Expand the answer after attempting the question.

<a id="pbi-077"></a>
## PBI-077 · April amount

**Interview question**

Scenario: There is a sales column. I need to show the sales for April month. What is the DAX expression?

<details>
<summary><strong>💡 Answer + PayBridge business scenario</strong></summary>

### Clear answer

A month name alone can combine multiple years. Filter an explicit date range for the intended April and use the agreed amount measure. Preserve or replace existing date selections deliberately, and use a half-open month boundary when appropriate.

### Applied example

```dax
April 2026 Successful Amount =
CALCULATE(
    [Successful Amount INR],
    REMOVEFILTERS(DimDate),
    DimDate[Date] >= DATE(2026, 4, 1),
    DimDate[Date] < DATE(2026, 5, 1)
)
-- The supplied fixture has no April attempts, so a blank amount is expected.
```

Use the schema and relationships in [CASE_STUDY.md](../CASE_STUDY.md). DAX/M examples are reviewed teaching patterns; they were not executed in a Power BI engine here.

### 🧑‍💼 Same case: PayBridge

**Situation:** Finance requests April 2026 successful payment value.

**My BA approach:** Use a clearly labelled fixed-period calculation that replaces the date filter but retains other intended context.

**What I validate:** Check April 1 and May 1 boundaries and confirm failed attempts are excluded.

**Decision supported:** Answer the specific month request without mixing years.

**Interview-ready response**

> “At fictional PayBridge, I would use a clearly labelled fixed-period calculation that replaces the date filter but retains other intended context. I would check April 1 and May 1 boundaries and confirm failed attempts are excluded. This would help the team answer the specific month request without mixing years.”

</details>

---

<a id="pbi-078"></a>
## PBI-078 · DATEADD versus PARALLELPERIOD

**Interview question**

Scenario: Difference between DATEADD & PARALLELPERIOD DAX functions, explain a case scenario in your project?

<details>
<summary><strong>💡 Answer + PayBridge business scenario</strong></summary>

### Clear answer

For the classic date-column patterns, DATEADD shifts the selected date set; PARALLELPERIOD returns complete periods at the requested granularity. Their results can differ for partial selections. Function overloads and calendar-based variants add nuances, so state the pattern used.

### Applied example

```dax
Shifted Previous Month =
CALCULATE([Successful Amount INR], DATEADD(DimDate[Date], -1, MONTH))

Complete Previous Month =
CALCULATE([Successful Amount INR], PARALLELPERIOD(DimDate[Date], -1, MONTH))
```

Use the schema and relationships in [CASE_STUDY.md](../CASE_STUDY.md). DAX/M examples are reviewed teaching patterns; they were not executed in a Power BI engine here.

### 🧑‍💼 Same case: PayBridge

**Situation:** A manager selects February 10–20 and asks for a prior-month comparison.

**My BA approach:** Ask whether they mean January 10–20 or the entire previous month, then choose the function accordingly.

**What I validate:** Test the partial selection and inspect the resulting date range.

**Decision supported:** Match the comparison to the actual question.

**Interview-ready response**

> “At fictional PayBridge, I would ask whether they mean January 10–20 or the entire previous month, then choose the function accordingly. I would test the partial selection and inspect the resulting date range. This would help the team match the comparison to the actual question.”

</details>

---

<a id="pbi-079"></a>
## PBI-079 · Only two visuals respond

**Interview question**

Scenario: There is a report with 5 visuals & a slicer. If the slicer is changed, only 2 visuals should be affected, and the remaining 3 visuals should not be affected. What will you do?

<details>
<summary><strong>💡 Answer + PayBridge business scenario</strong></summary>

### Clear answer

Use Edit interactions on the slicer to enable filtering for the two intended targets and disable it for the other three. Other context still applies. Explain unaffected visuals with clear scope labels.

### 🧑‍💼 Same case: PayBridge

**Situation:** The country slicer controls failure details but leaves global benchmarks unchanged.

**My BA approach:** Configure the five targets and document the two local and three global scopes.

**What I validate:** Test each visual after a country change and after clearing the slicer.

**Decision supported:** Provide deliberate local-versus-global analysis.

**Interview-ready response**

> “At fictional PayBridge, I would configure the five targets and document the two local and three global scopes. I would test each visual after a country change and after clearing the slicer. This would help the team provide deliberate local-versus-global analysis.”

</details>

---

<a id="pbi-080"></a>
## PBI-080 · Top ten regions

**Interview question**

Scenario: Donut chart is there that is region by volume. I want the top 10 regions by volume. How can I achieve that?

<details>
<summary><strong>💡 Answer + PayBridge business scenario</strong></summary>

### Clear answer

Use a visual-level Top N filter with the approved volume measure, then apply it and sort clearly. Define ties and whether the denominator includes all regions. A bar chart is often easier to compare than ten donut segments.

### 🧑‍💼 Same case: PayBridge

**Situation:** Managers want the countries or regions with the most failed attempts.

**My BA approach:** Rank by failed attempts rather than all attempts and label the chosen measure.

**What I validate:** Check ties, fewer than ten groups and excluded-region totals.

**Decision supported:** Focus investigation on the largest failure workloads.

**Interview-ready response**

> “At fictional PayBridge, I would rank by failed attempts rather than all attempts and label the chosen measure. I would check ties, fewer than ten groups and excluded-region totals. This would help the team focus investigation on the largest failure workloads.”

</details>

---

<a id="pbi-081"></a>
## PBI-081 · A rolling 24-month view

**Interview question**

Scenario: Rolling 24 months. So, volume, net sales & gross profit is there. In that visual (from line & stacked bar chart), you don't want a bar chart. So, what other charts can you use?

<details>
<summary><strong>💡 Answer + PayBridge business scenario</strong></summary>

### Clear answer

Use a line chart, separate aligned panels or small multiples when bars are unsuitable. Measures with different units or scales should not be combined ambiguously. Define the exact window anchor, treatment of incomplete months and displayed calendar coverage.

### 🧑‍💼 Same case: PayBridge

**Situation:** PayBridge tracks attempt count, successful amount and fee revenue over 24 months.

**My BA approach:** Use aligned trend panels with explicit units and a controlled end date.

**What I validate:** Test exactly 24 displayed month labels and identify incomplete or missing periods.

**Decision supported:** Show trends without implying amounts and counts share one scale.

**Interview-ready response**

> “At fictional PayBridge, I would use aligned trend panels with explicit units and a controlled end date. I would test exactly 24 displayed month labels and identify incomplete or missing periods. This would help the team show trends without implying amounts and counts share one scale.”

</details>

---

<a id="pbi-082"></a>
## PBI-082 · Country percentage

**Interview question**

Scenario: 5 countries of data, country-wise sales are there, so need to show sales in percentage-wise. How can you do that?

<details>
<summary><strong>💡 Answer + PayBridge business scenario</strong></summary>

### Clear answer

Divide each country's approved amount by a denominator with the intended country filter removed. ALLSELECTED can answer share within selections; REMOVEFILTERS can answer share of all countries while retaining other context. Format as percentage and name the denominator.

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

**Situation:** The executive page compares country shares of successful INR amount.

**My BA approach:** Use the same successful-amount measure on both sides and retain the selected period.

**What I validate:** Check the denominator and whether visible shares should sum to 100 percent.

**Decision supported:** Provide a defensible geographic contribution view.

**Interview-ready response**

> “At fictional PayBridge, I would use the same successful-amount measure on both sides and retain the selected period. I would check the denominator and whether visible shares should sum to 100 percent. This would help the team provide a defensible geographic contribution view.”

</details>

---

<a id="pbi-083"></a>
## PBI-083 · Two visuals in one tile

**Interview question**

Scenario: 2 visuals are there on page 1. In page 2, I have a tile. How can I bring 2 visuals into a tile?

<details>
<summary><strong>💡 Answer + PayBridge business scenario</strong></summary>

### Clear answer

Clarify whether the request concerns a report page or a service dashboard. A report page can contain multiple visuals; a service live-page tile can pin a supported report page as one tile. An ordinary single-visual tile cannot simply contain two independently pinned visuals.

### 🧑‍💼 Same case: PayBridge

**Situation:** The CEO wants one dashboard tile containing rate and trend.

**My BA approach:** Create a focused report page with the two visuals and evaluate a supported live-page pin.

**What I validate:** Check service behaviour, security and the tile's freshness.

**Decision supported:** Deliver the requested layout using the correct feature.

**Interview-ready response**

> “At fictional PayBridge, I would create a focused report page with the two visuals and evaluate a supported live-page pin. I would check service behaviour, security and the tile's freshness. This would help the team deliver the requested layout using the correct feature.”

</details>

---

<a id="pbi-084"></a>
## PBI-084 · Return to the home page

**Interview question**

Scenario: If there are 5 pages. To come to the home page, which feature will you use?

<details>
<summary><strong>💡 Answer + PayBridge business scenario</strong></summary>

### Clear answer

Use a button with page-navigation action to the home report page, or a navigator where appropriate. Bookmarks are useful when restoring a saved state is required, but simple navigation does not need a bookmark.

### 🧑‍💼 Same case: PayBridge

**Situation:** Analysts need a consistent way back from detail pages.

**My BA approach:** Add a labelled Home button and preserve intentional filter behaviour.

**What I validate:** Test every page and keyboard/accessibility usability.

**Decision supported:** Make the report easy to navigate.

**Interview-ready response**

> “At fictional PayBridge, I would add a labelled Home button and preserve intentional filter behaviour. I would test every page and keyboard/accessibility usability. This would help the team make the report easy to navigate.”

</details>

---

<a id="pbi-085"></a>
## PBI-085 · Detailed information

**Interview question**

Scenario: How will you move/showcase the detailed information by using which feature?

<details>
<summary><strong>💡 Answer + PayBridge business scenario</strong></summary>

### Clear answer

Drillthrough moves to a detail page filtered by selected fields; drilldown explores hierarchy levels within a visual. Tooltips offer lightweight context. Choose from the depth and task, and configure a Back action for the return path.

### 🧑‍💼 Same case: PayBridge

**Situation:** An analyst investigates failures for one merchant.

**My BA approach:** Create a merchant drillthrough page with attempt details and relevant filters.

**What I validate:** Confirm the merchant and intended period carry through and sensitive fields remain restricted.

**Decision supported:** Connect a KPI anomaly to actionable records.

**Interview-ready response**

> “At fictional PayBridge, I would create a merchant drillthrough page with attempt details and relevant filters. I would confirm the merchant and intended period carry through and sensitive fields remain restricted. This would help the team connect a KPI anomaly to actionable records.”

</details>

---

<a id="pbi-086"></a>
## PBI-086 · Visuals not loading

**Interview question**

Scenario: As you said that in your project, visuals are not loading, so how do you fix that?

<details>
<summary><strong>💡 Answer + PayBridge business scenario</strong></summary>

### Clear answer

Check connectivity, permissions, refresh state and errors before treating it as a performance issue. Then inspect visual timings, DAX, relationship complexity and source behaviour. Keep a reproducible failure case and avoid changing multiple variables at once.

### 🧑‍💼 Same case: PayBridge

**Situation:** The failure-detail page is blank for some users.

**My BA approach:** Reproduce with consumer access, inspect security scope and errors, then isolate the affected query.

**What I validate:** Distinguish legitimate no-access/no-data states from technical failures.

**Decision supported:** Resolve the cause instead of hiding the symptom.

**Interview-ready response**

> “At fictional PayBridge, I would reproduce with consumer access, inspect security scope and errors, then isolate the affected query. I would distinguish legitimate no-access/no-data states from technical failures. This would help the team resolve the cause instead of hiding the symptom.”

</details>

---

<a id="pbi-087"></a>
## PBI-087 · Removing filters from a card

**Interview question**

Scenario: In a measure, if you remove the filter, will it give the same data in the card visual?

<details>
<summary><strong>💡 Answer + PayBridge business scenario</strong></summary>

### Clear answer

The result depends on which filters are removed and which remain. A card has context from slicers, page/report filters, interactions and security. REMOVEFILTERS does not override RLS. An unchanged result can be correct if the removed filter was not restricting eligible rows.

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

**Situation:** A global amount card should ignore country selection but retain the reporting date.

**My BA approach:** Remove only the intended country filter and label the remaining scope.

**What I validate:** Test selections with different country contributions and a restricted user's access.

**Decision supported:** Keep benchmark behaviour clear and secure.

**Interview-ready response**

> “At fictional PayBridge, I would remove only the intended country filter and label the remaining scope. I would test selections with different country contributions and a restricted user's access. This would help the team keep benchmark behaviour clear and secure.”

</details>

---

<a id="pbi-088"></a>
## PBI-088 · Slow report performance

**Interview question**

Scenario: Report consists of so many visuals, some of the visuals are loading very slowly. So, I need to optimize these visuals to load very quickly. What are the steps to perform to improve the performance of the report?

<details>
<summary><strong>💡 Answer + PayBridge business scenario</strong></summary>

### Clear answer

Use Performance Analyzer to separate visual display, DAX query and other timing components, then inspect source and model factors. Reduce unnecessary visuals, simplify relationships and expensive queries, and retest. Data reduction must not discard required business detail silently.

### 🧑‍💼 Same case: PayBridge

**Situation:** The daily operations page takes too long during the morning review.

**My BA approach:** Agree a response-time target and test focused improvements one at a time.

**What I validate:** Compare representative filters, concurrent load and unchanged KPI results.

**Decision supported:** Meet the usability target with evidence.

**Interview-ready response**

> “At fictional PayBridge, I would agree a response-time target and test focused improvements one at a time. I would compare representative filters, concurrent load and unchanged KPI results. This would help the team meet the usability target with evidence.”

</details>

---

<a id="pbi-089"></a>
## PBI-089 · Syncing slicers

**Interview question**

Scenario: There are 2 pages in a report. On the 1st page, there is a slicer called country. If the country is changed from the slicer on the 1st page, then automatically the next page should also be impacted. How will you do it?

<details>
<summary><strong>💡 Answer + PayBridge business scenario</strong></summary>

### Clear answer

Use Sync slicers to share a slicer's selection across selected report pages, controlling visibility separately. Confirm compatible fields and interactions. A hidden synced slicer can still filter a page, so disclose its effect.

### 🧑‍💼 Same case: PayBridge

**Situation:** Country selected on Overview should also scope Failure Investigation.

**My BA approach:** Sync the country slicer across both pages and show the effective scope on the detail page.

**What I validate:** Change, clear and navigate between selections.

**Decision supported:** Keep the investigation aligned with the starting context.

**Interview-ready response**

> “At fictional PayBridge, I would sync the country slicer across both pages and show the effective scope on the detail page. I would change, clear and navigate between selections. This would help the team keep the investigation aligned with the starting context.”

</details>

---

<a id="pbi-090"></a>
## PBI-090 · One expression for row arithmetic and total

**Interview question**

Scenario: 1 calculated column is Qty x unit price & 1 calculated measure sum (sales amt). Can we write these 2 statements in 1 statement?

<details>
<summary><strong>💡 Answer + PayBridge business scenario</strong></summary>

### Clear answer

SUMX can compute a row expression and aggregate it without a stored intermediate column. For the source sales example, use SUMX over quantity times price. In PayBridge the analogous calculation is successful amount times fee rate. Choose upstream or measure calculation based on rules and use.

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

**Situation:** Finance needs total fee revenue without another stored fee column.

**My BA approach:** Use a reviewed row-level multiplication inside a successful-population iterator.

**What I validate:** Check fee-rate precision, rounding policy and totals.

**Decision supported:** Avoid an unnecessary stored column while preserving the correct fee calculation.

**Interview-ready response**

> “At fictional PayBridge, I would use a reviewed row-level multiplication inside a successful-population iterator. I would check fee-rate precision, rounding policy and totals. This would help the team avoid an unnecessary stored column while preserving the correct fee calculation.”

</details>

---

<a id="pbi-091"></a>
## PBI-091 · Country share in the model

**Interview question**

Scenario: 5 countries of data, country-wise sales are there, so need to show sales in percent-wise. How can you do that?

<details>
<summary><strong>💡 Answer + PayBridge business scenario</strong></summary>

### Clear answer

A share is a measure whose numerator and denominator evaluate at different geographic scopes. Removing a table filter can remove more than intended; specify the dimension and column scope and choose all-country versus selected-country meaning.

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

**Situation:** Country managers need contribution to PayBridge's selected-period successful amount.

**My BA approach:** Create a reusable share measure rather than a row-level percentage column.

**What I validate:** Check slicers, total rows and the agreed denominator.

**Decision supported:** Make contribution change correctly with the analysis period.

**Interview-ready response**

> “At fictional PayBridge, I would create a reusable share measure rather than a row-level percentage column. I would check slicers, total rows and the agreed denominator. This would help the team make contribution change correctly with the analysis period.”

</details>

---

<a id="pbi-092"></a>
## PBI-092 · City share

**Interview question**

Scenario: There are 2 columns city & sales amount. How to get a percentage based on sales amount?

<details>
<summary><strong>💡 Answer + PayBridge business scenario</strong></summary>

### Clear answer

Use a measure that removes the intended city filter from the denominator while preserving agreed date, country and other context. Removing only City does not remove another active merchant filter, so test combinations and label the scope.

### Applied example

```dax
City Share in Current Scope =
DIVIDE(
    [Successful Amount INR],
    CALCULATE([Successful Amount INR], REMOVEFILTERS(DimMerchant[City]))
)
-- Country/date context remains; other merchant restrictions also remain.
-- Agree whether this is the intended denominator for merchant-filtered views.
```

Use the schema and relationships in [CASE_STUDY.md](../CASE_STUDY.md). DAX/M examples are reviewed teaching patterns; they were not executed in a Power BI engine here.

### 🧑‍💼 Same case: PayBridge

**Situation:** Within a country, users compare city contributions to successful amount.

**My BA approach:** Define city share within the country and decide how merchant selections affect that denominator.

**What I validate:** Check city totals, country selection and a single-merchant filter.

**Decision supported:** Avoid an unexplained denominator changing between views.

**Interview-ready response**

> “At fictional PayBridge, I would define city share within the country and decide how merchant selections affect that denominator. I would check city totals, country selection and a single-merchant filter. This would help the team avoid an unexplained denominator changing between views.”

</details>

---

<a id="pbi-093"></a>
## PBI-093 · Many-to-many requirements

**Interview question**

Scenario: Many-to-many relationships, how have you faced them?

<details>
<summary><strong>💡 Answer + PayBridge business scenario</strong></summary>

### Clear answer

First investigate duplicates and table grain; not every repeated key justifies many-to-many cardinality. A real multi-segment merchant mapping may need a bridge and an explicit attribution policy. Segment totals may be non-additive when a merchant belongs to several segments.

### 🧑‍💼 Same case: PayBridge

**Situation:** One merchant belongs to two business segments.

**My BA approach:** Define the bridge grain and whether amounts are repeated, allocated or deduplicated across segments.

**What I validate:** Check a multi-segment merchant and compare overall versus summed segment totals.

**Decision supported:** Prevent segment reporting from overstating company performance.

**Interview-ready response**

> “At fictional PayBridge, I would define the bridge grain and whether amounts are repeated, allocated or deduplicated across segments. I would check a multi-segment merchant and compare overall versus summed segment totals. This would help the team prevent segment reporting from overstating company performance.”

</details>

---

<a id="pbi-094"></a>
## PBI-094 · Before scheduled refresh

**Interview question**

Scenario: Before schedule refresh, what steps do you take in SQL Server?

<details>
<summary><strong>💡 Answer + PayBridge business scenario</strong></summary>

### Clear answer

Check the upstream load has completed, extraction views and permissions are valid, schemas have not unexpectedly changed, and the service connection/gateway works. Coordinate heavy SQL jobs and refresh windows with owners; do not routinely rebuild indexes or restart servers just to refresh BI.

### 🧑‍💼 Same case: PayBridge

**Situation:** The morning report must include the completed nightly warehouse load.

**My BA approach:** Use a load-completion gate and freshness checks before model refresh.

**What I validate:** Reconcile loaded batches, source timestamps and refresh history.

**Decision supported:** Avoid publishing incomplete overnight data.

**Interview-ready response**

> “At fictional PayBridge, I would use a load-completion gate and freshness checks before model refresh. I would reconcile loaded batches, source timestamps and refresh history. This would help the team avoid publishing incomplete overnight data.”

</details>

---

<a id="pbi-095"></a>
## PBI-095 · Connectivity mode scenario

**Interview question**

Scenario: You have worked with direct query & import query, right? So what is the basic difference between those 2 modes?

<details>
<summary><strong>💡 Answer + PayBridge business scenario</strong></summary>

### Clear answer

Import needs a refresh policy and stores model data; DirectQuery relies on source query behaviour and capabilities. Compare end-to-end freshness, response time, source load and support constraints using the actual workload. Neither mode is always faster or more appropriate.

### 🧑‍💼 Same case: PayBridge

**Situation:** Operations asks for a fast daily overview and a fresher investigation view.

**My BA approach:** Evaluate separate supported patterns for each requirement rather than forcing one mode everywhere.

**What I validate:** Measure both use cases and verify shared metric definitions.

**Decision supported:** Match architecture to distinct business needs.

**Interview-ready response**

> “At fictional PayBridge, I would evaluate separate supported patterns for each requirement rather than forcing one mode everywhere. I would measure both use cases and verify shared metric definitions. This would help the team match architecture to distinct business needs.”

</details>

---

<a id="pbi-096"></a>
## PBI-096 · Major requirement change

**Interview question**

Scenario: During a project, a stakeholder requests a major change in requirements, and it results in a major change in data relationships. How would you handle this request?

<details>
<summary><strong>💡 Answer + PayBridge business scenario</strong></summary>

### Clear answer

Clarify the desired decision, document the change and assess impact on grain, keys, relationships, measures, security, refresh and existing reports. Present options and trade-offs, obtain the appropriate scope decision, update artefacts and regression-test through QA/UAT before release.

### 🧑‍💼 Same case: PayBridge

**Situation:** A stakeholder changes success reporting from attempt-based to logical-payment-based.

**My BA approach:** Treat the denominator change as a controlled metric and model change, not a cosmetic edit.

**What I validate:** Test retries, old/new definitions, affected reports and approved acceptance criteria.

**Decision supported:** Protect comparability and make the scope decision explicit.

**Interview-ready response**

> “At fictional PayBridge, I would treat the denominator change as a controlled metric and model change, not a cosmetic edit. I would test retries, old/new definitions, affected reports and approved acceptance criteria. This would help the team protect comparability and make the scope decision explicit.”

</details>

---

<a id="pbi-097"></a>
## PBI-097 · Discussing a requested storage mode

**Interview question**

Scenario: If you are a stakeholder where you have a normal amount of data, but you want direct query mode to be used. What will you suggest? Can you convince me why I should go for import mode? What are the steps you will be telling them, and what will be the dashboard performance? Will it be faster or slower?

<details>
<summary><strong>💡 Answer + PayBridge business scenario</strong></summary>

### Clear answer

Discover why the stakeholder wants DirectQuery: freshness, volume, policy or an assumption about speed. If Import meets requirements, show measured results and refresh design; if it does not, propose a suitable alternative. Do not promise performance from row count alone.

### 🧑‍💼 Same case: PayBridge

**Situation:** A stakeholder requests DirectQuery for a modest daily payments model.

**My BA approach:** Compare a representative Import prototype with DirectQuery and explain the freshness and operational trade-offs.

**What I validate:** Use agreed response-time, refresh and concurrency acceptance criteria.

**Decision supported:** Reach an evidence-based architecture decision together.

**Interview-ready response**

> “At fictional PayBridge, I would compare a representative Import prototype with DirectQuery and explain the freshness and operational trade-offs. I would use agreed response-time, refresh and concurrency acceptance criteria. This would help the team reach an evidence-based architecture decision together.”

</details>

---
